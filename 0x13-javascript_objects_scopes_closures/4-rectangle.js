#!/usr/bin/node

class Rectangle {
    constructor(w, h) {
        if (w > 0 && h > 0) {
            this.width = w;
            this.height = h; 
        } else {
            Object.create(null);
        }
    }
    print() {
        for (let i = 0; i < this.height; i++) {
            console.log('X'.repeat(this.width));
        }
    }
    rotate() {
        const t = this.height;
        this.height = this.width;
        this.width = t;
    }
    double() {
        this.height = 2 * this.height;
        this.width = 2 * this.width;
    }

}

module.exports = Rectangle;