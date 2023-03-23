import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { Prac11Component } from './prac11/prac11.component';
import { Prac12Component } from './prac12/prac12.component';
import { Prac13Component } from './prac13/prac13.component';

@NgModule({
  declarations: [
    AppComponent,
    Prac11Component,
    Prac12Component,
    Prac13Component
  ],
  imports: [
    BrowserModule, FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
