from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, CheckConstraint
from sqlalchemy.sql import func
from ..database import Base


class CommunityPlatform(Base):
    __tablename__ = "community_platforms"


    id = Column(
        Integer,

        primary_key=True,


        nullable=False,




    )

    community_management = Column(
        Text,





    )

    moderation_tools = Column(
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
