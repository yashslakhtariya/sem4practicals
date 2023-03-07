import { Component } from '@angular/core';

@Component({
  selector: 'app-parent',
  templateUrl: './parent.component.html',
  styleUrls: ['./parent.component.css']
})
export class ParentComponent {
  pAmnt: number = 0;

  addamnt()
  {
    this.pAmnt +=6432;
  }
}
