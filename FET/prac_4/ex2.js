nmbr = prompt("Enter a number between 1 and 5 : ");
while((!Number.isInteger(parseInt(nmbr))) || nmbr<1 || nmbr>5)
{
     alert("Invalid Input!");
     nmbr = prompt("Enter a valid number between 1 and 5 : ");     
}

rndm = rndmint(1,5);

if(nmbr == rndm)
{
     alert("Good Work!\nYes, the number is " + rndm);
}
else
{
     alert("Not matched!\nThe number is " + rndm);
}

function rndmint(min, max) 
{
     return Math.floor(Math.random() * (max+1 - min) ) + min;
}