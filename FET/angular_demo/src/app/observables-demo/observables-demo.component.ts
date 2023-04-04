import { Component, OnInit } from '@angular/core';
import { from, Observable, of } from 'rxjs';

@Component({
  selector: 'app-observables-demo',
  templateUrl: './observables-demo.component.html',
  styleUrls: ['./observables-demo.component.css']
})
export class ObservablesDemoComponent implements OnInit{
  obs1 = new Observable((observer) => {
    console.log('Observable has started streaming numbers!');
    setTimeout(() => {
      observer.next(Math.random() * 100)
    }, 300);
    if(Math.floor(Math.random() * 100) <= 50) 
    {
      observer.error('Custom Error!');
    }
    observer.next(Math.floor(Math.random() * 100));
    observer.next(Math.floor(Math.random() * 100));
    observer.next(Math.floor(Math.random() * 100));
    observer.next(Math.floor(Math.random() * 100));
    observer.next(Math.floor(Math.random() * 100));
    observer.next(Math.floor(Math.random() * 100));
    observer.complete();
  })

  ngOnInit(): void {
      this.obs1.subscribe({
        next: (num) => { console.log(num) },
        error: (err) => { console.log(`Error in streaming : ${err}`) },
        complete: () => { console.log('Number streaming ends here') }
      })
      const arr1 = [1,2,3,4,5,6,7];
      const arr2 = ['a','b','c','d','e','f','g'];
      // const obs2 = of(arr1, arr2);
      const obs2 = from(arr1);
      obs2.subscribe({
        next: (num) => { console.log(num) },
        error: (err) => { console.log(`Error in streaming : ${err}`) },
        complete: () => { console.log('Data Streaming ends here') }
      })
  }
}
