import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-child',
  templateUrl: './child.component.html',
  styleUrls: ['./child.component.css']
})
export class ChildComponent {
  @Input() amnt: number = 0;
  @Output() amntChange: EventEmitter<number> = new EventEmitter<number>;

  withdraw()
  {
    if (this.amnt <= 0 || (this.amnt - 6400) <= 0)
    {
      alert("Insufficient balance!");
    }
    else
    {
      this.amnt -= 6400;
      this.amntChange.emit(this.amnt);
    }
  }
}
