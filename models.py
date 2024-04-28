from fastapi import FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker, selectinload
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy import create_engine, MetaData

app = FastAPI()

SQLALCHEMY_DATABASE_URL = 'sqlite:///college_fastasy_data.db'


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

Base = declarative_base()

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
db  = Session()

# IMPLEMENT LOGIN, PASSWORD_HASHING
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String(64))
    lastName = Column(String(64))
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(64))
    tid = Column(Integer, ForeignKey('team.id'), index=True)

    def __repr__(self):
        return f'<User> {self.firstName}'

    def set_password(self, password):
        self.password_hash = password

class Team(Base):
    __tablename__ = 'team'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64))
    Lid = Column(Integer, ForeignKey('league.id'), index=True)
    league = relationship("League", back_populates="teams")
    
class PlayToTeam(Base):
    __tablename__ = 'player_to_team'
    id = Column(Integer, primary_key=True, index=True)
    tid = Column(Integer, ForeignKey('team.id'))
    pid = Column(Integer, ForeignKey('player.id'))
    
class Player(Base):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String(64))
    lastName = Column(String(64))
    avg_score = Column(Integer, index=True)

class League(Base):
    __tablename__ = 'league'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64))
    Tid = Column(Integer, ForeignKey('player.id'), index=True)

    teams = relationship("Team", back_populates="league")


class College(Base):
    __tablename__ = 'college'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64))
    location = Column(Integer, ForeignKey('location.id'), index=True)


class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64))
    city = Column(String(64))
    state = Column(String(64))
    zip = Column(Integer)
    lat = Column(Float)
    long = Column(Float)

    def __repr__(self):
        return f'<Location> {self.name}'


class Stat(Base):
    __tablename__ = 'stat'

    id = Column(Integer, primary_key=True, index=True)
    pid = Column(Integer, ForeignKey('player.id'), index=True)
    score = Column(Integer)
    week = Column(Integer)

class UserScore(Base):
    __tablename__ = 'user_score'

    id = Column(Integer, primary_key=True, index=True)
    uid = Column(Integer, ForeignKey('user.id'), index=True)
    pid = Column(Integer, ForeignKey('player.id'), index=True)
    wid = Column(Integer, ForeignKey('stat.week'), index=True)
    score = Column(Integer)


class Schedule(Base):
    __tablename__ = 'schedule'

    id = Column(Integer, primary_key=True, index=True)
    lid = Column(Integer, ForeignKey('league.id'), index=True)
    htid = Column(Integer, ForeignKey('team.id'), index=True)
    atid = Column(Integer, ForeignKey('team.id'), index=True)
    home_score = Column(Integer)
    ascore = Column(Integer)
    wid = Column(Integer, ForeignKey('stat.week'), index=True)
    htw = Column(Boolean)

Base.metadata.create_all(engine)
# Dummy data initialization
async def create_dummy_data():

        user = User(firstName="John", lastName="Doe", email="john@example.com")
        user.set_password("password")
        db.add(user)

        team = Team(name="Team A")
        db.add(team)

        league = League(name="League 1")
        db.add(league)

        player = Player(firstName="Player1", lastName="Last1", avg_score=80)
        db.add(player)

        location = Location(name="Location X", city="City X", state="State X", zip=12345, lat=42.123, long=-76.456)
        db.add(location)
        db.commit()
        return "Dummy data created"


@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application"}


# @app.on_event("startup")
# async def startup_event():
#     await create_dummy_data()
