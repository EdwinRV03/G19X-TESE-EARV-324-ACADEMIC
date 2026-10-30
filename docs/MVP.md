
# MVP — Sistema Automatizado para la Elaboración de Cartas y Notificaciones Legales

**Documento de Definición del Producto Mínimo Viable (Minimum Viable Product)**

**Empresa:** PluriOne S.A. de C.V. — Develop Talent & Technology
**Proyecto:** Sistema Automatizado para la Elaboración de Cartas y Notificaciones Legales
**Versión del documento:** 1.1
**Estado:** MVP ampliado, funcional en entorno de desarrollo local; validaciones finales pendientes
**Fecha:** Octubre de 2026

---

## 1. Introducción

El documento define el Producto Mínimo Viable (MVP) del Sistema Automatizado para la Elaboración de Cartas y Notificaciones Legales, desarrollado para atender necesidades de automatización documental identificadas por PluriOne S.A. de C.V., comercialmente conocida como Develop Talent & Technology.

El MVP constituye una versión funcional ampliada de una aplicación web que integra plantillas documentales, inteligencia artificial generativa, almacenamiento persistente, autenticación de usuarios y mecanismos de edición y versionado.

La implementación permite realizar el proceso de generación documental desde la captura inicial de información hasta la consulta, modificación y exportación de documentos.

El alcance del MVP distingue las funcionalidades implementadas y comprobadas, las capacidades que requieren nuevas pruebas de regresión y los elementos pendientes para futuras etapas.

## 2. Problema que resuelve el MVP

La elaboración de cartas y notificaciones legales requiere recopilar información, seleccionar estructuras documentales, redactar contenido formal y preparar archivos para su utilización.

Estas actividades pueden implicar procesos manuales repetitivos, inconsistencias en la documentación y dificultades para conservar o recuperar documentos elaborados anteriormente.

El MVP centraliza estas operaciones en una aplicación web que permite generar borradores mediante inteligencia artificial, editarlos, almacenarlos y consultar sus versiones anteriores.

La solución facilita la preparación y administración documental, sin sustituir la revisión humana ni garantizar automáticamente la validez jurídica de los documentos.

## 3. Objetivo del MVP

Implementar una aplicación web funcional que permita seleccionar plantillas, capturar información, generar borradores asistidos por inteligencia artificial, editar documentos, almacenar información en PostgreSQL, conservar versiones anteriores, administrar usuarios y exportar archivos PDF y Word.

## 4. Usuarios del MVP

### 4.1. Usuario operativo

El usuario operativo es la persona autorizada para elaborar y administrar sus documentos dentro de la plataforma.

Sus actividades incluyen:

- Iniciar sesión mediante correo electrónico y contraseña.
- Seleccionar una plantilla documental.
- Capturar los datos necesarios.
- Generar borradores con inteligencia artificial.
- Revisar y modificar el contenido.
- Guardar documentos.
- Consultar exclusivamente sus documentos.
- Editar documentos previamente guardados.
- Consultar versiones anteriores.
- Buscar documentos por nombre del empleado.
- Filtrar documentos por plantilla.
- Descargar documentos en PDF y Word.
- Gestionar las opciones disponibles de su cuenta.

### 4.2. Administrador

El administrador dispone de las funciones documentales y de capacidades adicionales para gestionar usuarios.

Entre sus funciones se encuentran:

- Crear cuentas de usuario.
- Consultar las cuentas registradas.
- Activar o desactivar usuarios.
- Administrar las contraseñas mediante las funciones autorizadas.
- Supervisar el acceso a las funcionalidades según los permisos establecidos.

### 4.3. Revisor jurídico

El perfil independiente de revisor jurídico y los flujos formales de aprobación no forman parte de la implementación actual.

La revisión jurídica continúa siendo responsabilidad de las personas autorizadas por la organización.

## 5. Alcance funcional del MVP

