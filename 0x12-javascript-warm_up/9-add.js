#!/usr/bin/node

function add (x, y) {
  return x + y;
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

console.log(add(a, b));
