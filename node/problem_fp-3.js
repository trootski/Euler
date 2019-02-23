/*
@author: troot
*/

const cond = require('lodash/fp/cond');
const compose = require('lodash/fp/compose');
const stubFalse = require('lodash/fp/stubFalse');
const stubTrue = require('lodash/fp/stubTrue');
const lt = require('lodash/fp/lt');
const constant = require('lodash/fp/constant');
const largeNumber = 600851475143;

console.log(cond);
const ln = Math.ceil(Math.sqrt(largeNumber));
const checkIsMorePrime = l => {
  let p = 5;
  while (p * p < l) {
    if (l % p === 0 || l % (l + 2) === 0) {
      return false;
    }
    p += 6;
  }
  return true
};
const ifLT3 = v => cond([
  [i => lt(i, 3), constant(false)],
  [i => i % 2 === 0, constant(false)],
  [i => i % 3 === 0, constant(false)],
  [checkIsMorePrime, constant(false)],
  [stubTrue, constant(true)],
]);
const checkIsLargestPrime = compose(
  ifLT3,
);
// console.log(lt(2, 3));
console.log(checkIsLargestPrime()(11));
// function is_prime(n)
//      if n ≤ 3
//         return n > 1
//      else if n mod 2 = 0 or n mod 3 = 0
//         return false
//      let i ← 5
//      while i * i ≤ n
//         if n mod i = 0 or n mod (i + 2) = 0
//             return false
//         i ← i + 6
//      return true
// for( let i = 3; i < largeNumber; i+=2) {
//
// }

// function isPrime(num) {
//   return [...new Array(parseInt(Math.ceil(Math.sqrt(num)))).keys()]
//     .slice(2)
//     .find((lp) => (num % lp) === 0) === undefined
// }
//
// const largest_prime = [
//   ...new Array(
//     parseInt(Math.floor(Math.sqrt(largeNumber/2)))
// ).keys()]
//   .reverse()
//   .find((num) => (largeNumber % num) === 0 && isPrime(num));
//
// console.log(`Largest Prime is: ${largest_prime}`);
//
