#!/usr/bin/node
const request = require('request');
const ApiUrl = process.argv[2];
request(ApiUrl, function (err, res, body) {
  if (err) {
    console.error(err);
  }
  const data = {};
  for (const task of JSON.parse(body)) {
    if (task.completed === true) {
      if (data[task.userId]) {
        data[task.userId]++;
      } else {
        data[task.userId] = 1;
      }
    }
  }
  console.log(data);
});
