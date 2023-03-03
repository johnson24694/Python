// Convert Celsius to Fahrenheit
// The formula to convert from Celsius to Fahrenheit is the temperature in Celsius times 9/5, plus 32.

// You are given a variable celsius representing a temperature in Celsius. Use the variable fahrenheit already defined and assign it the Fahrenheit temperature equivalent to the given Celsius temperature. Use the formula mentioned above to help convert the Celsius temperature to Fahrenheit.

// function convertCtoF(celsius) {
//     let fahrenheit = (celsius * 9/5) + 32;
//     return fahrenheit;
//   }
  
//   console.log(convertCtoF(30));

//   Reverse a String
//   Reverse the provided string and return the reversed string.
  
//   For example, "hello" should become "olleh".

// function reverseString(str) {
//     let newString = ""
//     for (let i = str.length - 1; i >= 0; i--) {
//         newString += str[i];
// }
//         return newString;

//   }
  
//   console.log(reverseString("hello"));

// Factorialize a Number
// Return the factorial of the provided integer.

// If the integer is represented with the letter n, a factorial is the product of all positive integers less than or equal to n.

// Factorials are often represented with the shorthand notation n!

// For example: 5! = 1 * 2 * 3 * 4 * 5 = 120

// Only integers greater than or equal to zero will be supplied to the function.

// function factorialize(num) {
//     let product = 1;
//     for (let i = 2; i <= num; i++) {
//       product *= i;
//     }
//     return product;
//   }
  
//   console.log(factorialize(4));

// Find the Longest Word in a String

// Return the length of the longest word in the provided sentence.

// Your response should be a number.

function findLongestWordLength(str) {
    let stringSpl = str.split(' ');
    let longest = 0;
    for (var i = 0; i < stringSpl.length; i++){
      if (stringSpl[i].length >= longest){
        longest = stringSpl[i].length;

      }
    }
  return longest;
}

console.log(findLongestWordLength("May the force be with you"));