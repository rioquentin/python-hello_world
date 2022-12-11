#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (h <= 0 || w <= 0 || h === undefined || w === undefined) {
      this.width = undefined;
      this.height = undefined;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    let x = 0;

    while (i < this.height) {
      while (x < this.width) {
        process.stdout.write('X');
        x += 1;
      }
      console.log('');
      i += 1;
      x = 0;
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
