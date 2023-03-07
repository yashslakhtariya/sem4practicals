function validate()
{
     let nme = document.forms['yslfrm']['name'].value;
     let eml = document.forms['yslfrm']['email'].value;
     let mbl = document.forms['yslfrm']['mobile'].value;
     let pswd = document.forms['yslfrm']['pswd'].value;
     let pswd2 = document.forms['yslfrm']['pswd2'].value;
     letter=/^[A-Z][a-z]+$/;
     mail=/^\w+([.-]?\w+)@\w+([.-]?\w+)(\.\w{2,3})$/;
     nmbr=/^\d{10}$/;
     passwrd=/^[A-Za-z]+([.#@%]?\w+)$/;
     if(letter.test(nme))
     {
          if(mail.test(eml))
          {
               if(nmbr.test(mbl))
               {
                    if(passwrd.test(pswd) && passwrd.test(pswd2))
                    {
                         if(pswd == pswd2)
                         {
                              alert("Login Successful!")
                         }
                         else
                         {
                              alert("Passwords don't match!")
                         }
                    }
                    else
                    {
                         alert("Password validation unsuccessful!")
                    }
               }
               else
               {
                    alert("Invalid contact number!")
               }
          }
          else
          {
               alert("Email validation unsuccessful!")
          }
     }
     else
     {
          alert("Invalid name!")
     }
}