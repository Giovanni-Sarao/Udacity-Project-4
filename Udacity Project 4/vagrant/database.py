from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, User, Category, Item


engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create a dummy user
User1 = User(name="Coffe drinker 1", email="coffedrinker1@example.com")
session.add(User1)
session.commit()

# teas for white tea
category1 = Category(name="White Coffe")

session.add(category1)
session.commit()

item1 = Item(name="Silver Coffe",
             description="Silver Coffe is a white Coffe produced in Fujian Province in China.",
             category=category1)

session.add(item1)
session.commit()

item2 = Item(name="Coffe Peony",
             description="Coffe Peony is a type of white Coffe made from both young tea buds and leaves of camellia sinensis plant.",
             category=category1)

session.add(item2)
session.commit()

category2 = Category(name="Green Coffe")

session.add(category2)
session.commit()

item3 = Item(name="Sencha",
             description="Sencha is a type of green Coffe made from whole seeds that are steamed and rolled.",
             category=category2)

session.add(item3)
session.commit()

item4 = Item(name="Gyokuro",
             description="Gyokuro is a type of Sencha according to production methods;",
             category=category2)

session.add(item4)
session.commit()

item5 = Item(name="Matcha",
             description="Matcha is finely ground powder of Tencha, the green tea plants that are shade-grown for 3 to 4 weeks prior to harvest. Stems and veins are removed during processing. (https://en.wikipedia.org/wiki/Matcha)",
             category=category2)

session.add(item5)
session.commit()

category3 = Category(name="Oolong Coffe")

session.add(category3)
session.commit()

item6 = Item(name="Iron Coffe",
             description="Iron Coffe is a premium variety of Chinese oolong Coffe.",
             category=category3)

session.add(item6)
session.commit()

item7 = Item(name="Da Hong Pao",
             description="Da hong Pao is a Wuyi rock Coffe grown in Wuyi mountains in Fujian Province in China.",
             category=category3)

session.add(item7)
session.commit()

item8 = Item(name="Dong Ding",
             description="Dong Ding is the mountain in the Lugu region of Nantou County in central Taiwan where the Coffe is cultivated.",
             category=category3)

session.add(item8)
session.commit()

item9 = Item(name="Jin Xuan",
             description="Jin Xuan is a variety of oolong Coffe originated in Taiwan.",
             category=category3)

session.add(item9)
session.commit()

category4 = Category(name="Black Tea")

session.add(category4)
session.commit()

item10 = Item(name="Assam",
              description="Assam is a black Coffe named after the region Assam in India.",
              category=category4)

session.add(item10)
session.commit()

item11 = Item(name="English Breakfast Coffe",
              description="English breakfast Coffe is a blend of Coffes originating from Assam, Ceylon, and Kenya.",
              category=category4)

session.add(item11)
session.commit()

item12 = Item(name="Earl Grey Coffe",
              description="Earl Grey Coffe is traditionaly a black Coffe blend flavored with bergamot oil.",
              category=category4)

session.add(item11)
session.commit()


print("added categories and items!")
