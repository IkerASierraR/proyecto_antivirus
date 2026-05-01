# 🐞 Issues del Proyecto — SecureGuard Antivirus

Este documento contiene los issues principales del proyecto SecureGuard Antivirus en formato de historias de usuario con criterios de aceptación en Gherkin.

> **Nota:** Estos issues deben ser creados en la sección [Issues](../../issues) del repositorio GitHub.

---

## Issue #1 — Implementar motor de escaneo basado en firmas SHA-256

**Labels:** `feature`, `priority: high`
**Milestone:** Fase 3 — Desarrollo
**Asignado a:** LLica Mamani, Jimmy Mijair

### Descripción

Como usuario final de SecureGuard Antivirus,  
Quiero que el sistema detecte malware mediante comparación de hashes SHA-256,  
Para tener protección confiable contra amenazas de malware conocido con 100% de precisión.

### Criterios de Aceptación

```gherkin
Scenario: Detectar archivo malicioso conocido
  Given existe un archivo cuyo hash SHA-256 está en la base de firmas
  When el motor escanea ese archivo
  Then se reporta como "Malware conocido (hash)" con confianza 1.0
  And el archivo es movido a cuarentena automáticamente

Scenario: No marcar archivo limpio como amenaza
  Given existe un archivo cuyo hash NO está en la base de firmas
  And el archivo no tiene características heurísticas sospechosas
  When el motor escanea ese archivo
  Then no se reporta como amenaza
  And el archivo permanece en su ubicación original
```

---

## Issue #2 — Implementar detección heurística por entropía

**Labels:** `feature`, `priority: high`
**Milestone:** Fase 3 — Desarrollo
**Asignado a:** LLica Mamani, Jimmy Mijair

### Descripción

Como usuario final de SecureGuard Antivirus,  
Quiero que el sistema detecte ejecutables sospechosos aunque no estén en la base de firmas,  
Para protegerme contra amenazas nuevas (zero-day) mediante análisis heurístico.

### Criterios de Aceptación

```gherkin
Scenario: Detectar ejecutable con alta entropía
  Given existe un archivo PE (header MZ) de más de 1024 bytes
  And la entropía del archivo supera los 7.5 bits/byte
  When el motor analiza el archivo
  Then se reporta como "Sospechoso (alta entropía + PE)" con confianza 0.5
  And se alerta al usuario para que decida la acción a tomar

Scenario: No marcar ejecutable legítimo como sospechoso
  Given existe un ejecutable PE con entropía normal (< 7.5 bits/byte)
  When el motor analiza el archivo
  Then no se genera alerta de alta entropía
  And el archivo no es enviado a cuarentena automáticamente
```

---

## Issue #3 — Implementar protección en tiempo real del sistema de archivos

**Labels:** `feature`, `priority: high`
**Milestone:** Fase 3 — Desarrollo
**Asignado a:** LLica Mamani, Jimmy Mijair

### Descripción

Como usuario final de SecureGuard Antivirus,  
Quiero que el sistema monitoree automáticamente los directorios críticos del sistema,  
Para detectar y aislar amenazas en el momento en que aparecen, sin intervención manual.

### Criterios de Aceptación

```gherkin
Scenario: Iniciar monitoreo en tiempo real
  Given el usuario activa el switch "Protección en Tiempo Real"
  When la GUI envía {"action": "start_realtime"}
  Then el motor inicia el file watcher en Documentos, Descargas y Public
  And el motor responde {"status": "ok", "message": "Real-time protection started"}

Scenario: Detectar y cuarentenar archivo malicioso automáticamente
  Given la protección en tiempo real está activa
  And la base de firmas contiene el hash del archivo
  When se crea un archivo malicioso en un directorio vigilado
  Then el motor lo detecta en menos de 5 segundos
  And mueve el archivo a C:\ProgramData\SecureGuard\Quarantine
  And envía el evento {"event": "threat_detected"} a la GUI
  And la GUI muestra la alerta visual en el dashboard
```

---

## Issue #4 — Implementar gestión completa de cuarentena

**Labels:** `feature`, `priority: high`
**Milestone:** Fase 3 — Desarrollo
**Asignado a:** Sierra Ruiz, Iker Alberto

### Descripción

Como usuario final de SecureGuard Antivirus,  
Quiero poder ver, restaurar y eliminar los archivos que están en cuarentena,  
Para tener control total sobre los archivos aislados y recuperar falsos positivos si es necesario.

### Criterios de Aceptación

```gherkin
Scenario: Listar archivos en cuarentena
  Given hay archivos en C:\ProgramData\SecureGuard\Quarantine
  When el usuario navega a la vista "Archivos en Cuarentena"
  Then se muestran los archivos con nombre original y tamaño en bytes

Scenario: Restaurar archivo de cuarentena (falso positivo)
  Given el usuario ha identificado un falso positivo en la lista
  When hace clic en "Restaurar seleccionado"
  Then el archivo vuelve a su ruta original
  And el archivo .meta es eliminado
  And la lista se actualiza automáticamente

Scenario: Eliminar archivo de cuarentena definitivamente
  Given el usuario quiere eliminar una amenaza confirmada
  When hace clic en "Eliminar seleccionado"
  Then el archivo .quar y su .meta son eliminados permanentemente
  And la lista se actualiza automáticamente
```

