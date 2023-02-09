import { validateInfo } from "./validate.js";
import { prcsPymnt } from "./payment.js";
import { calculateRating } from "./rating.js";

function createAc()
{
     let user = prompt("Enter your username : ");
     let pswd = prompt("Enter your password : ");
     let strID = prompt("Enter the Store ID : ");
     let cnfrm = validateInfo(user, pswd, strID);
     if(cnfrm)
     {
          alert("Details are valid! You can proceed further!");
     }
     else if(!cnfrm)
     {
          alert("Sorry, details entered are invalid! You cannot proceed further!");
          let y = confirm("Do you want to reenter the details?");
          if(y)
          {
               createAc();
          }
          else
          {
               close();
          }
     }
     let blnc = prompt("Enter your balance : ");
     while(!Number.isInteger(parseInt(blnc)))
     {
          alert("Invalid Balance!");
          blnc = prompt("Enter your balance : ");
     }
     blnc = parseInt(blnc);

     let price = prompt("Enter the total amount to pay : ");
     while(!Number.isInteger(parseInt(price)))
     {
          alert("Invalid Balance!");
          price = prompt("Enter the total amount to pay : "); 
     }
     price = parseInt(price);

     prcsPymnt(blnc, price);
     calculateRating();
}

window.createAc = createAc;