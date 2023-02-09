export function calculateRating()
{
     let r = prompt("Enter rating for your experience with us in 1 to 5 stars");
     while(!Number.isInteger(parseInt(r)))
     {
          alert("Invalid Input!");
          r = prompt("Enter rating for your experience with us in 1 to 5 stars");
     }
     r = parseInt(r);
     while(r < 1 || r > 5)
     {
          alert("Invalid Input!");
          r = prompt("Enter rating for your experience with us in 1 to 5 stars");
     }
     alert(`Thank you for giving us ratings!\nRating given : ${r}/5`);
}