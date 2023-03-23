import { Component } from '@angular/core';

@Component({
  selector: 'app-prac13',
  templateUrl: './prac13.component.html',
  styleUrls: ['./prac13.component.css']
})
export class Prac13Component
{
  genre!: number;

  comedy: cmdy[] = [{mv: 'comedy1'}, {mv: 'comedy2'}, {mv: 'comedy3'}, {mv: 'comedy4'}, {mv: 'comedy5'}];
  action: act[] = [{mv: 'action1'}, {mv: 'action2'}, {mv: 'action3'}, {mv: 'action4'}, {mv: 'action5'}];
  thriller: thrl[] = [{mv: 'thriller1'}, {mv: 'thriller2'}, {mv: 'thriller3'}, {mv: 'thriller4'}, {mv: 'thriller5'}]
  horror: hrr[] = [{mv: 'horror1'}, {mv: 'horror2'}, {mv: 'horror3'}, {mv: 'horror4'}, {mv: 'horror5'}]
}

class cmdy
{
  mv = '';
}

class act
{
  mv = '';
}

class thrl
{
  mv = '';
}

class hrr
{
  mv = '';
}