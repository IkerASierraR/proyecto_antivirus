# 🚀 Guía de Instalación

Esta página describe los pasos necesarios para instalar y ejecutar SecureGuard Antivirus en su equipo.

---

## Requisitos del Sistema

| Componente | Mínimo | Recomendado |
|:-----------|:------:|:-----------:|
| Sistema Operativo | Windows 10 64-bit | Windows 11 64-bit |
| CPU | 2 núcleos x64 | 4+ núcleos |
| RAM | 4 GB | 8 GB |
| Espacio en disco | 500 MB | 2 GB |
| Python | 3.10+ | 3.12 |
| Permisos | Administrador | Administrador |

> ⚠️ **Importante:** Se requieren permisos de administrador para el control del firewall y la cuarentena.

---

## Opción A: Instalador Precompilado (Recomendado)

### Paso 1 — Descargar

Ir a la sección [Releases](../../releases) del repositorio y descargar la última versión:

```
BitCraft_Antivirus_v1.0_Setup.exe
```

### Paso 2 — Ejecutar como administrador

1. Clic derecho sobre el instalador
2. Seleccionar **"Ejecutar como administrador"**
3. Seguir el asistente de instalación
4. Al finalizar, SecureGuard aparecerá en el escritorio y en el menú Inicio

---

## Opción B: Desde Código Fuente

### Paso 1 — Clonar el repositorio

```bash
git clone https://github.com/IkerASierraR/proyecto_antivirus.git
cd proyecto_antivirus
```

### Paso 2 — Instalar Rust (si no está instalado)

```powershell
# Descargar e instalar rustup
Invoke-WebRequest -Uri https://win.rustup.rs -OutFile rustup-init.exe
.\rustup-init.exe
# Cerrar y reabrir la terminal para actualizar el PATH
```

Verificar instalación:
```bash
rustc --version   # Debe mostrar rustc 1.75.0 o superior
cargo --version
```

### Paso 3 — Compilar el motor Rust

```bash
cd codigo-fuente/backend_rust
cargo build --release
```

La compilación toma aproximadamente 2-5 minutos la primera vez. El ejecutable resultante se encuentra en:
```
target/release/secureguard_engine.exe
```

### Paso 4 — Instalar dependencias Python

```bash
cd ../frontend_python
pip install -r requirements.txt
```

### Paso 5 — Copiar el motor al directorio frontend

```powershell
copy ..\backend_rust\target\release\secureguard_engine.exe .
```

### Paso 6 — Crear directorio de firmas

```bash
mkdir signatures

# Crear archivo de firmas vacío (necesario para inicio)
echo "# SecureGuard Malware Hashes - Actualizar con 'Actualizar Firmas'" > signatures/malware_hashes.txt
```

### Paso 7 — Ejecutar la aplicación

```bash
# Ejecutar como administrador (necesario para firewall y cuarentena)
python main.py
```

---

## Verificación de la Instalación

Al iniciar SecureGuard correctamente, debería ver:

1. ✅ La ventana principal con el sidebar de navegación
2. ✅ En la consola: `[SecureGuard] Motor iniciado correctamente`
3. ✅ En el Dashboard: indicador verde "Sistema Protegido"

Si el motor no se inicia, verificar:

```bash
# Probar el motor manualmente
secureguard_engine.exe daemon signatures/
# Debería mostrar: [SecureGuard] Iniciando motor en modo persistente...
```

---

## Solución de Problemas Comunes

| Problema | Causa probable | Solución |
|:---------|:---------------|:---------|
| "Motor no encontrado" | `secureguard_engine.exe` no está en el mismo directorio que `main.py` | Copiar el ejecutable al directorio `frontend_python/` |
| "Error de cuarentena" | Sin permisos de escritura en `C:\ProgramData` | Ejecutar como administrador |
| "Error firewall" | Sin permisos de administrador para `netsh` | Ejecutar como administrador |
| La GUI no abre | Error en la instalación de CustomTkinter | Ejecutar `pip install customtkinter==5.2.0` |
| Firmas no se actualizan | Sin acceso a internet o URL de firmas no configurada | Verificar conexión y configurar URL en `updater.rs` |

---

## Desinstalación

Para desinstalar SecureGuard Antivirus:

1. Usar el desinstalador desde el Panel de Control > Programas (si se usó instalador)
2. Eliminar el directorio de cuarentena manualmente: `C:\ProgramData\SecureGuard\`
3. Eliminar el directorio de la aplicación

---

*Guía de Instalación — SecureGuard Antivirus v1.0 — Mayo 2026*
