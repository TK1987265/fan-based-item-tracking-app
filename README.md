## Fan-Based Item Tracking Application


## Description
This project is a full-stack application built using Flask for the backend and React for the frontend. The application allows users to track items across various locations, submit and manage the items and their status (obtained or not obtained) at each location.

## user story
As a user
I can:
View all locations and items in the inventory system.
Add new items to specific locations in the inventory.
Edit details of existing items in the inventory.
Delete items from the inventory.
Mark items as obtained or not obtained.
So that I can:
Efficiently manage and track inventory items across different locations.
Ensure inventory data is accurate and up-to-date.
Quickly identify and rectify discrepancies in inventory.


## Acceptance Criteria:
View Locations and Items:

Given: I am on the Locations or Items page.
When: I access the page.
Then: I can see a list of all locations or items in the system.
Add New Location Item:

Given: I am on the Location Items page.
When: I select a location and an item, set the obtained status, and submit the form.
Then: The new location item is added to the list and stored in the system.
Edit Location Item:

Given: I am on the Location Items page and there are existing location items.
When: I click the edit button next to a location item, update the details, and submit the form.
Then: The updated location item is saved in the system and the changes are reflected in the list.

## Delete Location Item:

Given: I am on the Location Items page and there are existing location items.
When: I click the delete button next to a location item and confirm the deletion.
Then: The location item is removed from the list and deleted from the system.
Toggle Obtained Status:

Given: I am on the Location Items page and there are existing location items.
When: I view the obtained status of an item.
Then: I can see whether the item is marked as obtained or not obtained.

## Mockup:
Home Page:

Navigation bar with links to Home, Locations, Items, and Location Items.
Locations Page:

List of all locations with the ability to add new locations.
Items Page:

List of all items with the ability to add new items.
Location Items Page:

List of all location items.
Form to add a new location item.
Buttons to edit or delete existing location items.

## Directory Structure
client/
src/: Contains all the React components and other frontend code.
public/: Contains the public assets of the React app, including index.html.
package.json: Manages the frontend dependencies.
server/
app.py: Initializes the Flask application, sets up the database, and defines the

## API endpoints.
config.py: Contains the configuration settings for the Flask application.
models.py: Defines the SQLAlchemy models for Location, Item, and LocationItem.
seed.py: Seeds the database with initial data.
requirements.txt: Lists the dependencies for the Flask application.


## Installation and Setup

## Clone the repository:

sh
Copy code
git clone https://github.com/TK1987265/fan-based-item-tracking-app
cd fan-based-item-tracking-app

## Setup the backend:

sh
Copy code
cd server
pipenv install
pipenv shell
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python seed.py
python app.py

## Setup the frontend:

sh
Copy code
cd client
npm install
npm start

## Access the application:

The Flask API will run on http://localhost:5000
The React frontend will run on http://localhost:3000

## API Routes
Locations
GET /locations: Retrieve all locations.
POST /locations: Create a new location.
Items
GET /items: Retrieve all items.
POST /items: Create a new item.
LocationItems
GET /location_items: Retrieve all location items.
POST /location_items: Create a new location item.
PUT /location_items/<id>: Update a location item.
DELETE /location_items/<id>: Delete a location item.

## Models
Location
id: Integer, primary key
name: String, nullable=False
items: Relationship with LocationItem
Item
id: Integer, primary key
name: String, nullable=False
locations: Relationship with LocationItem
LocationItem
id: Integer, primary key
location_id: Foreign key to Location
item_id: Foreign key to Item
obtained: Boolean, default=False

## Seed Data
The seed.py file contains initial data for Location, Item, and LocationItem models. Running python seed.py will populate the database with this data.

