import { Component, OnInit } from '@angular/core';
import { activities } from '../activity';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import {API_URL} from '../env';

@Component({
  selector: 'app-activities-list',
  templateUrl: './activities-list.component.html',
  styleUrls: ['./activities-list.component.css']
})

export class ActivitiesListComponent implements OnInit {

  activities = activities;
  
  like() {
    window.alert("We like this activity too!");
  }
  
  constructor(private http: HttpClient) { }

  ngOnInit() {
    return this.http
    .get(`${API_URL}/`)
  }

}
