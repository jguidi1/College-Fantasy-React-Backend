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


Session = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
db  = Session()

# import hashlib

# input_string = "Hello, World!"
# input_bytes = input_string.encode('utf-8')
# sha256_hash = hashlib.sha256(input_bytes).hexdigest()
# print("SHA-256 Hash:", sha256_hash)

import csv
from models import User

with open("user_data.csv", "r") as f:
    
    c = csv.reader(f)
    next(c)
    
    for a in c:
        user = User(
            id=int(a[0]),
            firstName=a[1],
            lastName=a[2],
            email=a[3],
            password_hash=a[4]
        )
        db.add(user)
        db.commit()
        print(a)





