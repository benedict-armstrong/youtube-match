# coding: utf-8
from typing import Text
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class LoginSession(Base):
    __tablename__ = 'login_sessions'

    id = Column(Integer, primary_key=True, server_default=text("nextval('login_sessions_id_seq'::regclass)"))
    created_at = Column(DateTime(True), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    uuid = Column(UUID, server_default=text("uuid_generate_v4()"))

    users = relationship('User', cascade='all, delete')

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, server_default=text("nextval('users_id_seq'::regclass)"))
    name = Column(String(255))
    email = Column(String(255))
    credentials = Column(JSONB(astext_type=Text()))
    state = Column(String(255))
    login_session_id = Column(ForeignKey('login_sessions.id'))

    login_session = relationship('LoginSession', back_populates='users')
    subscriptions = relationship('Subscription', cascade='all, delete')


class Subscription(Base):
    __tablename__ = 'subscriptions'

    id = Column(Integer, primary_key=True, server_default=text("nextval('subscriptions_id_seq'::regclass)"))
    channel_name = Column(String(255))
    channel_id = Column(String(255))
    user_id = Column(ForeignKey('users.id'))
