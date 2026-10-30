
# PRD — Sistema Automatizado para la Elaboración de Cartas y Notificaciones Legales

**Documento de Requisitos del Producto (Product Requirements Document)**

**Empresa:** PluriOne S.A. de C.V. — Develop Talent & Technology
**Proyecto:** Sistema Automatizado para la Elaboración de Cartas y Notificaciones Legales
**Versión del documento:** 1.1
**Estado:** Documentación de requisitos y alcance actual actualizado
**Fecha:** Octubre de 2026

---

## 1. Introducción

El documento establece los requisitos funcionales, no funcionales, tecnológicos y operativos del Sistema Automatizado para la Elaboración de Cartas y Notificaciones Legales, desarrollado a partir de las necesidades identificadas por PluriOne S.A. de C.V., comercialmente conocida como Develop Talent & Technology.

El sistema consiste en una aplicación web que permite elaborar documentos laborales y notificaciones legales mediante plantillas parametrizadas e inteligencia artificial generativa. Su propósito es facilitar las actividades de redacción, revisión, almacenamiento y exportación de documentos formales.

El producto integra diferentes tecnologías de desarrollo de software, procesamiento documental, bases de datos y servicios de inteligencia artificial, proporcionando una interfaz que permite gestionar el proceso de elaboración de documentos desde un mismo entorno.

Este documento diferencia los requisitos planteados originalmente por la empresa, las funcionalidades implementadas y las capacidades consideradas para futuras versiones.

La versión actual también incorpora autenticación, administración de usuarios, edición de documentos guardados, control de versiones y herramientas de búsqueda documental, ampliando las capacidades contempladas inicialmente.

## 2. Planteamiento del problema

La elaboración de cartas y notificaciones legales puede requerir la captura repetitiva de información, la adaptación manual de documentos y la revisión de elementos formales relacionados con su presentación.

Cuando estas actividades se realizan sin una herramienta especializada, pueden presentarse inconsistencias en los formatos, duplicación de esfuerzos y dificultades para consultar documentos elaborados anteriormente.

Adicionalmente, la generación manual de diferentes tipos de comunicaciones exige mantener una estructura documental adecuada y adaptar su contenido a las circunstancias particulares de cada caso.

Por esta razón, se plantea el desarrollo de un sistema que centralice la captura de información, facilite la elaboración de borradores mediante inteligencia artificial y permita conservar los documentos generados para su consulta posterior.

Asimismo, se considera necesario administrar el acceso a la información, permitir modificaciones posteriores sin perder versiones anteriores y facilitar la localización de documentos mediante criterios de búsqueda.

## 3. Objetivo general

Desarrollar una aplicación web que permita automatizar la elaboración de cartas y notificaciones legales mediante plantillas parametrizadas e inteligencia artificial generativa, facilitando su redacción, edición, almacenamiento y exportación, con el propósito de optimizar los procesos de gestión documental.

La solución incorpora mecanismos de autenticación, administración de usuarios, control de acceso, edición de documentos guardados y conservación de versiones anteriores para fortalecer la gestión documental.

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
11. Implementar autenticación de usuarios mediante credenciales y tokens de acceso.
12. Establecer roles y permisos para controlar las funcionalidades disponibles.
13. Incorporar herramientas de administración de usuarios y recuperación de contraseñas.
14. Permitir la edición de documentos previamente almacenados.
15. Conservar y consultar versiones anteriores de los documentos.
16. Facilitar la búsqueda por nombre del empleado y el filtrado por plantilla.
17. Almacenar los datos variables utilizados durante la generación documental.
18. Aplicar mecanismos de control de acceso a los documentos y sus versiones.

## 5. Justificación

El desarrollo del Sistema Automatizado para la Elaboración de Cartas y Notificaciones Legales responde a la necesidad de contar con herramientas que faciliten la preparación de documentos formales mediante procesos estructurados y tecnologías de automatización.

La incorporación de inteligencia artificial generativa permite obtener borradores a partir de plantillas y datos capturados, reduciendo las actividades de redacción repetitiva y proporcionando una base editable para la preparación de documentos.

La integración con PostgreSQL permite almacenar la información generada, mientras que los mecanismos de exportación facilitan su utilización en formatos de documentos ampliamente utilizados.

