import { Component } from '@angular/core';
import { Emply } from '../employee';
import { EmployeeService } from '../employee.service';

@Component({
  selector: 'app-prac16',
  templateUrl: './prac16.component.html',
  styleUrls: ['./prac16.component.css']
})
export class Prac16Component {
 employees: Emply[] = [];

 constructor(private es: EmployeeService) {  }

 getdetails()
 {
    this.employees = this.es.getEmployees();
 }
}
