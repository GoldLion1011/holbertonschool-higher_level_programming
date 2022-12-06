#!/usr/bin/node
const fs = require('fs');

const content = 'Python is cool!';

try {
  fs.writeFileSync(process.argv[2], content);
} catch (err) {
  console.error(err);
}
