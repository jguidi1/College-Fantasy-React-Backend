from pydantic import BaseModel, EmailStr, constr
from typing import List, Tuple, Optional
from datetime import date
from fastapi import Form

class LoginForm(BaseModel):
    username: str = Form(..., description="Username")
    password: str = Form(..., description="Password")

class RegistrationForm(BaseModel):
    firstName: str = Form(..., description="First name")
    lastName: str = Form(..., description="Last name")
    email: EmailStr = Form(..., description="Email")
    password: str = Form(..., description="Password")
    password2: str = Form(..., description="Confirm Password")

class JoinLeague(BaseModel):
    joinCode: str = Form(..., description="Join Code")
    teamName: str = Form(..., description="Create Team Name")

class CreateLeague(BaseModel):
    leagueName: str = Form(..., description="League Name")
    leagueSize: int = Form(..., description="League Size")
    draftDate: date = Form(..., description="Draft Date")
    time: str = Form(..., description="Time")
    teamName: str = Form(..., description="Create Team Name")
