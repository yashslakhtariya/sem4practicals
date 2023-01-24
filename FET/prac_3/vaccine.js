alert("Welcome to the YSL Vaccine Portal!");

let nm = prompt("Enter your name : ");
let cntry = prompt("What is your current nationality?");
let n = prompt("Enter number of vaccine doses you have taken : ");

cnfrm = confirm(`Details Entered : \nName : ${nm}\nNationality : ${cntry}\nNumber of Vaccine Doses : ${n.toString()}`);
n = parseInt(n);

while(n<0 || n>3)
{
     alert("Incorrect number of doses!");
     n = parseInt(prompt("Enter valid number of vaccine doses you have taken (0 to 3) : "));
}
if(n>0)
{
     alert("Welcome to the YSL Voting Portal!\nYou can proceed further!");
}
else
{
     alert("Sorry! You are not vaccinated atleast one time\nYou cannot proceed further");
     close();
}