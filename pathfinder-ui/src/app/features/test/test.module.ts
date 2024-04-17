import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TestComponent } from './test.component';
import { TestRoutingModule } from './test.routes';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [TestComponent],
  imports: [CommonModule, TestRoutingModule, HttpClientModule],
})
export class TestModule {}
