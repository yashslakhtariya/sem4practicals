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
}