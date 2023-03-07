import { Component } from '@angular/core';

@Component({
  selector: 'app-child2',
  templateUrl: './child2.component.html',
  styleUrls: ['./child2.component.css']
})
export class Child2Component {
  dhams: Dham[] = [{dham: 'Vrindavan'}, {dham: 'Mayapur'}, {dham: 'Puri'}, {dham: 'Dwarka'}, {dham: 'Haridwar'}]
}
class Dham
{
  dham: string = '';
}