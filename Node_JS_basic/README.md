
# NodeJS Basics

This project is a set of tasks designed to teach the basics of Node.js, including creating HTTP servers, reading files, and using modules. This is part of the Holberton School curriculum and covers both basic and advanced concepts of Node.js.

## Project Structure

The project is divided into multiple tasks, with each task building on the previous one. Below is an overview of the key components of this project:

```
Node_JS_basic/
├── full_server/
│   ├── controllers/
│   │   ├── AppController.js
│   │   └── StudentsController.js
│   ├── routes/
│   │   └── index.js
│   ├── server.js
│   └── utils.js
├── node_modules/
├── .eslintrc.js
├── 0-console.js
├── 0-main.js
├── 1-stdin.js
├── 2-main_0.js
├── 2-main_1.js
├── 2-read_file.js
├── 3-main_0.js
├── 3-main_1.js
├── 3-read_file_async.js
├── 4-http.js
├── 5-http.js
├── 6-http_express.js
├── 7-http_express.js
├── babel.config.js
├── database.csv
└── package.json
```

## Tasks Overview

### Task 0: Executing basic JavaScript with Node.js
- **File:** `0-console.js`
- **Description:** A function named `displayMessage` that prints a string to the standard output.

### Task 1: Using Process stdin
- **File:** `1-stdin.js`
- **Description:** A program that prompts the user for their name and prints it back to the screen.

### Task 2: Reading a file synchronously
- **File:** `2-read_file.js`
- **Description:** Function `countStudents` reads a CSV file synchronously and logs the number of students and their fields.

### Task 3: Reading a file asynchronously
- **File:** `3-read_file_async.js`
- **Description:** A promise-based asynchronous function `countStudents` that reads a CSV file.

### Task 4: Creating an HTTP server with Node's HTTP module
- **File:** `4-http.js`
- **Description:** A simple HTTP server that responds with "Hello Holberton School!" on any endpoint.

### Task 5: More complex HTTP server using Node.js
- **File:** `5-http.js`
- **Description:** HTTP server that serves a list of students from a CSV file.

### Task 6: Creating an HTTP server with Express
- **File:** `6-http_express.js`
- **Description:** A simple HTTP server built using Express.

### Task 7: More complex HTTP server using Express
- **File:** `7-http_express.js`
- **Description:** HTTP server that lists students and filters them by their major using Express.

### Task 8: Organizing a complex HTTP server using Express
- **Directory:** `full_server/`
- **Description:** A complete server using Express, organized into controllers, routes, and utilities.

## Installation

### Prerequisites
- Node.js (version 20.x.x)
- npm

### Install dependencies

```bash
npm install
```

## Usage

To run the project in development mode using `nodemon`:

```bash
npm run dev
```

To run individual tasks, use:

```bash
node <filename>.js
```

For example, to run task 0:

```bash
node 0-main.js
```

## Project Details

### Linting and Testing
- **Lint:** `npm run lint`
- **Test:** `npm run test`

### Babel Configuration
The project uses Babel to transpile ES6+ code to ensure compatibility with Node.js.

```json
{
  "presets": [
    [
      "@babel/preset-env",
      {
        "targets": {
          "node": "current"
        }
      }
    ]
  ]
}
```

## Author

This project is part of the **Holberton School** curriculum.

Completed by: Jonathan Huybrechts

