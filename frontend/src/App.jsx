import React, { useState, useEffect } from 'react';
import API, { getPlantillas, redactarBorrador, guardarDocumento, getDocumentos } from './api';
import { FileText, Download, Sparkles, History, PlusCircle, AlertCircle, Loader2, Save, Building2, User, ShieldCheck, Image as ImageIcon } from 'lucide-react';
import Login from './Login';
import { establecerToken, obtenerMiPerfil } from './api';
import Usuarios from './Usuarios';
import MiCuenta from './MiCuenta';

function Dashboard({ usuario, onCerrarSesion }) {
  const [plantillas, setPlantillas] = useState([]);
  const [documentos, setDocumentos] = useState([]);
  const [plantillaSeleccionada, setPlantillaSeleccionada] = useState(null);
  
  // Manejo de Logo y Posición
  const [archivoLogo, setArchivoLogo] = useState(null);
  const [posicionLogo, setPosicionLogo] = useState('ninguno');

  const [variables, setVariables] = useState({
    empresa_nombre: '',
    empresa_correo: '',
    firmante_nombre: '',
    firmante_cargo: '',
    nombre_empleado: '',
    fecha_efectiva: '',
    motivo: ''
  });

  const [cargandoBorrador, setCargandoBorrador] = useState(false);
  const [cargandoGuardar, setCargandoGuardar] = useState(false);
  const [descargando, setDescargando] = useState(false);
  
  const [borradorGenerado, setBorradorGenerado] = useState(null);
  const [docGuardado, setDocGuardado] = useState(null);
  
  const [error, setError] = useState(null);
  const [vistaActiva, setVistaActiva] = useState('generar');

  useEffect(() => {
    cargarDatosIniciales();
  }, []);

  const cargarDatosIniciales = async () => {
    try {
      const [resPlantillas, resDocs] = await Promise.all([getPlantillas(), getDocumentos()]);
      const listaPlantillas = Array.isArray(resPlantillas.data) ? resPlantillas.data : [];
      const listaDocs = Array.isArray(resDocs.data) ? resDocs.data : [];

      setPlantillas(listaPlantillas);
      setDocumentos(listaDocs);

      if (listaPlantillas.length > 0) {
        setPlantillaSeleccionada(listaPlantillas[0]);
      }
    } catch (err) {
      console.error("Error al cargar datos iniciales:", err);
      setError("No se pudieron cargar las plantillas. Revisa que el backend esté activo.");
    }
  };

  const handleRedactarBorrador = async (e) => {
    e.preventDefault();
    if (!plantillaSeleccionada) {
      setError("Por favor selecciona una plantilla válida.");
      return;
    }

    setCargandoBorrador(true);
    setError(null);
    setBorradorGenerado(null);
    setDocGuardado(null);

    try {
      const payload = {
        plantilla_id: plantillaSeleccionada.id,
        datos_variables: variables
      };
      const res = await redactarBorrador(payload);
      setBorradorGenerado(res.data.contenido_generado);
    } catch (err) {
      setError("Error al generar borrador con IA. Revisa la conexión con el servidor.");
    } finally {
      setCargandoBorrador(false);
    }
  };

  const handleGuardarEnBD = async () => {
    if (!borradorGenerado || !plantillaSeleccionada) return;

    setCargandoGuardar(true);
    setError(null);

    try {
      const payload = {
        plantilla_id: plantillaSeleccionada.id,
        contenido: borradorGenerado,
        datos_variables: variables
      };
      const res = await guardarDocumento(payload);
      setDocGuardado(res.data);
      
      const resDocs = await getDocumentos();
      setDocumentos(Array.isArray(resDocs.data) ? resDocs.data : []);
    } catch (err) {
      setError("No se pudo guardar en la base de datos.");
    } finally {
      setCargandoGuardar(false);
    }
  };

  const descargarArchivo = async (documentoId, formato) => {
    setDescargando(true);
    setError(null);
    try {
      const formData = new FormData();
      formData.append('logo_pos', posicionLogo);
      if (archivoLogo) {
        formData.append('file', archivoLogo);
      }

      const response = await API.post(
        `/documentos/${documentoId}/exportar/${formato}`,
        formData,
        { responseType: 'blob' }
      );

      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `notificacion_${documentoId}.${formato}`);
      document.body.appendChild(link);
      link.click();
      link.remove();
    } catch (err) {
      setError("Error al descargar el archivo con formato.");
    } finally {
      setDescargando(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-900 text-slate-100 flex flex-col font-sans">
      <header className="bg-slate-800/80 backdrop-blur border-b border-slate-700 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
          <div className="flex items-center gap-3">
            <div className="p-2.5 bg-sky-600 rounded-xl shadow-lg shadow-sky-600/30">
              <FileText className="w-6 h-6 text-white" />
            </div>
            <div>
              <h1 className="text-xl font-bold tracking-tight text-white">Sistema de Notificaciones Legales</h1>
              <p className="text-xs text-sky-400 font-medium">Redacción Formal Asistida por IA</p>
            </div>
          </div>

          <nav className="flex flex-wrap items-center gap-2">
            <button
              type="button"
              onClick={onCerrarSesion}
              className="px-4 py-2 rounded-lg text-sm font-medium text-rose-300 hover:bg-rose-500/10 border border-rose-500/30 cursor-pointer"
            >
              Cerrar sesión
            </button>
            <button
              onClick={() => setVistaActiva('generar')}
              className={`flex items-center gap-2 px-4 py-2 rounded-lg font-medium text-sm transition-all cursor-pointer ${
                vistaActiva === 'generar' ? 'bg-sky-600 text-white shadow-md' : 'text-slate-400 hover:text-white hover:bg-slate-700/50'
              }`}
            >
              <Sparkles className="w-4 h-4" /> Redactar Carta
            </button>
            <button
              onClick={() => setVistaActiva('historial')}
              className={`flex items-center gap-2 px-4 py-2 rounded-lg font-medium text-sm transition-all cursor-pointer ${
                vistaActiva === 'historial' ? 'bg-sky-600 text-white shadow-md' : 'text-slate-400 hover:text-white hover:bg-slate-700/50'
              }`}
            >
              <History className="w-4 h-4" /> Historial ({documentos.length})
            </button>
            {usuario?.rol === 'admin' && (
              <button
                type="button"
                onClick={() => setVistaActiva('usuarios')}
                className={`flex items-center gap-2 px-4 py-2 rounded-lg font-medium text-sm transition-all cursor-pointer ${
                  vistaActiva === 'usuarios'
                  ? 'bg-sky-600 text-white shadow-md'
                  : 'text-slate-400 hover:text-white hover:bg-slate-700/50'
                }`}
              >
                <User className="w-4 h-4" />
                Usuarios
              </button>
            )}
            <button
              type="button"
              onClick={() => setVistaActiva('mi-cuenta')}
              className={`flex items-center gap-2 px-4 py-2 rounded-lg font-medium text-sm transition-all cursor-pointer ${
                vistaActiva === 'mi-cuenta'
                  ? 'bg-sky-600 text-white shadow-md'
                  : 'text-slate-400 hover:text-white hover:bg-slate-700/50'
              }`}
            >
              <User className="w-4 h-4" /> Mi cuenta
            </button>
          </nav>
        </div>
      </header>

      <main className="flex-1 max-w-7xl w-full mx-auto p-6">
        {vistaActiva === 'mi-cuenta' ? (
          <MiCuenta usuario={usuario} onCerrarSesion={onCerrarSesion} />
        ) : vistaActiva === 'usuarios' && usuario?.rol === 'admin' ? (
          <Usuarios />
        ) : vistaActiva === 'generar' ? (
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
            <div className="lg:col-span-5 bg-slate-800/50 border border-slate-700/60 rounded-2xl p-6 shadow-xl backdrop-blur-sm max-h-[80vh] overflow-y-auto space-y-4">
              <h2 className="text-lg font-semibold text-white mb-2 flex items-center gap-2">
                <PlusCircle className="w-5 h-5 text-sky-400" />
                Datos del Documento
              </h2>

              <form onSubmit={handleRedactarBorrador} className="space-y-4">
                <div>
                  <label className="block text-xs font-semibold uppercase tracking-wider text-slate-400 mb-1">
                    Plantilla Base
                  </label>
                  <select
                    className="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-2 text-sm text-slate-200 focus:ring-2 focus:ring-sky-500"
                    value={plantillaSeleccionada?.id || ''}
                    onChange={(e) => {
                      const sel = plantillas.find(p => p.id === parseInt(e.target.value));
                      setPlantillaSeleccionada(sel || null);
                    }}
                  >
                    {plantillas.length === 0 && (
                      <option value="">Cargando plantillas...</option>
                    )}
                    {plantillas.map((p) => (
                      <option key={p.id} value={p.id}>{p.titulo}</option>
                    ))}
                  </select>
                </div>

                <div className="pt-3 border-t border-slate-700/50 space-y-3">
                  <h3 className="text-xs font-semibold uppercase tracking-wider text-sky-400 flex items-center gap-1.5">
                    <ImageIcon className="w-4 h-4" /> Logo Institucional (Opcional)
                  </h3>

                  <div>
                    <label className="block text-xs text-slate-300 mb-1">Subir Archivo de Logo (PNG/JPG)</label>
                    <input
                      type="file"
                      accept="image/*"
                      className="w-full text-xs text-slate-400 bg-slate-900 border border-slate-700 rounded-xl p-2 file:mr-3 file:py-1 file:px-3 file:rounded-lg file:border-0 file:text-xs file:font-semibold file:bg-sky-600 file:text-white hover:file:bg-sky-500 cursor-pointer"
                      onChange={(e) => setArchivoLogo(e.target.files[0])}
                    />
                  </div>

                  <div>
                    <label className="block text-xs text-slate-300 mb-1">Posición del Logo en la Hoja</label>
                    <select
                      className="w-full bg-slate-900 border border-slate-700 rounded-xl px-3.5 py-2 text-sm text-slate-200"
                      value={posicionLogo}
                      onChange={(e) => setPosicionLogo(e.target.value)}
                    >
                      <option value="ninguno">Sin logo</option>
                      <option value="arriba_izquierda">Arriba a la Izquierda (Membrete)</option>
                      <option value="arriba_derecha">Arriba a la Derecha (Membrete)</option>
                      <option value="marca_agua">Al Centro (Marca de Agua Tenue)</option>
                    </select>
                  </div>
                </div>

                <div className="pt-3 border-t border-slate-700/50 space-y-3">
                  <h3 className="text-xs font-semibold uppercase tracking-wider text-sky-400 flex items-center gap-1.5">
                    <Building2 className="w-4 h-4" /> Datos de la Empresa
                  </h3>

                  <div>
                    <label className="block text-xs text-slate-300 mb-1">Nombre de la Empresa</label>
                    <input
                      type="text"
                      required
                      className="w-full bg-slate-900 border border-slate-700 rounded-xl px-3.5 py-2 text-sm text-slate-200"
                      value={variables.empresa_nombre}
                      onChange={(e) => setVariables({ ...variables, empresa_nombre: e.target.value })}
                    />
                  </div>

                  <div className="grid grid-cols-2 gap-3">
                    <div>
                      <label className="block text-xs text-slate-300 mb-1">Firmante</label>
                      <input
                        type="text"
                        required
                        className="w-full bg-slate-900 border border-slate-700 rounded-xl px-3.5 py-2 text-sm text-slate-200"
                        value={variables.firmante_nombre}
                        onChange={(e) => setVariables({ ...variables, firmante_nombre: e.target.value })}
                      />
                    </div>
                    <div>
                      <label className="block text-xs text-slate-300 mb-1">Cargo</label>
                      <input
                        type="text"
                        required
                        className="w-full bg-slate-900 border border-slate-700 rounded-xl px-3.5 py-2 text-sm text-slate-200"
                        value={variables.firmante_cargo}
                        onChange={(e) => setVariables({ ...variables, firmante_cargo: e.target.value })}
                      />
                    </div>
                  </div>
                </div>

                <div className="pt-3 border-t border-slate-700/50 space-y-3">
                  <h3 className="text-xs font-semibold uppercase tracking-wider text-sky-400 flex items-center gap-1.5">
                    <User className="w-4 h-4" /> Datos del Destinatario
                  </h3>

                  <div>
                    <label className="block text-xs text-slate-300 mb-1">Nombre Completo del Empleado</label>
                    <input
                      type="text"
                      required
                      className="w-full bg-slate-900 border border-slate-700 rounded-xl px-3.5 py-2 text-sm text-slate-200"
                      value={variables.nombre_empleado}
                      onChange={(e) => setVariables({ ...variables, nombre_empleado: e.target.value })}
                    />
                  </div>

                  <div>
                    <label className="block text-xs text-slate-300 mb-1">Fecha Efectiva</label>
                    <input
                      type="text"
                      required
                      className="w-full bg-slate-900 border border-slate-700 rounded-xl px-3.5 py-2 text-sm text-slate-200"
                      value={variables.fecha_efectiva}
                      onChange={(e) => setVariables({ ...variables, fecha_efectiva: e.target.value })}
                    />
                  </div>

                  <div>
                    <label className="block text-xs text-slate-300 mb-1">Motivo / Causal Legal</label>
                    <textarea
                      rows="2"
                      required
                      className="w-full bg-slate-900 border border-slate-700 rounded-xl px-3.5 py-2 text-sm text-slate-200 resize-none"
                      value={variables.motivo}
                      onChange={(e) => setVariables({ ...variables, motivo: e.target.value })}
                    />
                  </div>
                </div>

                <button
                  type="submit"
                  disabled={cargandoBorrador || plantillas.length === 0}
                  className="w-full py-3 px-4 bg-sky-600 hover:bg-sky-500 text-white font-semibold rounded-xl shadow-lg shadow-sky-600/20 transition-all flex items-center justify-center gap-2 disabled:opacity-50 cursor-pointer"
                >
                  {cargandoBorrador ? (
                    <>
                      <Loader2 className="w-5 h-5 animate-spin" />
                      Redactando borrador con Inteligancia Artificial...
                    </>
                  ) : (
                    <>
                      <Sparkles className="w-5 h-5" />
                      Paso 1: Generar Vista Previa
                    </>
                  )}
                </button>
              </form>
            </div>

            <div className="lg:col-span-7 flex flex-col">
              <div className="bg-slate-800/50 border border-slate-700/60 rounded-2xl p-6 flex-1 flex flex-col shadow-xl backdrop-blur-sm">
                
                <div className="flex justify-between items-center mb-4 pb-3 border-b border-slate-700/60">
                  <h2 className="text-lg font-semibold text-white flex items-center gap-2">
                    <FileText className="w-5 h-5 text-sky-400" />
                    Vista Previa del Borrador
                  </h2>

                  <div className="flex gap-2">
                    {borradorGenerado && !docGuardado && (
                      <button
                        onClick={handleGuardarEnBD}
                        disabled={cargandoGuardar}
                        className="px-4 py-2 bg-emerald-600 hover:bg-emerald-500 text-white rounded-xl text-xs font-semibold flex items-center gap-1.5 shadow-md cursor-pointer disabled:opacity-50"
                      >
                        {cargandoGuardar ? (
                          <Loader2 className="w-4 h-4 animate-spin" />
                        ) : (
                          <>
                            <Save className="w-4 h-4" /> Paso 2: Guardar en BD
                          </>
                        )}
                      </button>
                    )}

                    {docGuardado && (
                      <div className="flex gap-2">
                        <button
                          onClick={() => descargarArchivo(docGuardado.documento_id, 'pdf')}
                          disabled={descargando}
                          className="px-3 py-1.5 bg-rose-600/20 text-rose-300 border border-rose-500/30 hover:bg-rose-600/30 rounded-lg text-xs font-semibold flex items-center gap-1.5 transition-all cursor-pointer"
                        >
                          <Download className="w-3.5 h-3.5" /> PDF
                        </button>
                        <button
                          onClick={() => descargarArchivo(docGuardado.documento_id, 'docx')}
                          disabled={descargando}
                          className="px-3 py-1.5 bg-blue-600/20 text-blue-300 border border-blue-500/30 hover:bg-blue-600/30 rounded-lg text-xs font-semibold flex items-center gap-1.5 transition-all cursor-pointer"
                        >
                          <Download className="w-3.5 h-3.5" /> Word
                        </button>
                      </div>
                    )}
                  </div>
                </div>

                {error && (
                  <div className="p-4 bg-rose-500/10 border border-rose-500/30 rounded-xl text-rose-300 text-sm flex items-center gap-3 mb-4">
                    <AlertCircle className="w-5 h-5 flex-shrink-0" />
                    {error}
                  </div>
                )}

                <div className="flex-1 bg-slate-950/80 border border-slate-800 rounded-xl p-6 text-sm text-slate-300 overflow-y-auto max-h-[520px] shadow-inner font-sans">
                  {docGuardado && (
                    <div className="inline-flex items-center gap-2 px-3 py-1 bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs rounded-full mb-4">
                      <ShieldCheck className="w-3.5 h-3.5" /> Guardado exitosamente en PostgreSQL (ID #{docGuardado.documento_id}).
                    </div>
                  )}

                  {borradorGenerado ? (
                    <div className="flex flex-col gap-2">
                      <label className="text-xs font-semibold text-sky-400 uppercase tracking-wider flex items-center justify-between">
                        <span>Edición de borrador (puedes modificar el texto libremente)</span>
                        <span className="text-slate-500 font-normal normal-case">Cambios en tiempo real</span>
                      </label>
                      <textarea
                        rows="15"
                        className="w-full bg-slate-900/90 border border-slate-700/80 rounded-xl p-4 text-sm text-slate-100 leading-relaxed font-sans focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 resize-y"
                        value={borradorGenerado}
                        onChange={(e) => setBorradorGenerado(e.target.value)}
                      />
                    </div>
                  ) : (
                    <div className="h-full min-h-[320px] flex flex-col items-center justify-center text-slate-500 text-center">
                      <FileText className="w-12 h-12 mb-3 opacity-30" />
                      <p className="text-base font-medium">Borrador no generado</p>
                      <p className="text-xs text-slate-600 mt-1">Ingresa los datos requeridos y presiona "Paso 1: Generar Vista Previa"</p>
                    </div>
                  )}
                </div>

              </div>
            </div>

          </div>
        ) : (
          <div className="bg-slate-800/50 border border-slate-700/60 rounded-2xl p-6 shadow-xl backdrop-blur-sm">
            <h2 className="text-lg font-semibold text-white mb-6 flex items-center gap-2">
              <History className="w-5 h-5 text-sky-400" />
              Historial de Documentos Guardados
            </h2>

            <div className="overflow-x-auto">
              <table className="w-full text-left border-collapse">
                <thead>
                  <tr className="border-b border-slate-700 text-xs uppercase text-slate-400 font-semibold">
                    <th className="py-3 px-4">ID</th>
                    <th className="py-3 px-4">Plantilla</th>
                    <th className="py-3 px-4">Estado</th>
                    <th className="py-3 px-4 text-right">Descargas</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-700/50 text-sm">
                  {documentos.map((doc) => (
                    <tr key={doc.documento_id} className="hover:bg-slate-700/20 transition-all">
                      <td className="py-4 px-4 font-mono text-sky-400 font-semibold">#{doc.documento_id}</td>
                      <td className="py-4 px-4 text-slate-200 font-medium">{doc.titulo_plantilla}</td>
                      <td className="py-4 px-4">
                        <span className="px-2.5 py-1 bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs rounded-full capitalize">
                          {doc.estado}
                        </span>
                      </td>
                      <td className="py-4 px-4 text-right">
                        <div className="flex justify-end gap-2">
                          <button
                            onClick={() => descargarArchivo(doc.documento_id, 'pdf')}
                            className="px-2.5 py-1 bg-rose-600/20 text-rose-300 border border-rose-500/30 hover:bg-rose-600/30 rounded-lg text-xs font-semibold transition-all inline-flex items-center gap-1 cursor-pointer"
                          >
                            <Download className="w-3 h-3" /> PDF
                          </button>
                          <button
                            onClick={() => descargarArchivo(doc.documento_id, 'docx')}
                            className="px-2.5 py-1 bg-blue-600/20 text-blue-300 border border-blue-500/30 hover:bg-blue-600/30 rounded-lg text-xs font-semibold transition-all inline-flex items-center gap-1 cursor-pointer"
                          >
                            <Download className="w-3 h-3" /> Word
                          </button>
                        </div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}


export default function App() {
  const [usuarioActual, setUsuarioActual] = useState(null);

  const manejarLogin = async (datosLogin) => {
    establecerToken(datosLogin.access_token);

    try {
      const respuesta = await obtenerMiPerfil();
      setUsuarioActual(respuesta.data);
    } catch (error) {
      establecerToken(null);
      setUsuarioActual(null);
      throw error;
    }
  };

  const cerrarSesion = () => {
    establecerToken(null);
    setUsuarioActual(null);
  };

  if (!usuarioActual) {
    return <Login onLogin={manejarLogin} />;
  }

  return (
    <Dashboard
      usuario={usuarioActual}
      onCerrarSesion={cerrarSesion}
    />
  );
}
