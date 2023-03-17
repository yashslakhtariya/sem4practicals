import { Component } from '@angular/core';

@Component({
  selector: 'app-prac12',
  templateUrl: './prac12.component.html',
  styleUrls: ['./prac12.component.css']
})
export class Prac12Component {
  list: string[] = [];
  txt = "";
  create()
  {
    if(this.txt != "")
    {
      this.list.push(this.txt);
      this.txt = "";
    }
    else
    {
      alert("Empty Task not allowed");
    }
  }
  remove(item: string)
  {
    let indx = this.list.indexOf(item);
    if(indx >= 0)
    {
      this.list.splice(indx, 1);
    }
  }
}