import { HttpClient } from '@angular/common/http';
import { Component, OnInit, inject } from '@angular/core';

@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
  styleUrl: './test.component.scss',
})
export class TestComponent implements OnInit {
  http = inject(HttpClient);

  ngOnInit(): void {
    this.makeGetRequest();
  }

  makeGetRequest() {
    this.http.get('http://127.0.0.1:5000/add').subscribe(
      (response) => {
        console.log(response);
      },
      (error) => {
        console.error('Request failed with error', error);
      }
    );
  }
}
