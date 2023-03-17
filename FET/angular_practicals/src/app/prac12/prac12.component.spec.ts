import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Prac12Component } from './prac12.component';

describe('Prac12Component', () => {
  let component: Prac12Component;
  let fixture: ComponentFixture<Prac12Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ Prac12Component ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Prac12Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
