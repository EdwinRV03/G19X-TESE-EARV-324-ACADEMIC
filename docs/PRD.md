# PRD — Sistema Automatizado para la Elaboración de Cartas y Notificaciones Legales

**Documento de Requisitos del Producto (Product Requirements Document)**

**Empresa:** PluriOne S.A. de C.V. — Develop Talent & Technology  
**Proyecto:** Sistema Automatizado para la Elaboración de Cartas y Notificaciones Legales  
**Versión del documento:** 1.0  
**Estado:** Documentación de requisitos y alcance actual  
**Fecha:** Octubre de 2026

---

## 1. Introducción

El presente documento establece los requisitos funcionales, no funcionales, tecnológicos y operativos del Sistema Automatizado para la Elaboración de Cartas y Notificaciones Legales, desarrollado a partir de las necesidades identificadas por PluriOne S.A. de C.V., comercialmente conocida como Develop Talent & Technology.

El sistema consiste en una aplicación web que permite elaborar documentos laborales y notificaciones legales mediante plantillas parametrizadas e inteligencia artificial generativa. Su propósito es facilitar las actividades de redacción, revisión, almacenamiento y exportación de documentos formales.

El producto integra diferentes tecnologías de desarrollo de software, procesamiento documental, bases de datos y servicios de inteligencia artificial, proporcionando una interfaz que permite gestionar el proceso de elaboración de documentos desde un mismo entorno.

Este documento diferencia los requisitos planteados originalmente por la empresa, las funcionalidades implementadas y las capacidades consideradas para futuras versiones.

## 2. Planteamiento del problema

La elaboración de cartas y notificaciones legales puede requerir la captura repetitiva de información, la adaptación manual de documentos y la revisión de elementos formales relacionados con su presentación.

Cuando estas actividades se realizan sin una herramienta especializada, pueden presentarse inconsistencias en los formatos, duplicación de esfuerzos y dificultades para consultar documentos elaborados anteriormente.

Adicionalmente, la generación manual de diferentes tipos de comunicaciones exige mantener una estructura documental adecuada y adaptar su contenido a las circunstancias particulares de cada caso.

Por esta razón, se plantea el desarrollo de un sistema que centralice la captura de información, facilite la elaboración de borradores mediante inteligencia artificial y permita conservar los documentos generados para su consulta posterior.

## 3. Objetivo general

Desarrollar una aplicación web que permita automatizar la elaboración de cartas y notificaciones legales mediante plantillas parametrizadas e inteligencia artificial generativa, facilitando su redacción, edición, almacenamiento y exportación, con el propósito de optimizar los procesos de gestión documental.

## 4. Objetivos específicos

1. Analizar las necesidades relacionadas con la elaboración de documentos laborales y notificaciones legales.
2. Diseñar una arquitectura cliente-servidor que permita integrar una interfaz web, una API REST y una base de datos relacional.
3. Implementar un catálogo de plantillas para la generación de diferentes tipos de documentos.
4. Integrar un servicio de inteligencia artificial que produzca borradores a partir de información proporcionada por el usuario.
5. Permitir la revisión y modificación manual del contenido generado.
6. Almacenar los documentos mediante PostgreSQL para facilitar su consulta posterior.
7. Implementar mecanismos de exportación en formatos PDF y Word.
8. Facilitar la personalización de documentos mediante logotipos institucionales y opciones de presentación.
9. Realizar pruebas funcionales y de integración de los componentes del sistema.
10. Elaborar documentación técnica y de usuario para facilitar la instalación, utilización y mantenimiento del producto.

## 5. Justificación

El desarrollo del Sistema Automatizado para la Elaboración de Cartas y Notificaciones Legales responde a la necesidad de contar con herramientas que faciliten la preparación de documentos formales mediante procesos estructurados y tecnologías de automatización.

La incorporación de inteligencia artificial generativa permite obtener borradores a partir de plantillas y datos capturados, reduciendo las actividades de redacción repetitiva y proporcionando una base editable para la preparación de documentos.