| ID | Funcionalidad | Estado |
|---|---|---|
| MVP-01 | Interfaz web de generación documental | Implementada |
| MVP-02 | Catálogo de cinco plantillas | Implementada |
| MVP-03 | Formulario de captura de información | Implementada |
| MVP-04 | Generación de borradores mediante Groq API | Implementada |
| MVP-05 | Visualización y edición del borrador | Implementada |
| MVP-06 | Almacenamiento en PostgreSQL | Implementada |
| MVP-07 | Consulta del historial documental | Implementada |
| MVP-08 | Exportación en PDF | Implementada; requiere nueva prueba de regresión |
| MVP-09 | Exportación en Word | Implementada; requiere nueva prueba de regresión |
| MVP-10 | Logotipos y marcas de agua | Implementada |
| MVP-11 | Bloques de firma | Implementada |
| MVP-12 | Persistencia mediante PostgreSQL en Docker | Implementada |
| MVP-13 | Autenticación mediante JWT | Implementada y probada |
| MVP-14 | Roles de administrador y usuario | Implementada y probada |
| MVP-15 | Administración de cuentas | Implementada y probada |
| MVP-16 | Recuperación y cambio de contraseña | Implementada y probada |
| MVP-17 | Protección de endpoints | Implementada; pruebas parciales |
| MVP-18 | Edición de documentos guardados | Implementada y probada |
| MVP-19 | Historial de versiones documentales | Implementada y probada |
| MVP-20 | Persistencia de datos variables | Implementada y probada |
| MVP-21 | Búsqueda por nombre del empleado | Implementada y probada |
| MVP-22 | Filtro por plantilla | Implementada y probada |
| MVP-23 | Inicialización de plantillas desde el backend | Implementada y probada |

## 6. Plantillas disponibles

El sistema dispone de cinco plantillas predefinidas.

| Plantilla | Finalidad |
|---|---|
| Notificación de Rescisión Laboral | Elaborar borradores relacionados con la terminación de una relación laboral |
| Acta Administrativa por Incumplimiento | Registrar situaciones o hechos de incumplimiento |
| Carta de Recomendación Laboral | Elaborar comunicaciones de recomendación |
| Convenio de Confidencialidad (NDA) | Preparar borradores de acuerdos de confidencialidad |
| Aviso de Suspensión Temporal de Labores | Elaborar comunicaciones sobre suspensiones temporales |

Las cinco plantillas comparten actualmente un formulario general de captura.

Su inicialización se realiza desde el backend al iniciar el servicio, comprobando su existencia para evitar la inserción repetida de plantillas.

## 7. Flujo operativo del MVP

### 7.1. Autenticación

El usuario accede mediante correo electrónico y contraseña.

FastAPI valida las credenciales y utiliza un token JWT para autenticar las solicitudes protegidas.

### 7.2. Selección de plantilla

El usuario selecciona uno de los cinco tipos de documentos disponibles.

### 7.3. Captura de información

Se proporciona la información necesaria para la elaboración del documento, incluyendo datos empresariales, destinatario, firmante, fecha y motivo, según corresponda.

### 7.4. Generación mediante inteligencia artificial

React envía la solicitud a FastAPI, que integra la plantilla y los datos recibidos para solicitar un borrador a Groq API.

### 7.5. Revisión y edición

El usuario revisa el contenido generado y puede modificarlo antes de guardarlo.

### 7.6. Almacenamiento

El documento se registra en PostgreSQL mediante SQLAlchemy.

También pueden almacenarse los datos variables utilizados durante la elaboración del documento.

### 7.7. Consulta del historial

El usuario puede visualizar sus documentos guardados y utilizar las opciones de búsqueda y filtrado disponibles.

### 7.8. Edición de documentos guardados

El sistema permite modificar el contenido de documentos previamente almacenados.

La edición genera un nuevo número de versión y conserva el contenido anterior en una entidad independiente.

### 7.9. Consulta de versiones

