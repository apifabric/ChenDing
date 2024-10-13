import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {PRODUCTCATEGORY_MODULE_DECLARATIONS, ProductCategoryRoutingModule} from  './ProductCategory-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    ProductCategoryRoutingModule
  ],
  declarations: PRODUCTCATEGORY_MODULE_DECLARATIONS,
  exports: PRODUCTCATEGORY_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class ProductCategoryModule { }