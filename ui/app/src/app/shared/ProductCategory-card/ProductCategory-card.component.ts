import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './ProductCategory-card.component.html',
  styleUrls: ['./ProductCategory-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.ProductCategory-card]': 'true'
  }
})

export class ProductCategoryCardComponent {


}