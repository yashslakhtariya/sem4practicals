export function validateInfo(user, pswd, storeID)
{
     let users = ["haribol","yash","admin"];
     let pswds = ["harekrsna","sriradhe","haribol"];
     for(let i=0; i<users.length; i++)
     {
          if ((user == users[i]) && (pswd == pswds[i]) && (storeID == "YSL64"))
          {
               return true;
          }
          else
          {
               return false;
          }
     }
}