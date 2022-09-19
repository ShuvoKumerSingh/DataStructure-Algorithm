const ps = require("prompt-sync");
const prompt = ps();

function gcd(a , b)
{
    if(b==0) return a;
    else return gcd(b, a%b);
}

const output = ()=>{
    let num1;
    let num2;
    console.log("How to find Greatest Common Divisor between two numbers");
    while(true)
    {
        num1 = parseInt(prompt("Enter number1  : "));
        num2 = parseInt(prompt("Enter number2  : "));
        if(num1>=0 && num2>=0)
        {
            break;
        }
        console.log("The Number must be positive integer only");

    }
    return gcd(num1, num2);

}

console.log(output());
