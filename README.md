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

El proyecto utiliza dos archivos de configuración para separar las variables del servicio PostgreSQL y las utilizadas por el backend.

**Configuración de Docker Compose**

En la carpeta principal del proyecto, crear una copia de `.env.example` con el nombre `.env`.

Configurar las variables `POSTGRES_USER`, `POSTGRES_PASSWORD` y `POSTGRES_DB` con los valores correspondientes a PostgreSQL.

**Configuración del backend**

Dentro de la carpeta `backend`, crear una copia de `backend/.env.example` con el nombre `.env`.

Configurar las variables `GROQ_API_KEY` y `DATABASE_URL` para permitir la generación de documentos y la conexión con PostgreSQL.

La contraseña indicada en `DATABASE_URL` debe coincidir con la configurada en `POSTGRES_PASSWORD`. Si contiene caracteres reservados de URL, debe codificarse adecuadamente en la cadena de conexión.

Ambos archivos `.env` contienen información privada y se encuentran excluidos del repositorio mediante `.gitignore`. Los archivos `.env.example` únicamente incluyen valores de referencia para facilitar la configuración del sistema.

La separación permite administrar las configuraciones del contenedor PostgreSQL y del backend de manera independiente durante el desarrollo local.

**Configuración de autenticación JWT**

El backend utiliza JSON Web Tokens (JWT) para autenticar a los usuarios y controlar el acceso a las funcionalidades del sistema.

En el archivo `backend/.env`, configurar las siguientes variables:

```env
JWT_SECRET_KEY=coloca_aqui_una_clave_aleatoria_segura
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_MINUTES=30
```

Para generar una clave segura, ejecutar desde PowerShell:

```powershell
python -c "import secrets; print(secrets.token_urlsafe(48))"
```

Copiar el resultado en `JWT_SECRET_KEY` dentro de `backend/.env`. La clave generada es privada y no debe compartirse ni publicarse en GitHub.

**Configuración del correo electrónico SMTP**

El sistema utiliza SMTP para enviar enlaces de recuperación de contraseñas. En `backend/.env`, configurar:

```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=correo_de_envio@gmail.com
SMTP_PASSWORD=contraseña_de_aplicacion
SMTP_FROM_EMAIL=correo_de_envio@gmail.com
SMTP_USE_TLS=true
```

Para utilizar Gmail es necesario habilitar la verificación en dos pasos de la cuenta y generar una contraseña de aplicación, cuando Google permita esta opción.

La contraseña de aplicación se utiliza exclusivamente para autenticar el envío de correos SMTP. No debe confundirse con la contraseña habitual de Gmail.

Las credenciales reales deben almacenarse únicamente en archivos `.env` excluidos de Git. El archivo `backend/.env.example` contiene valores de referencia para facilitar la instalación.

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
py -3.11 -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
cd backend
```

El archivo `requirements.txt` contiene las dependencias necesarias para FastAPI, PostgreSQL, Groq y la generación de documentos PDF y Word.

**Creación del administrador inicial**

Antes de iniciar sesión por primera vez, es necesario registrar una cuenta de administrador en PostgreSQL.

Con PostgreSQL en ejecución, las tablas de la base de datos creadas y las variables de entorno del backend configuradas, ejecutar desde la carpeta `backend`:

```powershell
..\venv\Scripts\python.exe crear_admin.py
```

El programa solicitará los siguientes datos:

- Nombre del administrador.
- Correo electrónico.
- Contraseña de al menos ocho caracteres.
- Confirmación de contraseña.

El script comprueba que el correo no esté registrado, genera un hash seguro de la contraseña mediante Argon2 y crea el usuario con el rol `admin`.

Las contraseñas no se muestran durante su captura ni se almacenan en texto plano.

Una vez creado el administrador, podrá iniciar sesión desde la interfaz web utilizando su correo electrónico y contraseña.

Este procedimiento se realiza únicamente cuando se necesita registrar una cuenta administradora inicial; no debe repetirse durante cada arranque del sistema.

### 10.6. Ejecutar el backend

Dentro de la carpeta `backend`, ejecutar:

```powershell
..\venv\Scripts\python.exe -m uvicorn main:app --reload --port 8001
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

1. El usuario accede al sistema e inicia sesión con su correo electrónico y contraseña.
2. Selecciona una de las cinco plantillas disponibles.
3. Introduce los datos de la empresa, el destinatario y la información necesaria para elaborar el documento.
4. Solicita la generación de un borrador asistido por inteligencia artificial.
5. Revisa y modifica el contenido generado.
6. Guarda el documento en PostgreSQL junto con los datos utilizados para su elaboración.
7. Consulta sus documentos guardados desde el historial.
8. Puede buscar documentos por nombre del empleado o filtrarlos por plantilla.
9. Si necesita modificar un documento guardado, puede editarlo y conservar su versión anterior.
10. Consulta el historial de versiones para revisar el contenido de las modificaciones realizadas.
11. Descarga los documentos en formato PDF o Word.