Desde una perspectiva empresarial, la solución contribuye al desarrollo de herramientas tecnológicas relacionadas con la automatización documental y ofrece una base funcional que puede ampliarse mediante controles de seguridad, administración de usuarios y procesos de aprobación.

La aplicación no sustituye la revisión jurídica profesional ni garantiza automáticamente la validez legal de los documentos generados.

La incorporación de autenticación, permisos y control de versiones permite fortalecer la administración de la información, limitar el acceso según el usuario y conservar antecedentes de modificaciones documentales.

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
- Inicio de sesión mediante correo electrónico y contraseña.
- Autenticación mediante tokens JWT.
- Administración de usuarios con roles de administrador y usuario.
- Creación, activación y desactivación de cuentas de usuario.
- Recuperación y cambio de contraseñas.
- Protección de endpoints mediante autenticación y validación de permisos.
- Consulta de documentos según el usuario autorizado.
- Edición de documentos previamente guardados.
- Conservación del contenido de versiones anteriores.
- Consulta del historial de versiones.
- Almacenamiento de datos variables asociados a documentos.
- Búsqueda de documentos por nombre del empleado.
- Filtrado del historial por tipo de plantilla.
- Inicialización de las plantillas desde el backend.

Las funcionalidades de edición y versionado fueron comprobadas mediante documentos de prueba. También se verificó el bloqueo de consulta de versiones ajenas mediante una respuesta HTTP 403 Forbidden.

Las funciones de exportación PDF y Word fueron comprobadas anteriormente, aunque requieren una nueva prueba de regresión después de las modificaciones recientes.

### 6.2. Funcionalidades contempladas para evolución

Los requerimientos empresariales originales consideran capacidades adicionales que no forman parte del flujo funcional actualmente comprobado:

- Validaciones jurídicas automatizadas.
- Flujos de revisión y aprobación de documentos.
- Búsqueda avanzada por fechas.
- Registro integral de auditoría de operaciones.
- Administración de archivos adjuntos o documentos externos.
- Administración ampliada de plantillas.
- Pruebas automatizadas de regresión y seguridad.
- Preparación del sistema para un despliegue empresarial.
- Evaluaciones formales de rendimiento y carga.

La autenticación, administración de roles, búsqueda por empleado y plantilla y control básico de versiones ya forman parte de la implementación actual, por lo que dejaron de considerarse funcionalidades pendientes.

Las capacidades restantes deberán analizarse, diseñarse y validarse antes de incorporarlas a futuras versiones.

## 7. Usuarios previstos

### 7.1. Usuario operativo

Persona encargada de elaborar documentos dentro de la plataforma.

Sus actividades contemplan seleccionar plantillas, capturar información, generar borradores, editar contenido, consultar el historial y exportar documentos.

Actualmente dispone de autenticación y puede consultar, editar y revisar las versiones de los documentos que le corresponden.

### 7.2. Administrador del sistema

Perfil encargado de administrar usuarios, controlar accesos y supervisar aspectos de configuración del sistema.

La versión actual permite al administrador:

- Iniciar sesión mediante credenciales.
- Consultar su información de perfil.
- Crear cuentas de usuario.
- Consultar los usuarios registrados.
- Activar o desactivar cuentas.
- Gestionar las funciones autorizadas de contraseñas.
- Acceder a las funcionalidades administrativas protegidas.
- Realizar operaciones documentales de acuerdo con sus permisos.

Las acciones administrativas se encuentran restringidas mediante validaciones de rol en el backend.

### 7.3. Revisor o responsable jurídico

Perfil considerado para una futura implementación de flujos de validación documental.

Su participación consistiría en revisar el contenido y determinar si cumple con los requisitos formales y jurídicos aplicables antes de su utilización.

