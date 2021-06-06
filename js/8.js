//The function takes any number of strings and returns the sum of their lengths.
//
//Example:
//
//console.log(sumOfLen('hello', 'hi')); //7
//console.log(sumOfLen('hi')); //2
//console.log(sumOfLen()); //0
//console.log(sumOfLen('hello', 'hi', 'my name', 'is')); //16

const sumOfLen = (...args) => {
    let sum = 0
   for (let item of args) {
       sum += item.length
   }
   return sum;

};
