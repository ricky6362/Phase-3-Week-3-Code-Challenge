from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.customer import Customer

# Rest of your code


# Initialize your SQLAlchemy engine and session
engine = create_engine('postgresql://postgres:password@localhost:5432/restaurant_db')
Session = sessionmaker(bind=engine)
session = Session()


first_customer = session.query(Customer).first()
favorite_restaurant = first_customer.favorite_restaurant()
