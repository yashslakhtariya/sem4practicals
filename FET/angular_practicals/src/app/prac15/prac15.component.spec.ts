import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Prac15Component } from './prac15.component';

describe('Prac15Component', () => {
  let component: Prac15Component;
  let fixture: ComponentFixture<Prac15Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ Prac15Component ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Prac15Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
