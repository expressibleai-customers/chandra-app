from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, CheckConstraint
from sqlalchemy.sql import func
from ..database import Base


class UserManagement(Base):
    __tablename__ = "user_managements"


    id = Column(
        Integer,

        primary_key=True,


        nullable=False,




    )

    role = Column(
        Text,


        nullable=False,




    )

    created_at = Column(
        DateTime,


        nullable=False,



        server_default=CURRENT_TIMESTAMP,


    )

    updated_at = Column(
        DateTime,


        nullable=False,



        server_default=CURRENT_TIMESTAMP,


        onupdate=func.now(),

    )
