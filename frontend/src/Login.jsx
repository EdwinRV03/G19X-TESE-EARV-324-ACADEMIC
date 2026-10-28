import { useState } from 'react';
import { FileText, LockKeyhole, Mail, Loader2 } from 'lucide-react';
import { iniciarSesion } from './api';

export default function Login({ onLogin, onRecuperarContrasena }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [cargando, setCargando] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setCargando(true);

    try {
      const respuesta = await iniciarSesion(email.trim(), password);
      await onLogin(respuesta.data);
    } catch (err) {
      if (err.response?.status === 401) {
        setError('Correo o contraseña incorrectos, intenta de nuevo.');
      } else if (err.response?.status === 403) {
        setError('Tu cuenta no tiene un rol autorizado.');
      } else {
        setError('No se pudo iniciar sesión. Verifica la conexión.');
      }
    } finally {
      setCargando(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-900 flex items-center justify-center p-6">
      <div className="w-full max-w-md bg-slate-800 border border-slate-700 rounded-2xl shadow-2xl p-8">

        <div className="flex flex-col items-center text-center mb-8">
          <div className="bg-sky-600 p-4 rounded-2xl mb-4">
            <FileText className="w-9 h-9 text-white" />
          </div>

          <h1 className="text-2xl font-bold text-white">
            Sistema de Notificaciones Legales
          </h1>

          <p className="text-slate-400 text-sm mt-2">
            Inicia sesión para acceder a la plataforma
          </p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-5">

          <div>
            <label className="block text-sm font-medium text-slate-300 mb-2">
              Correo electrónico
            </label>

            <div className="relative">
              <Mail className="absolute left-3 top-3 w-5 h-5 text-slate-500" />

              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                autoComplete="username"
                placeholder="correo@empresa.com"
                className="w-full bg-slate-900 border border-slate-600 rounded-xl pl-11 pr-4 py-3 text-white focus:outline-none focus:border-sky-500"
              />
            </div>
          </div>

          <div>
            <label className="block text-sm font-medium text-slate-300 mb-2">
              Contraseña
            </label>

            <div className="relative">
              <LockKeyhole className="absolute left-3 top-3 w-5 h-5 text-slate-500" />

              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                autoComplete="current-password"
                placeholder="Introduce tu contraseña"
                className="w-full bg-slate-900 border border-slate-600 rounded-xl pl-11 pr-4 py-3 text-white focus:outline-none focus:border-sky-500"
              />
            </div>
          </div>

          {error && (
            <p role="alert" className="text-sm text-red-400">
              {error}
            </p>
          )}

          <button
            type="submit"
            disabled={cargando}
            className="w-full bg-sky-600 hover:bg-sky-500 disabled:opacity-50 text-white font-semibold py-3 rounded-xl flex items-center justify-center gap-2"
          >
            {cargando ? (
              <>
                <Loader2 className="w-5 h-5 animate-spin" />
                Verificando...
              </>
            ) : (
              'Iniciar sesión'
            )}
          </button>
        </form>

        <button
          type="button"
          onClick={onRecuperarContrasena}
          className="w-full text-center text-sm text-sky-400 hover:text-sky-300 mt-5 cursor-pointer"
        >
          ¿Olvidaste tu contraseña?
        </button>

        <p className="text-center text-xs text-slate-500 mt-8">
          Acceso exclusivo para usuarios autorizados
        </p>

      </div>
    </div>
  );
}
