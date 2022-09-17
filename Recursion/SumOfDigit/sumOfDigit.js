//Main Method
function sumOfDigits(num){
        if(num==0)
        {
            return num;
        }
        else
        {
            return (num%10) + sumOfDigits(num/10);
        }
}


const ps = require("prompt-sync");
const prompt = ps();

//User Input
//Console Method
const user = ()=>{
    let user;
    while(true)
    {
        user = parseInt(prompt("Enter Number: "));
        if(user>=0)
        {
            break;
        }
        console.log("The number has to be a positive integer only");

    }
    return user;

}

const inp = user();

const result = Math.floor(sumOfDigits(inp));
console.log(result);