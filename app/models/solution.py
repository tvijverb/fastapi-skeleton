from typing import List, Optional

from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.model_utils import Base, TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "user"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    fullname = mapped_column(String, nullable=True)
    # addresses = relationship("Address", back_populates="user")


# class Address(Base):
#     __tablename__ = "address"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     email_address: Mapped[str]
#     user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
#     user: Mapped["User"] = relationship(back_populates="addresses")