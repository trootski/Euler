/*
@author: troot
*/
function getFibonacci(val, prev1, acc) {
  const tmpVal = val;
  val = prev1 + val;
  prev1 = tmpVal;
  if ((val % 2) === 0) acc+= val;
  if (val >= 4000000) {
    return acc;
  } else {
    return getFibonacci(val, prev1, acc);
  }
}

console.log('Sum of even values that are part of the fibonacci series and less than 4,000,000: ', getFibonacci(1, 0, 0, 0));


