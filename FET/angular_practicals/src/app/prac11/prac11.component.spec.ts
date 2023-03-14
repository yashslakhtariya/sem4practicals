import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Prac11Component } from './prac11.component';

describe('Prac11Component', () => {
  let component: Prac11Component;
  let fixture: ComponentFixture<Prac11Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ Prac11Component ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Prac11Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
