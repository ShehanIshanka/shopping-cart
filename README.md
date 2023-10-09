# Shopping Cart

- [Overview](#Overview)<br/>
- [Running App with Docker](#Running-App-with-Docker)<br/>
- [Setting up App locally](#Setting-up-App-locally)<br/>
- [Notes](#Notes)<br/>


## Overview

This is a sample Restful API for Shopping Cart developed with Flask related to [labela_backend_assignment](https://github.com/LabelA/labela_backend_assignment).
Following user stories are covered with the app.

* As a company, I want all my products in a database, so I can offer them via our new platform to customers
* As a client, I want to add a product to my shopping cart, so I can order it at a later stage
* As a client, I want to remove a product from my shopping cart, so I can tailor the order to what I actually need
* As a client, I want to order the current contents in my shopping cart, so I can receive the products I need to repair my car
* As a client, I want to select a delivery date and time, so I will be there to receive the order
* As a client, I want to see an overview of all the products, so I can choose which product I want
* As a client, I want to view the details of a product, so I can see if the product satisfies my needs

The app has two services; Product & Cart. 
Product service can create and retrieve products. Cart service can create a cart, add or remove items to cart and checkout.

Example notebook is available [here](./resources/example.ipynb).
Postman collection is available [here](./resources/postman_collection.json).

## Running App with Docker

#### 1. Build the image

```shell
docker compose build
```

#### 2. Run the services

```shell
docker compose up
```
Point your browser to [http://localhost:5000/swagger](http://localhost:5000/swagger) to access swagger UI.


## Setting up App locally

#### 1. System Requirements

```shell
python 3.10
```

#### 2. Install Requirements

```shell
make setup
```

#### 3. Set Environments variables

Environment variables needed to run the app
```shell
export DB_URL=<db-url>
```
DB URL should be in following format. Refer [this](https://docs.sqlalchemy.org/en/20/core/engines.html#postgresql)

```
postgresql+psycopg2://<username>:<password>@<host>:<port>/<database>
```

#### 4. Run App
```shell
make run
```

#### 5. Access App

Point your browser to [http://localhost:5000/swagger](http://localhost:5000/swagger) to access swagger UI.


## Notes

* The API has been developed mostly for happy path flow. The probable improvements
  * Enable Pagination
  * Better Error handling
  * Covering edge cases
    * Handle adding duplicate products
    * Handle product quantity in cart
    * Handle adding same product to cart
    * Handle removing non exist item from cart etc.
  * Better service segregation such as product, cart, order, shipping, inventory.