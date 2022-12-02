#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = parseInt(w);
      this.height = parseInt(h);
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  doubles () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
};
