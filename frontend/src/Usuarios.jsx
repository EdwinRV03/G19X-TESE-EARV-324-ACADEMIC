import { useEffect, useState } from 'react';
import {
  Users,
  UserPlus,
  Loader2,
  ShieldCheck,
  AlertCircle,
  CheckCircle2,
  Pencil,
  X,
  UserRoundCheck,
  UserRoundX
} from 'lucide-react';

import { listarUsuarios, crearUsuario, editarUsuario, cambiarEstadoUsuario } from './api';

export default function Usuarios() {
  const [usuarios, setUsuarios] = useState([]);
  const [cargando, setCargando] = useState(true);
  const [guardando, setGuardando] = useState(false);
  const [usuarioEditando, setUsuarioEditando] = useState(null);

  const [formularioEdicion, setFormularioEdicion] = useState({
    nombre: '',
    email: ''
  });

  const [error, setError] = useState('');
  const [mensaje, setMensaje] = useState('');

  const [formulario, setFormulario] = useState({
    nombre: '',
    email: '',
    password: ''
  });

  const cargarUsuarios = async () => {
    try {
      const respuesta = await listarUsuarios();
      setUsuarios(respuesta.data);
      setError('');
    } catch (err) {
      setError('No se pudo obtener la lista de usuarios.');
    } finally {
      setCargando(false);
    }
  };

  useEffect(() => {
    cargarUsuarios();
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;

    setFormulario((anterior) => ({
      ...anterior,
      [name]: value
    }));
  };

  const handleCrearUsuario = async (e) => {
    e.preventDefault();

    setError('');
    setMensaje('');

    if (formulario.password.length < 8) {
      setError('La contraseña debe tener al menos 8 caracteres.');
      return;
    }

    setGuardando(true);

    try {
      await crearUsuario({
        nombre: formulario.nombre.trim(),
        email: formulario.email.trim().toLowerCase(),
        password: formulario.password
      });

      setMensaje('Usuario registrado correctamente.');

      setFormulario({
        nombre: '',
        email: '',
        password: ''
      });

      await cargarUsuarios();
    } catch (err) {
      const estado = err.response?.status;

      if (estado === 409) {
        setError('El correo electrónico ya está registrado.');
      } else if (estado === 403) {
        setError('No tienes permisos de administrador.');
      } else if (estado === 422) {
        setError('Revisa los datos del formulario.');
      } else if (estado === 401) {
        setError('Tu sesión no es válida o ha expirado.');
      } else {
        setError('No fue posible registrar el usuario.');
      }
    } finally {
      setGuardando(false);
    }
  };


const comenzarEdicion = (usuario) => {
  setUsuarioEditando(usuario.id);

  setFormularioEdicion({
    nombre: usuario.nombre,
    email: usuario.email
  });

  setError('');
  setMensaje('');
};

const cancelarEdicion = () => {
  setUsuarioEditando(null);
  setFormularioEdicion({
    nombre: '',
    email: ''
  });
};

const guardarEdicion = async (e) => {
  e.preventDefault();

  if (usuarioEditando === null) return;

  setGuardando(true);
  setError('');
  setMensaje('');

  try {
    await editarUsuario(usuarioEditando, {
      nombre: formularioEdicion.nombre.trim(),
      email: formularioEdicion.email.trim().toLowerCase()
    });

    await cargarUsuarios();
    cancelarEdicion();
    setMensaje('Usuario actualizado correctamente.');
  } catch (err) {
    const estado = err.response?.status;

    if (estado === 409) {
      setError('Ese correo ya está registrado.');
    } else if (estado === 403) {
      setError('No tienes permisos de administrador.');
    } else if (estado === 422) {
      setError('Revisa el nombre y el correo.');
    } else {
      setError('No fue posible actualizar el usuario.');
    }
  } finally {
    setGuardando(false);
  }
};

  const manejarCambioEstado = async (usuario) => {
    if (guardando || usuario.rol === 'admin') return;

    const accion = usuario.activo ? 'desactivar' : 'reactivar';
    const confirmado = window.confirm(
      `¿Deseas ${accion} la cuenta de ${usuario.nombre}?` +
      (usuario.activo
        ? '\nLa cuenta perderá acceso al sistema, pero sus documentos se conservarán.'
        : '\nLa cuenta podrá volver a iniciar sesión.')
    );

    if (!confirmado) return;

    setGuardando(true);
    setError('');
    setMensaje('');

    try {
      const respuesta = await cambiarEstadoUsuario(usuario.id);
      const listado = await listarUsuarios();
      setUsuarios(listado.data);
      setMensaje(respuesta.data.mensaje || 'Estado actualizado correctamente.');
    } catch (err) {
      const estado = err.response?.status;
      if (estado === 401) {
        setError('Tu sesión ha expirado. Vuelve a iniciar sesión.');
      } else if (estado === 403) {
        setError(err.response?.data?.detail || 'No tienes permisos para modificar esta cuenta.');
      } else if (estado === 404) {
        setError('La cuenta ya no existe. Actualiza la página.');
      } else {
        setError('No se pudo actualizar el estado de la cuenta.');
      }
    } finally {
      setGuardando(false);
    }
  };

  return (
    <div className="space-y-6">

      <div>
        <h2 className="text-xl font-bold text-white flex items-center gap-2">
          <Users className="w-6 h-6 text-sky-400" />
          Administración de Usuarios
        </h2>

        <p className="text-sm text-slate-400 mt-2">
          Consulta, registra y edita las cuentas de los colaboradores.
        </p>
      </div>

      {error && (
        <div
          role="alert"
          className="bg-red-500/10 border border-red-500/30 text-red-300 p-4 rounded-xl flex items-center gap-2"
        >
          <AlertCircle className="w-5 h-5" />
          {error}
        </div>
      )}

      {mensaje && (
        <div
          role="status"
          className="bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 p-4 rounded-xl flex items-center gap-2"
        >
          <CheckCircle2 className="w-5 h-5" />
          {mensaje}
        </div>
      )}

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">


        <section className="bg-slate-800/50 border border-slate-700 rounded-2xl p-6 shadow-xl">

          <h3 className="font-semibold text-white flex items-center gap-2 mb-5">
            <UserPlus className="w-5 h-5 text-sky-400" />
            Registrar usuario
          </h3>

          <form onSubmit={handleCrearUsuario} className="space-y-4">

            <div>
              <label className="block text-sm text-slate-300 mb-2">
                Nombre completo
              </label>

              <input
                type="text"
                name="nombre"
                value={formulario.nombre}
                onChange={handleChange}
                maxLength={100}
                required
                className="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-white"
                placeholder="Nombre del colaborador"
              />
            </div>

            <div>
              <label className="block text-sm text-slate-300 mb-2">
                Correo electrónico
              </label>

              <input
                type="email"
                name="email"
                value={formulario.email}
                onChange={handleChange}
                maxLength={100}
                required
                autoComplete="off"
                className="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-white"
                placeholder="correo@empresa.com"
              />
            </div>

            <div>
              <label className="block text-sm text-slate-300 mb-2">
                Contraseña inicial
              </label>

              <input
                type="password"
                name="password"
                value={formulario.password}
                onChange={handleChange}
                minLength={8}
                maxLength={128}
                required
                autoComplete="new-password"
                className="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-white"
                placeholder="Mínimo 8 caracteres"
              />

              <p className="text-xs text-slate-500 mt-2">
                La contraseña se almacenará como un hash seguro.
              </p>
            </div>

            <div className="bg-slate-900 border border-slate-700 rounded-xl p-3 text-sm text-slate-300 flex gap-2">
              <ShieldCheck className="w-5 h-5 text-sky-400 shrink-0" />

              <span>
                Las cuentas nuevas tendrán automáticamente el rol de usuario.
              </span>
            </div>

            <button
              type="submit"
              disabled={guardando}
              className="w-full bg-sky-600 hover:bg-sky-500 disabled:opacity-50 text-white font-semibold rounded-xl py-3 flex items-center justify-center gap-2 cursor-pointer"
            >
              {guardando ? (
                <>
                  <Loader2 className="w-5 h-5 animate-spin" />
                  Registrando...
                </>
              ) : (
                <>
                  <UserPlus className="w-5 h-5" />
                  Crear usuario
                </>
              )}
            </button>

          </form>
        </section>


        <section className="lg:col-span-2 bg-slate-800/50 border border-slate-700 rounded-2xl p-6 shadow-xl">

          <div className="flex justify-between items-center mb-5">
            <h3 className="font-semibold text-white flex items-center gap-2">
              <Users className="w-5 h-5 text-sky-400" />
              Usuarios registrados
            </h3>

            <span className="text-xs text-slate-400">
              {usuarios.length} cuentas
            </span>
          </div>

          {usuarioEditando !== null && (
            <form onSubmit={guardarEdicion} className="mb-6 p-5 bg-slate-900/80 border border-sky-500/40 rounded-xl space-y-4">
              <div className="flex items-center justify-between gap-3">
                <h4 className="text-sm font-semibold text-sky-300 flex items-center gap-2">
                  <Pencil className="w-4 h-4" />
                  Editar usuario #{usuarioEditando}
                </h4>
                <button
                  type="button"
                  onClick={cancelarEdicion}
                  disabled={guardando}
                  className="text-slate-400 hover:text-white cursor-pointer disabled:opacity-50"
                  aria-label="Cancelar edición"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label htmlFor="editar-nombre" className="block text-sm text-slate-300 mb-2">Nombre completo</label>
                  <input
                    id="editar-nombre"
                    type="text"
                    required
                    maxLength={100}
                    value={formularioEdicion.nombre}
                    onChange={(e) => setFormularioEdicion((prev) => ({ ...prev, nombre: e.target.value }))}
                    className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-sky-500"
                  />
                </div>
                <div>
                  <label htmlFor="editar-email" className="block text-sm text-slate-300 mb-2">Correo electrónico</label>
                  <input
                    id="editar-email"
                    type="email"
                    required
                    maxLength={100}
                    value={formularioEdicion.email}
                    onChange={(e) => setFormularioEdicion((prev) => ({ ...prev, email: e.target.value }))}
                    className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-sky-500"
                  />
                </div>
              </div>
              <div className="flex flex-wrap gap-3">
                <button
                  type="submit"
                  disabled={guardando}
                  className="bg-sky-600 hover:bg-sky-500 disabled:opacity-50 rounded-lg px-4 py-2 text-sm font-semibold text-white cursor-pointer"
                >
                  {guardando ? 'Guardando...' : 'Guardar cambios'}
                </button>
                <button
                  type="button"
                  onClick={cancelarEdicion}
                  disabled={guardando}
                  className="border border-slate-600 hover:bg-slate-800 rounded-lg px-4 py-2 text-sm text-slate-200 cursor-pointer disabled:opacity-50"
                >
                  Cancelar
                </button>
              </div>
            </form>
          )}

          {cargando ? (
            <div className="flex items-center gap-2 text-slate-400 py-10 justify-center">
              <Loader2 className="w-5 h-5 animate-spin" />
              Cargando usuarios...
            </div>
          ) : (
            <div className="overflow-x-auto">

              <table className="w-full text-left text-sm">
                <thead>
                  <tr className="border-b border-slate-700 text-slate-400">
                    <th className="p-3">ID</th>
                    <th className="p-3">Nombre</th>
                    <th className="p-3">Correo</th>
                    <th className="p-3">Rol</th>
                    <th className="p-3">Estado</th>
                    <th className="p-3 text-right">Acciones</th>
                  </tr>
                </thead>

                <tbody className="divide-y divide-slate-700/50">
                  {usuarios.map((usuario) => (
                    <tr key={usuario.id} className="text-slate-200">
                      <td className="p-3">{usuario.id}</td>
                      <td className="p-3">{usuario.nombre}</td>
                      <td className="p-3">{usuario.email}</td>
                      <td className="p-3">
                        <span
                          className={
                            usuario.rol === 'admin'
                              ? 'text-sky-300 bg-sky-500/10 px-3 py-1 rounded-full text-xs'
                              : 'text-emerald-300 bg-emerald-500/10 px-3 py-1 rounded-full text-xs'
                          }
                        >
                          {usuario.rol === 'admin'
                            ? 'Administrador'
                            : 'Usuario'}
                        </span>
                      </td>
                      <td className="p-3">
                        <span className={usuario.activo
                          ? 'text-emerald-300 bg-emerald-500/10 px-3 py-1 rounded-full text-xs'
                          : 'text-amber-300 bg-amber-500/10 px-3 py-1 rounded-full text-xs'}>
                          {usuario.activo ? 'Activo' : 'Inactivo'}
                        </span>
                      </td>
                      <td className="p-3 text-right">
                        <div className="flex flex-wrap justify-end gap-2">
                        <button
                          type="button"
                          onClick={() => comenzarEdicion(usuario)}
                          disabled={guardando}
                          className="inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-semibold text-sky-300 border border-sky-500/30 hover:bg-sky-500/10 rounded-lg cursor-pointer disabled:opacity-50"
                        >
                          <Pencil className="w-3.5 h-3.5" />
                          Editar
                        </button>
                        {usuario.rol === 'admin' ? (
                          <span className="px-3 py-1.5 text-xs text-slate-500" title="No se permite cambiar el estado de administradores">
                            No disponible
                          </span>
                        ) : (
                          <button
                            type="button"
                            onClick={() => manejarCambioEstado(usuario)}
                            disabled={guardando}
                            className={`inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-semibold border rounded-lg cursor-pointer disabled:opacity-50 ${usuario.activo
                              ? 'text-rose-300 border-rose-500/30 hover:bg-rose-500/10'
                              : 'text-emerald-300 border-emerald-500/30 hover:bg-emerald-500/10'}`}
                          >
                            {usuario.activo ? <UserRoundX className="w-3.5 h-3.5" /> : <UserRoundCheck className="w-3.5 h-3.5" />}
                            {usuario.activo ? 'Desactivar' : 'Reactivar'}
                          </button>
                        )}
                        </div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>

              {usuarios.length === 0 && (
                <p className="text-center text-slate-400 py-8">
                  No hay usuarios para mostrar.
                </p>
              )}
            </div>
          )}

        </section>
      </div>
    </div>
  );
}
