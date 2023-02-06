export function checkAge()
{
     var age = prompt('Enter Your Age:')
     confirm("Confirm, your age is " + age + "yrs.");
     if(age >= 18)
     {
     alert('You\'re eligible to vote!')
     }
     else
     {
     alert('Sorry, you\'re not old enough to vote.')
     }
     return age;
}