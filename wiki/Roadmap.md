# 🗺️ Roadmap de SecureGuard Antivirus

Esta página detalla el plan de versiones futuras. Para la gestión completa del proyecto, ver [FD02-Informe-Gestion.md](../../blob/main/FD02-Informe-Gestion.md).

---

## Estado Actual

| Versión | Estado | Fecha |
|:--------|:------:|:-----:|
| v1.0 — MVP | ✅ Lanzada | Mayo 2026 |
| v1.1 — Calidad | 🔜 Planificada | Julio 2026 |
| v2.0 — Plataforma | 📋 Conceptual | Enero 2027 |

---

## v1.0 — Producto Mínimo Viable (MVP)

**Lanzamiento:** 30 de mayo de 2026

Versión inicial con todas las funcionalidades esenciales de un antivirus de escritorio.

### Incluido en v1.0

- ✅ Motor de escaneo: hash SHA-256, entropía, strings sospechosos
- ✅ Protección en tiempo real (file watcher con `notify`)
- ✅ Gestión completa de cuarentena (mover/restaurar/eliminar)
- ✅ Control del Firewall de Windows desde GUI
- ✅ Limpieza de archivos temporales
- ✅ Actualización de firmas desde repositorio remoto
- ✅ Interfaz gráfica con CustomTkinter (modo oscuro)
- ✅ Dashboard con indicador de estado y alertas en tiempo real
- ✅ Vista FirewallView con indicadores por perfil de red
- ✅ Vista SettingsView con métricas del sistema
- ✅ Documentación académica completa (FD01-FD04)
- ✅ Instalador empaquetado con PyInstaller

---

## v1.1 — Mejoras de Calidad y CI/CD

**Lanzamiento estimado:** 31 de julio de 2026

Esta versión se enfoca en la calidad del código, automatización de pruebas y mejoras de experiencia de usuario.

### Planificado para v1.1

#### DevOps y Calidad
- 🔜 Pipeline CI/CD con GitHub Actions
  - Compilación automática del motor Rust
  - Pruebas automatizadas con `pytest`
  - Análisis estático con `clippy` (Rust) y `flake8` (Python)
- 🔜 Cobertura de pruebas unitarias >= 80% en módulos críticos
- 🔜 Pruebas de integración frontend-backend (protocolo JSON)
- 🔜 Firma de commits con GPG

#### Nuevas Funcionalidades
- 🔜 Notificaciones de escritorio nativas (usando `plyer`)
- 🔜 Historial de escaneos con fecha, ruta y resultados
- 🔜 Actualizaciones automáticas programadas (cada 24 horas)
- 🔜 Soporte multiidioma (Español/Inglés)
- 🔜 Modo Anti-Ransomware mejorado (detección de cifrado masivo)

#### Mejoras de Seguridad
- 🔜 GitHub Security Advisories habilitados
- 🔜 Dependabot para actualizaciones automáticas de dependencias
- 🔜 SBOM (Software Bill of Materials) generado automáticamente

---

## v2.0 — Plataforma de Seguridad Completa

**Lanzamiento estimado:** 31 de enero de 2027

Transformación de SecureGuard en una plataforma de seguridad robusta con infraestructura en nube.

### Planificado para v2.0

#### Infraestructura en Nube
- 📋 Servidor de firmas en AWS/Azure con Terraform (ver FD01 seccion 4.2.7)
- 📋 CDN global para distribución de actualizaciones
- 📋 Base de datos PostgreSQL para historial y telemetría
- 📋 API REST para integración con herramientas empresariales

#### Motor de Detección Avanzado
- 📋 Integración del motor YARA para detección de familias de malware
- 📋 Análisis de comportamiento con machine learning (detección zero-day)
- 📋 Escaneo de procesos activos en memoria RAM
- 📋 Sandbox de archivos sospechosos (entorno virtualizado)

#### Plataforma
- 📋 Dashboard web para administradores (React + FastAPI)
- 📋 Soporte nativo para Linux (`.deb` y `.rpm`)
- 📋 VPN integrada básica para protección de red
- 📋 GitHub Pages — Landing page del proyecto
- 📋 Evaluación de conformidad ISO/IEC 27001

---

## Historial de Versiones

| Versión | Fecha | Cambios principales |
|:--------|:-----:|:---------------------|
| v0.3.0 | Abril 2026 | Motor Rust con escaneo, cuarentena, daemon mode |
| v1.0 | Mayo 2026 | GUI completa, todas las vistas, instalador |
| v1.1 | Julio 2026 | CI/CD, pruebas automatizadas, notificaciones |
| v2.0 | Enero 2027 | Infraestructura nube, ML, soporte Linux |

---

*Roadmap de SecureGuard Antivirus — Actualizado: Mayo 2026*
