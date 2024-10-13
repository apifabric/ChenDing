# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  October 13, 2024 20:07:17
# Database: sqlite:////tmp/tmp.jsgrMOmut7/ChenDing/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Category(SAFRSBaseX, Base):
    """
    description: Categories for products.
    """
    __tablename__ = 'categories'
    _s_collection_name = 'Category'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    ProductCategoryList : Mapped[List["ProductCategory"]] = relationship(back_populates="category")



class Customer(SAFRSBaseX, Base):
    """
    description: Stores customer information.
    """
    __tablename__ = 'customers'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone_number = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    AddressList : Mapped[List["Address"]] = relationship(back_populates="customer")
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")
    PaymentList : Mapped[List["Payment"]] = relationship(back_populates="customer")



class Employee(SAFRSBaseX, Base):
    """
    description: Employee details.
    """
    __tablename__ = 'employees'
    _s_collection_name = 'Employee'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hire_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)



class Product(SAFRSBaseX, Base):
    """
    description: Contains information about products.
    """
    __tablename__ = 'products'
    _s_collection_name = 'Product'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float)

    # parent relationships (access parent)

    # child relationships (access children)
    InventoryList : Mapped[List["Inventory"]] = relationship(back_populates="product")
    ProductCategoryList : Mapped[List["ProductCategory"]] = relationship(back_populates="product")
    OrderDetailList : Mapped[List["OrderDetail"]] = relationship(back_populates="product")



class Supplier(SAFRSBaseX, Base):
    """
    description: Details of suppliers.
    """
    __tablename__ = 'suppliers'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_name = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    InventoryList : Mapped[List["Inventory"]] = relationship(back_populates="supplier")



class Address(SAFRSBaseX, Base):
    """
    description: Stores customer addresses.
    """
    __tablename__ = 'addresses'
    _s_collection_name = 'Address'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'), nullable=False)
    address_line1 = Column(String, nullable=False)
    address_line2 = Column(String)
    city = Column(String, nullable=False)
    postal_code = Column(String)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("AddressList"))

    # child relationships (access children)



class Inventory(SAFRSBaseX, Base):
    """
    description: Stores product inventory information.
    """
    __tablename__ = 'inventory'
    _s_collection_name = 'Inventory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('products.id'), nullable=False)
    supplier_id = Column(ForeignKey('suppliers.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("InventoryList"))
    supplier : Mapped["Supplier"] = relationship(back_populates=("InventoryList"))

    # child relationships (access children)



class Order(SAFRSBaseX, Base):
    """
    description: Represents customer orders.
    """
    __tablename__ = 'orders'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    OrderDetailList : Mapped[List["OrderDetail"]] = relationship(back_populates="order")
    ShipmentList : Mapped[List["Shipment"]] = relationship(back_populates="order")



class Payment(SAFRSBaseX, Base):
    """
    description: Records customer payments.
    """
    __tablename__ = 'payments'
    _s_collection_name = 'Payment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'), nullable=False)
    amount = Column(Float, nullable=False)
    payment_date = Column(DateTime)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("PaymentList"))

    # child relationships (access children)



class ProductCategory(SAFRSBaseX, Base):
    """
    description: Links products to categories.
    """
    __tablename__ = 'product_categories'
    _s_collection_name = 'ProductCategory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('products.id'), nullable=False)
    category_id = Column(ForeignKey('categories.id'), nullable=False)

    # parent relationships (access parent)
    category : Mapped["Category"] = relationship(back_populates=("ProductCategoryList"))
    product : Mapped["Product"] = relationship(back_populates=("ProductCategoryList"))

    # child relationships (access children)



class OrderDetail(SAFRSBaseX, Base):
    """
    description: Stores details of each order.
    """
    __tablename__ = 'order_details'
    _s_collection_name = 'OrderDetail'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('orders.id'), nullable=False)
    product_id = Column(ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("OrderDetailList"))
    product : Mapped["Product"] = relationship(back_populates=("OrderDetailList"))

    # child relationships (access children)



class Shipment(SAFRSBaseX, Base):
    """
    description: Records shipments of orders.
    """
    __tablename__ = 'shipments'
    _s_collection_name = 'Shipment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('orders.id'), nullable=False)
    ship_date = Column(DateTime)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("ShipmentList"))

    # child relationships (access children)
