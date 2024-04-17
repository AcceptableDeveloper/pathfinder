import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: '',
    loadChildren: () =>
      import('./features/test/test.module').then((m) => m.TestModule),
  },
];
