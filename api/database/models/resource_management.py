from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, CheckConstraint
from sqlalchemy.sql import func
from ..database import Base


class ResourceManagement(Base):
    __tablename__ = "resource_managements"


    id = Column(
        Integer,

        primary_key=True,


        nullable=False,




    )

    filtering = Column(
        Text,





    )

    categorization = Column(
        Text,





    )

    content_management_capabilities = Column(
        Text,





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