La integración con PostgreSQL permite almacenar la información generada, mientras que los mecanismos de exportación facilitan su utilización en formatos de documentos ampliamente utilizados.

Desde una perspectiva empresarial, la solución contribuye al desarrollo de herramientas tecnológicas relacionadas con la automatización documental y ofrece una base funcional que puede ampliarse mediante controles de seguridad, administración de usuarios y procesos de aprobación.

La aplicación no sustituye la revisión jurídica profesional ni garantiza automáticamente la validez legal de los documentos generados.

## 6. Alcance del producto

### 6.1. Alcance funcional implementado

El sistema contempla actualmente las siguientes capacidades:

- Interfaz web para la captura de información documental.
- Selección de cinco plantillas predefinidas.
- Captura de datos de la empresa, firmante y destinatario.
- Incorporación de fechas y motivos relacionados con el documento.
- Integración con Groq API para generar borradores asistidos por inteligencia artificial.
- Visualización y edición manual del contenido generado.
- Almacenamiento de documentos en PostgreSQL.
- Consulta del historial de documentos guardados.
- Exportación de documentos en PDF.
- Exportación de documentos en Word.
- Incorporación de logotipos institucionales.
- Configuración de posición de imágenes y marcas de agua.
- Generación de espacios y bloques de firma.
- Persistencia de la información mediante PostgreSQL ejecutado en Docker.

### 6.2. Funcionalidades contempladas para evolución

Los requerimientos empresariales originales consideran capacidades adicionales que no forman parte del flujo funcional actualmente comprobado:

- Autenticación y autorización de usuarios.
- Administración de roles y permisos.
- Validaciones jurídicas automatizadas.
- Flujos de revisión y aprobación de documentos.
- Control de versiones documentales con historial de revisiones.
- Búsqueda avanzada por empleado, tipo de documento o fecha.
- Registro de auditoría de operaciones.
- Administración de archivos adjuntos o documentos externos.
- Administración ampliada de plantillas.

Estas funcionalidades deberán analizarse, diseñarse y validarse antes de incorporarlas a futuras versiones.

## 7. Usuarios previstos

### 7.1. Usuario operativo

Persona encargada de elaborar documentos dentro de la plataforma.

Sus actividades contemplan seleccionar plantillas, capturar información, generar borradores, editar contenido, consultar el historial y exportar documentos.

### 7.2. Administrador del sistema

Perfil considerado para una futura implementación de autenticación y permisos.

Podría encargarse de administrar usuarios, controlar accesos y supervisar aspectos de configuración del sistema.

### 7.3. Revisor o responsable jurídico

Perfil considerado para una futura implementación de flujos de validación documental.

Su participación consistiría en revisar el contenido y determinar si cumple con los requisitos formales y jurídicos aplicables antes de su utilización.

**Estado actual:** La aplicación no cuenta con un sistema completo de autenticación y autorización que distinga estos perfiles.

## 8. Requisitos funcionales

| ID | Requisito funcional | Prioridad | Estado |
|---|---|---|---|
| RF-01 | Mostrar una interfaz principal de generación de documentos | Alta | Implementado |
| RF-02 | Permitir seleccionar una plantilla documental | Alta | Implementado |
| RF-03 | Capturar los datos necesarios para la generación | Alta | Implementado |
| RF-04 | Generar borradores mediante inteligencia artificial | Alta | Implementado |
| RF-05 | Permitir editar manualmente el borrador | Alta | Implementado |
| RF-06 | Guardar documentos en PostgreSQL | Alta | Implementado |
| RF-07 | Consultar documentos mediante el historial | Alta | Implementado |
| RF-08 | Exportar documentos en formato PDF | Alta | Implementado |
| RF-09 | Exportar documentos en formato Word | Alta | Implementado |
| RF-10 | Incorporar logotipos y personalización visual | Media | Implementado |
| RF-11 | Generar bloques de firma | Media | Implementado |
| RF-12 | Implementar inicio de sesión de usuarios | Alta | Pendiente |
| RF-13 | Administrar roles y permisos | Alta | Pendiente |
| RF-14 | Controlar versiones y revisiones documentales | Media | Pendiente |
| RF-15 | Implementar flujos de aprobación | Media | Pendiente |
| RF-16 | Incorporar validación jurídica automatizada | Media | Pendiente |
| RF-17 | Permitir búsquedas avanzadas de documentos | Media | Pendiente |

