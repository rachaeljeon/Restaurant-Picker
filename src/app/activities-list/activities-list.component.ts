import { Component, OnInit } from '@angular/core';
import { activities } from '../activity';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import {API_URL} from '../env';

@Component({
  selector: 'app-activities-list',
  templateUrl: './activities-list.component.html',
  styleUrls: ['./activities-list.component.css']
})

export class ActivitiesListComponent {

  constructor(private http: HttpClient) { }
 
  more:boolean[]=[]
  activities = activities;
  businesses: any;

  showBusinesses() {
    // window.alert("We like this activity too!");
    return this.http.get(`${API_URL}/`)
    .subscribe(data => {
      console.log("YAYY, data------>>", data)
      this.businesses = data
    })
  }
}
