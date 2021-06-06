//The function filterByN receives an array of integers, a number and a parameter
//(greater, less). Print a new array, where all elements will be greater/less than this number
//
//By default, the number is 0, the parameter is greater.
//Example:
//filterNums([-1, 2, 4, 0, 55, -12, 3], 11, 'greater');  //[ 55]
//filterNums([-2, 2, 3, 0, 43, -13, 6], 6, 'less'); // [-2, 2, 3, 0, -13]
//filterNums([-2, 2, 3, 0, 43, -13, 6], -33, 'less'); //  []
//filterNums([-2, 2, 3, 0, 43, -13, 6]); // [2, 3, 43, 6]
//filterNums([-2, 2, 3, 0, 43, -13, 6], 23);  // [43]

function filterNums (array, num, condition) {

  var outputarray = [];
  for (let i = 0; i < array.length; i = i + 1) {

    if (num != undefined) {

      if (condition == undefined || condition == "greater") {
        if (array[i] > num) {
          outputarray.push(array[i]); // put the array number in to the output array
        }
      } else if (condition == "less") {
        if (array[i] < num) {
          outputarray.push(array[i]); // put the array number in to the output array
        }
      }
    } else {
      if (array[i] > 0) {
        outputarray.push(array[i]); // put the positive array number in to the output array
      }
    }
  }

  return outputarray;
}
