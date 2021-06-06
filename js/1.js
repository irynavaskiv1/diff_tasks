// Implement the modifyArray(array) function, which takes an arbitrary array,
// changes the value of the first element of the array to “Start”,
// the last element of the array to “End” and returns the modified array.

// Function example:
// modifyArray([12, 6, 22, 0, -8])); // [‘Start’, 6, 22, 0, ‘End’]

function modifyArray(array) {
   array[0] = "Start"
   array.pop()
   array.push('End')
   return array
}
