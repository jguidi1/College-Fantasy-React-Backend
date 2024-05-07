from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from models import User, Player, Team, League, College, Location, Stat, Schedule, UserScore, db
from pydantic import BaseModel
import jwt
import hashlib


class UserSignIn(BaseModel):
    email: str
    password: str

app = FastAPI()

SECRET_KEY = "COLLEGE_FANTASY"
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "Hello World"}

def hash_password(password: str):
    input_bytes = password.encode('utf-8')
    sha256_hash = hashlib.sha256(input_bytes).hexdigest()
    return sha256_hash

def decode_token(token: str):
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])   
    return decoded_token

@app.post("/sign-in")
def verify_user(userSignIn: UserSignIn, response: Response):
    

    user = db.query(User).filter(User.email == userSignIn.email, User.password_hash == hash_password(userSignIn.password)).first()
    if not user:
        response.status_code = 404
        return {"message": "User not found", "code": 404}
    
    user.password = None
    

    token = jwt.encode({
        "firstName": user.firstName,
        "lastName": user.lastName,
        "email": user.email,
        "tid": user.tid
        }, SECRET_KEY, algorithm='HS256')
    
    return {"message": "Login successful", "code": 200, "token": token}

@app.get("/verify")
def verify_token(token: str, response: Response):
    if not token or len(token) <= 0:
        response.status_code = 400
        return {"message": "Please input a token", "code": 400}
    
    print("TOKEN", token)
    try:
        decoded = decode_token(token)
        return {"message": "", "code": 200, "user_data": decoded}
       
    except jwt.ExpiredSignatureError:
        response.status_code = 400
        return {"message": "Token expired", "code": 400}
        
    except jwt.InvalidTokenError:
        response.status_code = 400
        return {"message": "Invalid token", "code": 400}
    
    

@app.post("/sign-up")
def sign_up_user():
    return "asdasddasd"


@app.get("/test")
async def add():
    
    location = Location(
        name = "Times Square",
        city = "New York City",
        state = "New York",
        zip = 000,
        lat = 0.0,
        long = 0.0)   
    
    
    db.add(location)
    db.commit()
    
    print(vars(location))
    
    all_locations = db.query(Location).all()
    
    print(all_locations)
    

@app.get("/populate_db")
async def populate_db():
    user1 = User(firstName="John", lastName="Doe", email="john@example.com")
    user1.set_password("password123")

    user2 = User(firstName="Jane", lastName="Doe", email="jane@example.com")
    user2.set_password("password456")

    db.session.add_all([user1, user2])
    db.session.commit()

    # Teams
    team1 = Team(name="Team A")
    team2 = Team(name="Team B")

    db.session.add_all([team1, team2])
    db.session.commit()

    # Leagues
    league1 = League(name="League 1")
    league2 = League(name="League 2")

    db.session.add_all([league1, league2])
    db.session.commit()

    # Players
    player1 = Player(firstName="Player1", lastName="Last1", avgScore=80)
    player2 = Player(firstName="Player2", lastName="Last2", avgScore=75)

    db.session.add_all([player1, player2])
    db.session.commit()

    # Colleges
    college1 = College(name="College A", location="Location A")
    college2 = College(name="College B", location="Location B")

    db.session.add_all([college1, college2])
    db.session.commit()

    # Locations
    location1 = Location(name="Location X", city="City X", state="State X", zip=12345, lat=42.123, long=-76.456)
    location2 = Location(name="Location Y", city="City Y", state="State Y", zip=54321, lat=43.987, long=-75.321)

    db.session.add_all([location1, location2])
    db.session.commit()

    # Stats
    stat1 = Stat(pid=1, score=85, week=1)
    stat2 = Stat(pid=2, score=78, week=1)

    db.session.add_all([stat1, stat2])
    db.session.commit()

    # User Scores
    user_score1 = UserScore(uid=1, pid=1, wid=1, score=90)
    user_score2 = UserScore(uid=2, pid=2, wid=1, score=85)

    db.session.add_all([user_score1, user_score2])
    db.session.commit()

    # Schedule
    schedule1 = Schedule(lid=1, htid=1, atid=2, hscore=3, ascore=2, wid=1, htw=True)
    schedule2 = Schedule(lid=2, htid=2, atid=1, hscore=2, ascore=1, wid=1, htw=False)

    db.session.add_all([schedule1, schedule2])
    db.session.commit()

    print("Database populated successfully")
    
    return {"message": "Database populated successfully"}