Los requisitos identificados como implementados corresponden al funcionamiento actual reportado y comprobado en el entorno de desarrollo. Los pendientes no deben considerarse funcionalidades disponibles.

## 9. Plantillas documentales

El sistema dispone de cinco plantillas base.

### 9.1. Notificación de Rescisión Laboral

Permite elaborar un borrador de comunicación formal relacionado con la terminación de una relación laboral, utilizando la información capturada y el motivo indicado.

### 9.2. Acta Administrativa por Incumplimiento

Permite generar un documento orientado al registro de hechos o situaciones relacionadas con incumplimientos dentro de un entorno laboral.

### 9.3. Carta de Recomendación Laboral

Facilita la elaboración de una comunicación formal de recomendación a partir de la información proporcionada sobre el destinatario.

### 9.4. Convenio de Confidencialidad (NDA)

Permite generar un borrador de acuerdo relacionado con obligaciones de confidencialidad y protección de información.

### 9.5. Aviso de Suspensión Temporal de Labores

Permite elaborar un borrador de comunicación formal relacionado con una suspensión temporal de actividades laborales.

Las cinco plantillas utilizan actualmente una estructura compartida de campos de captura. El contenido generado se adapta al tipo de documento seleccionado.

La utilización formal de cualquiera de estos documentos requiere revisión y, cuando corresponda, adecuación jurídica.

## 10. Requisitos no funcionales

| ID | Requisito | Descripción |
|---|---|---|
| RNF-01 | Usabilidad | La interfaz debe permitir una navegación comprensible y una captura organizada de información |
| RNF-02 | Mantenibilidad | El código debe conservar una separación clara entre interfaz, API, lógica de negocio y persistencia |
| RNF-03 | Persistencia | La información almacenada debe mantenerse disponible después de reiniciar el servicio PostgreSQL |
| RNF-04 | Integridad | El sistema debe evitar registros inconsistentes y validar los datos recibidos |
| RNF-05 | Seguridad | Las credenciales no deben almacenarse directamente en el código publicado |
| RNF-06 | Confidencialidad | El acceso a documentos laborales debe restringirse a usuarios autorizados |
| RNF-07 | Portabilidad | El proyecto debe contar con instrucciones reproducibles de instalación |
| RNF-08 | Compatibilidad | La aplicación debe funcionar en navegadores modernos compatibles con las tecnologías utilizadas |
| RNF-09 | Disponibilidad | Los servicios deben poder iniciarse y verificarse mediante procedimientos documentados |
| RNF-10 | Calidad documental | Los documentos exportados deben conservar una presentación formal y legible |

Los requisitos no funcionales constituyen criterios de calidad del producto. Su inclusión no implica que todos hayan sido verificados mediante pruebas específicas.

## 11. Arquitectura tecnológica

El sistema está desarrollado bajo una arquitectura cliente-servidor con comunicación mediante API REST.

### 11.1. Frontend

**Tecnologías:** React, Vite, Tailwind CSS y Lucide React.

Responsabilidades principales:

- Presentar la interfaz del sistema.
- Administrar la selección de plantillas.
- Capturar información documental.
- Mostrar y permitir la edición del borrador.
- Consultar el historial.
- Solicitar la exportación de documentos.

### 11.2. Backend

**Tecnologías:** Python, FastAPI, Pydantic y SQLAlchemy.

Responsabilidades principales:

- Recibir y procesar solicitudes HTTP.
- Consultar las plantillas disponibles.
- Integrar los datos proporcionados por el usuario.
- Comunicarse con el servicio de inteligencia artificial.
- Almacenar y recuperar documentos.
- Generar archivos de exportación.

### 11.3. Inteligencia artificial

**Servicio:** Groq API.

**Modelo configurado:** `openai/gpt-oss-20b`.

El sistema envía instrucciones de redacción, contenido de la plantilla y datos variables para obtener un borrador documental.

El contenido devuelto puede modificarse manualmente antes de su almacenamiento.

### 11.4. Base de datos

**Tecnología:** PostgreSQL 16.

**Herramienta de acceso:** SQLAlchemy.

La base de datos almacena las plantillas y el contenido de los documentos generados.

### 11.5. Exportación documental

**Tecnologías:** ReportLab, python-docx y Pillow.

Estas herramientas permiten generar archivos PDF y Word, así como procesar las imágenes utilizadas en los documentos.

### 11.6. Infraestructura

**Tecnologías:** Docker y Docker Compose.

El servicio PostgreSQL se ejecuta mediante un contenedor con almacenamiento persistente. El frontend y el backend se ejecutan localmente durante el desarrollo.

## 12. Modelo de datos

### 12.1. Entidad Plantilla

Almacena la información de las plantillas base utilizadas por el sistema.

Entre sus atributos principales se encuentran:

- Identificador.
- Título.
- Cuerpo base.
- Fecha de creación.

### 12.2. Entidad DocumentoGenerado

Almacena la información asociada con los documentos generados.

Entre sus atributos principales se encuentran:

- Identificador.
- Identificador de plantilla.
- Contenido.
- Estado.
- Versión.
- Fecha de creación.

### 12.3. Relación entre entidades

Una plantilla puede asociarse con múltiples documentos generados.

El campo de versión disponible en el modelo no representa, por sí solo, un mecanismo completo de control de cambios ni un historial de revisiones.

## 13. Flujo de funcionamiento

1. El usuario accede a la interfaz principal.
2. Selecciona una de las cinco plantillas.
3. Captura los datos correspondientes al documento.
4. Configura opcionalmente un logotipo y su posición.
5. Solicita la generación del borrador.
6. El backend envía la información al servicio de inteligencia artificial.
7. El servicio devuelve el contenido generado.
8. El usuario revisa y modifica el borrador.
9. El documento se guarda en PostgreSQL.
10. El sistema permite consultar el documento desde el historial.
11. El usuario puede solicitar su exportación en PDF o Word.

## 14. Criterios de aceptación

| ID | Criterio | Método de verificación |
|---|---|---|
| CA-01 | Las cinco plantillas se muestran correctamente | Prueba funcional de interfaz |
| CA-02 | La IA genera un borrador con datos capturados | Prueba de integración con Groq |
| CA-03 | El contenido generado puede editarse | Prueba funcional |
| CA-04 | El documento puede almacenarse | Comprobación de persistencia |
| CA-05 | El historial permite consultar documentos guardados | Prueba funcional |
| CA-06 | El sistema permite generar PDF | Prueba de exportación |
| CA-07 | El sistema permite generar Word | Prueba de exportación |
| CA-08 | Los logotipos se incorporan correctamente | Inspección del archivo generado |
| CA-09 | La información persiste después de reiniciar Docker | Prueba de persistencia |
| CA-10 | Las dependencias pueden instalarse desde requirements.txt | Instalación en entorno virtual limpio |
| CA-11 | El backend puede importar sus módulos principales | Prueba de importación |

Estos criterios permiten determinar el cumplimiento del alcance funcional actual. Su ejecución debe documentarse mediante evidencias cuando se realicen entregas o evaluaciones formales.

## 15. Restricciones y consideraciones