**Estado actual:** La aplicación cuenta con autenticación y autorización para los roles administrador y usuario. El perfil independiente de revisor jurídico y los flujos formales de aprobación continúan pendientes.

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
| RF-08 | Exportar documentos en formato PDF | Alta | Implementado; pendiente prueba de regresión |
| RF-09 | Exportar documentos en formato Word | Alta | Implementado; pendiente prueba de regresión |
| RF-10 | Incorporar logotipos y personalización visual | Media | Implementado |
| RF-11 | Generar bloques de firma | Media | Implementado |
| RF-12 | Implementar inicio de sesión de usuarios | Alta | Implementado |
| RF-13 | Administrar roles y permisos | Alta | Implementado |
| RF-14 | Controlar versiones y revisiones documentales | Alta | Implementado |
| RF-15 | Implementar flujos de aprobación | Media | Pendiente |
| RF-16 | Incorporar validación jurídica automatizada | Media | Pendiente |
| RF-17 | Permitir búsquedas avanzadas de documentos | Media | Implementado parcialmente: empleado y plantilla |
| RF-18 | Crear cuentas desde el módulo de administración | Alta | Implementado |
| RF-19 | Activar y desactivar usuarios | Alta | Implementado |
| RF-20 | Restringir funciones administrativas por rol | Alta | Implementado |
| RF-21 | Permitir recuperación de contraseñas | Alta | Implementado |
| RF-22 | Permitir cambio de contraseña | Alta | Implementado |
| RF-23 | Proteger endpoints mediante JWT | Alta | Implementado |
| RF-24 | Restringir acceso a documentos según permisos | Alta | Implementado; pruebas parciales |
| RF-25 | Editar documentos previamente guardados | Alta | Implementado |
| RF-26 | Conservar versiones anteriores durante la edición | Alta | Implementado |
| RF-27 | Consultar versiones anteriores y versión actual | Alta | Implementado |
| RF-28 | Almacenar datos variables de los documentos | Alta | Implementado |
| RF-29 | Buscar documentos por nombre del empleado | Media | Implementado |
| RF-30 | Filtrar documentos por plantilla | Media | Implementado |
| RF-31 | Inicializar las plantillas al iniciar el backend | Media | Implementado |
| RF-32 | Evitar sobrescrituras mediante validación de versión | Alta | Implementado |
| RF-33 | Mostrar un mensaje cuando la búsqueda no encuentre resultados | Baja | Implementado |
| RF-34 | Mantener un registro integral de auditoría de operaciones | Media | Pendiente |

Los requisitos identificados como implementados corresponden a funcionalidades incorporadas al código del proyecto.

Los requisitos parcialmente implementados o pendientes requieren desarrollo adicional o pruebas específicas antes de considerarse completamente validados.

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

**Actualización técnica:** Las plantillas base se encuentran definidas en el módulo `backend/app/plantillas.py`. Durante el inicio del backend se comprueba su existencia en PostgreSQL para registrar las faltantes y evitar inserciones repetidas.

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
| RNF-11 | Autenticación | Las operaciones protegidas deben requerir credenciales válidas y un token JWT |
| RNF-12 | Protección de contraseñas | Las contraseñas deben almacenarse mediante algoritmos de hash seguros como Argon2 |
| RNF-13 | Autorización | Las acciones administrativas y documentales deben validar los permisos del usuario |
| RNF-14 | Trazabilidad documental | Las modificaciones deben conservar el contenido de las versiones anteriores |
| RNF-15 | Consistencia de versiones | La edición debe verificar la versión vigente del documento |
| RNF-16 | Protección de configuración | Las claves API y contraseñas deben gestionarse mediante variables de entorno |
| RNF-17 | Recuperación de acceso | Los mecanismos de recuperación de contraseñas deben validar la identidad y proteger los datos sensibles |
| RNF-18 | Recuperación de datos | Se deben definir procedimientos de respaldo y restauración de PostgreSQL |

Los requisitos no funcionales constituyen criterios de calidad del producto. Su inclusión no implica que todos hayan sido verificados mediante pruebas específicas.

La autenticación, la asignación de roles y la comprobación de permisos cuentan con pruebas funcionales parciales. Las auditorías de seguridad, rendimiento y recuperación ante fallos permanecen pendientes.

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
- Presentar el inicio de sesión y recuperación de contraseña.
- Mostrar las funciones disponibles según el rol del usuario.
- Administrar usuarios desde el módulo autorizado.
- Permitir editar documentos guardados.
- Consultar el historial de versiones.
- Buscar documentos por empleado y filtrarlos por plantilla.
- Mostrar mensajes de validación y errores.

