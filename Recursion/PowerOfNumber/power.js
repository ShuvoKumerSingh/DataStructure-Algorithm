const ps = require("prompt-sync");
const prompt = ps();

function power(base,exp)
{
    if(exp==0)
    {
        return 1;
    }
    if(exp == 1)
    {
        return base;
    }
    else
    {
        return base * power(base, exp-1);
    }
}

const result = ()=>{
    let base;
    let exp;
    while(true)
    {
        base = parseInt(prompt("Enter base  : "));
        exp = parseInt(prompt("Enter exponent  : "));
        if(base>=0 && exp>=0)
        {
            break;
        }
        console.log("The base & exponent must be positive integer number");

    }
    return power(base,exp);

}

console.log(result());