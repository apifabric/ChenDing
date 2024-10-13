import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProductCategoryHomeComponent } from './home/ProductCategory-home.component';
import { ProductCategoryNewComponent } from './new/ProductCategory-new.component';
import { ProductCategoryDetailComponent } from './detail/ProductCategory-detail.component';

const routes: Routes = [
  {path: '', component: ProductCategoryHomeComponent},
  { path: 'new', component: ProductCategoryNewComponent },
  { path: ':id', component: ProductCategoryDetailComponent,
    data: {
      oPermission: {
        permissionId: 'ProductCategory-detail-permissions'
      }
    }
  }
];

export const PRODUCTCATEGORY_MODULE_DECLARATIONS = [
    ProductCategoryHomeComponent,
    ProductCategoryNewComponent,
    ProductCategoryDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProductCategoryRoutingModule { }