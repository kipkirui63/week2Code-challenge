# week2Code-challenge

## Restaurant Review System
This is a simple Python program that models a restaurant review system. It consists of three main classes: Customer, Review, and Restaurant.

## Table of Contents
Introduction
Getting Started
Classes
Customer
Review
Restaurant
Usage
Contributing
License
Introduction
The Restaurant Review System is designed to simulate the process of customers reviewing restaurants. It includes the following classes:


Customer: Represents a customer who can leave reviews for restaurants.
Review: Represents a review given by a customer for a specific restaurant.
Restaurant: Represents a restaurant and manages its reviews and customers.
Getting Started
To run the Restaurant Review System, make sure you have Python 3.x installed on your system. No external libraries are required. Follow these steps:

Clone this repository to your local machine.
Navigate to the project directory.
Classes
Customer
The Customer class represents a customer. It has attributes for given name and family name, and a method to generate the full name. Customers can leave reviews for restaurants.

## Properties
given_name: The given name of the customer.
family_name: The family name of the customer.
full_name: The full name of the customer.

## Methods
set_given_name(given_name): Sets the given name of the customer.
get_given_name(): Gets the given name of the customer.
set_family_name(family_name): Sets the family name of the customer.
get_family_name(): Gets the family name of the customer.
set_full_name(): Generates the full name of the customer.
get_full_name(): Gets the full name of the customer.
all(): Returns a list of all customer instances.
Review
The Review class represents a review given by a customer for a specific restaurant. It includes the customer, restaurant, and rating.

## Properties
rating: The rating given in the review.
Methods
set_rating(rating): Sets the rating of the review.
get_rating(): Gets the rating of the review.
all(): Returns a list of all reviews.
Restaurant
The Restaurant class represents a restaurant. It includes attributes for the restaurant name, reviews, and customers who have reviewed the restaurant.

### Properties
name: The name of the restaurant.
reviews: A list of reviews for the restaurant.
Methods
set_name(name): Sets the name of the restaurant.
add_review(customer, rating): Adds a review to the restaurant.
customers(): Returns a list of customers who have reviewed the restaurant.
Usage
Create instances of Customer using the Customer class constructor.
Create instances of Restaurant using the Restaurant class constructor.
Use the add_review() method of the Restaurant class to add reviews to a restaurant.
Access customer and review information using the defined methods and properties.
Example code can be found in the provided Python file.

### Contributing
Contributions are welcome! If you find any issues or improvements, feel free to create a pull request.

You can reach me on : Email: enocksang8356@@gmail.com Mattermost: @kipkirui Enock Linkedin: @enock-sang License This project is licensed under the MIT License.

Copyright (c) [2023] [Kipkirui Enock]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.