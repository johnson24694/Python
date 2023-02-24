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

// var y = 15;
// var arr = [2, 52, 9, 33, 16, 3, -55];
// var count = 0;
// for (var i = 0; i < arr.length; i++) {
//     if (arr[i] > y) {
//         count++;
        
//     }
    
// }
// console.log(count);


// Given an array, print the max, min and average values for that array.

// var max = 0;
// var min = 0;
// var sum = 0;
// var arr1 = [12, 5, 89, 45, 6, 0, 33];
// for (var i =0; i < arr1.length; i++) {
//     if (arr1[i] > max) {
//         max = arr1[i];
//     }
//     if (arr1[i] < min ) {
//         min = arr1[i];
//     }
//     sum = sum + arr1[i];
//     avg = sum/2;
// }
// console.log(max, min, avg);

// Swap String For Array Negative Values
// Replace any negative array values with 'Dojo'.



// var arr1 = [0, 23, -5, 87, -63, 15];

// for (var i = 0; i < arr1.length; i++) {
    
//     if (arr1[i] < 0) {
//         arr1[i] = "Dojo";
//         }
       
// }

// console.log(arr1);


// function sumnum(num1, num2) {
//     sum = num1 + num2;
//     return sum;
    
// };
// console.log(sumnum(12, 5))

// Print all odd integers from 1 to 255.

// for (var i = 1; i < 256; i++) {
//     if (i % 2 != 0){
//         console.log(i);
//     }
// }

// Iterate through a given array, printing each value.

// var myArr = [1, 25, 36, 'dojo', -58, 0];

// for (var i = 0; i < myArr.length; i++) {
//     console.log(myArr[i]);
// }

// Get and Print Average
// Analyze an array’s values and print the average.

// var avgArr = [5,22,95,13,4,2];
// var sum = 0;

//     for (var i = 0; i < avgArr.length; i++) {
//         sum += avgArr[i];
//         avg = sum / avgArr.length;

//     }
//     console.log(avg);


// Square each value in a given array, returning that same array with changed values.    

// var sqArr = [9, 45, 15, 80, 4, 3];

// for (var i=0; i < sqArr.length; i++) {
//     sqArr[i]  = sqArr[i]*sqArr[i];
    
// }
// console.log(sqArr);

// Zero Out Negative Numbers
// Return the given array, after setting any negative values to zero.

// newArr = [0, 24, -5, 6, -88, -1];

//     for (var i = 0; i < newArr.length; i++) {
//         if (newArr[i] < 0) {
//             newArr[i] = 0
//         }
//     }
//     console.log(newArr);

// Shift Array Values
// Given an array, move all values forward by one index, dropping the first and leaving a '0' value at the
// end


// myArr = [5, 3, 24, 7, 22, 0, 3, 8];
//             myArr.push(0);
//             myArr.shift();
//             console.log(myArr);