- El sistema depende de una conexión válida con Groq API para la generación de borradores.
- La generación de contenido puede variar según las respuestas del modelo de inteligencia artificial.
- La precisión jurídica no está garantizada automáticamente.
- El sistema requiere revisar manualmente los documentos antes de utilizarlos formalmente.
- La implementación actual no cuenta con autenticación y autorización completas.
- La base de datos depende de la disponibilidad del servicio PostgreSQL.
- La implementación está orientada actualmente a un entorno de desarrollo local.
- No se consideran implementados los flujos completos de aprobación ni la auditoría documental.
- La información confidencial enviada a servicios externos requiere controles organizacionales adecuados.

## 16. Riesgos del proyecto

| Riesgo | Consecuencia potencial | Medida propuesta |
|---|---|---|
| Generación de información incorrecta por IA | Documentos con errores de contenido | Revisión humana obligatoria |
| Acceso no autorizado | Exposición de información documental | Implementar autenticación y permisos |
| Fallos de PostgreSQL | Interrupción del almacenamiento | Respaldos y mantenimiento |
| Dependencia de Groq API | Fallos en la generación de borradores | Manejo de errores y disponibilidad |
| Configuración incorrecta | Problemas durante la instalación | Documentar variables y dependencias |
| Modificaciones no controladas | Regresiones funcionales | Control de versiones y pruebas |

## 17. Estrategia de pruebas

Las actividades de verificación se organizan en las siguientes categorías:

**Pruebas funcionales:** selección de plantillas, captura de información, generación de borradores, edición, historial y exportaciones.

**Pruebas de integración:** comunicación entre React, FastAPI, Groq API y PostgreSQL.

**Pruebas de persistencia:** recuperación de documentos después de reiniciar los servicios.

**Pruebas de instalación:** instalación de dependencias en un entorno Python independiente y comprobación de importaciones.

**Pruebas de seguridad pendientes:** validación de accesos, permisos, manejo de documentos confidenciales y protección de endpoints.

Las pruebas confirmadas durante el desarrollo no sustituyen una batería completa de pruebas automatizadas.

## 18. Entregables del proyecto

Los entregables contemplados son:

1. Código fuente del frontend.
2. Código fuente del backend.
3. Configuración de PostgreSQL mediante Docker Compose.
4. Integración con Groq API.
5. Módulo de generación y edición de documentos.
6. Módulo de historial.
7. Funciones de exportación en PDF y Word.
8. Archivo README con instrucciones de instalación.
9. Archivo de dependencias del backend.
10. Archivos de ejemplo de variables de entorno.
11. Documento PRD.
12. Documento de definición del MVP.
13. Manual técnico y manual de usuario, como entregables documentales pendientes.
14. Evidencias de pruebas y mantenimiento, según el avance de las siguientes etapas.

## 19. Evolución del producto

La evolución del sistema deberá priorizar las funcionalidades que mejoren la seguridad, la gestión documental y la calidad técnica.

Entre los desarrollos propuestos destacan la implementación de autenticación, administración de roles, protección de endpoints, mecanismos de búsqueda, control de revisiones y flujos de aprobación.

La incorporación de nuevas funcionalidades estará sujeta a su análisis técnico, prioridad empresarial y validación funcional.

## 20. Conclusión

El Sistema Automatizado para la Elaboración de Cartas y Notificaciones Legales constituye una solución web funcional para la generación, edición, almacenamiento, consulta y exportación de documentos mediante inteligencia artificial.

La arquitectura desarrollada integra tecnologías de frontend, backend, persistencia de datos y procesamiento documental, proporcionando una base sobre la que pueden incorporarse nuevas capacidades.

El producto cubre las funciones principales de generación documental, mientras que los aspectos relacionados con seguridad de acceso, validación jurídica automatizada, aprobación y control avanzado de versiones permanecen como áreas de mejora.

El PRD establece una referencia para el mantenimiento, evaluación y evolución del sistema, distinguiendo el alcance implementado de los requisitos planteados para futuras etapas.