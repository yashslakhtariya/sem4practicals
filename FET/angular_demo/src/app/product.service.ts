import { Injectable } from '@angular/core';
import { product } from './product.model';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  getProducts(): product[]
  {
    return [
      {id:1, pname:'Laptop'},
      {id:2, pname:'Mobile'},
      {id:3, pname:'Tablet'},
      {id:4, pname:'Desktop'}
    ];
  }
}
