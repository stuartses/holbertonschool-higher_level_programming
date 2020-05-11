#!/usr/bin/node

// imports module
const Rectangle = require('./4-rectangle');

// Class Square inherits from Rectangle
class Square extends Rectangle {
  // constructor
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
