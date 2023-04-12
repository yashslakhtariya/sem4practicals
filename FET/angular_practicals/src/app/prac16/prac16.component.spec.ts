import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Prac16Component } from './prac16.component';

describe('Prac16Component', () => {
  let component: Prac16Component;
  let fixture: ComponentFixture<Prac16Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ Prac16Component ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Prac16Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
