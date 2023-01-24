function prfctornot(n)
{
    sum = 1;
 
    for (let i=2; i*i<=n; i++)
    {
        if (n%i==0)
        {
            if(i*i!=n)
                sum = sum + i + n/i;
            else
                sum=sum+i;
        }
    }

    if (sum == n && n != 1)
        return true;
 
    return false;
}

nmbr = prompt("Enter a number to find perfect numbers greater than it : ");
while(!Number.isInteger(parseInt(nmbr)))
{
     alert("Invalid Input!");
     nmbr = prompt("Enter a valid number : ");     
}
nmbr = parseInt(nmbr);

let i = nmbr+1;
while(i > nmbr)
{
     if(prfctornot(i))
     {
          alert(`The perfect number greater than ${nmbr} is ${i}`);
          break;
     }
     i++;
}