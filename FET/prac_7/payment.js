export function prcsPymnt(blnc, price)
{
     if(blnc < price)
     {
          alert("Insufficient balance! This window will be closed");
          close();
     }
     else
     {
          alert(`Previous Balance : Rs.${blnc}\nPayment processed : Rs.${price}\nPresent Balance : Rs.${blnc - price}`);
     }
}