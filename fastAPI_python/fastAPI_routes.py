from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home():
    return {"message": "Welcome to the FastAPI application"}

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
    stat1 = stat(pid=1, score=85, week=1)
    stat2 = stat(pid=2, score=78, week=1)

    db.session.add_all([stat1, stat2])
    db.session.commit()

    # User Scores
    user_score1 = user_score(uid=1, pid=1, wid=1, score=90)
    user_score2 = user_score(uid=2, pid=2, wid=1, score=85)

    db.session.add_all([user_score1, user_score2])
    db.session.commit()

    # Schedule
    schedule1 = schedule(lid=1, htid=1, atid=2, hscore=3, ascore=2, wid=1, htw=True)
    schedule2 = schedule(lid=2, htid=2, atid=1, hscore=2, ascore=1, wid=1, htw=False)

    db.session.add_all([schedule1, schedule2])
    db.session.commit()

    print("Database populated successfully")
    
    return {"message": "Database populated successfully"}

@app.exception_handler(404)
async def not_found_error(request, exc):
    return templates.TemplateResponse("404.html", {"request": request}, status_code=404)

@app.exception_handler(500)
async def internal_server_error(request, exc):
    return templates.TemplateResponse("500.html", {"request": request}, status_code=500)