### 11.2. Backend

**Tecnologías:** Python, FastAPI, Pydantic y SQLAlchemy.

Responsabilidades principales:

- Recibir y procesar solicitudes HTTP.
- Consultar las plantillas disponibles.
- Integrar los datos proporcionados por el usuario.
- Comunicarse con el servicio de inteligencia artificial.
- Almacenar y recuperar documentos.
- Generar archivos de exportación.
- Autenticar usuarios mediante JWT.
- Validar los permisos según el rol.
- Gestionar usuarios y sus estados.
- Proporcionar funciones de recuperación y cambio de contraseña.
- Guardar modificaciones documentales.
- Conservar las versiones anteriores.
- Consultar el historial de versiones.
- Comprobar la versión actual antes de aplicar cambios.
- Inicializar las plantillas existentes durante el arranque del servicio.

### 11.3. Inteligencia artificial

**Servicio:** Groq API.

**Modelo configurado:** `openai/gpt-oss-20b`.

El sistema envía instrucciones de redacción, contenido de la plantilla y datos variables para obtener un borrador documental.

El contenido devuelto puede modificarse manualmente antes de su almacenamiento.

### 11.4. Base de datos

**Tecnología:** PostgreSQL 16.

**Herramienta de acceso:** SQLAlchemy.

La base de datos almacena las plantillas y el contenido de los documentos generados.

La implementación actual también contempla entidades para usuarios y versiones documentales, así como el almacenamiento de datos variables mediante campos JSONB.

### 11.5. Exportación documental

**Tecnologías:** ReportLab, python-docx y Pillow.

Estas herramientas permiten generar archivos PDF y Word, así como procesar las imágenes utilizadas en los documentos.

Las exportaciones deben volver a comprobarse después de las modificaciones recientes al backend.

### 11.6. Infraestructura

**Tecnologías:** Docker y Docker Compose.

El servicio PostgreSQL se ejecuta mediante un contenedor con almacenamiento persistente. El frontend y el backend se ejecutan localmente durante el desarrollo.

El proyecto utiliza archivos de configuración de ejemplo para documentar las variables necesarias de PostgreSQL, Groq API, autenticación y correo electrónico.

### 11.7. Autenticación y seguridad

El backend utiliza autenticación mediante tokens JWT para controlar el acceso a los endpoints protegidos.

Las contraseñas se almacenan mediante hashes Argon2.

Los permisos distinguen entre los roles administrador y usuario.

Las funciones administrativas requieren autorización, mientras que las operaciones documentales verifican el acceso correspondiente al usuario autenticado.

### 11.8. Gestión de versiones

La edición documental se realiza mediante endpoints específicos de FastAPI.

Antes de guardar una modificación, el backend comprueba la versión vigente del documento.

La versión anterior se conserva en PostgreSQL y el documento principal recibe un nuevo número de versión.

Esto permite consultar los antecedentes de edición y reducir los riesgos de sobrescritura accidental.

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
- Datos variables utilizados durante la generación.

### 12.3. Relación entre entidades

Una plantilla puede asociarse con múltiples documentos generados.

El sistema también relaciona los documentos con sus usuarios y mantiene un registro independiente de versiones anteriores.

### 12.4. Entidad Usuario

Almacena la información de las cuentas autorizadas para utilizar el sistema.

Entre sus atributos principales se encuentran:

- Identificador.
- Nombre.
- Correo electrónico.
- Hash de contraseña.
- Rol.
- Estado activo o inactivo.
- Fecha de creación.

Los roles establecidos son `admin` y `usuario`.

### 12.5. Entidad VersionDocumento

Almacena las versiones anteriores de los documentos editados.

Entre sus atributos principales se encuentran:

- Identificador.
- Identificador del documento relacionado.
- Número de versión.
- Contenido archivado.
- Datos variables.
- Fecha de conservación de la versión.

La combinación del identificador del documento y su número de versión cuenta con una restricción de unicidad.

### 12.6. Persistencia y consistencia

El contenido principal de cada documento permanece en la entidad DocumentoGenerado.

Al realizar una edición, el sistema conserva el contenido anterior en VersionDocumento y actualiza la versión del documento principal.

