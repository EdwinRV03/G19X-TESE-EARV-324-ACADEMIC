
import axios from 'axios';

const API = axios.create({
  baseURL: 'http://127.0.0.1:8001',
});

let tokenAcceso = null;

export const establecerToken = (token) => {
  tokenAcceso = token;
};

API.interceptors.request.use((config) => {
  if (tokenAcceso) {
    config.headers.Authorization = `Bearer ${tokenAcceso}`;
  }

  return config;
});

export const iniciarSesion = (email, password) =>
  API.post('/auth/login', { email, password });

export const obtenerMiPerfil = () =>
  API.get('/auth/me');

export const getPlantillas = () => API.get('/plantillas/');

export const redactarBorrador = (data) =>
  API.post('/documentos/redactar-borrador/', data);

export const guardarDocumento = (data) =>
  API.post('/documentos/guardar/', data);

export const getDocumentos = () =>
  API.get('/documentos/');

export const listarUsuarios = () =>
  API.get('/auth/usuarios');

export const crearUsuario = (datos) =>
  API.post('/auth/usuarios', datos);

export const editarUsuario = (usuarioId, datos) =>
  API.put(`/auth/usuarios/${usuarioId}`, datos);

export const cambiarEstadoUsuario = (usuarioId) =>
  API.patch(`/auth/usuarios/${usuarioId}/estado`);

export const cambiarPassword = (passwordActual, passwordNueva) =>
  API.post('/auth/cambiar-password', {
    password_actual: passwordActual,
    password_nueva: passwordNueva
  });

export const solicitarRecuperacion = (email) =>
  API.post('/auth/solicitar-recuperacion', { email });

export const restablecerPassword = (token, passwordNueva) =>
  API.post('/auth/restablecer-password', {
    token,
    password_nueva: passwordNueva
  });

export default API;
