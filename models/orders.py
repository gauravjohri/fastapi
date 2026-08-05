from database.database import Base
from sqlalchemy import Column,Integer,String,Float

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer,primary_key=True,index=True)
    product_name = Column(String(100))
    customer_name = Column(String(100))
    quantity = Column(Integer)
    price = Column(Float)