<center>

![./media/logo-upt.png](./media/logo-upt.png)

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERIA**

**Escuela Profesional de Ingeniería de Sistemas**

**Proyecto de Antivirus**

Curso: *Calidad y Pruebas de Software*

Docente: *Mag. Patrick Cuadros Quiroga*

Integrantes:

***LLica Mamani, Jimmy Mijair (2023076789)***

***Sierra Ruiz, Iker Alberto (2023077090)***

**Tacna – Perú**

***2026***

</center>

<div style="page-break-after: always; visibility: hidden"></div>

Sistema *SecureGuard Antivirus*

Informe de Vsion

Versión *1.0*

| CONTROL DE VERSIONES | | | | |
|:---:|:---|:---|:---|:---|
| Versión | Hecha por | Revisada por | Aprobada por | Fecha | Motivo |
| 1.0 | LLica Mamani, Jimmy Mijair | Sierra Ruiz, Iker Alberto | LLica Mamani, Jimmy Mijair | 28/03/2026 | Versión Original |

<div style="page-break-after: always; visibility: hidden"></div>

**INDICE GENERAL**

[1. Introducción](#_Toc52661346)

1.1 Propósito

1.2 Alcance

1.3 Definiciones, Siglas y Abreviaturas

1.4 Referencias

1.5 Visión General

[2. Posicionamiento](#_Toc52661347)

2.1 Oportunidad de negocio

2.2 Definición del problema

[3. Descripción de los interesados y usuarios](#_Toc52661348)

3.1 Resumen de los interesados

3.2 Resumen de los usuarios

3.3 Entorno de usuario

3.4 Perfiles de los interesados

3.5 Perfiles de los Usuarios

3.6 Necesidades de los interesados y usuarios

[4. Vista General del Producto](#_Toc52661349)

4.1 Perspectiva del producto

4.2 Resumen de capacidades

4.3 Suposiciones y dependencias

4.4 Costos y precios

4.5 Licenciamiento e instalación

[5. Características del producto](#_Toc52661350)

[6. Restricciones](#_Toc52661351)

[7. Rangos de calidad](#_Toc52661352)

[8. Precedencia y Prioridad](#_Toc52661353)

[9. Otros requerimientos del producto](#_Toc52661354)

[CONCLUSIONES](#_Toc52661355)

[RECOMENDACIONES](#_Toc52661356)

[BIBLIOGRAFIA](#_Toc52661357)

[WEBGRAFIA](#_Toc52661358)

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

**<u>Informe de Visión</u>**

## 1. <span id="_Toc52661346" class="anchor"></span>**Introducción**

### 1.1 Propósito

El presente documento de visión describe la conceptualización, alcance y propósito del Sistema de Antivirus Académico, un proyecto desarrollado en el contexto del curso de Calidad y Pruebas de Software de la Escuela Profesional de Ingeniería de Sistemas. Este documento proporciona una perspectiva integral del producto desde el punto de vista de los requisitos, características, restricciones y criterios de calidad que deben satisfacerse durante su desarrollo y validación.

El propósito principal es establecer las bases para un plan de aseguramiento de calidad y pruebas de software, demostrando la aplicación de técnicas de verificación y validación en un sistema de seguridad informática de complejidad académica.

### 1.2 Alcance

El proyecto abarca el desarrollo de un software antivirus académico con énfasis en:

- **Desarrollo del motor de escaneo**: Lógica básica para identificación de amenazas mediante comparación de firmas y patrones.
- **Gestión de base de datos de amenazas**: Repositorio de prueba para almacenar definiciones de malware simulado.
- **Interfaz de usuario funcional**: Módulo para ejecución de escaneos manuales y visualización de resultados.
- **Sistema de monitoreo básico**: Capacidad para detectar cambios en el sistema de archivos y registrar eventos.
- **Plan exhaustivo de pruebas**: Casos de prueba, pruebas unitarias, pruebas dinámicas y registro de defectos.
- **Evaluación de calidad**: Análisis basado en el estándar ISO/IEC 25010 para verificar características de fiabilidad, seguridad, usabilidad, mantenibilidad y eficiencia.

El alcance excluye el desarrollo de un motor antivirus real o la implementación de técnicas avanzadas de análisis heurístico y detección basada en aprendizaje automático.

### 1.3 Definiciones, Siglas y Abreviaturas

| Sigla/Término | Definición |
| :- | :- |
| **QA** | Aseguramiento de Calidad (Quality Assurance) |
| **SQA** | Aseguramiento de Calidad de Software (Software Quality Assurance) |
| **ISO/IEC 25010** | Estándar de calidad de producto de software |
| **Verificación** | Proceso de evaluar si el software cumple con sus especificaciones técnicas |
| **Validación** | Proceso de evaluar si el software satisface las necesidades del usuario |
| **Caso de Prueba** | Conjunto de condiciones y pasos para ejecutar una prueba específica |
| **Defecto** | Desviación del comportamiento esperado del software |
| **Malware** | Software malicioso diseñado para dañar o comprometer un sistema |
| **Firma de Malware** | Patrón de código o característica única que identifica un tipo de malware |
| **Motor de Escaneo** | Componente responsable de analizar archivos en búsqueda de amenazas |

### 1.4 Referencias

- ISO/IEC 25010:2023. Calidad de producto de software.
- IEEE 829-2023. Standard for Software and System Test Documentation.
- Sommerville, I. (2015). Software Engineering (10th ed.). Pearson.
- IEEE Std 1062-1998. Recommended Practice for Software Acquisition.
- Guía de Aseguramiento de Calidad de Software - UPT FAING EPIS.

### 1.5 Visión General

El Sistema de Antivirus Académico es una aplicación de escritorio desarrollada para demostrar la aplicación de técnicas de aseguramiento de calidad y pruebas de software en un dominio de seguridad informática. El producto permitirá a estudiantes universitarios comprender la importancia de la verificación, validación y métricas de calidad en el desarrollo de software crítico.

El sistema está diseñado para ser simple, mantenible y completamente documentado, proporcionando una plataforma ideal para la implementación de casos de prueba, detección de defectos y evaluación de características de calidad definidas por estándares internacionales.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 2. <span id="_Toc52661347" class="anchor"></span>**Posicionamiento**

### 2.1 Oportunidad de negocio

Desde la perspectiva académica, este proyecto representa una oportunidad significativa para:

1. **Formación Integral en Calidad de Software**: Permitir que los estudiantes de ingeniería de sistemas apliquen metodologías de aseguramiento de calidad en un proyecto real de complejidad controlada.

2. **Comprensión Práctica de Ciclos de Vida**: Demostrar las fases de desarrollo de software incluyendo análisis de requisitos, diseño, implementación, pruebas y mantenimiento.

3. **Aplicación de Estándares Internacionales**: Utilizar el estándar ISO/IEC 25010 para evaluar características de calidad como fiabilidad, seguridad y usabilidad.

4. **Documentación Profesional**: Desarrollar habilidades en documentación técnica, casos de prueba y reportes de calidad, competencias esenciales en la industria de software.

5. **Portafolio Académico**: Crear un proyecto documentado que demuestre competencias en ingeniería de software y aseguramiento de calidad para futuras oportunidades profesionales.

### 2.2 Definición del problema

**Contexto del Problema:**

Actualmente, los cursos de Calidad y Pruebas de Software carecen de un proyecto práctico que permita a los estudiantes aplicar técnicas de verificación, validación y aseguramiento de calidad en un dominio específico. Esto genera una brecha entre el conocimiento teórico y la práctica profesional.

**Problema Identificado:**

Los estudiantes requieren una plataforma de software funcional pero de complejidad controlada para:

1. Diseñar e implementar planes exhaustivos de pruebas.
2. Crear y ejecutar casos de prueba para diferentes escenarios.
3. Identificar, registrar y reportar defectos encontrados.
4. Aplicar métricas de calidad basadas en estándares reconocidos.
5. Documentar evidencia de verificación y validación del producto.

**Solución Propuesta:**

Desarrollar un Sistema de Antivirus Académico que incorpore componentes funcionales básicos (motor de escaneo, base de datos de amenazas, interfaz de usuario, monitoreo) permitiendo que los estudiantes enfoquen sus esfuerzos en actividades de aseguramiento de calidad, pruebas y documentación, sin necesidad de desarrollar un motor de seguridad complejo o comercialmente viable.

**Valor Agregado:**

Este enfoque permite equilibrar la complejidad técnica del desarrollo con la profundidad requerida en aseguramiento de calidad, haciendo el proyecto académicamente valioso y completamente documentado.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 3. <span id="_Toc52661348" class="anchor"></span>**Descripción de los interesados y usuarios**

### 3.1 Resumen de los interesados

| Interesado | Descripción | Rol |
| :- | :- | :- |
| **Docente del Curso** | Responsable de orientar el desarrollo del proyecto y evaluar la calidad de entregables | Supervisor académico, evaluador |
| **Estudiantes Desarrolladores** | Responsables del desarrollo, pruebas y documentación del sistema | Desarrolladores, testers, documentadores |
| **Departamento de Ingeniería de Sistemas** | Beneficiario de mejoras en metodología de enseñanza de calidad de software | Institución académica |
| **Futuros Empleadores** | Interesados en competencias de estudiantes en aseguramiento de calidad | Usuarios potenciales del portafolio académico |

### 3.2 Resumen de los usuarios

| Tipo de Usuario | Descripción | Función |
| :- | :- | :- |
| **Usuario Administrador** | Personal técnico responsable de la configuración y mantenimiento del sistema | Gestionar configuraciones, actualizar bases de datos de amenazas |
| **Usuario Final** | Personas que utilizan el antivirus para proteger sus sistemas | Ejecutar escaneos, revisar resultados, tomar acciones correctivas |
| **Evaluador de Calidad** | Persona que verifica el cumplimiento de criterios de calidad | Ejecutar pruebas, reportar defectos, validar requisitos |

### 3.3 Entorno de usuario

El sistema opera en un entorno de laboratorio académico con las siguientes características:

- **Plataforma**: Sistema operativo Windows o Linux en máquinas virtuales o físicas.
- **Hardware**: Computadoras de laboratorio con recursos moderados (procesador dual-core, 4GB RAM mínimo).
- **Conectividad**: Red local del laboratorio para distribución de definiciones de amenazas simuladas.
- **Período de Uso**: Semestre académico (marzo a junio 2026) con uso intensivo durante fases de pruebas.
- **Usuarios Simultáneos**: Máximo 30 estudiantes ejecutando pruebas en paralelo.

### 3.4 Perfiles de los interesados

**Docente del Curso:**
- Responsable de definir criterios de evaluación basados en estándares de calidad.
- Necesita evidencia clara de procesos de verificación y validación.
- Requiere documentación completa de defectos encontrados y resolución.
- Interesado en demostrar aplicación de metodologías de aseguramiento de calidad.

**Estudiantes Desarrolladores:**
- Requieren herramientas y documentación clara para desarrollar componentes.
- Necesitan comprender cómo aplicar pruebas y aseguramiento de calidad.
- Interesados en crear un portafolio académico profesional.
- Requieren retroalimentación sobre defectos y mejoras de calidad.

**Departamento Académico:**
- Interesado en mejorar la enseñanza de calidad de software.
- Requiere evidencia de cumplimiento de competencias establecidas.
- Busca que el proyecto sea replicable en futuras cohortes.

### 3.5 Perfiles de los Usuarios

**Usuario Administrador:**
- Técnico en sistemas con conocimiento básico de seguridad informática.
- Capacitado para ejecutar procedimientos de actualización de definiciones.
- Responsable de mantener logs y reportes de estado del sistema.
- Debe tener acceso a funciones privilegiadas de configuración.

**Usuario Final (Operador del Antivirus):**
- Persona no técnica que requiere interfaz intuitiva.
- Necesita entender resultados de escaneos de forma clara.
- Requiere instrucciones simples para ejecutar acciones preventivas.
- Debe comprender alertas de amenazas detectadas sin conocimiento técnico profundo.

**Evaluador de Calidad (QA/Tester):**
- Profesional técnico conocedor de metodologías de prueba.
- Capacitado para crear casos de prueba y reportar defectos.
- Responsable de validar requisitos y características de calidad.
- Debe documentar evidencia de pruebas ejecutadas.

### 3.6 Necesidades de los interesados y usuarios

| Interesado/Usuario | Necesidades |
| :- | :- |
| **Docente** | Evidencia de procesos QA, documentación de defectos, métricas de calidad, cumplimiento de requisitos |
| **Estudiantes** | Guía clara de requisitos, entorno de desarrollo estable, feedback constructivo, documentación técnica |
| **Usuario Final** | Interfaz amigable, resultados claros de escaneos, acciones recomendadas, sistema confiable |
| **Usuario Administrador** | Funciones de configuración, acceso a logs, gestión de definiciones de amenazas, reportes de estado |
| **Evaluador QA** | Herramientas para registro de pruebas, ambiente reproducible, trazabilidad de requisitos, defectos rastreables |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 4. <span id="_Toc52661349" class="anchor"></span>**Vista General del Producto**

### 4.1 Perspectiva del producto

El Sistema de Antivirus Académico se posiciona como una aplicación de escritorio independiente (standalone) que integra componentes de seguridad básica en una solución de propósito académico. El producto no depende de servicios externos críticos, permitiendo su ejecución en entornos aislados de laboratorio.

**Relación con otros sistemas:**

El antivirus interactúa con:
- **Sistema operativo**: Para acceso al sistema de archivos, procesos en ejecución y eventos del sistema.
- **Base de datos local**: Repositorio local de definiciones de malware simulado (no requiere conexión a internet).
- **Interfaz gráfica**: Capa de presentación independiente del motor de detección.

La arquitectura modular permite que cada componente sea probado independientemente, facilitando la identificación y aislamiento de defectos.

### 4.2 Resumen de capacidades

El Sistema de Antivirus Académico proporciona las siguientes capacidades principales:

**Motor de Escaneo:**
- Análisis de archivos basado en comparación de firmas contra base de datos de amenazas.
- Búsqueda de patrones simples en contenido de archivos.
- Identificación de extensiones de archivo potencialmente peligrosas.
- Generación de reportes de detección con nivel de severidad.

**Base de Datos de Amenazas:**
- Almacenamiento de firmas de malware de prueba.
- Gestión de definiciones de amenazas (agregar, actualizar, eliminar).
- Versionado de definiciones para trazabilidad.
- Categorización de amenazas por tipo (virus, troyano, spyware, etc.).

**Interfaz de Usuario:**
- Panel de control intuitivo para navegación del sistema.
- Módulo de escaneo manual con selección de rutas y archivos.
- Visualización de resultados en tiempo real o diferido.
- Listado de archivos detectados con información detallada.
- Indicador de estado general del sistema.

**Sistema de Monitoreo Básico:**
- Detección de cambios en directorios críticos del sistema.
- Registro de eventos de creación, modificación y eliminación de archivos.
- Notificaciones de actividad sospechosa (simulada).
- Log de eventos persistente para auditoría.

**Características de Aseguramiento de Calidad:**
- Trazabilidad completa de requisitos a casos de prueba.
- Registro sistemático de defectos encontrados.
- Métricas de cobertura de pruebas.
- Documentación de evidencia de verificación y validación.
- Cumplimiento con características de calidad ISO/IEC 25010.

### 4.3 Suposiciones y dependencias

**Suposiciones:**

1. Los usuarios tienen acceso a computadoras con capacidad para ejecutar aplicaciones de escritorio.
2. Los usuarios tienen conocimiento básico de sistemas de archivos y operaciones de seguridad.
3. La base de datos de amenazas puede ser actualizada manualmente mediante archivos de configuración.
4. El proyecto cuenta con recursos humanos (equipo de estudiantes) durante el período académico establecido.
5. Las máquinas de prueba pueden ser reiniciadas sin afectar datos críticos (laboratorio académico).

**Dependencias Técnicas:**

1. **Disponibilidad de lenguaje de programación**: Se requiere lenguaje con librerías estándar para I/O de archivos y interfaz gráfica (Python, C#, Java).
2. **Sistema operativo**: Compatibilidad con Windows o Linux en ambiente de máquinas virtuales o físicas.
3. **Entorno de desarrollo**: IDE, compilador/intérprete, herramientas de testing disponibles en laboratorio.
4. **Documentación técnica**: Acceso a estándares ISO/IEC 25010 y metodologías de pruebas de software.

**Dependencias Organizacionales:**

1. Disponibilidad del docente para revisión y retroalimentación.
2. Acceso sostenido al laboratorio de cómputo del departamento.
3. Coordinación entre equipos de desarrollo, testing y documentación.

### 4.4 Costos y precios

Este es un proyecto académico, por lo que no se generan costos de licencia o precios de venta. Sin embargo, se consideran los siguientes recursos:

**Recursos de Tiempo (Horas-Estudiante):**

| Actividad | Estimado (horas) |
| :- | :- |
| Análisis de requisitos y visión | 10 |
| Diseño arquitectónico | 15 |
| Desarrollo del motor de escaneo | 20 |
| Desarrollo de base de datos | 12 |
| Desarrollo de interfaz de usuario | 18 |
| Desarrollo de monitoreo | 15 |
| Planificación de pruebas | 12 |
| Implementación de casos de prueba | 25 |
| Ejecución y reportaje de pruebas | 20 |
| Documentación y entregables | 15 |
| **Total** | **162 horas** |

**Recursos de Software:**

- Herramientas de desarrollo: Gratuitas (IDE open-source, Python, .NET Framework Community).
- Herramientas de control de versiones: GitHub (gratuito para repositorios académicos).
- Herramientas de testing: JUnit, unittest, Pytest (gratuitas).
- Herramientas de documentación: Markdown, PlantUML (gratuitas).

**Recursos de Infraestructura:**

- Laboratorio de cómputo de la facultad (existente).
- Máquinas virtuales en servidores disponibles.

### 4.5 Licenciamiento e instalación

**Modelo de Licenciamiento:**

El software antivirus académico se distribuye bajo licencia de uso educativo interno. No se permite distribución comercial ni uso fuera del contexto académico del curso sin autorización del departamento.

**Instalación:**

1. **Requisitos del Sistema:**
   - Sistema operativo: Windows 7+ o Linux (Ubuntu 18.04+)
   - Memoria RAM: Mínimo 4 GB
   - Espacio en disco: 500 MB
   - Procesador: Dual-core 2.0 GHz

2. **Proceso de Instalación:**
   - Descargar archivo ejecutable desde repositorio GitHub del proyecto.
   - Ejecutar instalador con permisos de administrador.
   - Seguir asistente de instalación para seleccionar directorio destino.
   - Completar instalación e iniciar aplicación.

3. **Configuración Inicial:**
   - Crear perfil de usuario (administrador o estándar).
   - Cargar base de datos inicial de definiciones de amenazas.
   - Configurar directorios de monitoreo.
   - Ejecutar prueba de funcionamiento básico.

4. **Actualización:**
   - Las actualizaciones de definiciones de amenazas se realizan mediante archivo de configuración.
   - Las nuevas versiones del software se distribuyen mediante releases de GitHub.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 5. <span id="_Toc52661350" class="anchor"></span>**Características del producto**

El Sistema de Antivirus Académico incluye las siguientes características fundamentales:

### Características Funcionales

**CF01: Escaneo Manual de Archivos**
- El sistema permite al usuario seleccionar archivos o directorios específicos para análisis.
- Examina contenido de archivos contra definiciones de amenazas.
- Genera reporte de resultados con detalle de amenazas detectadas.
- Prioridad: Alta | Estado: Requerido

**CF02: Escaneo Automático Programado**
- El sistema puede ejecutar escaneos automáticos en horarios predefinidos.
- Realiza escaneo completo o de directorios específicos según configuración.
- Genera logs de actividad automática.
- Prioridad: Media | Estado: Requerido

**CF03: Gestión de Base de Datos de Amenazas**
- Permite agregar nuevas definiciones de malware de prueba.
- Permite actualizar definiciones existentes.
- Permite eliminar definiciones obsoletas.
- Categoriza amenazas por tipo (virus, troyano, spyware, adware).
- Prioridad: Alta | Estado: Requerido

**CF04: Visualización de Resultados**
- Muestra listado de archivos sospechosos detectados durante escaneo.
- Presenta información de severidad (crítico, alto, medio, bajo).
- Permite ver detalles de cada amenaza detectada (tipo, firma, archivo afectado).
- Prioridad: Alta | Estado: Requerido

**CF05: Monitoreo de Sistema en Tiempo Real**
- Supervisa cambios en directorios críticos del sistema.
- Detecta creación de nuevos archivos potencialmente peligrosos.
- Registra modificaciones de archivos ejecutables.
- Genera alertas de actividad sospechosa.
- Prioridad: Media | Estado: Requerido

**CF06: Gestión de Cuarentena**
- Permite aislar archivos sospechosos en área de cuarentena.
- Mantiene listado de archivos en cuarentena.
- Permite eliminar archivos de cuarentena de forma segura.
- Permite restaurar archivos erróneamente cuarentenados.
- Prioridad: Media | Estado: Requerido

**CF07: Generación de Reportes**
- Genera reportes de escaneo con fecha, hora y resultados.
- Exporta reportes en formatos PDF y CSV.
- Incluye estadísticas de archivos analizados y amenazas detectadas.
- Prioridad: Media | Estado: Requerido

### Características de Calidad (No-Funcionales)

**CNF01: Fiabilidad**
- El sistema mantiene disponibilidad de servicio del 95% durante período de uso.
- Recuperación automática ante fallos no catastróficos.
- Validación de integridad de base de datos de amenazas.
- Prioridad: Alta | Métrica: Uptime >= 95%

**CNF02: Seguridad**
- Protección de base de datos de amenazas contra modificación no autorizada.
- Validación de integridad de archivos de configuración.
- Logs auditables de todas las operaciones críticas.
- Prioridad: Alta | Métrica: Cero vulnerabilidades críticas

**CNF03: Usabilidad**
- Interfaz intuitiva que no requiere entrenamiento extenso.
- Mensaje de error claro y accionable.
- Ayuda contextual disponible para funcionalidades principales.
- Prioridad: Alta | Métrica: 90% de usuarios pueden ejecutar escaneo sin manual

**CNF04: Mantenibilidad**
- Código modular con separación clara de responsabilidades.
- Documentación técnica completa de arquitectura y componentes.
- Comentarios de código en secciones complejas.
- Prioridad: Alta | Métrica: Cobertura de código >= 70%

**CNF05: Eficiencia**
- Escaneo de archivo de 10 MB completado en menos de 5 segundos.
- Consumo de memoria RAM < 200 MB durante operación normal.
- Tiempo de respuesta de interfaz < 1 segundo en operaciones estándar.
- Prioridad: Media | Métrica: Performance baseline establecido

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 6. <span id="_Toc52661351" class="anchor"></span>**Restricciones**

El Sistema de Antivirus Académico opera bajo las siguientes restricciones:

### Restricciones Técnicas

**RT01: Motor de Detección Simplificado**
- El motor utiliza únicamente comparación de firmas y patrones básicos.
- No incluye análisis heurístico avanzado o detección basada en comportamiento.
- No utiliza técnicas de aprendizaje automático para mejorar detección.
- Limitación necesaria para mantener proyecto académicamente viable.

**RT02: Ambiente de Ejecución Limitado**
- El sistema opera únicamente en ambiente de laboratorio académico.
- No se soporta ejecución en servidores o entornos productivos.
- Limitado a máquinas virtuales o físicas con hardware moderado.

**RT03: Conectividad Restringida**
- No requiere conexión a internet para operación básica.
- Actualizaciones de definiciones realizadas mediante archivo local, no por descarga automática.
- Sin capacidad de reportar telemetría a servidores externos.

**RT04: Capacidad de Procesamiento**
- Tamaño máximo de archivos analizados: 1 GB.
- Cantidad máxima de definiciones de amenazas: 10,000 firmas.
- Usuarios simultáneos: Máximo 30 en laboratorio académico.

### Restricciones Organizacionales

**RO01: Período de Desarrollo Limitado**
- Desarrollo debe completarse dentro del semestre académico (Marzo - Junio 2026).
- Disponibilidad limitada de docente para revisiones (2-3 horas por semana).
- Equipo de desarrollo compuesto por estudiantes con disponibilidad parcial.

**RO02: Alcance Académico**
- Proyecto enfocado en aseguramiento de calidad, no en complejidad técnica del motor antivirus.
- No incluye funcionalidades avanzadas de seguridad como análisis en nube o inteligencia colectiva.
- Debe ser completamente documentado para propósitos de evaluación.

**RO03: Recursos Disponibles**
- Únicamente herramientas de software libre y gratuitas.
- Acceso limitado a laboratorio (horario de clases y prácticas autorizadas).
- No se asignan presupuestos para software comercial o servidores dedicados.

### Restricciones Legales y Regulatorias

**RL01: Propósito Educativo**
- Software destinado exclusivamente a uso académico dentro de UPT FAING EPIS.
- Prohibida la distribución comercial o uso fuera del contexto educativo.
- Requiere autorización del departamento para cualquier uso externo.

**RL02: Cumplimiento de Normativa Institucional**
- Debe cumplir con política de integridad académica de la universidad.
- Se requiere documentación completa de fuentes y referencias.
- No se permite plagio de código de proyectos anteriores sin cita apropiada.

**RL03: Datos de Prueba**
- Utiliza únicamente malware simulado y definiciones de prueba.
- No incluye muestras reales de malware.
- Archivos de prueba no representan amenazas reales.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 7. <span id="_Toc52661352" class="anchor"></span>**Rangos de calidad**

La evaluación de calidad del Sistema de Antivirus Académico se basa en el estándar ISO/IEC 25010, considerando las siguientes características de calidad de producto de software:

### Fiabilidad

**Objetivo:** El sistema debe ejecutar sus funciones de forma consistente sin fallos no esperados.

| Métrica | Criterio de Aceptación | Responsable |
| :- | :- | :- |
| Disponibilidad del sistema | >= 95% uptime en período de pruebas | QA Team |
| Tasa de fallos críticos | <= 1 fallo crítico por 100 horas de uso | QA Team |
| Recuperación ante errores | Recuperación automática en < 30 segundos | Desarrollo |
| Integridad de datos | 100% de datos sin corrupción ante fallos | Desarrollo |

### Seguridad

**Objetivo:** El sistema protege datos y operaciones contra acceso no autorizado.

| Métrica | Criterio de Aceptación | Responsable |
| :- | :- | :- |
| Vulnerabilidades críticas | 0 vulnerabilidades de severidad crítica | QA Team |
| Control de acceso | Todos los usuarios autenticados correctamente | Desarrollo |
| Integridad de BD de amenazas | Base de datos protegida contra modificación no autorizada | Desarrollo |
| Logs de auditoría | Todas las operaciones sensibles registradas | Desarrollo |

### Usabilidad

**Objetivo:** El sistema es fácil de aprender y usar para el usuario final.

| Métrica | Criterio de Aceptación | Responsable |
| :- | :- | :- |
| Aprendibilidad | 90% de usuarios ejecutan escaneo sin manual | QA Team |
| Claridad de interfaz | Menús y botones claramente identificados | UX/Desarrollo |
| Mensajes de error | 100% de errores con mensaje claro y accionable | QA Team |
| Eficiencia de uso | Escaneo completo ejecutable en 3 clics máximo | UX/Desarrollo |

### Mantenibilidad

**Objetivo:** El sistema es fácil de modificar y corregir.

| Métrica | Criterio de Aceptación | Responsable |
| :- | :- | :- |
| Modularidad del código | Cohesión alta, acoplamiento bajo | Desarrollo |
| Cobertura de pruebas | >= 70% cobertura de código | QA Team |
| Documentación técnica | Documentación de todas las clases y métodos | Desarrollo |
| Facilidad de corrección | Corrección de defecto menor < 2 horas | QA Team/Desarrollo |

### Eficiencia

**Objetivo:** El sistema utiliza recursos de forma óptima.

| Métrica | Criterio de Aceptación | Responsable |
| :- | :- | :- |
| Tiempo de respuesta | Interfaz responde en < 1 segundo | Desarrollo |
| Consumo de memoria | < 200 MB en operación normal | Desarrollo |
| Velocidad de escaneo | Archivo 10 MB escaneado en < 5 segundos | Desarrollo |
| Utilización de CPU | < 80% en operación normal | Desarrollo |

### Plan de Aseguramiento de Calidad

1. **Revisiones de Código**: Mínimo 2 revisores por cambio significativo.
2. **Pruebas Automatizadas**: Ejecución de suite de pruebas unitarias ante cada cambio.
3. **Pruebas de Integración**: Verificación de funcionalidad entre módulos semanalmente.
4. **Pruebas Funcionales**: Casos de prueba documentados para todas las características.
5. **Pruebas de Carga**: Validación de comportamiento bajo carga de 30 usuarios simultáneos.
6. **Pruebas de Seguridad**: Validación de protecciones contra modificación no autorizada.
7. **Auditorías de Documentación**: Verificación que documentación refleja código actual.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 8. <span id="_Toc52661353" class="anchor"></span>**Precedencia y Prioridad**

La implementación del Sistema de Antivirus Académico sigue un orden de precedencia establecido basado en dependencias técnicas y valor académico:

### Fases de Desarrollo y Prioridades

**Fase 1: Arquitectura Base y Motor de Escaneo (Prioridad Crítica)**

| Componente | Descripción | Prioridad | Dependencia |
| :- | :- | :- | :- |
| Diseño arquitectónico | Definición de componentes y interfaces | Crítica | Ninguna |
| Motor de escaneo básico | Capacidad de comparación de firmas | Crítica | Arquitectura |
| Estructura de datos de amenazas | Definición de firma de malware | Alta | Motor de escaneo |

**Fase 2: Componentes Centrales (Prioridad Alta)**

| Componente | Descripción | Prioridad | Dependencia |
| :- | :- | :- | :- |
| Base de datos de amenazas | Almacenamiento y gestión de definiciones | Alta | Estructura de datos |
| Interfaz gráfica básica | Pantalla principal y navegación | Alta | Arquitectura |
| Funcionalidad de escaneo manual | Ejecución de escaneos desde interfaz | Alta | Motor + Base de datos + UI |

**Fase 3: Características Complementarias (Prioridad Media)**

| Componente | Descripción | Prioridad | Dependencia |
| :- | :- | :- | :- |
| Sistema de monitoreo | Detección de cambios en tiempo real | Media | Motor de escaneo |
| Funcionalidad de reportes | Generación de reportes de escaneo | Media | Escaneo manual |
| Sistema de cuarentena | Aislamiento de archivos detectados | Media | Escaneo manual |

**Fase 4: Aseguramiento de Calidad (Prioridad Crítica Paralela)**

| Actividad | Descripción | Prioridad | Dependencia |
| :- | :- | :- | :- |
| Planificación de pruebas | Definición de estrategia y casos de prueba | Crítica | Especificación de requisitos |
| Pruebas unitarias | Verificación de componentes individuales | Alta | Componentes completados |
| Pruebas de integración | Verificación de interacción entre módulos | Alta | Fase 2 completada |
| Pruebas funcionales | Validación de requisitos | Alta | Funcionalidades completadas |
| Reportes de defectos | Documentación de problemas encontrados | Alta | Pruebas en ejecución |

**Fase 5: Documentación y Entrega (Prioridad Alta)**

| Entregable | Descripción | Prioridad | Dependencia |
| :- | :- | :- | :- |
| Documento de Visión | Este documento | Crítica | Análisis inicial |
| Especificación de requisitos | Detalle de todos los requisitos | Crítica | Visión completada |
| Diseño arquitectónico | Diagramas y descripción de estructura | Alta | Especificación |
| Plan de pruebas | Estrategia y casos de prueba | Alta | Especificación |
| Manual de usuario | Guía de uso de la aplicación | Media | Funcionalidades finales |
| Manual técnico | Documentación de código y arquitectura | Alta | Desarrollo completado |
| Informe de calidad | Evidencia de aseguramiento de calidad | Crítica | Todas las pruebas completadas |

### Criterios de Precedencia

1. **Dependencias técnicas**: Componentes fundamentales deben implementarse antes de componentes que los utilizan.
2. **Cadena de valor de pruebas**: Pruebas unitarias antes de integración, integración antes de funcionales.
3. **Valor académico**: Actividades que demuestren aseguramiento de calidad tienen alta prioridad.
4. **Documentación**: Documentación se realiza en paralelo al desarrollo, validando completitud.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 9. <span id="_Toc52661354" class="anchor"></span>**Otros requerimientos del producto**

### Estándares Legales Aplicables

**Propiedad Intelectual**
- El software se desarrolla bajo licencia de uso académico exclusivo.
- Todos los derechos se reservan a la Universidad Privada de Tacna.
- No se permite reproducción, distribución o modificación sin consentimiento expreso.

**Cumplimiento Normativo**
- Proyecto debe cumplir con Código de Ética de Ingeniería de Sistemas de la UPT.
- Se requiere documentación de todas las decisiones de diseño y justificación técnica.
- Evaluación basada en criterios establecidos por el departamento académico.

### Estándares de Comunicación

**Documentación Técnica**
- Toda documentación se redacta en español con terminología técnica en inglés cuando corresponda.
- Se utiliza formato Markdown para documentos de planificación y especificación.
- Diagramas en formato PlantUML o Graphviz para reproducibilidad.
- Versionado de documentos con control de cambios.

**Reportes y Comunicación**
- Reportes de avance semanales al docente supervisor.
- Reportes de defectos en formato estándar con campos: ID, descripción, severidad, estado, asignado a.
- Actas de reuniones documentadas con decisiones y responsabilidades.
- Comunicación formal mediante correo institucional.

**Control de Versiones**
- Repositorio GitHub del proyecto con estructura clara.
- Commits con mensajes descriptivos en idioma español.
- Branches por funcionalidad con nomenclatura estándar (feature/nombre, bugfix/nombre).
- Tags de versión semántica (v1.0, v1.1, etc.).

### Estándares de Cumplimiento de la Plataforma

**Compatibilidad de Sistema Operativo**
- Windows 10 en adelante con .NET Framework 4.7.2 o superior (si se usa C#).
- Linux (Ubuntu 18.04+, Debian 10+) con Python 3.8+ (si se usa Python).
- Interfaz gráfica responsiva a diferentes resoluciones (1024x768 mínimo).

**Estándares de Desarrollo**
- Código desarrollado siguiendo estándares reconocidos del lenguaje utilizado.
- Nombres de variables, funciones y clases en inglés para internacionalización.
- Indentación consistente (4 espacios o 1 tabulación según estándar del lenguaje).
- Máximo 120 caracteres por línea de código.

**Integración Continua (CI)**
- GitHub Actions configurado para ejecutar pruebas ante cada push.
- Compilación/interpretación exitosa requerida para merge de ramas.
- Reporte automático de cobertura de pruebas.

### Estándares de Calidad y Seguridad

**Seguridad de Código**
- Validación de todas las entradas de usuario.
- Prevención de inyección de código mediante parametrización.
- Manejo seguro de excepciones sin exposición de información sensible.
- Protección contra acceso no autorizado a funciones administrativas.

**Calidad de Código**
- Análisis estático con herramientas como SonarQube o linter específico del lenguaje.
- Cobertura de pruebas >= 70% de líneas de código ejecutables.
- Documentación de código con comentarios en funciones complejas.
- Reutilización de código mediante librerías y módulos.

**Gestión de Defectos**
- Registro de todos los defectos encontrados en herramienta de tracking (GitHub Issues).
- Clasificación por severidad: Crítico, Alto, Medio, Bajo.
- Asignación de responsable y seguimiento hasta resolución.
- Cierre de defecto únicamente tras verificación de corrección.

**Pruebas de Regresión**
- Ejecución de suite completa de pruebas antes de cada release.
- Mantención de casos de prueba relevantes conforme el sistema evoluciona.
- Pruebas de compatibilidad con versiones anteriores cuando corresponda.

**Métricas de Calidad**
- Porcentaje de defectos encontrados en pruebas vs. producción (meta: > 95%).
- Densidad de defectos: Defectos por 1000 líneas de código (meta: < 5).
- Eficiencia de pruebas: Porcentaje de defectos encontrados vs. esperados.
- Tiempo medio de corrección de defectos por severidad.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

**CONCLUSIONES**

El Sistema de Antivirus Académico representa una oportunidad integral para que estudiantes de Ingeniería de Sistemas apliquen metodologías de aseguramiento de calidad y pruebas de software en un proyecto prácticamente significativo. El presente documento de visión establece las bases fundamentales para este desarrollo, definiendo claramente:

1. **Propósito académico**: Enfoque en calidad de software más que en complejidad de seguridad informática.

2. **Alcance controlado**: Funcionalidades viables en período académico con recursos disponibles.

3. **Stakeholders definidos**: Claridad sobre roles, responsabilidades y necesidades de todos los actores involucrados.

4. **Características balanceadas**: Equilibrio entre complejidad técnica y profundidad de aseguramiento de calidad.

5. **Criterios de calidad medibles**: Evaluación basada en estándar ISO/IEC 25010 con métricas objetivas.

6. **Restricciones realistas**: Reconocimiento de limitaciones técnicas, organizacionales y legales inherentes a contexto académico.

7. **Documentación exhaustiva**: Énfasis en trazabilidad, registros de defectos y evidencia de verificación/validación.

Este proyecto proporcionará a los estudiantes experiencia práctica valiosa en:
- Desarrollo de software estructurado bajo metodología de aseguramiento de calidad.
- Diseño e implementación de casos de prueba comprensivos.
- Análisis y reporte de defectos de forma sistemática.
- Documentación técnica profesional de nivel industrial.
- Aplicación de estándares reconocidos internacionalmente.

La ejecución exitosa de este proyecto contribuirá significativamente a la formación integral de profesionales en Ingeniería de Sistemas, preparándolos adecuadamente para desafíos de aseguramiento de calidad en la industria de software.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

**RECOMENDACIONES**

Se proponen las siguientes recomendaciones para el desarrollo e implementación exitosa del Sistema de Antivirus Académico:

### Recomendaciones Técnicas

1. **Selección de lenguaje de programación**: Se recomienda Python por su sintaxis clara, abundancia de librerías y herramientas de testing maduros (unittest, pytest), facilitando el aprendizaje de aseguramiento de calidad.

2. **Arquitectura modular**: Implementar separación clara entre lógica de negocio, acceso a datos e interfaz gráfica, permitiendo pruebas independientes de cada capa.

3. **Gestión de versiones**: Utilizar Git desde el inicio del proyecto con estructura de branches clara, facilitando trabajo colaborativo y trazabilidad de cambios.

4. **Herramientas de testing**: Adoptar herramientas de testing automatizado desde etapas tempranas del desarrollo para detectar defectos sin costo incremental.

### Recomendaciones de Calidad

1. **Planificación exhaustiva de pruebas**: Desarrollar matriz de trazabilidad requisitos-casos de prueba antes de codificación, asegurando cobertura completa.

2. **Pruebas tempranas**: Implementar pruebas unitarias inmediatamente tras desarrollo de cada módulo, reduciendo costo de corrección de defectos.

3. **Documentación en paralelo**: Actualizar documentación simultáneamente con desarrollo, evitando obsolescencia y mejorando exactitud.

4. **Métricas desde el inicio**: Recopilar métricas de cobertura, defectos y eficiencia desde las primeras iteraciones para análisis de tendencias.

### Recomendaciones Organizacionales

1. **Roles claramente definidos**: Asignar roles específicos (arquitecto, desarrollador, tester, documentador) aunque sean asumidos por los mismos estudiantes en rotación.

2. **Reuniones estructuradas**: Establecer reuniones semanales con agenda clara, facilitando comunicación y coordinación.

3. **Gestión de cambios**: Implementar proceso formal para cambios de requisitos, evaluando impacto en cronograma y calidad.

4. **Asignación de mentores**: Que docente y ayudantes asuman rol de mentores técnicos, guiando decisiones de arquitectura y calidad.

### Recomendaciones para Evaluación

1. **Evaluación integral**: Considerar no solo funcionalidad sino aseguramiento de calidad, documentación y aplicación de estándares.

2. **Evidencia tangible**: Exigir evidencia de pruebas ejecutadas (casos de prueba, logs, reportes de defectos) como parte de evaluación.

3. **Productos intermedios**: Evaluar incrementalmente documentos de visión, especificación, planes de prueba, no solo producto final.

4. **Retroalimentación continua**: Proporcionar retroalimentación formativa durante desarrollo, permitiendo correcciones en tiempo real.

### Recomendaciones para Futuras Iteraciones

1. **Escalabilidad**: Diseñar sistema considerando extensibilidad para futuras cohortes sin redesarrollo mayor.

2. **Reusabilidad**: Documentar componentes genéricos que puedan ser reutilizados en futuros proyectos académicos.

3. **Mejora continua**: Compilar lecciones aprendidas para mejorar próximas iteraciones del proyecto.

4. **Integración curricular**: Coordinar con otros cursos (Verificación y Validación, Ingeniería de Requisitos) para reforzar conceptos.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

**BIBLIOGRAFÍA**

1. Sommerville, I. (2015). Software Engineering (10th ed.). Pearson Education. ISBN: 978-0133943038.

2. IEEE Computer Society. (2023). IEEE 829-2023 Standard for Software and System Test Documentation. IEEE Standards Association.

3. IEEE Computer Society. (2023). IEEE 1062-2020 Recommended Practice for Software Acquisition. IEEE Standards Association.

4. ISO/IEC. (2023). ISO/IEC 25010:2023 Systems and software engineering — Software product quality and system quality models. International Organization for Standardization.

5. ISO/IEC. (2017). ISO/IEC 25040:2017 Software engineering — Software product Quality Requirements and Evaluation (SQuaRE) — Evaluation process. International Organization for Standardization.

6. Pressman, R. S., & Maxim, B. R. (2014). Software Engineering: A Practitioner's Approach (8th ed.). McGraw-Hill. ISBN: 978-0078918705.

7. Beizer, B. (1990). Software Testing Techniques (2nd ed.). Van Nostrand Reinhold. ISBN: 978-0442206529.

8. Myers, G. J., Sandler, C., & Badgett, T. (2011). The Art of Software Testing (3rd ed.). John Wiley & Sons. ISBN: 978-1118031962.

9. Sinha, N. (2016). Software Quality Assurance: An Introduction. Springer Publishing. ISBN: 978-3319307795.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

**WEBGRAFÍA**

1. GitHub Guides. (2024). Hello World. Recuperado de https://guides.github.com/activities/hello-world/

2. Python Software Foundation. (2024). The Python Tutorial. Recuperado de https://docs.python.org/3/tutorial/

3. Microsoft. (2024). .NET Documentation. Recuperado de https://docs.microsoft.com/en-us/dotnet/

4. JetBrains. (2024). PyCharm Documentation. Recuperado de https://www.jetbrains.com/help/pycharm/

5. ISO. (2024). ISO/IEC 25010 Software product quality. Recuperado de https://www.iso.org/standard/35683.html

6. IEEE. (2024). IEEE 829 Standard. Recuperado de https://standards.ieee.org/standard/829-2023.html

7. SonarQube. (2024). Code Quality and Code Security. Recuperado de https://www.sonarqube.org/

8. Pytest. (2024). Pytest Documentation. Recuperado de https://docs.pytest.org/

9. PlantUML. (2024). PlantUML Language Reference Guide. Recuperado de http://plantuml.com/guide

10. SEI/CMU. (2024). Software Assurance Resources. Recuperado de https://www.sei.cmu.edu/
