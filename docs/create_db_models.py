import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Define base class for declarative models
Base = declarative_base()

# Define models
class Customer(Base):
    """description: Stores customer information."""
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone_number = Column(String)

class Product(Base):
    """description: Contains information about products."""
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float)

class Order(Base):
    """description: Represents customer orders."""
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime, default=datetime.datetime.now)

class OrderDetail(Base):
    """description: Stores details of each order."""
    __tablename__ = 'order_details'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

class Address(Base):
    """description: Stores customer addresses."""
    __tablename__ = 'addresses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    address_line1 = Column(String, nullable=False)
    address_line2 = Column(String)
    city = Column(String, nullable=False)
    postal_code = Column(String)

class Supplier(Base):
    """description: Details of suppliers."""
    __tablename__ = 'suppliers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    contact_name = Column(String)

class Inventory(Base):
    """description: Stores product inventory information."""
    __tablename__ = 'inventory'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

class Payment(Base):
    """description: Records customer payments."""
    __tablename__ = 'payments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    amount = Column(Float, nullable=False)
    payment_date = Column(DateTime, default=datetime.datetime.now)

class Category(Base):
    """description: Categories for products."""
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class ProductCategory(Base):
    """description: Links products to categories."""
    __tablename__ = 'product_categories'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

class Employee(Base):
    """description: Employee details."""
    __tablename__ = 'employees'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    hire_date = Column(DateTime, default=datetime.datetime.now)

class Shipment(Base):
    """description: Records shipments of orders."""
    __tablename__ = 'shipments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    ship_date = Column(DateTime)

# Create the database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

# Establishing session
Session = sessionmaker(bind=engine)
session = Session()

# Insert sample data
customers = [
    Customer(name="John Doe", email="john.doe@example.com", phone_number="123456789"),
    Customer(name="Jane Smith", email="jane.smith@example.com", phone_number="987654321")
]

products = [
    Product(name="Widget", description="A useful widget", price=19.99),
    Product(name="Gadget", description="An awesome gadget", price=29.99)
]

orders = [
    Order(customer_id=1, order_date=datetime.datetime(2023, 1, 1)),
    Order(customer_id=2, order_date=datetime.datetime(2023, 2, 1))
]

order_details = [
    OrderDetail(order_id=1, product_id=1, quantity=5),
    OrderDetail(order_id=2, product_id=2, quantity=3)
]

addresses = [
    Address(customer_id=1, address_line1="123 Elm St", city="Somewhere", postal_code="12345"),
    Address(customer_id=2, address_line1="456 Maple Ave", city="Anywhere", postal_code="67890")
]

suppliers = [
    Supplier(name="ABC Supplies", contact_name="Alice"),
    Supplier(name="XYZ Wholesale", contact_name="Bob")
]

inventory = [
    Inventory(product_id=1, supplier_id=1, quantity=100),
    Inventory(product_id=2, supplier_id=2, quantity=200)
]

payments = [
    Payment(customer_id=1, amount=99.95, payment_date=datetime.datetime(2023, 1, 15)),
    Payment(customer_id=2, amount=89.97, payment_date=datetime.datetime(2023, 2, 16))
]

categories = [
    Category(name="Technology"),
    Category(name="Household")
]

product_categories = [
    ProductCategory(product_id=1, category_id=1),
    ProductCategory(product_id=2, category_id=2)
]

employees = [
    Employee(name="Manager Mike", hire_date=datetime.datetime(2022, 1, 1)),
    Employee(name="Worker Wanda", hire_date=datetime.datetime(2022, 2, 1))
]

shipments = [
    Shipment(order_id=1, ship_date=datetime.datetime(2023, 1, 10)),
    Shipment(order_id=2, ship_date=datetime.datetime(2023, 2, 10))
]

# Add data to the session
session.add_all(customers)
session.add_all(products)
session.add_all(orders)
session.add_all(order_details)
session.add_all(addresses)
session.add_all(suppliers)
session.add_all(inventory)
session.add_all(payments)
session.add_all(categories)
session.add_all(product_categories)
session.add_all(employees)
session.add_all(shipments)

# Commit the session
session.commit()

# Close the session
session.close()
