/*
@author: troot
*/


// Find the sum of all the multiples of 3 or 5 below 1000.
const nArrLength = 1000;
const summed = new Array(nArrLength)
  .fill(0)
  .map((val, i, v) => i)
  .filter((val, i) => {
    return (((i % 3) === 0) || ((i % 5) === 0))
  })
  .reduce((acc, val) => acc + val, 0);

console.log('Filtered array value: ', summed);

