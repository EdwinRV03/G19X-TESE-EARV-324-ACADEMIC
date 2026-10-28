import { useState } from 'react';
import { KeyRound, Loader2, ShieldCheck, AlertCircle } from 'lucide-react';
import { cambiarPassword } from './api';

export default function MiCuenta({ usuario, onCerrarSesion }) {
  const [passwordActual, setPasswordActual] = useState('');
  const [passwordNueva, setPasswordNueva] = useState('');
  const [confirmacion, setConfirmacion] = useState('');
  const [guardando, setGuardando] = useState(false);
  const [error, setError] = useState('');

  const handleCambiarPassword = async (e) => {
    e.preventDefault();
    setError('');

    if (passwordNueva.length < 8) {
      setError('La nueva contraseña debe tener al menos 8 caracteres.');
      return;
    }

    if (passwordNueva !== confirmacion) {
      setError('Las contraseñas nuevas no coinciden.');
      return;
    }

    setGuardando(true);

    try {
      await cambiarPassword(passwordActual, passwordNueva);

      setPasswordActual('');
      setPasswordNueva('');
      setConfirmacion('');

      onCerrarSesion();
    } catch (err) {
      const detalle = err.response?.data?.detail;

      if (err.response?.status === 400) {
        setError(
          typeof detalle === 'string'
            ? detalle
            : 'Revisa tu contraseña actual.'
        );
      } else if (err.response?.status === 401) {
        setError('Tu sesión ya no es válida. Vuelve a iniciar sesión.');
      } else if (err.response?.status === 422) {
        setError('La nueva contraseña no cumple los requisitos.');
      } else {
        setError('No se pudo actualizar la contraseña.');
      }
    } finally {
      setGuardando(false);
    }
  };

  return (
    <div className="max-w-2xl mx-auto space-y-6">
      <div>
        <h2 className="text-xl font-bold text-white flex items-center gap-2">
          <KeyRound className="w-6 h-6 text-sky-400" />
          Mi cuenta
        </h2>
        <p className="text-sm text-slate-400 mt-2">
          Consulta tu información y actualiza tu contraseña.
        </p>
      </div>

      <section className="bg-slate-800/50 border border-slate-700 rounded-2xl p-6">
        <h3 className="text-white font-semibold mb-4">
          Información de la cuenta
        </h3>

        <div className="space-y-2 text-sm text-slate-300">
          <p><strong>Nombre:</strong> {usuario.nombre}</p>
          <p><strong>Correo:</strong> {usuario.email}</p>
          <p>
            <strong>Rol:</strong>{' '}
            {usuario.rol === 'admin' ? 'Administrador' : 'Usuario'}
          </p>
        </div>
      </section>

      <section className="bg-slate-800/50 border border-slate-700 rounded-2xl p-6">
        <h3 className="text-white font-semibold flex items-center gap-2 mb-5">
          <ShieldCheck className="w-5 h-5 text-sky-400" />
          Cambiar contraseña
        </h3>

        {error && (
          <div
            role="alert"
            className="mb-4 p-3 bg-red-500/10 border border-red-500/30 rounded-xl text-red-300 text-sm flex items-center gap-2"
          >
            <AlertCircle className="w-4 h-4" />
            {error}
          </div>
        )}

        <form onSubmit={handleCambiarPassword} className="space-y-4">
          <div>
            <label className="block text-sm text-slate-300 mb-2">
              Contraseña actual
            </label>
            <input
              type="password"
              value={passwordActual}
              onChange={(e) => setPasswordActual(e.target.value)}
              autoComplete="current-password"
              required
              className="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-white"
            />
          </div>

          <div>
            <label className="block text-sm text-slate-300 mb-2">
              Nueva contraseña
            </label>
            <input
              type="password"
              value={passwordNueva}
              onChange={(e) => setPasswordNueva(e.target.value)}
              autoComplete="new-password"
              minLength={8}
              maxLength={128}
              required
              className="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-white"
              placeholder="Mínimo 8 caracteres"
            />
          </div>

          <div>
            <label className="block text-sm text-slate-300 mb-2">
              Confirmar nueva contraseña
            </label>
            <input
              type="password"
              value={confirmacion}
              onChange={(e) => setConfirmacion(e.target.value)}
              autoComplete="new-password"
              required
              className="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-white"
            />
          </div>

          <button
            type="submit"
            disabled={guardando}
            className="w-full bg-sky-600 hover:bg-sky-500 disabled:opacity-50 text-white font-semibold rounded-xl py-3 flex items-center justify-center gap-2 cursor-pointer"
          >
            {guardando ? (
              <>
                <Loader2 className="w-5 h-5 animate-spin" />
                Actualizando...
              </>
            ) : (
              'Actualizar contraseña'
            )}
          </button>
        </form>

        <p className="text-xs text-slate-400 mt-4">
          Por seguridad, después de cambiar tu contraseña tendrás
          que iniciar sesión nuevamente.
        </p>
      </section>
    </div>
  );
}
