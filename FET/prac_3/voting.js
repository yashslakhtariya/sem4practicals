alert("Welcome to YSL Voting Portal!");

init = confirm("Please enter your details to proceed!");

if(init)
{
     let name = prompt("Enter your name : ");
     let age = prompt("Enter your age : ");
     details = confirm(`Details Entered :\n\tName : ${name}\n\tAge : ${age}\n\nShould we further proceed?`);
     if(details)
     {
          age = parseInt(age);
          while(age < 0)
          {
               alert("Invalid age entered!");
               age = parseInt(prompt("Please enter your valid age : "));
          }
          if(age >= 18)
          {
               alert("You are eligible to vote!")
          }
          else
          {
               alert("Sorry, you are not eligible to vote!")
          }
     }
     else
     {
          alert("Okay! You don't want to proceed further");
     }
}

else
{
     alert("Okay fine! You don't want to proceed!");
}