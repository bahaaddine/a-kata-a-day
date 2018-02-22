/*
You have k apple boxes full of apples. Each square box of size m contains m × m apples. You just noticed two interesting properties about the boxes:

The smallest box is size 1, the next one is size 2,..., all the way up to size k.
Boxes that have an odd size contain only yellow apples. Boxes that have an even size contain only red apples.
Your task is to calculate the difference between the number of red apples and the number of yellow apples.

Example

For k = 5, the output should be
appleBoxes(k) = -15.

There are 1 + 3 * 3 + 5 * 5 = 35 yellow apples and 2 * 2 + 4 * 4 = 20 red apples, making the answer 20 - 35 = -15.
*/

function appleBoxes(k) {
    let redApple = 0;
    let yellowApple = 0;
    
    for(let n=1; n<= k; n++){
        if(n%2) yellowApple += n*n;
        else redApple += n*n;
    }
    return redApple - yellowApple;
}

