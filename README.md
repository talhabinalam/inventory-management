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
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
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
