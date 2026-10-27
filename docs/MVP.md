# MVP — Sistema Automatizado para la Elaboración de Cartas y Notificaciones Legales

**Documento de Definición del Producto Mínimo Viable (Minimum Viable Product)**

**Empresa:** PluriOne S.A. de C.V. — Develop Talent & Technology  
**Proyecto:** Sistema Automatizado para la Elaboración de Cartas y Notificaciones Legales  
**Versión del documento:** 1.0  
**Estado:** MVP funcional en entorno de desarrollo local  
**Fecha:** Octubre de 2026

---

## 1. Introducción

El presente documento define el Producto Mínimo Viable (MVP) del Sistema Automatizado para la Elaboración de Cartas y Notificaciones Legales, desarrollado para atender necesidades de automatización documental identificadas por PluriOne S.A. de C.V., comercialmente conocida como Develop Talent & Technology.

El MVP representa una primera versión funcional del producto, orientada a comprobar la viabilidad técnica de integrar plantillas documentales, inteligencia artificial generativa, almacenamiento persistente y exportación de documentos desde una aplicación web.

La implementación permite desarrollar el proceso de generación documental desde la captura inicial de información hasta la consulta y exportación de documentos.

El alcance del MVP se limita a las funcionalidades actualmente desarrolladas y comprobadas, diferenciándolas de las capacidades que podrán incorporarse en etapas posteriores.

## 2. Problema que resuelve el MVP

La elaboración de cartas y notificaciones legales requiere recopilar información, seleccionar estructuras documentales, redactar contenido formal y preparar archivos para su utilización.

Estas actividades pueden implicar procesos manuales repetitivos y dificultades para conservar o recuperar documentos previamente elaborados.

El MVP propone centralizar estas operaciones en una aplicación web que permita generar borradores mediante inteligencia artificial, editarlos y almacenarlos en una base de datos.

La solución busca facilitar la preparación de documentos, sin sustituir la revisión humana ni garantizar automáticamente su validez jurídica.

## 3. Objetivo del MVP

Implementar una primera versión funcional del Sistema Automatizado para la Elaboración de Cartas y Notificaciones Legales que permita seleccionar plantillas, capturar información, generar borradores asistidos por inteligencia artificial, editar su contenido, almacenarlos y exportarlos en formatos PDF y Word.

## 4. Usuarios del MVP

### 4.1. Usuario operativo

El usuario operativo representa a la persona encargada de elaborar documentos mediante la aplicación.

Sus actividades consisten en:

- Seleccionar una plantilla.
- Capturar datos documentales.
- Solicitar la generación de un borrador.
- Revisar y editar el contenido.
- Guardar el documento.
- Consultar documentos anteriores.
- Exportar archivos PDF y Word.

### 4.2. Usuarios considerados para futuras versiones

Se contempla la incorporación posterior de administradores y revisores jurídicos, así como mecanismos de autenticación, roles y permisos.

Estos perfiles no se encuentran diferenciados mediante controles de acceso en el MVP actual.

## 5. Alcance funcional del MVP

El producto incluye las siguientes funcionalidades principales:

| ID | Funcionalidad | Estado |
|---|---|---|
| MVP-01 | Interfaz web de generación documental | Implementada |
| MVP-02 | Catálogo de cinco plantillas | Implementada |
| MVP-03 | Formulario de captura de información | Implementada |
| MVP-04 | Generación de borradores mediante Groq API | Implementada |
| MVP-05 | Visualización y edición del borrador | Implementada |
| MVP-06 | Almacenamiento en PostgreSQL | Implementada |
| MVP-07 | Consulta del historial de documentos | Implementada |
| MVP-08 | Exportación en PDF | Implementada |
| MVP-09 | Exportación en Word | Implementada |
| MVP-10 | Incorporación de logotipos y marcas de agua | Implementada |
| MVP-11 | Generación de bloques de firma | Implementada |
| MVP-12 | Persistencia mediante PostgreSQL en Docker | Implementada |

Estas funcionalidades conforman el flujo principal del producto mínimo viable.

## 6. Plantillas disponibles

El MVP incluye cinco tipos de documentos predefinidos.

| Plantilla | Finalidad |
|---|---|
| Notificación de Rescisión Laboral | Elaboración de borradores de comunicación relacionados con la terminación laboral |
| Acta Administrativa por Incumplimiento | Registro formal de hechos o situaciones de incumplimiento |
| Carta de Recomendación Laboral | Elaboración de documentos de recomendación |
| Convenio de Confidencialidad (NDA) | Preparación de borradores de acuerdos de confidencialidad |
| Aviso de Suspensión Temporal de Labores | Comunicación relacionada con la suspensión temporal de actividades laborales |

Actualmente las cinco plantillas comparten un formulario general de captura. El sistema utiliza la plantilla seleccionada y los datos proporcionados para generar contenido adaptado al tipo de documento.

