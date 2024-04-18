import datetime
from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, SelectMultipleField, SelectField, \
     RadioField, TimeField, IntegerField
from wtforms.validators import DataRequired, NumberRange, length
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.python.models import User, Team, League, Player, College, Location,stat, user_score, schedule

# Need to add a remember me check box
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    firstName = StringField('First name', validators=[DataRequired()])
    lastName = StringField('Last name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create Account')

    # def validate_username(self, username):
    #     user = User.query.filter_by(username=username.data).first()
    #     if user is not None:
    #         raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
        
class JoinLeague(FlaskForm):
    joinCode = StringField('Join Code', validators=[DataRequired()])
    teamName = StringField('Create Team Name', validators=[DataRequired()])
    submit = SubmitField('Sign In')

    def validate_teamName(self, teamName):
        user = User.query.filter_by(teamName=teamName.data).first()
        if user is not None:
            raise ValidationError('Please use a different team name.')
        
class createLeague(FlaskForm):
    leagueName = StringField('League Name', validators=[DataRequired()])
    leagueSize = RadioField('League Size', choices=[(0, '2'), (1, '4'), (2, '6'), (3, '8'), (4, '10')], validators=[DataRequired()])
    draftDate = DateField('Draft Date', format='%Y-%m-%d')
    time = StringField('Time', validators=[DataRequired()])
    teamName = StringField('Create Team Name', validators=[DataRequired()])
    submit = SubmitField('Search')

# class HomeSearch(FlaskForm):
#     zipcode = StringField('Zipcode', validators=[DataRequired()])
#     date = DateField('Date', format='%Y-%m-%d')
#     time = StringField('Time', validators=[DataRequired()])
#     price = RadioField('Price', choices=[(0, 'Free'), (1, '$$$')], validators=[DataRequired()])
#     submit = SubmitField('Search')

#     def validate_zipcode(self, zipcode):
#         if len(zipcode) != 5:
#             raise ValidationError("Please enter a 5 digit zipcode.")


# class FullSearch(FlaskForm):
#     zipcode = StringField('Zipcode', validators=[DataRequired(), Length(5,5,"Please enter a 5 digit zipcode")])
#     date = DateField('Date', format='%Y-%m-%d')
#     startTime = TimeField('Start', validators=[DataRequired()])
#     endTime = TimeField('End', validators=[DataRequired()])
#     price = RadioField('Paid or free space?', validators=[DataRequired()])
#     tech = SelectMultipleField('Technology', coerce=int, choices=[])
#     groupSize = IntegerField('Group Size', [NumberRange(min=1, max=100)])
#     submit = SubmitField('Search')

#     def validate_startTime(self, field):
#         if field.data > self.endTime.data:
#             raise ValidationError("Meeting can't start after it has ended")

#     def validate_endTime(self, field):
#         if field.data == self.startTime.data:
#             raise ValidationError("Meeting start and end time are equal")


# class Booking(FlaskForm):
#     space = StringField()
#     date = DateField('Date', format='%Y-%m-%d')
#     startTime = TimeField('Start', validators=[DataRequired()])
#     endTime = TimeField('End', validators=[DataRequired()])
#     groupSize = IntegerField('Group Size', [NumberRange(min=1, max=100)])
#     submit = SubmitField('Book')

#     def validate_startTime(self, field):
#         if field.data > self.endTime.data:
#             raise ValidationError("Meeting can't start after it has ended")

#     def validate_endTime(self, field):
#         if field.data == self.startTime.data:
#             raise ValidationError("Meeting start and end time are equal")

#     def validate_groupSize(self, field):
#         space = Space.query.filter_by(name=self.space.data).first()
#         if space.sizeCap < field.data:
#             raise ValidationError("Your group size is too large for this space")

#     def validate_date(self, field):
#         if self.date.data < date.today():
#             raise ValidationError("Pick a current or future time!")
#         else:
#             space = Space.query.filter_by(name=self.space.data).first()
#             upcoming = upcomingMeeting.query.filter(upcomingMeeting.spid == space.id,
#                                                     upcomingMeeting.date == field.data,
#                                                     upcomingMeeting.startTime < self.endTime.data).all()
#             if len(upcoming) != 0:
#                 raise ValidationError("Scheduling conflict with date and/or time")

# class ReviewForm(FlaskForm):
#     score = IntegerField("Score:", validators=[DataRequired(), NumberRange(min=1, max=5)])
#     desc = StringField("What were your thoughts on the space?", validators=[length(max=200)] )
#     submit = SubmitField("Leave Review")



