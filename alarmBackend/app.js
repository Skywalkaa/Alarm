const express = require('express');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.json());

const mysql = require('mysql');

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'alarm'
});

connection.connect((err) => {
  if (err) throw err;
  console.log('Connected to MySQL');
});

app.post('/api/data', (req, res) => {
  console.log(req.body);
  const { current_digit, alarm_state } = req.body;
  const sql = 'INSERT INTO alarm_data (current_digit, alarm_state) VALUES (?, ?)';
  connection.query(sql, [current_digit, alarm_state], (err, result) => {
    if (err) throw err;
    res.json({ message: 'Data saved successfully' });
  });
});


app.post('/api/command', (req, res) => {
  console.log(req.body.button);
  const button = req.body.button;

  const sql = 'INSERT INTO button_commands (button) VALUES (?)';
  connection.query(sql, [button], (err, result) => {
    if (err) {
      console.error(err);
      res.status(500).json({ message: 'Failed to save button command' });
      return;
    }

    console.log(`Button command received: ${button}`);
    res.json({ message: 'Button command received and saved' });
  });
});



app.get('/api/command', (req, res) => {
  connection.query('SELECT * FROM button_commands ORDER BY created_at DESC LIMIT 1', (err, result) => {
    if (err) throw err;
    res.json({ button: result[0].button });
  });
});

app.get('/api/data', (req, res) => {
  const sql = 'SELECT * FROM alarm_data ORDER BY created_at DESC LIMIT 1';
  connection.query(sql, (err, result) => {
    if (err) throw err;
    const data = {
      current_digit: result[0].current_digit,
      alarm_state: result[0].alarm_state,
      created_at: result[0].created_at
    };
    res.json(data);
  });
});

// app.post('/api/command/clear', (req, res) => {
//   const sql = 'DELETE FROM button_commands WHERE id = ?';
//   connection.query(sql, [req.body.id], (err, result) => {
//     if (err) {
//       console.error(err);
//       res.status(500).json({ message: 'Failed to clear button command' });
//       return;
//     }

//     res.json({ message: 'Button command cleared' });
//   });
// });

app.listen(3000, '192.168.1.109', () => {
  console.log('Server is running on port 3000');
});
