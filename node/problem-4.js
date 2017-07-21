/*
@author: troot
*/

function isPalindrome(num) {
  const arrMid = Math.floor(num.toString().length);
  const mirrorVal = (arr, i) => arr[arr.length - i - 1];
  return num
    .toString()
    .split('')
    .find((ele, i, arr) => {
      if (i >= arrMid) {
        return true;
      } else {
        return ele !== mirrorVal(arr, i);
      }
    }) === undefined
}

console.log(isPalindrome(19091));