## 7. Flujo operativo del MVP

El funcionamiento del MVP se organiza en las siguientes etapas.

### 7.1. Selección de plantilla

El usuario accede a la interfaz principal y selecciona el tipo de documento que desea elaborar.

### 7.2. Captura de información

El usuario proporciona los datos necesarios, incluyendo información de la empresa, firmante, destinatario, fecha y motivo.

### 7.3. Generación mediante inteligencia artificial

El frontend envía la solicitud al backend, que utiliza la plantilla seleccionada y los datos capturados para solicitar un borrador a Groq API.

### 7.4. Revisión y edición

El contenido generado se presenta en la interfaz y puede modificarse manualmente antes de guardarse.

### 7.5. Almacenamiento

El documento se guarda en PostgreSQL mediante los servicios implementados en FastAPI y SQLAlchemy.

### 7.6. Consulta del historial

Los documentos guardados pueden consultarse posteriormente desde la sección de historial.

### 7.7. Exportación

El usuario puede generar archivos PDF o Word, incorporando las opciones disponibles de presentación, imágenes y firmas.

## 8. Tecnologías utilizadas

| Componente | Tecnología |
|---|---|
| Frontend | React y Vite |
| Interfaz | Tailwind CSS y Lucide React |
| Backend | Python y FastAPI |
| Validación de datos | Pydantic |
| Persistencia | PostgreSQL 16 |
| ORM | SQLAlchemy |
| Inteligencia artificial | Groq API |
| Modelo de IA configurado | openai/gpt-oss-20b |
| Generación PDF | ReportLab |
| Generación Word | python-docx |
| Procesamiento de imágenes | Pillow |
| Contenedores | Docker y Docker Compose |
| Control de versiones | Git y GitHub |
| Entorno de desarrollo | Visual Studio Code |

Las tecnologías indicadas corresponden a la implementación actual del producto.

## 9. Arquitectura mínima

El MVP utiliza una arquitectura cliente-servidor organizada en cuatro componentes principales.

**Frontend:** administra la interacción del usuario, la captura de información y la presentación de documentos.

**Backend:** recibe solicitudes, procesa los datos, administra documentos y coordina los servicios de generación y exportación.

**Servicio de inteligencia artificial:** genera borradores utilizando Groq API.

**Base de datos:** PostgreSQL almacena las plantillas y documentos generados, utilizando Docker para la ejecución del servicio.

El frontend y backend se ejecutan localmente durante el desarrollo, mientras PostgreSQL funciona dentro de un contenedor Docker.

## 10. Modelo de almacenamiento

El sistema utiliza dos entidades principales.

### 10.1. Plantilla

Contiene los documentos base utilizados para generar borradores.

### 10.2. DocumentoGenerado

Almacena el contenido de los documentos, su plantilla relacionada, estado, versión y fecha de creación.

La relación entre ambas entidades permite identificar el tipo de documento utilizado.

Aunque existe un atributo de versión, el MVP no incorpora un mecanismo completo de control de revisiones documentales.

## 11. Funcionalidades excluidas del MVP actual

Los siguientes elementos forman parte de las necesidades identificadas para la evolución del producto, pero no están implementados completamente en la versión actual.

| Funcionalidad | Situación actual |
|---|---|
| Autenticación de usuarios | No implementada |
| Roles y permisos | No implementados |
| Protección de endpoints por usuario | No implementada |
| Carga y gestión de documentos externos | No implementada como módulo independiente |
| Búsqueda avanzada por empleado o tipo | No implementada |
| Control de revisiones y versiones | No implementado completamente |
| Flujos de aprobación | No implementados |
| Validación jurídica automatizada | No comprobada |
| Registro detallado de auditoría | No implementado |

La exclusión de estas funcionalidades delimita el alcance actual y no implica que carezcan de importancia para una versión empresarial posterior.

Especialmente, la autenticación y autorización deben atenderse antes de permitir acceso compartido a información laboral confidencial.

## 12. Criterios de aceptación del MVP

| ID | Criterio | Estado de comprobación |
|---|---|---|
| CA-01 | El sistema muestra las cinco plantillas | Comprobado |
| CA-02 | Permite capturar información documental | Comprobado |
| CA-03 | Genera un borrador mediante Groq | Comprobado |
| CA-04 | Permite modificar el contenido generado | Comprobado |
| CA-05 | Guarda documentos en PostgreSQL | Comprobado |
| CA-06 | Permite consultar el historial | Comprobado |
| CA-07 | Genera documentos PDF | Comprobado |
| CA-08 | Genera documentos Word | Comprobado |
| CA-09 | Permite incorporar logotipos y marcas de agua | Comprobado |
| CA-10 | Conserva documentos después de reiniciar Docker | Comprobado |
| CA-11 | Permite instalar dependencias desde requirements.txt | Comprobado en entorno independiente |
| CA-12 | Permite importar el backend con las dependencias instaladas | Comprobado |

