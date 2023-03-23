import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";
import { DashboardComponent } from "./dashboard/dashboard.component";
import { LoginComponent } from "./login/login.component";

const routes: Routes = 
[
     { path: 'login', component: LoginComponent },
     { path: 'dashboard', component: DashboardComponent },
     { path: 'home', redirectTo: 'login' }
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