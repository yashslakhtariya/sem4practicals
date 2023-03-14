import { Component } from '@angular/core';

@Component({
  selector: 'app-prac11',
  templateUrl: './prac11.component.html',
  styleUrls: ['./prac11.component.css']
})
export class Prac11Component {
  frst = 0;
  scnd = 1;
  add(f:number, s:number) 
  {
    alert(f + s);
  };
  diff(f:number, s:number) 
  {
    alert(f - s);
  };
  mul(f:number, s:number) 
  {
    alert(f * s);
  };
  dvd(f:number, s:number) 
  {
    alert(f / s);
  };
}
