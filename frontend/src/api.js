import axios from 'axios';

const API = axios.create({
  baseURL: 'http://127.0.0.1:8001',
});

export const getPlantillas = () => API.get('/plantillas/');
export const redactarBorrador = (data) => API.post('/documentos/redactar-borrador/', data);
export const guardarDocumento = (data) => API.post('/documentos/guardar/', data);
export const getDocumentos = () => API.get('/documentos/');

export default API;