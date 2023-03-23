import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Prac13Component } from './prac13.component';

describe('Prac13Component', () => {
  let component: Prac13Component;
  let fixture: ComponentFixture<Prac13Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ Prac13Component ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Prac13Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
