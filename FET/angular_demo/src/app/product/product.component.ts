import { Component, OnInit } from '@angular/core';
import { product } from '../product.model';
import { ProductService } from '../product.service';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css'],
  // providers: [ProductService] // to use this service in this component only 
})
export class ProductComponent implements OnInit{
  products: product[] = [];
  // ps = new ProductService();

  constructor(private ps: ProductService){  } // loosely coupled i.e. dynamically loaded whenever required

  ngOnInit(): void {
    this.products = this.ps.getProducts(); // tightly coupled i.e. later changes would have to be done everywhere
  }
}
