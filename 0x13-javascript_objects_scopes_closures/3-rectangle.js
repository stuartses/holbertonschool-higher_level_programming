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
}

module.exports = Rectangle;
