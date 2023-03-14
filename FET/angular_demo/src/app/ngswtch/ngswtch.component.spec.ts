import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NgswtchComponent } from './ngswtch.component';

describe('NgswtchComponent', () => {
  let component: NgswtchComponent;
  let fixture: ComponentFixture<NgswtchComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NgswtchComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NgswtchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
