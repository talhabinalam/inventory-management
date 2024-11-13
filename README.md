# Inventory Management System

This Inventory Management System is a web application built with Django for managing products, orders, and staff. The system provides a comprehensive interface for administrators to manage the inventory, track orders, and oversee staff members. It demonstrates CRUD operations, user authentication, and role-based access control.

## Features

### User Authentication and Roles
* **Admin Access**: Admin users have permissions to manage products, view orders, and access staff details.
* **Regular User Access**: Regular users can log in and view the product inventory but cannot perform modifications.

### Product Management (Admin Only)
* **Add Product**: Admins can add new products, specifying details like name, description, and price.
* **Edit Product**: Admins can update existing product information.
* **Delete Product**: Admins can remove products from the inventory.

### Order Management
* **View Orders**: Admins can view all orders placed in the system.
* **Add Order**: Orders can be created, with the current logged-in user recorded as the staff member responsible.

### Staff Management
* **View Staff List**: Admins can see all registered staff members and their details.
* **View Staff Details**: Individual staff details can be viewed by selecting a specific staff member.

## Installation

### Prerequisites
* **Python 3.8+**: Ensure Python is installed on your machine. You can download it from [python.org](https://www.python.org).

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/talhabinalam/inventory-management.git
   ```
   Navigate to the project directory:
   ```bash
   cd inventory-management
   ```
2. Set Up a Virtual Environment Create a virtual environment to isolate dependencies.
   ```bash
   python -m venv env
   source venv/bin/activate   # On macOS/Linux
   env\Scripts\activate      # On Windows
   ```
3. Install Dependencies Install all required dependencies from requirements.txt
   ```bash  
   pip install -r requirements.txt
   ```
4. Apply Migrations Set up the database by applying migrations (For new database).
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create an admin user to access the management features.
   ```bash  
   python manage.py createsuperuser
   ```
6. Run the Development Server Start the Django development server.
   ```bash  
   python manage.py runserver
   ```

## Project Structure
* **views.py**: Defines views for handling CRUD operations, authentication, and staff, product, and order management.
* **models.py**: Contains models for Product, Order, and User, capturing the essential fields for each entity.
* **templates/**: HTML templates for the dashboard, product, order, and user interfaces.
* **urls.py**: URL routes for the application, linking views to accessible endpoints.

## Usage

### Admin Access
Admins have full access to:
* **Manage Products**: Add, edit, or delete product entries.
* **Track Orders**: View all orders and record new orders.
* **Oversee Staff**: View staff lists and individual details.

### User Access
Regular users can:
* **View Products**: Access the list of available products.
* **View Orders**: Check the list of orders but without editing rights.

## Requirements

The `requirements.txt` file contains all necessary Python packages. Major dependencies include:
* **Django**: Framework for building the application.
* **Bootstrap**: Integrated for styling and responsive design in templates.

## Overview
![Screenshot 2024-11-13 183018](https://github.com/user-attachments/assets/f529f882-f3bd-404f-aa82-4b12a6da153d)


