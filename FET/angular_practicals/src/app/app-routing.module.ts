import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";
import { Prac11Component } from "./prac11/prac11.component";
import { Prac12Component } from "./prac12/prac12.component";
import { Prac13Component } from "./prac13/prac13.component";


const routes: Routes = 
[
     { path: 'P11', component: Prac11Component },
     { path: 'P12', component: Prac12Component },
     { path: 'P13', component: Prac13Component }
]

@NgModule(
     {
          imports: [RouterModule.forRoot(routes)],
          exports: [RouterModule]
     }
)

export class AppRoutingModule
{

}