El backend comprueba la versión indicada por el cliente para evitar modificaciones basadas en información desactualizada.

La persistencia se realiza mediante PostgreSQL y SQLAlchemy.

## 13. Flujo de funcionamiento

1. El usuario accede a la aplicación web.
2. Inicia sesión mediante correo electrónico y contraseña.
3. El backend valida las credenciales y proporciona un token de acceso.
4. El usuario accede a las funcionalidades autorizadas según su rol.
5. Selecciona una de las cinco plantillas.
6. Captura los datos correspondientes al documento.
7. Configura opcionalmente un logotipo y su posición.
8. Solicita la generación del borrador.
9. El backend envía la información al servicio de inteligencia artificial.
10. El servicio devuelve el contenido generado.
11. El usuario revisa y modifica el borrador.
12. El documento se guarda en PostgreSQL junto con sus datos variables.
13. El usuario puede consultar el documento desde el historial.
14. Puede buscar documentos por nombre del empleado.
15. Puede filtrar los documentos por plantilla.
16. Puede abrir un documento previamente guardado para modificarlo.
17. El backend valida los permisos y la versión actual.
18. La versión anterior se conserva y se registra la modificación.
19. El usuario puede consultar las versiones anteriores y la vigente.
20. El sistema permite solicitar la exportación en PDF o Word.
21. El administrador puede acceder a las funciones de gestión de usuarios.
22. El usuario puede cerrar su sesión al finalizar.

## 14. Criterios de aceptación

| ID | Criterio | Método de verificación | Estado |
|---|---|---|---|
| CA-01 | Las cinco plantillas se muestran correctamente | Prueba funcional de interfaz | Comprobado |
| CA-02 | La IA genera un borrador con datos capturados | Prueba de integración con Groq | Comprobado |
| CA-03 | El contenido generado puede editarse | Prueba funcional | Comprobado |
| CA-04 | El documento puede almacenarse | Comprobación de persistencia | Comprobado |
| CA-05 | El historial permite consultar documentos guardados | Prueba funcional | Comprobado |
| CA-06 | El sistema permite generar PDF | Prueba de exportación | Comprobado anteriormente; repetir |
| CA-07 | El sistema permite generar Word | Prueba de exportación | Comprobado anteriormente; repetir |
| CA-08 | Los logotipos se incorporan correctamente | Inspección del archivo generado | Comprobado anteriormente |
| CA-09 | La información persiste después de reiniciar Docker | Prueba de persistencia | Comprobado |
| CA-10 | Las dependencias pueden instalarse desde requirements.txt | Instalación en entorno virtual limpio | Comprobado anteriormente |
| CA-11 | El backend puede importar sus módulos principales | Prueba de importación | Comprobado |
| CA-12 | El sistema permite iniciar sesión mediante JWT | Prueba de autenticación | Comprobado |
| CA-13 | El usuario normal no puede administrar cuentas | Prueba de autorización | Comprobado |
| CA-14 | El administrador puede crear y gestionar usuarios | Prueba funcional | Comprobado |
| CA-15 | Se permite recuperar y cambiar contraseñas | Prueba funcional | Comprobado |
| CA-16 | El usuario puede modificar un documento guardado | Prueba de edición | Comprobado |
| CA-17 | Las modificaciones generan nuevas versiones | Prueba de versionado | Comprobado |
| CA-18 | Se conserva el contenido de versiones anteriores | Consulta de PostgreSQL y API | Comprobado |
| CA-19 | Las versiones pueden consultarse desde React | Prueba de interfaz | Comprobado |
| CA-20 | El historial permite buscar por empleado | Prueba de búsqueda | Comprobado |
| CA-21 | El historial permite filtrar por plantilla | Prueba de filtrado | Comprobado |
| CA-22 | El usuario normal únicamente ve sus documentos | Prueba funcional | Comprobado |
| CA-23 | Se bloquea la consulta de versiones ajenas | Solicitud autenticada | Comprobado: HTTP 403 |
| CA-24 | Se bloquea la edición de documentos ajenos | Prueba de autorización | Pendiente de comprobación específica |
| CA-25 | El backend rechaza ediciones basadas en versiones desactualizadas | Prueba de concurrencia | Pendiente de comprobación específica |
| CA-26 | Las plantillas se inicializan sin duplicarse | Prueba de arranque | Comprobado |
| CA-27 | El frontend compila después de los cambios | npm run build | Comprobado |

