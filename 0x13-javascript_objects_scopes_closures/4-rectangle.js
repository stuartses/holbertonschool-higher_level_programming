#!/usr/bin/node

// Class Rectangle
class Rectangle {
  // Constructor
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Method print Rectangle with char 'x'
  print () {
    for (let i = 1; i <= this.height; i++) console.log('X'.repeat(this.width));
  }

  // Method rotate rectangle
  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }

  // Method double
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
