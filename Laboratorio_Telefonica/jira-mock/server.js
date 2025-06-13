// jira-mock/server.js
const express = require('express');
const fs = require('fs');
const app = express();
app.use(express.json());

// Credenciales válidas
const users = { 'juan@telefonica.es': 'Passw0rd!' };

app.post('/login', (req, res) => {
  const { user, pass } = req.body;
  if (users[user] === pass) return res.json({ token: 'valid-token' });
  res.status(401).json({ error: 'Unauthorized' });
});

app.get('/logs', (req, res) => {
  if (req.headers.authorization !== 'Bearer valid-token')
    return res.status(403).end();
  const logs = fs.readFileSync('./data/jira_logs.json');
  res.set('Content-Type', 'application/json').send(logs);
});

app.get('/tickets', (req, res) => {
  if (req.headers.authorization !== 'Bearer valid-token')
    return res.status(403).end();
  const csv = fs.readFileSync('./data/tickets.csv', 'utf-8');
  res.set('Content-Type', 'text/csv').send(csv);
});

app.listen(3000, () => console.log('Jira mock on 3000'));