Estos criterios permiten determinar el cumplimiento del alcance funcional actual. Su ejecución debe documentarse mediante evidencias cuando se realicen entregas o evaluaciones formales.

Los criterios pendientes no deben considerarse validados únicamente porque su lógica esté implementada.

## 15. Restricciones y consideraciones

- El sistema depende de una conexión válida con Groq API para la generación de borradores.
- La generación de contenido puede variar según las respuestas del modelo de inteligencia artificial.
- La precisión jurídica no está garantizada automáticamente.
- El sistema requiere revisar manualmente los documentos antes de utilizarlos formalmente.
- La implementación cuenta con autenticación y autorización, pero requiere completar las verificaciones de seguridad.
- La base de datos depende de la disponibilidad del servicio PostgreSQL.
- La implementación está orientada actualmente a un entorno de desarrollo local.
- No se consideran implementados los flujos completos de aprobación ni la auditoría documental.
- La información confidencial enviada a servicios externos requiere controles organizacionales adecuados.
- Las contraseñas y claves API deben mantenerse fuera del repositorio público.
- La recuperación de contraseñas requiere una configuración válida del servicio SMTP.
- El sistema no dispone todavía de pruebas formales de rendimiento y carga.
- La exportación PDF y Word requiere repetir pruebas después de los cambios recientes.
- El versionado conserva revisiones documentales, pero no sustituye un sistema integral de auditoría.
- La instalación completa en un entorno empresarial independiente necesita validación adicional.

## 16. Riesgos del proyecto

| Riesgo | Consecuencia potencial | Medida propuesta |
|---|---|---|
| Generación de información incorrecta por IA | Documentos con errores de contenido | Revisión humana obligatoria |
| Acceso no autorizado | Exposición de información documental | Mantener autenticación, autorización y pruebas de permisos |
| Fallos de PostgreSQL | Interrupción del almacenamiento | Respaldos y mantenimiento |
| Dependencia de Groq API | Fallos en la generación de borradores | Manejo de errores y disponibilidad |
| Configuración incorrecta | Problemas durante la instalación | Documentar variables y dependencias |
| Modificaciones no controladas | Regresiones funcionales | Control de versiones y pruebas |
| Exposición de credenciales | Acceso indebido a los servicios | Variables de entorno y exclusión de secretos en Git |
| Ediciones simultáneas | Sobrescritura o pérdida de cambios | Validación de la versión vigente |
| Pérdida de versiones anteriores | Dificultades de trazabilidad | Conservación de revisiones en PostgreSQL |
| Fallos en recuperación de contraseñas | Imposibilidad de recuperar el acceso | Validaciones, configuración SMTP y pruebas |
| Exportaciones incorrectas | Documentos incompletos o ilegibles | Pruebas de regresión de PDF y Word |
| Uso de documentos sin revisión jurídica | Riesgos administrativos o legales | Revisión humana y aprobación institucional |

## 17. Estrategia de pruebas

Las actividades de verificación se organizan en las siguientes categorías:

**Pruebas funcionales:** selección de plantillas, captura de información, generación de borradores, edición, historial y exportaciones.

**Pruebas de integración:** comunicación entre React, FastAPI, Groq API y PostgreSQL.

**Pruebas de persistencia:** recuperación de documentos después de reiniciar los servicios.

**Pruebas de instalación:** instalación de dependencias en un entorno Python independiente y comprobación de importaciones.

**Pruebas de seguridad:** validación de accesos, permisos, manejo de documentos confidenciales y protección de endpoints.

**Pruebas de autenticación:** comprobación del inicio de sesión, token JWT, consulta del perfil y restricciones por rol.

**Pruebas de usuarios:** creación de cuentas, activación, desactivación, recuperación y cambio de contraseñas.

**Pruebas de edición documental:** modificación de documentos guardados y actualización de su contenido.

**Pruebas de versionado:** conservación de revisiones anteriores y consulta del historial de versiones.

