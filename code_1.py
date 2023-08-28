class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)
    
    def get_given_name(self):
        return self.given_name
    
    def get_family_name(self):
        return self.family_name
    
    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    
    def restaurants(self):
        return [review.restaurant.get_name() for review in self.reviews]
    
    @classmethod
    def all(cls):
        return cls.all_customers


class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.restaurant_name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)
    
    def get_name(self):
        return self.restaurant_name
    
    def get_reviews(self):
        return self.reviews
    
    def customers(self):
        return [review.customer.full_name() for review in self.reviews]
    
    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_ratings = sum(review.get_rating() for review in self.reviews)
        return total_ratings / len(self.reviews)
    
    @classmethod
    def all(cls):
        return cls.all_restaurants


class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating_value = rating
        customer.reviews.append(self)
        restaurant.reviews.append(self)
        Review.all_reviews.append(self)
    
    def get_rating(self):
        return self.rating_value
    
    def get_customer(self):
        return self.customer
    
    def get_restaurant(self):
        return self.restaurant
    
    @classmethod
    def all(cls):
        return cls.all_reviews


# Testing the code
if __name__ == "__main__":

    # Create customers
    customer1 = Customer("Faith", "Chepkoech")
    customer2 = Customer("Jurgen", "Klop")

    # Create restaurants
    restaurant1 = Restaurant("Restaurant A")
    restaurant2 = Restaurant("Restaurant B")

    # Create reviews
    review1 = Review(customer1, restaurant1, 4)
    review2 = Review(customer2, restaurant1, 5)
    review3 = Review(customer1, restaurant2, 3)

    # Testing methods
    print(customer1.full_name())  # Output: John Doe
    print(restaurant1.get_name())  # Output: Restaurant A
    print(review1.get_rating())    # Output: 4
    print(customer1.restaurants()) # Output: ['Restaurant A', 'Restaurant B']
    print(restaurant1.customers()) # Output: ['John Doe', 'Jane Smith']
    print(restaurant1.average_star_rating())  # Output: 4.0  # Note: Changed output to match the given reviews
