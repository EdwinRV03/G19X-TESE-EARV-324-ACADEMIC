# Sistema de Elaboración de Cartas y Notificaciones Legales

**Sistema web para la generación de cartas y notificaciones legales asistida por inteligencia artificial.**

## 1. Descripción del proyecto

El Sistema de Notificaciones Legales es una aplicación web desarrollada para facilitar y automatizar la elaboración de cartas, avisos y notificaciones legales mediante el uso de plantillas parametrizadas e inteligencia artificial.

El proyecto surge de una necesidad de automatización documental planteada por PluriOne S.A. de C.V., comercialmente conocida como Develop Talent & Technology, con el propósito de agilizar la redacción de comunicaciones formales, reducir actividades repetitivas y facilitar la administración de documentos.

La solución integra una interfaz web desarrollada con React, un backend implementado mediante FastAPI, generación de contenido asistida por inteligencia artificial a través de Groq API y almacenamiento persistente en PostgreSQL mediante Docker.

El sistema permite seleccionar plantillas, capturar información, generar borradores, editar su contenido, almacenar documentos y exportarlos a formatos PDF y Word.

## 2. Objetivo general

Desarrollar un sistema web inteligente que permita automatizar la elaboración de cartas y notificaciones legales mediante plantillas parametrizadas e inteligencia artificial, facilitando la generación, revisión, almacenamiento y exportación de documentos, con la finalidad de optimizar los procesos de gestión documental y reducir el tiempo destinado a la redacción de comunicaciones formales.

## 3. Funcionalidades principales

- Selección de cinco plantillas de documentos.
- Captura de información de empresas y destinatarios.
- Generación automática de borradores mediante inteligencia artificial.
- Edición manual del contenido generado.
- Almacenamiento de documentos en PostgreSQL.
- Consulta del historial de documentos generados.
- Exportación de documentos en formatos PDF y Word.
- Incorporación de logotipos institucionales.
- Personalización de la ubicación de imágenes y marcas de agua.
- Generación de bloques de firma en documentos exportados.

## 4. Plantillas disponibles

1. Notificación de Rescisión Laboral.
2. Acta Administrativa por Incumplimiento.
3. Carta de Recomendación Laboral.
4. Convenio de Confidencialidad (NDA).
5. Aviso de Suspensión Temporal de Labores.

Las plantillas permiten proporcionar información para generar documentos adaptados a cada situación.

## 5. Tecnologías utilizadas

| Componente | Tecnología |
|---|---|
| Frontend | React y Vite |
| Estilos | Tailwind CSS |
| Iconografía | Lucide React |
| Backend | Python y FastAPI |
| Base de datos | PostgreSQL 16 |
| ORM | SQLAlchemy |
| Inteligencia artificial | Groq API |
| Exportación PDF | ReportLab |
| Exportación Word | python-docx |
| Procesamiento de imágenes | Pillow |
| Contenedores | Docker y Docker Compose |
| Entorno de desarrollo | Visual Studio Code |
| Control de versiones | Git y GitHub |

## 6. Arquitectura general

La aplicación utiliza una arquitectura cliente-servidor.

El frontend desarrollado en React permite capturar datos, seleccionar plantillas, visualizar documentos e interactuar con las funcionalidades del sistema.

El backend desarrollado con FastAPI procesa las solicitudes del frontend, se comunica con Groq para generar borradores, administra la información mediante SQLAlchemy y realiza las exportaciones de documentos.

PostgreSQL almacena las plantillas y los documentos generados. La base de datos se ejecuta mediante un contenedor Docker con almacenamiento persistente.

## 7. Base de datos

La aplicación emplea PostgreSQL y contempla dos entidades principales:

- **Plantilla:** almacena los formatos base disponibles para generar documentos.
- **DocumentoGenerado:** almacena el contenido, estado, versión y fecha de creación de los documentos.

La relación entre ambas entidades permite identificar la plantilla utilizada para generar cada documento.

## 8. Requisitos para ejecutar el proyecto

Se requiere contar con:

- Python y sus dependencias.
- Node.js y npm.
- Docker Desktop con Docker Compose.
- PostgreSQL configurado mediante Docker.
- Una clave de API válida de Groq.
- Git para el control de versiones.

## 9. Configuración del entorno

Las credenciales deben mantenerse en archivos `.env` privados, excluidos del control de versiones.

La configuración utiliza variables como:

- `GROQ_API_KEY`
- `DATABASE_URL`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_DB`

No deben publicarse claves reales ni contraseñas en el repositorio.

## 10. Ejecución en desarrollo

Desde la carpeta principal del proyecto, iniciar PostgreSQL mediante Docker Compose:

`docker compose up -d`

Posteriormente, iniciar el backend FastAPI desde su carpeta correspondiente:

`python -m uvicorn main:app --reload --port 8001`

Finalmente, iniciar el frontend React desde la carpeta `frontend`:

`npm install`

`npm run dev`

Antes de ejecutar los servicios es necesario instalar las dependencias correspondientes y configurar las variables de entorno.

## 11. Flujo de funcionamiento

1. El usuario accede a la interfaz principal del sistema.
2. Selecciona una de las cinco plantillas disponibles.
3. Introduce los datos de la empresa, el destinatario y la información del documento.
4. Solicita la generación del borrador asistido por inteligencia artificial.
5. Revisa y modifica el contenido generado.
6. Guarda el documento en PostgreSQL.
7. Consulta los documentos almacenados desde el historial.
8. Exporta los documentos en PDF o Word.

## 12. Consideraciones de seguridad

El sistema utiliza archivos de configuración privados para almacenar las credenciales de acceso a servicios externos y a la base de datos.

Los documentos generados mediante inteligencia artificial deben revisarse antes de utilizarse, especialmente cuando contienen información laboral o jurídica.

La generación automatizada de documentos no sustituye la revisión de un profesional del derecho.

## 13. Estado del proyecto

El proyecto cuenta con un flujo funcional de generación, edición, almacenamiento, consulta y exportación de documentos.

Actualmente se trabaja en la organización del repositorio y la elaboración de su documentación técnica.

## 14. Contexto empresarial del proyecto

El Sistema de Notificaciones Legales se desarrolla a partir de los requerimientos planteados por PluriOne S.A. de C.V. (Develop Talent & Technology), empresa dedicada a servicios de consultoría, desarrollo de software y capacitación en tecnologías de la información.

La solución se orienta a facilitar los procesos de elaboración y gestión de documentos laborales y comunicaciones legales mediante tecnologías de desarrollo web, almacenamiento estructurado e inteligencia artificial generativa.

Las herramientas tecnológicas empleadas fueron seleccionadas de acuerdo con las necesidades y características de la implementación, priorizando la integración de componentes, la funcionalidad del sistema y la posibilidad de continuar su evolución.

Actualmente, la aplicación cuenta con funcionalidades de generación, edición, almacenamiento, consulta y exportación documental, y se encuentra en una etapa de organización del repositorio y elaboración de documentación técnica.

Los documentos generados requieren revisión humana antes de su utilización formal.