// Save this file in: frontend/vite.config.js

import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: true, // This is crucial for Docker to map the port correctly
    strictPort: true,
    port: 5173,
  }
});