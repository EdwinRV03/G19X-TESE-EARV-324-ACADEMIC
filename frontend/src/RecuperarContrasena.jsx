import { useState } from 'react';
import { KeyRound, Mail, Loader2, AlertCircle, CheckCircle2 } from 'lucide-react';
import { solicitarRecuperacion, restablecerPassword } from './api';

export default function RecuperarContrasena({ token, onVolver }) {
  const [email, setEmail] = useState('');
  const [passwordNueva, setPasswordNueva] = useState('');
  const [confirmacion, setConfirmacion] = useState('');
  const [cargando, setCargando] = useState(false);
  const [error, setError] = useState('');
  const [mensaje, setMensaje] = useState('');
  const [completado, setCompletado] = useState(false);

  const solicitarEnlace = async (e) => {
    e.preventDefault();
    setError('');
    setMensaje('');
    setCargando(true);

    try {
      await solicitarRecuperacion(email.trim().toLowerCase());
      setMensaje(
        'Si el correo está registrado y activo, recibirás instrucciones de recuperación.'
      );
    } catch {
      setError('No fue posible procesar la solicitud. Inténtalo más tarde.');
    } finally {
      setCargando(false);
    }
  };

  const cambiarPassword = async (e) => {
    e.preventDefault();
    setError('');
    setMensaje('');

    if (passwordNueva.length < 8 || passwordNueva.length > 128) {
      setError('La contraseña debe tener entre 8 y 128 caracteres.');
      return;
    }

    if (passwordNueva !== confirmacion) {
      setError('Las contraseñas no coinciden.');
      return;
    }

    setCargando(true);

    try {
      await restablecerPassword(token, passwordNueva);
      setPasswordNueva('');
      setConfirmacion('');
      setCompletado(true);
      setMensaje('Contraseña restablecida correctamente. Ya puedes iniciar sesión.');
    } catch (err) {
      if (err.response?.status === 400) {
        setError('El enlace no es válido, ya fue utilizado o ha expirado.');
      } else if (err.response?.status === 422) {
        setError('La nueva contraseña no cumple los requisitos.');
      } else {
        setError('No fue posible restablecer la contraseña.');
      }
    } finally {
      setCargando(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-900 flex items-center justify-center p-6">
      <div className="w-full max-w-md bg-slate-800 border border-slate-700 rounded-2xl shadow-2xl p-8">
        <div className="text-center mb-7">
          <div className="inline-flex bg-sky-600 p-3 rounded-xl mb-4">
            {token ? (
              <KeyRound className="w-8 h-8 text-white" />
            ) : (
              <Mail className="w-8 h-8 text-white" />
            )}
          </div>

          <h1 className="text-2xl font-bold text-white">
            {token ? 'Restablecer contraseña' : 'Recuperar contraseña'}
          </h1>

          <p className="text-sm text-slate-400 mt-2">
            {token
              ? 'Establece una nueva contraseña para tu cuenta.'
              : 'Introduce tu correo para recibir un enlace de recuperación.'}
          </p>
        </div>

        {error && (
          <div role="alert" className="mb-4 p-3 rounded-xl bg-red-500/10 border border-red-500/30 text-red-300 text-sm flex gap-2">
            <AlertCircle className="w-4 h-4 shrink-0" />
            {error}
          </div>
        )}

        {mensaje && (
          <div role="status" className="mb-4 p-3 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 text-sm flex gap-2">
            <CheckCircle2 className="w-4 h-4 shrink-0" />
            {mensaje}
          </div>
        )}

        {!token ? (
          <form onSubmit={solicitarEnlace} className="space-y-4">
            <label className="block text-sm text-slate-300">
              Correo electrónico
            </label>
            <input
              type="email"
              required
              maxLength={100}
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              autoComplete="email"
              placeholder="correo@empresa.com"
              className="w-full bg-slate-900 border border-slate-600 rounded-xl px-4 py-3 text-white"
            />
            <button
              type="submit"
              disabled={cargando}
              className="w-full bg-sky-600 hover:bg-sky-500 disabled:opacity-50 text-white font-semibold rounded-xl py-3 flex items-center justify-center gap-2"
            >
              {cargando ? <Loader2 className="w-5 h-5 animate-spin" /> : null}
              Enviar enlace
            </button>
          </form>
        ) : !completado ? (
          <form onSubmit={cambiarPassword} className="space-y-4">
            <label className="block text-sm text-slate-300">
              Nueva contraseña
            </label>
            <input
              type="password"
              required
              minLength={8}
              maxLength={128}
              autoComplete="new-password"
              value={passwordNueva}
              onChange={(e) => setPasswordNueva(e.target.value)}
              className="w-full bg-slate-900 border border-slate-600 rounded-xl px-4 py-3 text-white"
              placeholder="Mínimo 8 caracteres"
            />

            <label className="block text-sm text-slate-300">
              Confirmar contraseña
            </label>
            <input
              type="password"
              required
              autoComplete="new-password"
              value={confirmacion}
              onChange={(e) => setConfirmacion(e.target.value)}
              className="w-full bg-slate-900 border border-slate-600 rounded-xl px-4 py-3 text-white"
            />

            <button
              type="submit"
              disabled={cargando}
              className="w-full bg-sky-600 hover:bg-sky-500 disabled:opacity-50 text-white font-semibold rounded-xl py-3 flex items-center justify-center gap-2"
            >
              {cargando ? <Loader2 className="w-5 h-5 animate-spin" /> : null}
              Restablecer contraseña
            </button>
          </form>
        ) : null}

        <button
          type="button"
          onClick={onVolver}
          className="w-full mt-5 text-sm text-sky-400 hover:text-sky-300 cursor-pointer"
        >
          Volver al inicio de sesión
        </button>
      </div>
    </div>
  );
}
