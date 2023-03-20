import { Component, DoCheck, EventEmitter, Input, OnChanges, OnInit, Output, SimpleChanges } from '@angular/core';

@Component({
  selector: 'app-child',
  templateUrl: './child.component.html',
  styleUrls: ['./child.component.css']
})
export class ChildComponent implements OnChanges, DoCheck, OnInit{
  @Input() amnt: number = 0;
  @Output() amntChange: EventEmitter<number> = new EventEmitter<number>;

  ngOnChanges(changes: SimpleChanges): void
  {
    console.log(`OnChanges in Child Component : ${changes}`);
  }

  ngDoCheck(): void {
      console.log(`DoCheck in Child Component`);
  }
  
  ngOnInit(): void {
      console.log(`OnInit in Child Component`);
  }

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
