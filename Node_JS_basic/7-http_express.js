const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  countStudents(process.argv[2])
    .then((fields) => {
      let response = 'This is the list of our students\n';
      const totalStudents = Object.values(fields).reduce((acc, curr) => acc + curr.length, 0);
      response += `Number of students: ${totalStudents}\n`;

      for (const field in fields) {
        if (fields.hasOwnProperty(field)) {
          response += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
        }
      }

      res.send(response);
    })
    .catch((error) => {
      res.status(500).send('Cannot load the database');
    });
});

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

module.exports = app;
