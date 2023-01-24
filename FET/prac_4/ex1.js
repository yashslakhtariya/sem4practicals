nmbr = prompt("Enter any number : ");
while(!Number.isInteger(parseInt(nmbr)))
{
     alert("Invalid Input!");
     nmbr = prompt("Enter a valid number : ");     
}

alert(absdiff(nmbr));

function absdiff(n)
{
     n = parseInt(n);
     return 2*Math.abs(n-13);
}