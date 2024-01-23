from customer import Customer
from restaurant import Restaurant
from review import Review

def main():
    # Create customers
    customer1 = Customer("John", "Doe")
    customer2 = Customer("Alice", "Smith")
    customer3 = Customer("Dian", "Johnson")
    customer4 = Customer("mercy", "Williams")
    customer5 = Customer("Ian", "Brownex")

    # Create restaurants
    restaurant1 = Restaurant("Tasty Treats")
    restaurant2 = Restaurant("Burger Palace")

    # Create reviews
    review1 = Review(customer1, restaurant1, 4)
    review2 = Review(customer2, restaurant2, 5)

    # Additional reviews
    review3 = Review(customer1, restaurant2, 3)
    review4 = Review(customer2, restaurant1, 4)

    # Reviews for new customers
    review5 = Review(customer3, restaurant1, 2)
    review6 = Review(customer4, restaurant2, 5)
    review7 = Review(customer5, restaurant1, 3)

    # Display results
    print(customer1.full_name())
    print(restaurant2.average_star_rating())
    print(customer2.num_reviews())

    # Display results for additional customers
    print(customer3.full_name())
    print(restaurant1.average_star_rating())
    print(customer4.num_reviews())

    print(customer5.full_name())
    print(restaurant1.average_star_rating())
    print(customer5.num_reviews())

if __name__ == '__main__':
    main()
