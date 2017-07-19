/*
@author: troot
*/

function isPalindrome(num) {
  const arrMid = Math.floor(num.toString().length);
  return num
    .toString()
    .split('')
    .find((ele, i, arr) => { console.log(ele, arr[arr.length - i - 1]); return i < arrMid && ele !== arr[arr.length - i - 1]; })
}

console.log(isPalindrome(9009));

