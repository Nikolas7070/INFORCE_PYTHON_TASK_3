# Internal Lunch Service

This is an internal lunch service for employees to help them make a decision about where to have lunch.

## Functionality

- Authentication
- Creating restaurants
- Uploading menus for restaurants (menu for each day)
- Creating employees
- Getting the current day's menu
- Voting for menu items

## Tech Stack

- Django + Django Rest Framework
- PostgreSQL
- Docker (docker-compose)
- PyTest
- JWT for authentication

## How to Run

1. Install Docker and Docker Compose.
2. Clone this repository.
3. Navigate to the project directory.
4. Run `docker-compose up` to start the service.
5. Access the API endpoints to interact with the system.

## API Endpoints

- `/api/add_user/` (POST): Add a user.
- `/api/remove_user/<int:user_id>/` (DELETE): Remove a user.
- `/api/add_restaurant/` (POST): Add a restaurant.
- `/api/remove_restaurant/<int:restaurant_id>/` (DELETE): Remove a restaurant.
- `/api/add_menu_item/` (POST): Add a menu item.
- `/api/get_menu/<int:restaurant_id>/` (GET): Get the menu for a restaurant.
- `/api/add_employee/` (POST): Add an employee.
- `/api/add_vote/` (POST): Add a vote for a menu item.

## Contributors

- [Your Name]
