function fabonacci(n){
        if(n==0||n==1)
        {
            return n;
        }
        else
        {
            return fabonacci(n-1) + fabonacci(n-2);
        }
}
const ps = require("prompt-sync");
const prompt = ps();
let user;
while(true)
{
    user = parseInt(prompt("Enter Number: "));
    if(user>=0)
    {
        break;
    }
    console.log("Number can not be zero");

}
const result = fabonacci(user);
console.log(result);
