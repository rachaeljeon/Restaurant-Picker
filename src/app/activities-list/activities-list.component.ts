import { Component, OnInit } from '@angular/core';
import { activities } from '../activity';

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
  
  constructor() { }

  ngOnInit(): void {
  }

}
