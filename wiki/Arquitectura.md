# 🏗️ Arquitectura de SecureGuard Antivirus

Esta página describe la arquitectura técnica del sistema. Para la documentación completa, ver [FD04-Informe-Arquitectura.md](../../blob/main/FD04-Informe-Arquitectura.md).

---

## Visión General

SecureGuard implementa una arquitectura **cliente-servidor de proceso** en capas:

```
┌─────────────────────────────────────────────────┐
│         CAPA DE PRESENTACIÓN                    │
│     Python / CustomTkinter (GUI)                │
├─────────────────────────────────────────────────┤
│         CAPA DE INTEGRACIÓN                     │
│     EngineBridge (IPC — JSON stdin/stdout)      │
├─────────────────────────────────────────────────┤
│         CAPA DE LÓGICA DE NEGOCIO               │
│     Motor Rust — secureguard_engine.exe         │
├─────────────────────────────────────────────────┤
│         CAPA DE DATOS / SISTEMA                 │
│     Sistema de Archivos + Windows APIs          │
└─────────────────────────────────────────────────┘
```

---

## Componentes Principales

### Frontend — Python (GUI)

| Archivo | Responsabilidad |
|:--------|:----------------|
| `main.py` | Punto de entrada, construcción de la ventana y navegación |
| `engine_bridge.py` | Gestión del subproceso motor, colas de mensajes, callbacks |
| `views/dashboard_view.py` | Vista principal, escaneo manual, alertas de amenazas |
| `views/protection_view.py` | Switches de protección en tiempo real y anti-ransomware |
| `views/firewall_view.py` | Control de firewall con indicadores por perfil |
| `views/quarantine_view.py` | Listado y gestión de cuarentena |
| `views/cleaning_view.py` | Limpieza de archivos temporales |
| `views/update_view.py` | Actualización de firmas |
| `views/settings_view.py` | Información del sistema (CPU, RAM, disco) |

### Backend — Rust (Motor)

| Módulo | Responsabilidad |
|:-------|:----------------|
| `main.rs` | Punto de entrada CLI, dispatcher de comandos |
| `daemon.rs` | Bucle de lectura de comandos JSON, coordinación de módulos |
| `scanner.rs` | Motor de escaneo: hash SHA-256, entropía, strings sospechosos |
| `quarantine.rs` | Mover/restaurar/eliminar archivos `.quar` |
| `network.rs` | Ejecutar `netsh advfirewall` para control de firewall |
| `cleaner.rs` | Eliminar archivos de `C:\Windows\Temp` y `%TEMP%` |
| `updater.rs` | Descargar firmas vía HTTP desde repositorio remoto |
| `protection.rs` | (Planificado) Módulo de protección adicional |
| `utils.rs` | Helpers `ok_response()` y `error_response()` |

---

## Protocolo de Comunicación IPC

La comunicación entre GUI y motor es **asíncrona** mediante JSON sobre pipes:

```
GUI Python                    Motor Rust
    │                              │
    │── stdin ──────────────────▶ │  {"action": "scan", "path": "C:\\..."}
    │                              │
    │◀─────────────────── stdout ──│  {"status": "ok", "threats_found": 2}
    │                              │
    │◀─────────────────── stdout ──│  {"event": "threat_detected", "file": "..."}
```

### Tipos de mensajes

| Tipo | Dirección | Ejemplo |
|:-----|:----------|:--------|
| **Comando** | GUI → Motor | `{"action": "scan", "path": "C:\\Users"}` |
| **Respuesta** | Motor → GUI | `{"status": "ok", "data": {...}}` |
| **Evento** | Motor → GUI | `{"event": "threat_detected", "file": "..."}` |

Los **eventos** son identificados por la presencia del campo `"event"` y son enrutados a los callbacks registrados en el EngineBridge, sin bloquear la cola de respuestas.

---

## Flujo de Inicio del Sistema

```
main.py
  └─▶ EngineBridge()
        └─▶ subprocess.Popen([secureguard_engine.exe, "daemon", "signatures/"])
              └─▶ initialize_with_offline_signatures()
                    └─▶ Cargar malware_hashes.txt → OFFLINE_HASHES (memoria)
              └─▶ Bucle: leer stdin → handle_command() → escribir stdout
  └─▶ Lanzar thread _read_output() (lee stdout del motor)
  └─▶ Lanzar thread _monitor_process() (detecta si el motor muere)
  └─▶ Mostrar ventana GUI
```

---

## Dependencias Técnicas

### Rust (Cargo.toml)

| Crate | Versión | Función |
|:------|:--------|:--------|
| `serde_json` | 1.0 | JSON serialización/deserialización |
| `walkdir` | 2.4 | Traversal del sistema de archivos |
| `sha2` | 0.10 | Hashing SHA-256 |
| `notify` | 6.1 | Monitoreo de cambios de archivos |
| `reqwest` | 0.11 | Cliente HTTP para actualizaciones |
| `dirs` | 5.0 | Rutas estándar del SO |

### Python (requirements.txt)

| Librería | Versión | Función |
|:---------|:--------|:--------|
| `customtkinter` | 5.2.0 | Framework GUI moderno |
| `psutil` | 5.9.5 | Métricas de sistema |
| `Pillow` | 10.0.0 | Procesamiento de imágenes |
| `plyer` | 2.1.0 | Notificaciones del SO |

---

*Arquitectura de SecureGuard Antivirus v1.0 — Para la documentación completa, ver FD04-Informe-Arquitectura.md*
