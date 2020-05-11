#!/usr/bin/node

// imports module
const squareOld = require('./5-square');

// Class Square inherits from Square
class Square extends squareOld {
  // Method charPrint
  charPrint (c) {
    if (c === undefined) c = 'X';
    for (let i = 1; i <= this.width; i++) console.log(c.repeat(this.width));
  }
}

module.exports = Square;
