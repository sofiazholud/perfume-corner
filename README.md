# Perfume Corner

**Perfume Corner** is a web application designed for 
company employees where you can select your favorite perfume
from 3 categories such as fresh, morning, or evening scents. 
In the application, you can manage and add perfumes, 
manufacturers, and employees.
All perfumes are selected only from the top 5 best niche manufacturers
It is designed to be flexible and scalable, 
with a clean and intuitive UI based on Bootstrap.

## Features

- **Perfume Catalog**: Browse and search for perfumes by category: 
- Evening scents 
- Fresh flavors 
- Morning fragrances
- **Manufacturer Management**: Add, edit, and manage perfume manufacturers.
- **Employee Management**: Add new employees, track favorite perfumes.
- **User Authentication**: Secure login/logout functionality with 
- different levels of access (staff, superusers).
- **Custom Admin Dashboard**: Manage perfumes and manufacturers through 
- the Django admin interface.
- **Search Functionality**: Search perfumes, manufacturers and 
- employees using a custom search bar.
- **Responsive Design**: Mobile-friendly interface using Bootstrap 5.
- **Debugging Tools**: Integrated with Django Debug Toolbar 
- for enhanced development debugging.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sofiazholud/perfume-corner.git
# perfume-corner
Django project initialized.

# Usage
Visit http://127.0.0.1:8000/ to browse perfumes, manage manufacturers, 
and interact with the app.
Admin panel can be accessed at http://127.0.0.1:8000/admin/ for managing the data.

# Technologies Used
Django: Backend framework for building scalable applications.
Bootstrap 5: Frontend framework for building responsive layouts.
SQLite: Default database for development.
Crispy Forms: For better form rendering with Bootstrap.
Django Debug Toolbar: For debugging during development.