---

## Issue #5 — Implementar control del Firewall de Windows desde GUI

**Labels:** `feature`, `priority: medium`
**Milestone:** Fase 3 — Desarrollo
**Asignado a:** Sierra Ruiz, Iker Alberto

### Descripción

Como usuario final de SecureGuard Antivirus,  
Quiero activar y desactivar el Firewall de Windows desde la interfaz del antivirus,  
Para gestionar la protección de red de mi equipo sin necesidad de acceder a la configuración avanzada del sistema.

### Criterios de Aceptación

```gherkin
Scenario: Activar el firewall exitosamente
  Given el switch de firewall está desactivado
  And la aplicación tiene permisos de administrador
  When el usuario activa el switch
  Then el motor ejecuta: netsh advfirewall set allprofiles state on
  And el estado muestra "✅ Activo" en verde
  And los tres perfiles (Dominio, Privado, Público) muestran "✔" en verde

Scenario: Manejar error por falta de permisos
  Given la aplicación NO tiene permisos de administrador
  When el usuario intenta activar el firewall
  Then se muestra el mensaje de error del motor
  And el switch se revierte a su estado anterior
```

---

## Issue #6 — Implementar limpieza de archivos temporales

**Labels:** `feature`, `priority: medium`
**Milestone:** Fase 3 — Desarrollo
**Asignado a:** Sierra Ruiz, Iker Alberto

### Descripción

Como usuario final de SecureGuard Antivirus,  
Quiero limpiar los archivos temporales del sistema con un solo clic,  
Para liberar espacio en disco y eliminar posibles archivos maliciosos residuales que usan los directorios temporales como punto de ejecución.

### Criterios de Aceptación

```gherkin
Scenario: Limpiar archivos temporales exitosamente
  Given existen archivos en C:\Windows\Temp o en %TEMP%
  When el usuario hace clic en "Limpiar archivos temporales"
  Then el botón muestra "Limpiando..." y se deshabilita
  And el motor elimina todos los archivos accesibles
  And el resultado muestra: "N archivos/carpetas temporales eliminados"
  And el botón vuelve a habilitarse

Scenario: Limpieza sin archivos que eliminar
  Given los directorios temporales están vacíos
  When el usuario ejecuta la limpieza
  Then el resultado muestra "0 archivos/carpetas temporales eliminados"
  And no se producen errores
```

---

## Issue #7 — Implementar actualización de firmas de malware

**Labels:** `feature`, `priority: high`
**Milestone:** Fase 3 — Desarrollo
**Asignado a:** LLica Mamani, Jimmy Mijair

### Descripción

Como usuario final de SecureGuard Antivirus,  
Quiero actualizar la base de datos de firmas de malware desde el repositorio oficial con un clic,  
Para mantener la protección del sistema actualizada contra las amenazas de seguridad más recientes.

### Criterios de Aceptación

```gherkin
Scenario: Actualizar firmas exitosamente
  Given hay conexión a internet disponible
  And el repositorio de firmas está disponible
  When el usuario hace clic en "Actualizar firmas"
  Then se descarga malware_hashes.txt al directorio signatures/
  And se descarga yara_rules.yar al directorio signatures/
  And se muestra confirmación con el número de hashes actualizados

Scenario: Fallo de actualización por falta de internet
  Given no hay conexión a internet
  When el usuario intenta actualizar firmas
  Then se muestra mensaje de error descriptivo
  And las firmas existentes permanecen intactas
  And el sistema continúa funcionando con las firmas anteriores
```

---

## Issue #8 — Implementar notificaciones de escritorio para amenazas

**Labels:** `enhancement`, `priority: high`
**Milestone:** v1.1
**Asignado a:** Sierra Ruiz, Iker Alberto

### Descripción

Como usuario final de SecureGuard Antivirus,  
Quiero recibir notificaciones nativas del sistema operativo cuando se detecte una amenaza,  
Para estar informado en tiempo real aunque la ventana del antivirus esté minimizada o en segundo plano.

### Criterios de Aceptación

```gherkin
Scenario: Notificación al detectar amenaza con GUI minimizada
  Given la protección en tiempo real está activa
  And la ventana de SecureGuard está minimizada
  When el motor detecta un archivo malicioso
  Then se muestra una notificación nativa de Windows con:
    - Título: "⚠️ SecureGuard — Amenaza detectada"
    - Cuerpo: nombre del archivo y tipo de amenaza
  And al hacer clic en la notificación se restaura la ventana de SecureGuard

Scenario: No mostrar notificación duplicada
  Given ya se mostró una notificación para un archivo específico
  When el mismo archivo es detectado nuevamente (antes de limpiarse)
  Then NO se muestra una segunda notificación duplicada
```

---

*Issues de SecureGuard Antivirus — Para crear estos issues en GitHub, ir a la sección Issues del repositorio.*
