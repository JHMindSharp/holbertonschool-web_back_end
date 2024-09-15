const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    countStudents(process.argv[2])
      .then((fields) => {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.write('This is the list of our students\n');
        const totalStudents = Object.values(fields).reduce((acc, curr) => acc + curr.length, 0);
        res.write(`Number of students: ${totalStudents}\n`);
        for (const field in fields) {
          if (fields.hasOwnProperty(field)) {
            res.write(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`);
          }
        }
        res.end();
      })
      .catch((error) => {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end(error.message);
      });
  }
});

app.listen(1245);

module.exports = app;
