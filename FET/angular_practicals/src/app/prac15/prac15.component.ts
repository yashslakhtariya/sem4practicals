import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';


@Component({
  selector: 'app-prac15',
  templateUrl: './prac15.component.html',
  styleUrls: ['./prac15.component.css']
})
export class Prac15Component implements OnInit{
  nmbrs = new Observable<number>((observer) => {
    console.log('Number streaming is started from 0 to 50!');
    let y: number = 0;
    // using the function timeout for demo without specifying timout milliseconds
    setTimeout(() => {
      while(y < 50)
      {
        observer.next(y);
        y++;
      }
      observer.complete();
    });
  });

  ngOnInit()
  {
    this.nmbrs.subscribe({
      next:  (n) => {
        if(n % 2 === 0)
        {
          console.log(n);
        }
      },
      error: (err) => {
        console.log(`Error : ${err}`);
      },
      complete: () => {
        console.log('Number streaming completed and even numbers are logged!');
      }
    })
  }  
}
