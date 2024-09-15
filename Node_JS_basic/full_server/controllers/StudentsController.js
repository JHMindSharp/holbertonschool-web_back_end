const readDatabase = require('../utils');

class StudentsController {
  static getAllStudents(req, res) {
    const filePath = process.argv[2];

    readDatabase(filePath)
      .then((fields) => {
        let response = 'This is the list of our students\n';
        for (const field in fields) {
          response += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
        }
        res.status(200).send(response.trim());
      })
      .catch(() => res.status(500).send('Cannot load the database'));
  }

  static getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    const filePath = process.argv[2];

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(filePath)
      .then((fields) => {
        const list = fields[major];
        res.status(200).send(`List: ${list.join(', ')}`);
      })
      .catch(() => res.status(500).send('Cannot load the database'));
  }
}

module.exports = StudentsController;
