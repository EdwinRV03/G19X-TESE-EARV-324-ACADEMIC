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

## 10. Instalación y ejecución del sistema

### 10.1. Requisitos previos

Antes de instalar el sistema, es necesario contar con:

- Python 3.11.
- Node.js y npm.
- Docker Desktop con Docker Compose.
- Git.
- Una clave API válida de Groq.

### 10.2. Clonar el repositorio

Abrir una terminal y ejecutar:

```bash
git clone https://github.com/EdwinRV03/G19X-TESE-EARV-324-ACADEMIC.git
cd G19X-TESE-EARV-324-ACADEMIC
```

### 10.3. Configurar las variables de entorno

En la carpeta principal del proyecto, crear una copia del archivo `.env.example` y nombrarla `.env`.

Configurar los valores correspondientes a:

- `GROQ_API_KEY`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_DB`
- `DATABASE_URL`

La contraseña establecida en `POSTGRES_PASSWORD` debe coincidir con la contraseña utilizada en `DATABASE_URL`.

Las credenciales reales deben mantenerse exclusivamente en el archivo `.env`, que está excluido del repositorio mediante `.gitignore`.

### 10.4. Iniciar PostgreSQL con Docker

Desde la carpeta principal del proyecto, ejecutar:

```bash
docker compose up -d
```

Este comando inicia PostgreSQL 16 mediante Docker Compose. La base de datos utiliza un volumen persistente para conservar la información entre reinicios.

Para comprobar el estado del contenedor:

```bash
docker ps
```

Debe aparecer el contenedor `postgres_legal_db` en ejecución.

### 10.5. Preparar el backend

Desde la carpeta principal del proyecto, ejecutar los siguientes comandos en PowerShell:

```powershell
cd backend
py -3.11 -m venv venv
.\venv\Scripts\python.exe -m pip install -r ..\requirements.txt
```

El archivo `requirements.txt` contiene las dependencias necesarias para FastAPI, PostgreSQL, Groq y la generación de documentos PDF y Word.

### 10.6. Ejecutar el backend

Dentro de la carpeta `backend`, ejecutar:

```powershell
.\venv\Scripts\python.exe -m uvicorn main:app --reload --port 8001
```

Una vez iniciado el servidor, la documentación interactiva de la API estará disponible en:

`http://127.0.0.1:8001/docs`

### 10.7. Preparar y ejecutar el frontend

Abrir otra terminal y acceder a la carpeta `frontend`:

```powershell
cd frontend
npm ci
npm run dev
```

El servidor de Vite mostrará en la terminal la dirección local desde la cual se puede acceder a la aplicación.

### 10.8. Verificación del funcionamiento

Con PostgreSQL, FastAPI y React en ejecución, comprobar:

1. Que se carguen las cinco plantillas disponibles.
2. Que puedan capturarse los datos del documento.
3. Que Groq genere un borrador.
4. Que el contenido pueda editarse.
5. Que el documento pueda guardarse en PostgreSQL.
6. Que aparezca en el historial.
7. Que pueda exportarse a PDF y Word.
8. Que la información permanezca disponible después de reiniciar el contenedor.

### 10.9. Consideraciones

El sistema utiliza una configuración de desarrollo local. Para desplegarlo en un entorno empresarial accesible por red es necesario incorporar medidas adicionales de autenticación, autorización, seguridad y administración de secretos.

Los documentos generados mediante inteligencia artificial deben revisarse antes de su utilización formal.

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