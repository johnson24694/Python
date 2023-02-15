//Print all integers from 1 to 255.

// for (var i = 1; i < 256; i++) {
//     console.log(i);
// }

//Print integers from 0 to 255, and with each integer, print the sum so far.
// sum = 0
// for (var i = 0; i < 256; i++) {
//     sum = sum + i;
//     console.log(i, sum)
// }

//Given an array, find and print its largest element.
// var max = 0;
// var arr1 = [12, 5, 89, 45, 6, 0, 33];
// for (var i =0; i < arr1.length; i++) {
//     if (arr1[i] > max) {
//         max = arr1[i];
//     }
// }
// console.log(max);

// Create an array with odd integers between 1 and 255 (inclusive):

// var newArr = [];
// for (var i = 1; i < 256; i++) {
//     if (i % 2 != 0) {
        
//         newArr.push(i);
//     }
// }
// console.log(newArr)


// Given an array and a value Y count and print the number of array values greater than Y.:

var y = 15;
var arr = [2, 52, 9, 33, 16, 3, -55];
var count = 0;
for (var i = 0; i < arr.length; i++) {
    if (arr[i] > y) {
        count++;
        
    }
    
}
console.log(count);




