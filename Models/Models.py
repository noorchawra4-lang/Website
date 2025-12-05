# Models/models.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float, func
from sqlalchemy.orm import relationship
from Database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    otp = Column(String, nullable=True)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    orders = relationship("Order", back_populates="customer")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)

    orders = relationship("Order", back_populates="category")


class Manufacture(Base):
    __tablename__ = "manufactures"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    address = Column(String, nullable=True)
    contact = Column(String, nullable=True)

    orders = relationship("Order", back_populates="manufacture")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    manufacture_id = Column(Integer, ForeignKey("manufactures.id"), nullable=False)

    quantity = Column(Integer, nullable=False)
    price_per_unit = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)
    status = Column(String, default="PENDING")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    customer = relationship("User", back_populates="orders")
    category = relationship("Category", back_populates="orders")
    manufacture = relationship("Manufacture", back_populates="orders")
