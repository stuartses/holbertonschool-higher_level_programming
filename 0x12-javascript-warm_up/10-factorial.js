#!/usr/bin/node
const number = parseInt(process.argv[2]);

/* Factorial of n */
function factorial (n) {
  if (isNaN(number) || n === 1) return 1;
  return n * factorial(n - 1);
}

console.log(factorial(number));
