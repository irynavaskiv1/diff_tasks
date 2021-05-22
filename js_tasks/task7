//Find the maximum interval between two consecutive numbers.
//Numbers are entered as arguments
//
//Example:
//
//maxInterv(3, 5, 2, 7); //5
//maxInterv(3, 5, 2, 7, 11, 0, -2); //11
//maxInterv(3, 5); //2
//maxInterv(3); //0

const maxInterv = (...args) => {
    let i = 0;
    let j = 1;
    let arr = [];
    if (args.length < 1) {
        return 0
    }
    else {
        while(j < args.length - 1) {
        arr.push(Math.abs(args[i] - args[j]));
        j++;
        i++;
    }
}
    return Math.max.apply(null, arr);

};
