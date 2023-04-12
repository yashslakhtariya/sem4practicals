import { Injectable } from '@angular/core';
import { Emply } from './employee';


@Injectable({
  providedIn: 'root'
})
export class EmployeeService {

  empls: Emply[] = 
  [
    {
      id: 1,
      name: 'Yash',
      salary: 64321616,
      department: 'CEO',
      contact: 6351573711
    },
    {
      id: 2,
      name: 'Prarthi',
      salary: 50000,
      department: 'HR',
      contact: 9033304012
    },
    {
      id: 3,
      name: 'Dhruvi',
      salary: 30000,
      department: 'IT',
      contact: 7575877079
    },
    {
      id: 4,
      name: 'Steve',
      salary: 4000,
      department: 'Cleaning',
      contact: 1234567890
    },
    {
      id: 5,
      name: 'Jane',
      salary: 15000,
      department: 'IT',
      contact: 9876543210
    }
  ];

  getEmployees()
  {
    return this.empls;
  }
}
