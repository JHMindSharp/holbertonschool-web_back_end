const express = require('express');
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n').slice(1);
      const students = lines.filter(line => line).map(line => line.split(','));
      const numberOfStudents = students.length;

      const fields = {};
      students.forEach((student) => {
        const field = student[3];
        const firstName = student[0];
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
      });

      resolve({ numberOfStudents, fields });
    });
  });
}

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  countStudents(process.argv[2])
    .then(({ numberOfStudents, fields }) => {
      let response = 'This is the list of our students\n';
      response += `Number of students: ${numberOfStudents}\n`;
      
      for (const field in fields) {
        response += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
      }

      res.status(200).send(response.trim());
    })
    .catch((error) => {
      res.status(500).send(error.message);
    });
});

app.listen(1245);

module.exports = app;
