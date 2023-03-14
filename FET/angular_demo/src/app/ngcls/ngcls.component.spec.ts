import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NgclsComponent } from './ngcls.component';

describe('NgclsComponent', () => {
  let component: NgclsComponent;
  let fixture: ComponentFixture<NgclsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NgclsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NgclsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
