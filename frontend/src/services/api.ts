/** Endereço base da API (veja `.env.example`). */
export const API_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:8000/api';

/**
 * Faz uma requisição à API e retorna o JSON da resposta.
 *
 * @example
 * const usuarios = await api<Usuario[]>('/usuarios/');
 */
export async function api<T>(caminho: string, opcoes: RequestInit = {}): Promise<T> {
  const resposta = await fetch(`${API_URL}${caminho}`, {
    ...opcoes,
    headers: { 'Content-Type': 'application/json', ...opcoes.headers },
  });
  if (!resposta.ok) throw new Error(`Erro ${resposta.status} em ${caminho}`);
  return (resposta.status === 204 ? null : await resposta.json()) as T;
}
