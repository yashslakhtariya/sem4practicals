function haribol()
{
     let h = prompt("Is Kayo's health well?");
     let cakes = 0;
     let health;
     if(h.includes("yes") || h.includes("ok"))
     {    
          health = true;
     }
     else if(h.includes("no") || h.includes("bad"))
     {
          health = false;
     }
     else
     {
          alert("Invalid Input!");
          haribol();
     }
     
     let prmse =  new Promise(function(resolve, reject)
     {
          if(health)
          {
               resolve(function()
               {
                    alert("Great! Your health is well! Nice to hear that!");
                    cakes = prompt("So how many cakes can you bake?");
                    while(!Number.isInteger(parseInt(cakes)))
                    {
                         cakes = prompt("Please enter valid number of cakes you can bake?");
                    } 
                    cakes = parseInt(cakes);
                    alert(`Thank you for baking ${cakes.toString} cakes for me Kayo!`);
               });
          }
          else
          {
               reject(alert("Sorry to hear that your health is unwell!\nGet well soon Kayo!"));
          }
     });
     prmse.finally(alert("Thanks for giving me party Kayo!"));
}