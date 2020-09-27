  
    //math.sqrt - find the root square number and floor for for both a-1 and b
    //use a-1 to get a included example: a=1, b=2 countPerfectSquares = 1 - 0
    //substract both values to count the number of perfect squares between a and b

    
function squares(a, b) {

    let valB = Math.floor(Math.sqrt(b));
    let valA = Math.floor(Math.sqrt(a-1));
    let countPerfectSquares = valB - valA
    
    return countPerfectSquares
}