const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('./data/ribridges.db');

db.serialize(() => {
  db.run(`CREATE TABLE IF NOT EXISTS residents (id INTEGER PRIMARY KEY, name TEXT, ssn TEXT, bank_account TEXT)`);
  db.run(`INSERT INTO residents (name, ssn, bank_account) VALUES
    ('Alice Johnson','123-45-6789','1111222233334444'),
    ('Bob Smith','987-65-4321','4444333322221111')`);
  db.run(`CREATE TABLE IF NOT EXISTS vendors (user TEXT, pass TEXT)`);
  db.run(`INSERT INTO vendors (user, pass) VALUES ('deloitte_user','Deloitte#123')`);
});
db.close();
console.log('DB initialized');
