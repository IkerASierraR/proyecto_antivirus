# ✨ Características de SecureGuard Antivirus

Esta página describe todas las funcionalidades implementadas en SecureGuard Antivirus v1.0.

---

## 🔍 Motor de Escaneo

El motor de escaneo es el núcleo del sistema, implementado en Rust para máximo rendimiento.

### Métodos de Detección

| Método | Descripción | Confianza |
|:-------|:------------|:---------:|
| **Hash SHA-256** | Compara el hash del archivo contra una base de firmas conocidas | 100% |
| **Heurística de entropía** | Detecta ejecutables PE con entropía > 7.5 bits/byte (indicativo de cifrado/empaquetado) | 50% |
| **Strings sospechosos** | Busca cadenas de texto maliciosas en los primeros 4096 bytes del archivo | 60% |

### Strings sospechosos monitoreados

- `CreateRemoteThread` — Inyección de código en procesos remotos
- `VirtualAllocEx` — Asignación de memoria en proceso remoto
- `WriteProcessMemory` — Escritura en memoria de otro proceso
- `powershell -enc` — PowerShell con payload codificado en Base64
- `Invoke-Mimikatz` — Herramienta de extracción de credenciales
- `ransom` — Indicador de ransomware
- `bitcoin_wallet` — Indicador de actividad de ransomware/cryptominer

---

## 🛡️ Protección en Tiempo Real

El módulo de protección en tiempo real monitorea continuamente el sistema de archivos usando la librería `notify` de Rust.

### Directorios vigilados

- `Documentos` del usuario actual
- `Descargas` del usuario actual
- `C:\Users\Public`

### Comportamiento ante amenaza

1. Se detecta creación o modificación de un archivo
2. El motor calcula el hash SHA-256 y aplica todos los métodos de detección
3. Si se detecta amenaza: el archivo es movido automáticamente a cuarentena
4. La GUI recibe el evento `threat_detected` y muestra alerta visual inmediata

---

## 🔒 Gestión de Cuarentena

Los archivos detectados como amenazas son aislados en un directorio seguro.

### Directorio de cuarentena

```
C:\ProgramData\SecureGuard\Quarantine\
├── <sha256>.quar    ← Archivo malicioso renombrado e inutilizable
└── <sha256>.meta    ← Ruta original del archivo (para restauración)
```

### Operaciones disponibles

| Operación | Descripción |
|:----------|:------------|
| **Listar** | Ver todos los archivos en cuarentena con nombre original y tamaño |
| **Restaurar** | Devolver el archivo a su ubicación original (para falsos positivos) |
| **Eliminar** | Borrar permanentemente el archivo y sus metadatos |

---

## 🌐 Control del Firewall de Windows

SecureGuard permite activar y desactivar el Firewall de Windows desde la interfaz gráfica.

- Utiliza `netsh advfirewall set allprofiles state on/off`
- Aplica a todos los perfiles: Dominio, Privado y Público
- Requiere permisos de administrador
- La vista FirewallView muestra el estado actual con indicadores visuales por perfil

---

## 🧹 Limpieza del Sistema

El módulo de limpieza elimina archivos temporales que pueden servir como vectores de infección.

### Directorios limpiados

- `C:\Windows\Temp`
- Directorio `%TEMP%` del usuario actual

### Resultado

Retorna el número de archivos y carpetas eliminadas con un mensaje de confirmación.

---

## 🔄 Actualización de Firmas

SecureGuard descarga automáticamente las últimas firmas de malware desde el repositorio oficial.

### Archivos actualizados

| Archivo | Descripción |
|:--------|:------------|
| `signatures/malware_hashes.txt` | Lista de hashes SHA-256 de malware conocido (1 por línea) |
| `signatures/yara_rules.yar` | Reglas YARA para detección de familias de malware |

Las líneas que comienzan con `#` son comentarios y se ignoran al cargar las firmas.

---

## 📊 Dashboard

El Dashboard es la vista principal del sistema y proporciona:

- **Indicador de estado circular:** Verde (protegido) o Rojo (amenaza detectada)
- **Botón de escaneo rápido:** Inicia escaneo de `C:\Users\Public`
- **Barra de progreso animada:** Muestra el escaneo en curso
- **Versión del sistema:** SecureGuard v0.3.0 + estado del motor

---

## ⚙️ Información del Sistema

La vista de Configuración muestra métricas del sistema en tiempo real usando `psutil`:

- **CPU:** Porcentaje de uso actual
- **RAM:** Memoria usada vs. total + porcentaje
- **Disco C:** Espacio libre vs. total

---

*Características de SecureGuard Antivirus v1.0 — Mayo 2026*
