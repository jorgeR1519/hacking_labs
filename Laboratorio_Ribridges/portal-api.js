// portal-api.js - versión sin SQLite para evitar crashes
const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.json());

// Simula datos sensibles en memoria
const residents = [
  { name: 'Alice Johnson', ssn: '123-45-6789', bank_account: '1111222233334444' },
  { name: 'Bob Smith',     ssn: '987-65-4321', bank_account: '4444333322221111' }
];

// Middleware de autenticación simple
app.use((req, res, next) => {
  const auth = req.headers.authorization;
  if (!auth) return res.status(401).send('Missing token');
  const token = auth.split(' ')[1];
  // Aquí podrías validar firma HMAC, pero para demo se asume base64 válido
  const [user, pass] = Buffer.from(token, 'base64').toString().split(':');
  // Opcional: verificar user/pass en un array de vendors si lo deseas
  next();
});

// Endpoint que devuelve datos simulados
app.get('/residents', (req, res) => {
  console.log('Exfiltrated:', residents);
  res.json(residents);
});

// Escucha en todas las interfaces
app.listen(3001, '0.0.0.0', () => console.log('Portal API running on 3001'));