Los estados corresponden a las pruebas realizadas durante el desarrollo. No constituyen una certificación de seguridad, rendimiento o cumplimiento jurídico.

## 13. Pruebas efectuadas

### 13.1. Pruebas funcionales

Se comprobó el funcionamiento de las cinco plantillas, la generación de borradores, la edición manual, el historial y la exportación documental.

### 13.2. Pruebas de integración

Se verificó la interacción entre frontend, backend, Groq API y PostgreSQL en el entorno de desarrollo.

### 13.3. Pruebas de persistencia

Se comprobó la conservación de documentos después de reiniciar el contenedor Docker.

### 13.4. Pruebas de dependencias

Se realizó una instalación de las dependencias de Python 3.11 en un entorno virtual independiente.

La verificación mediante `pip check` no reportó dependencias incompatibles.

### 13.5. Prueba de importación del backend

Se comprobó que el módulo principal del backend podía importarse desde el entorno independiente utilizando las dependencias declaradas.

Esta prueba no sustituye una validación integral del producto en otra computadora.

## 14. Limitaciones conocidas

El MVP presenta las siguientes limitaciones:

1. No existe autenticación ni autorización de usuarios.
2. Los endpoints no cuentan con controles de acceso basados en roles.
3. La validación jurídica requiere revisión humana.
4. El contenido generado depende de la disponibilidad y respuestas de Groq API.
5. Los formularios comparten campos generales entre las cinco plantillas.
6. No se dispone de un historial completo de modificaciones por documento.
7. La implementación se encuentra orientada a ejecución local.
8. No se ha documentado una evaluación formal de rendimiento o carga.
9. La instalación completa del sistema en otra computadora aún requiere verificación adicional.

## 15. Riesgos y medidas de mitigación

| Riesgo | Medida propuesta |
|---|---|
| Exposición de documentos a usuarios no autorizados | Incorporar autenticación, permisos y protección de endpoints |
| Errores en contenido generado por IA | Mantener revisión humana antes de utilizar documentos |
| Indisponibilidad de Groq API | Implementar mensajes de error y estrategias de recuperación |
| Pérdida de datos | Establecer respaldos periódicos de PostgreSQL |
| Errores durante instalación | Mantener actualizados README, requirements.txt y archivos de ejemplo |
| Inconsistencias documentales | Incorporar validaciones específicas por plantilla |

## 16. Entregables del MVP

Los principales entregables de la versión actual son:

- Código fuente del frontend.
- Código fuente del backend.
- Integración de generación documental mediante Groq API.
- Catálogo de cinco plantillas.
- Módulo de captura y edición de contenido.
- Almacenamiento e historial en PostgreSQL.
- Generación de PDF y Word.
- Configuración Docker Compose.
- Archivo de dependencias.
- Archivos de ejemplo de variables de entorno.
- README con instrucciones de instalación.
- Documentación de requisitos PRD.
- Documento de definición del MVP.

## 17. Evolución propuesta después del MVP

La siguiente etapa de desarrollo deberá priorizar:

1. Implementación de inicio de sesión.
2. Definición de al menos dos roles de usuario.
3. Protección de los endpoints de consulta, guardado y exportación.
4. Incorporación de controles de acceso a los documentos.
5. Mejoras de validación y manejo de errores.
6. Pruebas de seguridad y funcionamiento.
7. Funcionalidades adicionales de gestión documental según prioridades de la empresa.

La implementación de búsqueda avanzada, carga de documentos, aprobación y control completo de versiones requerirá una evaluación posterior de alcance y recursos.

## 18. Condiciones para una implementación empresarial

Aunque el flujo principal del MVP se encuentra operativo, su utilización en un entorno empresarial compartido requiere controles adicionales.

La versión actual no debe considerarse preparada para exposición pública o acceso multiusuario sin mecanismos de autenticación, autorización y protección de datos.

Antes de habilitar este tipo de utilización, deben evaluarse los requisitos de confidencialidad, tratamiento de información, respaldos y seguridad del servicio de inteligencia artificial.

## 19. Conclusión

El Producto Mínimo Viable del Sistema Automatizado para la Elaboración de Cartas y Notificaciones Legales demuestra la viabilidad de integrar tecnologías web, inteligencia artificial generativa, persistencia de datos y procesamiento documental en una solución funcional.

Las capacidades implementadas permiten realizar el proceso principal de generación, revisión, almacenamiento, consulta y exportación de documentos desde una misma plataforma.

El MVP cumple con el flujo funcional esencial definido para esta primera versión. Sin embargo, los mecanismos de seguridad, autenticación y gestión documental avanzada continúan como aspectos pendientes para su evolución.

El documento establece el alcance de la versión implementada, sus limitaciones y los criterios que deberán considerarse en las siguientes etapas de desarrollo.