El usuario puede consultar el contenido correspondiente a las versiones anteriores y a la versión vigente del documento.

### 7.10. Exportación

La plataforma ofrece funciones de descarga en PDF y Word, incorporando las opciones de personalización disponibles.

## 8. Tecnologías utilizadas

| Componente | Tecnología |
|---|---|
| Frontend | React y Vite |
| Interfaz | Tailwind CSS y Lucide React |
| Backend | Python y FastAPI |
| Validación | Pydantic |
| Persistencia | PostgreSQL 16 |
| ORM | SQLAlchemy |
| Inteligencia artificial | Groq API |
| Modelo de IA configurado | openai/gpt-oss-20b |
| Autenticación | JWT |
| Hash de contraseñas | Argon2 |
| Recuperación de contraseña | SMTP y mecanismos de validación |
| PDF | ReportLab |
| Word | python-docx |
| Procesamiento de imágenes | Pillow |
| Contenedores | Docker y Docker Compose |
| Control de versiones | Git y GitHub |
| Desarrollo | Visual Studio Code |

## 9. Arquitectura mínima

El sistema utiliza una arquitectura cliente-servidor integrada por los siguientes componentes.

**Frontend:** proporciona la interfaz de autenticación, generación documental, historial, edición, versionado y administración de usuarios.

**Backend:** procesa las solicitudes HTTP, valida las credenciales, administra los permisos, almacena información y coordina los servicios documentales.

**Servicio de inteligencia artificial:** genera borradores mediante Groq API.

**Base de datos:** PostgreSQL almacena usuarios, plantillas, documentos y versiones.

**Infraestructura:** PostgreSQL se ejecuta mediante Docker Compose, mientras el frontend y el backend se utilizan localmente durante el desarrollo.

## 10. Modelo de almacenamiento

### 10.1. Plantilla

Almacena las estructuras base utilizadas para generar documentos.

Entre sus atributos se encuentran el identificador, título, cuerpo base y fecha de creación.

### 10.2. DocumentoGenerado

Almacena los documentos elaborados en la aplicación.

Incluye identificador, plantilla relacionada, contenido, estado, versión, fecha de creación y datos variables.

### 10.3. Usuario

Almacena la información de las cuentas autorizadas.

Incluye identificador, nombre, correo electrónico, hash de contraseña, rol, estado de activación y fecha de creación.

### 10.4. VersionDocumento

Conserva las revisiones anteriores de los documentos modificados.

Incluye identificador, documento relacionado, número de versión, contenido anterior, datos variables y fecha de conservación de la versión.

### 10.5. Relaciones

Las plantillas pueden asociarse con múltiples documentos.

Los documentos se relacionan con los usuarios correspondientes y pueden tener múltiples versiones archivadas.

El sistema utiliza restricciones y comprobaciones para evitar inconsistencias en la numeración de versiones.

## 11. Funcionalidades excluidas del MVP actual

| Funcionalidad | Situación actual |
|---|---|
| Autenticación y roles | Implementados |
| Protección de documentos por usuario | Implementada; pruebas parciales |
| Búsqueda por empleado y plantilla | Implementada |
| Edición y versiones documentales | Implementadas |
| Carga y gestión independiente de documentos externos | Pendiente |
| Flujos formales de aprobación | Pendiente |
| Perfil independiente de revisor jurídico | Pendiente |
| Validación jurídica automatizada | No comprobada |
| Registro detallado de auditoría | Pendiente |
| Búsqueda avanzada por fechas | Pendiente |
| Administración avanzada de plantillas desde la interfaz | Pendiente |
| Despliegue empresarial en producción | Pendiente |

Estas funcionalidades representan necesidades de evolución y no deben confundirse con las capacidades ya disponibles.

## 12. Criterios de aceptación del MVP

