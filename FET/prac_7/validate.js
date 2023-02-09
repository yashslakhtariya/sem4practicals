export function validateInfo(user, pswd, storeID)
{
     let users = ["haribol","yash","admin"];
     let pswds = ["harekrsna","sriradhe","haribol"];
     let i = 0;
     while(i < users.length)
     {
          if ((user == users[i]) && (pswd == pswds[i]) && (storeID == "YSL64"))
          {
               return true;
          }
          i++;
          if(i == users.length)
          {
               return false;
          }
     }
}