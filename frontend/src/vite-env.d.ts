/// <reference types="vite/client" />

// Tipagem das variáveis de ambiente (veja `.env.example`).
interface ImportMetaEnv {
  readonly VITE_API_URL: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