| ID | Criterio | Estado de comprobación |
|---|---|---|
| CA-01 | Mostrar las cinco plantillas | Comprobado |
| CA-02 | Capturar información documental | Comprobado |
| CA-03 | Generar borradores mediante Groq | Comprobado |
| CA-04 | Modificar el contenido generado | Comprobado |
| CA-05 | Guardar documentos en PostgreSQL | Comprobado |
| CA-06 | Consultar el historial | Comprobado |
| CA-07 | Generar documentos PDF | Comprobado anteriormente; repetir prueba |
| CA-08 | Generar documentos Word | Comprobado anteriormente; repetir prueba |
| CA-09 | Incorporar logotipos y marcas de agua | Comprobado anteriormente |
| CA-10 | Conservar información después de reiniciar Docker | Comprobado |
| CA-11 | Instalar dependencias desde requirements.txt | Comprobado anteriormente |
| CA-12 | Importar el backend correctamente | Comprobado |
| CA-13 | Autenticar usuarios mediante JWT | Comprobado |
| CA-14 | Restringir funciones administrativas por rol | Comprobado |
| CA-15 | Administrar cuentas de usuario | Comprobado |
| CA-16 | Recuperar y cambiar contraseñas | Comprobado |
| CA-17 | Editar documentos guardados | Comprobado |
| CA-18 | Conservar versiones anteriores | Comprobado |
| CA-19 | Consultar versiones desde React | Comprobado |
| CA-20 | Filtrar documentos por plantilla | Comprobado |
| CA-21 | Buscar documentos por empleado | Comprobado |
| CA-22 | Bloquear consulta de versiones ajenas | Comprobado: HTTP 403 |
| CA-23 | Bloquear edición de documentos ajenos | Pendiente de prueba específica |

## 13. Pruebas efectuadas

### 13.1. Pruebas funcionales

Se verificó la generación de borradores, la visualización de documentos, la edición, el historial y las funciones principales de administración.

Las pruebas anteriores de exportación no sustituyen la necesidad de volver a comprobar los archivos después de los cambios recientes.

### 13.2. Pruebas de autenticación

Se comprobó el inicio de sesión mediante JWT, la consulta del perfil y el acceso restringido a funcionalidades según el rol.

### 13.3. Pruebas de administración de usuarios

Se comprobó la creación de cuentas, los cambios de estado, las restricciones por rol y los mecanismos de cambio y recuperación de contraseña.

### 13.4. Pruebas de edición y versionado

Se utilizó un documento de prueba para realizar modificaciones sucesivas y comprobar el incremento de versiones.

También se verificó la recuperación del contenido archivado y su presentación desde React.

### 13.5. Pruebas de permisos

Se comprobó que un usuario operativo visualiza sus documentos y puede consultar sus versiones.

Una solicitud autenticada para consultar las versiones de un documento ajeno devolvió HTTP 403 Forbidden.

La prueba específica de rechazo de edición ajena permanece pendiente.

### 13.6. Pruebas de persistencia

Se verificó el almacenamiento en PostgreSQL y la conservación de documentos después de reiniciar Docker.

### 13.7. Pruebas de dependencias

Se verificaron las dependencias del backend y se actualizó el archivo requirements.txt para incluir las necesarias.

### 13.8. Pruebas de compilación

Se realizaron compilaciones del frontend mediante npm run build después de los cambios principales.

### 13.9. Control de versiones

Las mejoras de gestión documental, seguridad y documentación técnica fueron integradas en Git y publicadas en GitHub.

## 14. Limitaciones conocidas

1. El sistema se encuentra orientado a un entorno de desarrollo local.
2. No existe un flujo formal de aprobación jurídica.
3. Los documentos generados requieren revisión humana.
4. La generación de borradores depende de Groq API.
5. Las cinco plantillas comparten un formulario general de captura.
6. No se dispone de un registro integral de auditoría de todas las operaciones.
7. El historial de versiones se centra en las modificaciones documentales.
8. No se han realizado pruebas formales de carga y rendimiento.
9. La instalación integral en una computadora independiente requiere validación adicional.
10. Las descargas PDF y Word deben someterse a pruebas de regresión después de las modificaciones recientes.
11. La comprobación específica de rechazo de edición ajena permanece pendiente.
12. La recuperación de contraseñas depende de la configuración correcta del servicio de correo.

