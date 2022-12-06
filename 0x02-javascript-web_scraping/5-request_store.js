#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) throw err;
  fs.writeFile(process.argv[3], body, function (err) {
    if (err) throw err;
  });
});
