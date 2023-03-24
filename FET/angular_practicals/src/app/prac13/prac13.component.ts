import { Component } from '@angular/core';

@Component({
  selector: 'app-prac13',
  templateUrl: './prac13.component.html',
  styleUrls: ['./prac13.component.css']
})
export class Prac13Component
{
  genre!: number;

  comedy: cmdy[] = [{mv: '3 Idiots (Genre: Comedy, Year: 2009)'}, {mv: 'Free Guy (Genre: Comedy, Year: 2021)'}, {mv: 'Dolittle (Genre: Comedy, Year: 2020)'}, {mv: 'Zero (Genre: Comedy, Year: 2018)'}, {mv: 'Entertainment (Genre: Comedy, Year: 2014)'}];
  action: act[] = [{mv: 'Free Guy (Genre: Action, Year: 2021)'}, {mv: 'RRR (Genre: Action, Year: 2022)'}, {mv: 'Vikram (Genre: Action, Year: 2022)'}, {mv: 'Don2 (Genre: Action, Year: 2011)'}, {mv: 'Baby (Genre: Action, Year: 2015)'}];
  thriller: thrl[] = [{mv: 'M3GAN (Genre: Thriller, Year: 2022)'}, {mv: 'Fall (Genre: Thriller, Year: 2022)'}, {mv: 'Predestination (Genre: Thriller, Year: 2014)'}, {mv: 'Lucy (Genre: Thriller, Year: 2014)'}, {mv: 'Bell Bottom (Genre: Thriller, Year: 2021)'}]
  horror: hrr[] = [{mv: 'Smile (Genre: Horror, Year: 2022)'}, {mv: 'The Witch (Genre: Horror, Year: 2015)'}, {mv: 'M3GAN (Genre: Horror, Year: 2022)'}, {mv: 'Orphan (Genre: Horror, Year: 2009)'}, {mv: 'Roohi (Genre: Horror, Year: 2021)'}]
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