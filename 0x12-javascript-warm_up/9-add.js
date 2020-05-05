#!/usr/bin/node
const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);

/* Print the add of two numbers */
function add (a, b) {
  console.log(a + b);
}

add(num1, num2);
