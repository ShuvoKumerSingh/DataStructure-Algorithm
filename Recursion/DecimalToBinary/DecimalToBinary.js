const ps = require("prompt-sync");
const prompt = ps();

function decimalToBinary(num)
{
    if(num==0)
    {
        return 0;
    }
    else
    {
        return num%2 + (decimalToBinary(parseInt(num/2))*10);
    }
}

console.log("How to convert a number from Decimal to Binary");
let num = parseInt(prompt("Enter Number: "));
let result = decimalToBinary(num);
console.log(result);