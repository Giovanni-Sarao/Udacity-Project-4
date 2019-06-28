# -*- coding: utf-8 -*-

import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Category, Base, Item, User

TEMP_PATH = '/tmp/sqlalchemy-media'
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

user1 = User(
    name='Giovanni Sarao Araki',
    email='giovanni.saraoaraki@gmail.com',
    picture='/img/creator.png')
session.add(user1)
session.commit()

category1 = Category(name="RTS Games")
session.add(category1)
session.commit()

category2 = Category(name="RPG Games")
session.add(category2)
session.commit()

category3 = Category(name="Race Games")
session.add(category3)
session.commit()

item1 = Item(
    user_id=1,
    name="Age of Empires III",
    description="""Age of Empires III. Age of Empires III is a real-time 
	strategy video game developed by Microsoft Corporation's Ensemble Studios
	and published by Microsoft Game Studios. The Mac version was ported over 
	and developed and published by Destineer's MacSoft.""",
    category=category1,
    picture='https://ibb.co/zF5Td81',
    )
session.add(item1)
session.commit()

item2 = Item(
    user_id=1,
    name="Age of Mythology",
    description=""" Age of Mythology is a mythology-based, real-time strategy 
	computer game developed by Ensemble Studios, and published by Microsoft 
	Game Studios.""",
    category=category1,
    picture='https://ibb.co/D90cWCF'
    )
session.add(item2)
session.commit()



item3 = Item(
    user_id=1,
    name="The Witcher 3: Wild Hunt",
    description="""Unparalleled novel-like story spanning over 150 hours of gameplay.
	With over 100 hours of core and side-quest gameplay and over 50 hours of 
	additional content, The Witcher 3: Wild Hunt combines the intense, plot-driven 
	pull of traditional RPGs with the freedom of choice only open world games can 
	offer.""",
    category=category2,
    picture='https://ibb.co/KmJ8yZ9'
    )
session.add(item3)
session.commit()

item4 = Item(
    user_id=1,
    name="Forza Horizon 4",
    description="""Forza Horizon 4 is an open world racing video game developed
	by Playground Games and published by Microsoft Studios.""",
    category=category3,
    picture='https://ibb.co/FHbc3ZV'
    )
session.add(item4)
session.commit()



