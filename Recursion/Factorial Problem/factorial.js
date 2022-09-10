function Factorial(n){
    if (n==0||n==1){
        return 1;
    }
    else{
        return n*Factorial(n-1);
    }
}

const result = Factorial(4);
console.log(result);