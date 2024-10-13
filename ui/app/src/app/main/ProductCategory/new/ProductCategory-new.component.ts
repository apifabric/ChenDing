import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'ProductCategory-new',
  templateUrl: './ProductCategory-new.component.html',
  styleUrls: ['./ProductCategory-new.component.scss']
})
export class ProductCategoryNewComponent {
  @ViewChild("ProductCategoryForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}