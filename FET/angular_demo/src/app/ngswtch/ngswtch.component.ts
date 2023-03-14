import { Component } from '@angular/core';

@Component({
  selector: 'app-ngswtch',
  templateUrl: './ngswtch.component.html',
  styleUrls: ['./ngswtch.component.css']
})
export class NgswtchComponent {
  dhams: Dham[] = [{dham: 'Vrindavan'}, {dham: 'Mayapur'}, {dham: 'Puri'}, {dham: 'Dwarka'}, {dham: 'Haridwar'}];
  n = 0;
}
class Dham
{
  dham: string = '';
}
