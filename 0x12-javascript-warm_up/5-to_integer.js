#!/usr/bin/node
const arg = process.argv[2];
if (arg === undefined) {
  console.log('Not a number');
} else {
  console.log('My number: ' + +arg);
}
