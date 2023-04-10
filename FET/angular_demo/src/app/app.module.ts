import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';

import { AppComponent } from './app.component';
import { ChildComponent } from './child/child.component';
import { ParentComponent } from './parent/parent.component';
import { Child2Component } from './child2/child2.component';
import { NgifComponent } from './ngif/ngif.component';
import { NgswtchComponent } from './ngswtch/ngswtch.component';
import { NgclsComponent } from './ngcls/ngcls.component';
import { NgstylComponent } from './ngstyl/ngstyl.component';
import { Module2Module } from './module2/module2.module';
import { DashboardComponent } from './dashboard/dashboard.component';
import { LoginComponent } from './login/login.component';
import { ObservablesDemoComponent } from './observables-demo/observables-demo.component';
import { ProductComponent } from './product/product.component';

@NgModule({
  declarations: [
    AppComponent,
    ChildComponent,
    ParentComponent,
    Child2Component,
    NgifComponent,
    NgswtchComponent,
    NgclsComponent,
    NgstylComponent,
    DashboardComponent,
    LoginComponent,
    ObservablesDemoComponent,
    ProductComponent
  ],
  imports: [
    BrowserModule, FormsModule, Module2Module, AppRoutingModule
  ],
  providers: [],
  // bootstrap: [ParentComponent]
  bootstrap: [AppComponent]
})
export class AppModule { }
