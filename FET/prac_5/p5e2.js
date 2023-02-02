
let slryperday = 6400;

function emp(name, wdpm)
{
     return {
          name: name,
          wdpm: wdpm
     };
};

function getslry(wdpm)
{
     return slryperday * wdpm;
};

let emp1 = emp("Yash",22);
let emp2 = emp("Yash2",19);
let emp3 = emp("Yash3",16);
let emp4 = emp("Yash4",15);
let emp5 = emp("Yash5",10);

function show(empl)
{
     alert(`Employee Name : ${empl.name}\nEmployee Salary : ${getslry(empl.wdpm)}`);
};

show(emp1);
show(emp2);
show(emp3);
show(emp4);
show(emp5);
