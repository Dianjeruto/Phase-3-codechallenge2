# restaurant.py

class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def get_name(self):
        return self.name

    def get_reviews(self):
        return self.reviews

    def get_customers(self):
        return list({review.customer for review in self.reviews})

    @classmethod
    def all(cls):
        return cls.all_restaurants

    def average_star_rating(self):
        total_ratings = sum(review.rating for review in self.reviews)
        num_reviews = len(self.reviews)
        if num_reviews > 0:
            return round(total_ratings / num_reviews)
        else:
            return 0
