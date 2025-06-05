#!/usr/bin/env python3

# Script goes here!
from models import Company, Dev, Freebie, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.query(Freebie).delete()
session.query(Company).delete()
session.query(Dev).delete()
session.commit()

company1 = Company(name="safaricom", founding_year=1997)
company2 = Company(name="tangazolety",founding_year=2004)


dev1= Dev(name="john")
dev2 =Dev(name="elliot")

freebie1 = Freebie(item_name="Tshirt", value=3,dev=dev1,company=company1)
freebie2 = Freebie(item_name="water bottle", value=4,dev=dev2,company=company2)