El sistema utiliza roles de administrador y usuario para controlar las funciones disponibles y restringir el acceso a la información documental.

## 11.1 Permisos de usuario

El sistema cuenta con dos roles: administrador (`admin`) y usuario (`usuario`). Ambos pueden elaborar y gestionar documentos, pero las funciones administrativas están reservadas al administrador.

| Funcionalidad | Administrador (`admin`) | Usuario (`usuario`) |
|---|---|---|
| Iniciar sesión | Sí | Sí |
| Generar y guardar documentos | Sí | Sí |
| Consultar el historial | Sí | Sí, sus propios documentos |
| Editar documentos guardados | Sí | Sí, sus propios documentos |
| Consultar versiones anteriores | Sí | Sí, de sus documentos |
| Buscar y filtrar documentos | Sí | Sí |
| Descargar PDF y Word | Sí | Sí, de sus documentos |
| Consultar y modificar su cuenta | Sí | Sí |
| Crear y administrar usuarios | Sí | No |
| Activar o desactivar cuentas | Sí | No |

El administrador puede gestionar las cuentas registradas y realizar las operaciones autorizadas por el backend. El usuario normal únicamente puede acceder a los documentos que le corresponden.

Los permisos se comprueban en el backend, por lo que no dependen solamente de los botones visibles en la interfaz.

## 12. Consideraciones de seguridad

El sistema utiliza archivos de configuración privados para almacenar las credenciales de acceso a servicios externos y a la base de datos.

Los documentos generados mediante inteligencia artificial deben revisarse antes de utilizarse, especialmente cuando contienen información laboral o jurídica.

La generación automatizada de documentos no sustituye la revisión de un profesional del derecho.

## 12.1 Pruebas automatizadas

El backend cuenta con tres pruebas automatizadas desarrolladas con `pytest` y `TestClient` de FastAPI.

Las pruebas comprueban:

- **401 Unauthorized:** se rechaza una solicitud de edición sin token.
- **403 Forbidden:** un usuario normal no puede editar un documento que pertenece a otra persona.
- **409 Conflict:** se rechaza una edición cuando se utiliza una versión desactualizada.

Las pruebas utilizan SQLite en memoria y usuarios y documentos ficticios para no modificar la información almacenada en PostgreSQL.

Para ejecutarlas, abre una terminal desde la carpeta `backend`, activa el entorno virtual del proyecto y utiliza:

```powershell
python -m pytest tests/test_documentos.py -v
```

**Resultado obtenido:** 3 pruebas aprobadas, 0 fallidas y 2 advertencias de dependencias.

Estas comprobaciones respaldan las validaciones de autenticación, permisos y control de versiones, pero no sustituyen una evaluación integral de seguridad.

## 13. Estado del proyecto

El proyecto cuenta con un sistema funcional de generación, edición, almacenamiento, consulta y exportación de documentos mediante una aplicación web.

Actualmente incorpora autenticación de usuarios, administración de cuentas, control de acceso por roles y recuperación de contraseñas.

También permite editar documentos previamente guardados, conservar versiones anteriores, consultar el historial de modificaciones y buscar documentos por nombre del empleado o tipo de plantilla.

La información se almacena en PostgreSQL y el sistema utiliza Groq API para generar borradores asistidos por inteligencia artificial.

La aplicación funciona en un entorno de desarrollo local. Aunque sus principales funcionalidades han sido comprobadas, todavía se requieren pruebas automatizadas, verificaciones adicionales de seguridad y una revisión final de las exportaciones PDF y Word antes de considerar su utilización en producción.

## 14. Contexto empresarial del proyecto

El Sistema de Notificaciones Legales se desarrolla a partir de los requerimientos planteados por PluriOne S.A. de C.V. (Develop Talent & Technology), empresa dedicada a servicios de consultoría, desarrollo de software y capacitación en tecnologías de la información.

La solución se orienta a facilitar los procesos de elaboración y gestión de documentos laborales y comunicaciones legales mediante tecnologías de desarrollo web, almacenamiento estructurado e inteligencia artificial generativa.

Las herramientas tecnológicas empleadas fueron seleccionadas de acuerdo con las necesidades y características de la implementación, priorizando la integración de componentes, la funcionalidad del sistema y la posibilidad de continuar su evolución.

Actualmente, la aplicación cuenta con funcionalidades de generación, edición, almacenamiento, consulta y exportación documental, y se encuentra en una etapa de organización del repositorio y elaboración de documentación técnica.

Los documentos generados requieren revisión humana antes de su utilización formal.