from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, CheckConstraint
from sqlalchemy.sql import func
from ..database import Base


class CareProviderPortal(Base):
    __tablename__ = "care_provider_portals"


    id = Column(
        Integer,

        primary_key=True,


        nullable=False,




    )

    caregivers = Column(
        Text,





    )

    care_receivers = Column(
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
