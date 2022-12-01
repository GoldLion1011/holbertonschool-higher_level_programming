#!/usr/bin/node
if (!process.argv[3]) {
  console.log(0);
} else {
  const arr = process.argv.slice(2);
  for (const z in arr) {
    arr[z] = parseInt(arr[z]);
  }
  console.log(arr.sort((a, b) => a - b).reverse()[1]);
}
