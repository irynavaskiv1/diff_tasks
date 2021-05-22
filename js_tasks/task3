// Implement the longestLogin(loginList) function, which takes an array of user
// logins loginList  and returns the longest login. If the logins of the same
// length are the longest in the array, the login element with the largest
// index is returned. Tip: You can use the reduce() method to solve the task.

// Function examples:
// longestLogin(["serg22", "tester_2", "Prokopenko", "guest"]);   //  Prokopenko
// longestLogin(["user1", "user2", "333", "user4", "aa"]);   //  user4

function longestLogin(loginList) {
    const newArr=[];
    let temp =    Math.max(...(loginList.map(el => el.length)));
     loginList.forEach(item => {
        if(temp == item.length){
          newArr.push(item);
        }
    });
    return newArr.slice(-1)[0]
}
