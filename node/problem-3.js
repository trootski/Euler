/*
@author: troot
*/

function isPrime(num) {
  return [...new Array(parseInt(Math.ceil(Math.sqrt(num)))).keys()]
    .slice(2)
    .find((lp) => (num % lp) === 0) === undefined
}

const large_number = 600851475143;
const largest_prime = [
  ...new Array(
    parseInt(Math.floor(Math.sqrt(large_number/2)))
).keys()]
  .reverse()
  .find((num) => (large_number % num) === 0 && isPrime(num));

console.log(`Largest Prime is: ${largest_prime}`);

