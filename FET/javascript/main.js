import {greet} from "/greet.js"
import {getName} from "/getname.js"
import {checkAge} from "/checkage.js"
greet();
var name = getName();
var age = checkAge();
alert('Your Name: ' + name + '\nYour Age: ' + age)