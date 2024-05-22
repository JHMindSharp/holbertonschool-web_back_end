# ES6 Data Manipulation

## Description

This project focuses on learning and mastering data manipulation techniques using advanced JavaScript features, specifically ES6 syntax. You will learn to work efficiently with data structures like arrays, sets, and maps. Additionally, you will explore how to use array manipulation functions such as `map`, `filter`, and `reduce`.

## Learning Objectives

By the end of this project, you should be able to:

- Understand and use the `map`, `filter`, and `reduce` functions on arrays.
- Work with typed arrays for handling binary data.
- Utilize the `Set` data structure to store unique values.
- Implement the `Map` data structure for key-value pairs.
- Understand and use `WeakMap` for storing weakly held key-value pairs.
- Apply these concepts to solve practical problems and manipulate data effectively.

## Requirements

- All files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x.
- Code editors allowed: vi, vim, emacs, Visual Studio Code.
- All files should end with a new line.
- A `README.md` file, at the root of the project folder, is mandatory.
- Your code should use the `.js` extension.
- Your code will be tested using Jest and the command `npm run test`.
- Your code will be verified against lint using ESLint.
- Your code needs to pass all the tests and lint. You can verify the entire project running `npm run full-test`.
- All of your functions must be exported.

## Setup

1. **Install NodeJS 12.11.x**:

    ```bash
    curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
    sudo bash nodesource_setup.sh
    sudo apt install nodejs -y
    ```

2. **Verify installation**:

    ```bash
    nodejs -v
    # Expected output: v12.11.1

    npm -v
    # Expected output: 6.11.3
    ```

3. **Install project dependencies**:

    ```bash
    npm install
    ```

## Scripts

- **Run lint**: Check your code for linting errors using ESLint.
  
    ```bash
    npm run lint
    ```

- **Run tests**: Execute tests using Jest.
  
    ```bash
    npm run test
    ```

- **Run full test**: Run both linting and tests.
  
    ```bash
    npm run full-test
    ```

- **Run development**: Run a specific JavaScript file using Babel-node.

    ```bash
    npm run dev <file-name>.js
    ```

## Resources

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [Typed Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Typed_arrays)
- [Set Data Structure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
- [Map Data Structure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
- [WeakMap](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)

Happy coding!
