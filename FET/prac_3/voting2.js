function vrfyage()
{
     let nm = document.getElementById("nm").value;
     let age = document.getElementById("age").value;
     let age2 = document.getElementById("age2").value;
     if(age != age2)
     {
          alert("Age inputs don't match!");
     }
     else
     {
          if(age<0)
          {
               alert("Invalid age!");
          }
          else if(age >= 18)
          {
               alert("You are eligible to vote!");
          }
          else if(age < 18)
          {
               alert("Sorry! You are not eligible to vote!");
          }
          else
          {
               alert("Invalid input!");
          }
     }
}