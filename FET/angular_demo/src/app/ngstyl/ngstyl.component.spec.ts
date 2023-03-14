import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NgstylComponent } from './ngstyl.component';

describe('NgstylComponent', () => {
  let component: NgstylComponent;
  let fixture: ComponentFixture<NgstylComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NgstylComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NgstylComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