## 15. Riesgos y medidas de mitigación

| Riesgo | Medida propuesta |
|---|---|
| Acceso no autorizado | Mantener autenticación, permisos y pruebas de control de acceso |
| Errores del contenido generado por IA | Revisión humana antes de utilizar los documentos |
| Indisponibilidad de Groq API | Manejo de errores y procedimientos de recuperación |
| Pérdida de información | Respaldos periódicos de PostgreSQL |
| Exposición de credenciales | Variables de entorno y exclusión de secretos en Git |
| Ediciones concurrentes | Comprobación de versión vigente antes de guardar |
| Errores de instalación | README y dependencias actualizadas |
| Fallas de exportación | Pruebas de regresión sobre PDF y Word |
| Inconsistencias jurídicas | Revisión profesional y mejora de las validaciones |

## 16. Entregables del MVP

Los entregables incluyen:

- Código fuente del frontend React.
- Código fuente del backend FastAPI.
- Integración con Groq API.
- Catálogo de cinco plantillas.
- Autenticación y administración de usuarios.
- Gestión de documentos e historial.
- Edición y control de versiones.
- Búsqueda y filtros documentales.
- Almacenamiento PostgreSQL.
- Funciones de exportación PDF y Word.
- Configuración de Docker Compose.
- Dependencias del proyecto.
- Archivos de ejemplo de variables de entorno.
- README de instalación y funcionamiento.
- PRD actualizado.
- Documento MVP actualizado.
- Historial de cambios en GitHub.

## 17. Evolución propuesta después del MVP

Las siguientes etapas deberán considerar:

1. Realizar pruebas finales de exportación PDF y Word.
2. Completar la verificación de permisos de edición.
3. Incorporar pruebas automatizadas de seguridad y regresión.
4. Evaluar validaciones específicas por plantilla.
5. Incorporar flujos de revisión y aprobación jurídica.
6. Desarrollar un registro más amplio de auditoría.
7. Evaluar carga y rendimiento del sistema.
8. Implementar respaldos y recuperación operativa.
9. Preparar el despliegue empresarial.
10. Evaluar la administración de documentos externos.

## 18. Condiciones para una implementación empresarial

La versión actual incorpora autenticación, roles y protección de operaciones documentales, lo que representa un avance respecto a la primera versión del MVP.

Sin embargo, su utilización en un entorno empresarial compartido requiere completar las pruebas de seguridad, definir políticas de respaldo, configurar adecuadamente los servicios externos y establecer procedimientos de mantenimiento.

Asimismo, deben evaluarse los requisitos de confidencialidad de la información laboral, el tratamiento de datos personales, la protección de credenciales y las condiciones para compartir información con servicios de inteligencia artificial.

La implementación actual no debe considerarse certificada para producción únicamente por haber superado pruebas funcionales en desarrollo.

## 19. Conclusión

El MVP del Sistema Automatizado para la Elaboración de Cartas y Notificaciones Legales demuestra la viabilidad de integrar tecnologías web, inteligencia artificial generativa, autenticación, almacenamiento persistente y gestión documental en una misma plataforma.

Además del flujo inicial de generación de documentos, el producto incorpora administración de usuarios, edición de documentos guardados, conservación de versiones anteriores y mecanismos para localizar información dentro del historial.

Las pruebas realizadas respaldan el funcionamiento de las capacidades principales, aunque permanecen pendientes verificaciones específicas de seguridad, exportación y preparación para un entorno empresarial.

El documento establece el alcance actualizado del MVP y sirve como referencia para su mantenimiento y evolución.
