# Frontend — Sistema de Notificaciones Legales

Interfaz web del Sistema Automatizado para la Elaboración de Cartas y Notificaciones Legales, desarrollado con React y Vite.

Este módulo permite a los usuarios generar documentos con apoyo de inteligencia artificial, consultar su historial y administrar las funciones disponibles según su rol.

## 1. Tecnologías utilizadas

- React
- Vite
- JavaScript
- Tailwind CSS
- Lucide React
- Axios

## 2. Funcionalidades

El frontend permite:

- Iniciar y cerrar sesión.
- Seleccionar una de las cinco plantillas disponibles.
- Capturar la información necesaria para elaborar documentos.
- Solicitar borradores mediante el backend y Groq API.
- Revisar y modificar el contenido generado.
- Guardar documentos en PostgreSQL mediante la API.
- Consultar documentos previamente guardados.
- Buscar documentos por nombre del empleado.
- Filtrar el historial por plantilla.
- Editar documentos guardados.
- Consultar las versiones anteriores y la versión actual.
- Descargar documentos en PDF y Word.
- Consultar las opciones de la cuenta.
- Recuperar y cambiar contraseñas.
- Administrar usuarios cuando se cuenta con el rol correspondiente.

## 3. Roles de usuario

El sistema distingue dos roles:

| Funcionalidad | Administrador (`admin`) | Usuario (`usuario`) |
|---|---|---|
| Generar documentos | Sí | Sí |
| Consultar el historial | Sí | Sí, sus documentos |
| Editar documentos | Sí | Sí, sus documentos |
| Consultar versiones | Sí | Sí, sus documentos |
| Buscar y filtrar documentos | Sí | Sí |
| Descargar documentos | Sí | Sí, sus documentos |
| Consultar y modificar su cuenta | Sí | Sí |
| Administrar usuarios | Sí | No |
| Activar y desactivar cuentas | Sí | No |

Los permisos de acceso son validados por FastAPI. El frontend muestra las opciones correspondientes al rol autenticado.

## 4. Requisitos

Para ejecutar el frontend se necesita:

- Node.js y npm instalados.
- El backend FastAPI configurado y en funcionamiento.
- PostgreSQL disponible para las operaciones que requieren almacenamiento.

Las instrucciones para configurar el proyecto completo se encuentran en el README principal del repositorio.

## 5. Instalación

Abrir una terminal dentro de la carpeta `frontend` y ejecutar:

```bash
npm install
```

Esto instala las dependencias indicadas en `package.json`.

## 6. Ejecución en desarrollo

Desde la carpeta `frontend`, ejecutar:

```bash
npm run dev
```

Por defecto, Vite proporciona la aplicación en:

http://localhost:5173/

El backend debe estar disponible en la dirección configurada para las solicitudes de la API.

## 7. Compilación

Para comprobar que el frontend puede compilarse:

```bash
npm run build
```

Los archivos generados se almacenan en la carpeta `dist`.

## 8. Comunicación con el backend

El frontend utiliza Axios para comunicarse con FastAPI mediante las funciones definidas en `src/api.js`.

En la configuración actual de desarrollo, la API utiliza:

http://127.0.0.1:8001

Entre las operaciones disponibles se encuentran:

- Autenticación y consulta del perfil.
- Consulta de plantillas.
- Generación y guardado de documentos.
- Consulta del historial documental.
- Edición de documentos.
- Consulta de versiones anteriores.
- Administración de usuarios.
- Recuperación y cambio de contraseñas.

La dirección de la API está definida actualmente en `src/api.js`. Su configuración mediante variables de entorno puede incorporarse en una mejora posterior.

## 9. Seguridad

Las solicitudes a endpoints protegidos utilizan el token de autenticación proporcionado por el backend.

Los permisos sobre usuarios y documentos se validan en FastAPI, no solamente mediante los controles visibles en React.

No se deben almacenar contraseñas, claves API ni otras credenciales privadas en el código del frontend.

## 10. Estado actual

El frontend funciona en un entorno de desarrollo local y cuenta con las principales funciones de generación y gestión documental.

Se han realizado pruebas manuales de autenticación, edición de documentos, consulta de versiones y búsqueda en el historial.

Todavía se requieren pruebas automatizadas y verificaciones adicionales de exportación y seguridad antes de considerar el sistema preparado para producción.