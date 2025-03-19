#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game, Base  # Import Base to create tables

fake = Faker()

if __name__ == '__main__':
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    Base.metadata.create_all(engine)  # Create the database and tables if they don't exist
    session.query(Game).delete()  # Clear existing records
    session.commit()
    print("Seeding games...")
    
    games = [
        Game(
            title=fake.name(),
            genre=fake.word(),
            platform=fake.word(),
            price=random.randint(0, 60)
        )
        for i in range(50)
    ]
    
    session.bulk_save_objects(games)
    session.commit()
    
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()
