export interface Activity {
    id: number;
    name: string;
    priority: number;
    description: string;
  }
  
  export const activities = [
    {
      id: 1,
      name: 'Meditate',
      priority: 1,
      description: 'Stay in tune with myself'
    },
    {
      id: 2,
      name: 'Mindfulness',
      priority: 2,
      description: 'Be aware of my thoughts and make sure my actions align with what I am passionate about'
    },
    {
      id: 3,
      name: 'Journaling',
      priority: 3,
      description: 'A platform where I can pour out and take mental note of the lessons I have accumulated in my 22 years of living!'
    }
  ];
  
  
  /*
  Copyright Google LLC. All Rights Reserved.
  Use of this source code is governed by an MIT-style license that
  can be found in the LICENSE file at https://angular.io/license
  */