**Pruebas de búsqueda:** filtrado por nombre del empleado y tipo de plantilla.

**Pruebas de autorización documental:** comprobación del acceso a documentos propios y rechazo de solicitudes sobre documentos ajenos.

**Pruebas de compilación:** ejecución de `npm run build` para verificar la compilación del frontend.

### 17.1. Pruebas realizadas

Durante el desarrollo se comprobaron la autenticación, administración de usuarios, edición documental, generación de versiones, consulta del historial y funcionamiento de los filtros.

También se verificó que un usuario normal únicamente visualizara sus documentos y que una consulta directa de versiones ajenas devolviera HTTP 403 Forbidden.

Se confirmó la persistencia de documentos en PostgreSQL y el funcionamiento de las plantillas durante el inicio del backend.

### 17.2. Pruebas pendientes

Permanecen pendientes las siguientes verificaciones:

- Repetir las pruebas de exportación PDF y Word después de los cambios recientes.
- Comprobar específicamente el rechazo de edición de documentos ajenos.
- Ejecutar una prueba controlada de conflicto por versión desactualizada.
- Realizar pruebas automatizadas de regresión.
- Evaluar formalmente seguridad y rendimiento.
- Comprobar la instalación integral del sistema en otra computadora.
- Verificar los procedimientos de respaldo y restauración de la base de datos.

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
15. Módulo de autenticación mediante JWT.
16. Administración de usuarios y roles.
17. Recuperación y cambio de contraseñas.
18. Protección de endpoints.
19. Módulo de edición de documentos guardados.
20. Sistema de conservación y consulta de versiones.
21. Búsqueda por nombre del empleado y filtro por plantilla.
22. Almacenamiento de datos variables documentales.
23. Módulo de inicialización de plantillas.
24. Historial de cambios mediante Git y GitHub.

## 19. Evolución del producto

La evolución del sistema deberá priorizar las funcionalidades que mejoren la seguridad, la gestión documental y la calidad técnica.

Entre los desarrollos propuestos destacan la implementación de autenticación, administración de roles, protección de endpoints, mecanismos de búsqueda, control de revisiones y flujos de aprobación.

**Actualización del alcance:** La autenticación, la administración de roles, la protección de endpoints, la búsqueda por empleado y plantilla, y el control de versiones ya cuentan con una implementación funcional.

Por lo tanto, las siguientes prioridades se concentran en:

1. Completar las verificaciones pendientes de permisos.
2. Realizar pruebas de regresión de exportación PDF y Word.
3. Incorporar pruebas automatizadas de seguridad y funcionamiento.
4. Desarrollar flujos formales de revisión y aprobación.
5. Ampliar el sistema de auditoría documental.
6. Incorporar validaciones específicas por tipo de plantilla.
7. Mejorar la administración de documentos externos.
8. Implementar respaldos y procedimientos de recuperación.
9. Evaluar el rendimiento y la capacidad del sistema.
10. Preparar su despliegue en un entorno empresarial.

La incorporación de nuevas funcionalidades estará sujeta a su análisis técnico, prioridad empresarial y validación funcional.

## 20. Conclusión

El Sistema Automatizado para la Elaboración de Cartas y Notificaciones Legales constituye una solución web funcional para la generación, edición, almacenamiento, consulta y exportación de documentos mediante inteligencia artificial.

La arquitectura desarrollada integra tecnologías de frontend, backend, persistencia de datos y procesamiento documental, proporcionando una base sobre la que pueden incorporarse nuevas capacidades.

El producto cubre las funciones principales de generación documental, mientras que los aspectos relacionados con seguridad de acceso, validación jurídica automatizada, aprobación y control avanzado de versiones permanecen como áreas de mejora.

La implementación actual amplía las capacidades originales mediante autenticación JWT, administración de usuarios, permisos, edición de documentos guardados, historial de versiones y herramientas de búsqueda.

Las pruebas funcionales realizadas respaldan el funcionamiento de los principales módulos. No obstante, todavía deben completarse las verificaciones específicas de exportación, permisos de edición y preparación del sistema para un entorno empresarial.

El PRD establece una referencia para el mantenimiento, evaluación y evolución del sistema, distinguiendo el alcance implementado de los requisitos planteados para futuras etapas.