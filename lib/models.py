from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    freebies = relationship('Freebie', backref='company')
    devs =relationship('Dev',secondary='freebies',backref='companies')

    def __repr__(self):
        return f'<Company {self.name}>'

    def give_freebie(self,dev,item_name,value):
        new_freebie = Freebie(
            item_name=item_name,
            value=value,
            dev=dev,
            company=self
        )
        return new_freebie
    @classmethod
    def oldest_company(cls):
        return sesseion.query(cls).order_by(cls.founding_year).first()
        
class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    def __repr__(self):
        return f'<Dev {self.name}>'



