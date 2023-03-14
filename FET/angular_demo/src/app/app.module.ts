import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { ChildComponent } from './child/child.component';
import { ParentComponent } from './parent/parent.component';
import { Child2Component } from './child2/child2.component';
import { NgifComponent } from './ngif/ngif.component';
import { NgswtchComponent } from './ngswtch/ngswtch.component';
import { NgclsComponent } from './ngcls/ngcls.component';
import { NgstylComponent } from './ngstyl/ngstyl.component';

@NgModule({
  declarations: [
    AppComponent,
    ChildComponent,
    ParentComponent,
    Child2Component,
    NgifComponent,
    NgswtchComponent,
    NgclsComponent,
    NgstylComponent
  ],
  imports: [
    BrowserModule, FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
