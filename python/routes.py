import datetime
from datetime import date, time, datetime
from flask import render_template, flash, redirect, url_for
from app import app, db
from app.python.models import User, Team, League, Player, College, Location, stat, user_score, schedule
from app.python.forms import LoginForm, RegistrationForm, JoinLeague, createLeague
from flask_login import current_user, login_user, logout_user, login_required
from apscheduler.schedulers.background import BackgroundScheduler

# def updateMeetings():
#     with app.app_context():
#         print('updating db')
#         upcoming = upcomingMeeting.query.all()
#         updated = []
#         changes = False
#         for meeting in upcoming:
#             if meeting.date <= datetime.today().date():
#                 if meeting.startTime < datetime.now().time():
#                     changes = True
#                     prev = meetingHistory(uid=meeting.uid,
#                                           spid=meeting.spid,
#                                           date=meeting.date,
#                                           startTime=meeting.startTime,
#                                           endTime=meeting.endTime,
#                                           review=False)
#                     db.session.delete(meeting)
#                     updated.append(prev)
#         if changes:
#             db.session.add_all(updated)
#             db.session.commit()
#             print("db changed")
#         else:
#             print("no changes")


# @app.route('/')
# @app.route('/home')
# def home():
#     sched = BackgroundScheduler(daemon=True)
#     sched.add_job(updateMeetings, 'interval', minutes=1)
#     sched.start()
#     return render_template('home.html', title="Home")


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('home'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user is None or not user.check_password(form.password.data):
#             flash('Invalid username or password')
#             return redirect(url_for('login'))
#         login_user(user)
#         return redirect(url_for('home'))
#     return render_template('login.html', title='Log In', form=form)


# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('home'))


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('home'))
#     form = RegistrationForm()
#     form.guest.choices = [(True, 'User'), (False, 'Host')]
#     if form.validate_on_submit():
#         user = User(username=form.username.data, email=form.email.data, name=form.fullName.data, guest=form.guest.data)
#         user.set_password(form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Congratulations, you are now a registered user!')
#         login_user(user)
#         return redirect(url_for('upcoming', username=user.username))
#     return render_template('register.html', title='Register', form=form)


# @app.route('/user/<username>/previous')
# def previous(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     upcoming = upcomingMeeting.query.filter_by(uid=user.id)
#     history = meetingHistory.query.filter_by(uid=user.id)
#     uMeetings = []
#     pMeetings = []
#     for meet in upcoming:
#         curr = {
#             "space": Space.query.filter_by(id=meet.spid).first(),
#             "location": Location.query.filter_by(id=Space.location).first(),
#             "date": meet.date,
#             "start": meet.startTime,
#             "end": meet.endTime
#         }
#         uMeetings.append(curr)

#     for meet in history:
#         curr = {
#             "space": Space.query.filter_by(id=meet.spid).first(),
#             "location": Location.query.filter_by(id=Space.location).first(),
#             "date": meet.date,
#             "start": meet.startTime,
#             "end": meet.endTime,
#             "review": meet.review
#         }
#         pMeetings.append(curr)

#     return render_template('previous.html', user=user, meetings=uMeetings, history=pMeetings)

# @app.route('/user/<username>/upcoming')
# def upcoming(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     upcoming = upcomingMeeting.query.filter_by(uid=user.id)
#     history = meetingHistory.query.filter_by(uid=user.id)
#     uMeetings = []
#     pMeetings = []
#     for meet in upcoming:
#         curr = {
#             "space": Space.query.filter_by(id=meet.spid).first(),
#             "location": Location.query.filter_by(id=Space.location).first(),
#             "date": meet.date,
#             "start": meet.startTime,
#             "end": meet.endTime
#         }
#         uMeetings.append(curr)

#     for meet in history:
#         curr = {
#             "space": Space.query.filter_by(id=meet.spid).first(),
#             "location": Location.query.filter_by(id=Space.location).first(),
#             "date": meet.date,
#             "start": meet.startTime,
#             "end": meet.endTime,
#             "review": meet.review
#         }
#         pMeetings.append(curr)

#     return render_template('upcoming.html', user=user, meetings=uMeetings, history=pMeetings)



# @app.route('/booking/<space>', methods=['GET', 'POST'])
# @login_required
# def book(space):
#     space = Space.query.filter_by(name=space).first()
#     tech = TechToSpace.query.filter_by(spid=space.id).all()
#     techInSpace = []
#     for t in tech:
#         curr = {
#             "tech": Tech.query.filter_by(id=t.tid).all(),
#             "count": TechToSpace.query.filter_by(tid=t.tid, spid=space.id).all()
#         }
#         techInSpace.append(curr)
#     form = Booking()
#     form.space.data = space.name
#     if form.validate_on_submit():
#         flash("You've booked: {}".format(space.name))
#         confirm = upcomingMeeting(uid=current_user.id, spid=space.id, date=form.date.data, startTime=form.startTime.data, endTime=form.endTime.data)
#         db.session.add(confirm)
#         db.session.commit()
#         return redirect(url_for('upcoming', username=current_user.username))
#     return render_template('booking.html', title='Search', form=form, space=space, tech=techInSpace)


# @app.route('/confirm', methods=['GET', 'POST'])
# @login_required
# def confirm():
#     form = Booking()
#     if form.validate_on_submit():

#         confirmed = Booking(date=form.date.data,
#                             space=form.space.data,
#                             tech=form.tech.data,
#                             groupSize=form.groupSize.data)
#         db.session.add(confirmed)
#         db.session.commit()
#         return redirect(url_for('confirm', date=form.date.data,
#                                 space=form.space.data,
#                                 tech=form.tech.data,
#                                 groupSize=form.groupSize.data))
#     return render_template('booking.html', form=form)


# @app.route('/search', methods=['GET', 'POST'])
# def search():
#     form = FullSearch()
#     form.price.choices = [(True, 'Free'), (False, '$$$')]
#     form.groupSize.data = 1
#     technology = []
#     for t in Tech.query.all():
#         technology.append((t.id, t.name))
#     form.tech.choices = technology

#     if form.validate_on_submit():
#         zip = form.zipcode.data
#         date = form.date.data
#         #sT = form.startTime.data
#         eT = form.endTime.data
#         tech = form.tech.data
#         gSize = form.groupSize.data
#         free = form.price.data

#         if free == "True":
#             if tech is None:
#                 s = db.session.query(Space).filter(Space.hourlyRate == 0, Space.sizeCap >= gSize) \
#                     .join(Location).filter(Location.zip == zip) \
#                     .join(upcomingMeeting).filter(eT <= upcomingMeeting.startTime, date == upcomingMeeting.date)
#                 s2 = db.session.query(Space).filter(Space.hourlyRate == 0, Space.sizeCap >= gSize) \
#                     .join(Location).filter(Location.zip == zip) \
#                     .join(upcomingMeeting).filter(date != upcomingMeeting.date)
#                 spaces = s.union(s2)
#             else:
#                 s = db.session.query(Space).filter(Space.hourlyRate == 0, Space.sizeCap >= gSize) \
#                 .join(Location).filter(Location.zip == zip) \
#                 .join(TechToSpace).filter(Space.id == TechToSpace.spid, TechToSpace.tid.in_(tech))\
#                 .join(upcomingMeeting).filter(eT <= upcomingMeeting.startTime, date == upcomingMeeting.date)
#                 s2 = db.session.query(Space).filter(Space.hourlyRate == 0, Space.sizeCap >= gSize) \
#                     .join(Location).filter(Location.zip == zip) \
#                     .join(TechToSpace).filter(Space.id == TechToSpace.spid, TechToSpace.tid.in_(tech)) \
#                     .join(upcomingMeeting).filter(date != upcomingMeeting.date)
#                 spaces = s.union(s2)
#             return results(spaces)
#         else:
#             if tech is None:
#                 s = db.session.query(Space).filter(Space.hourlyRate >= 1, Space.sizeCap >= gSize) \
#                     .join(Location).filter(Location.zip == zip) \
#                     .join(upcomingMeeting).filter(eT <= upcomingMeeting.startTime, date == upcomingMeeting.date)
#                 s2 = db.session.query(Space).filter(Space.hourlyRate >= 1, Space.sizeCap >= gSize) \
#                     .join(Location).filter(Location.zip == zip) \
#                     .join(upcomingMeeting).filter(date != upcomingMeeting.date)
#                 spaces = s.union(s2)
#             else:
#                 s = db.session.query(Space).filter(Space.hourlyRate >= 1, Space.sizeCap >= gSize) \
#                     .join(Location).filter(Location.zip == zip) \
#                     .join(TechToSpace).filter(Space.id == TechToSpace.spid, TechToSpace.tid.in_(tech))\
#                     .join(upcomingMeeting).filter(eT <= upcomingMeeting.startTime, date == upcomingMeeting.date)
#                 s2 = db.session.query(Space).filter(Space.hourlyRate >= 1, Space.sizeCap >= gSize) \
#                     .join(Location).filter(Location.zip == zip) \
#                     .join(TechToSpace).filter(Space.id == TechToSpace.spid, TechToSpace.tid.in_(tech)) \
#                     .join(upcomingMeeting).filter(date != upcomingMeeting.date)
#                 spaces = s.union(s2)
#         return results(spaces)
#     return render_template('search.html', title='Search', form=form)


# @app.route("/search_results")
# def results(spaces):
#     return render_template("searchResults.html", title="Results", spaces=spaces)


# @app.route('/space/<space>')
# def space(space):
#     space = Space.query.filter_by(name=space).first_or_404()
#     location = Location.query.filter_by(id=space.location).first_or_404()
#     r = reviews.query.filter_by(spid=space.id).all()
#     tech = TechToSpace.query.filter_by(spid=space.id).all()
#     techInSpace = []
#     for t in tech:
#         curr = {
#             "tech": Tech.query.filter_by(id=t.tid).all(),
#             "count": TechToSpace.query.filter_by(tid=t.tid, spid=space.id).all()
#         }
#         techInSpace.append(curr)

#     return render_template('space.html', space=space, location=location, reviews=r, tech=techInSpace)


# @app.route('/spaces')
# def spaces():
#     spaces = Space.query.all()
#     locations = []
#     for space in spaces:
#         l = Location.query.filter_by(id=space.location).first_or_404()
#         locations.append(l)
#     return render_template('listings.html', spaces=spaces)

# @app.route('/review/<space>/<date>/<time>', methods=['GET', 'POST'])
# def review(space, date, time):
#     form = ReviewForm()
#     day = datetime.strptime(date, '%Y-%m-%d').date()
#     st = datetime.strptime(time, '%H:%M:%S').time()
#     meetSpace = Space.query.filter_by(name=space).first()
#     meet = meetingHistory.query.filter_by(uid=current_user.id, spid=meetSpace.id, date=day, startTime=st, review=0).first()
#     if form.validate_on_submit():
#         flash("Thanks for your review!")
#         r = reviews(uid=current_user.id, spid=meetSpace.id, score=form.score.data, desc=form.desc.data)
#         meetingHistory.__setattr__(meet, 'review', 1)
#         db.session.add(r)
#         db.session.commit()
#         return redirect(url_for('upcoming', username=current_user.username))
#     return render_template('review.html', title="Review", form=form, space=space, date=date, time=time)


def reset_db():
    flash("Resetting database: deleting old data and repopulating with dummy data")
    # clear all data from all tables
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        db.session.execute(table.delete())
    db.session.commit()
    return render_template('home.html', title="Home")

@app.route('/populate_db')
def populate_db():
    reset_db()

    # Populate the database with sample data

    # Users
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

    return "Database populated successfully"


# players = [ 

#     {firstName: "", lastName: "", avgScore: 100},
#       {firstName: "", lastName: "", avgScore: 100},
#         {firstName: "", lastName: "", avgScore: 100},
#           {firstName: "", lastName: "", avgScore: 100},
#             {firstName: "", lastName: "", avgScore: 100},
#               {firstName: "", lastName: "", avgScore: 100},
    
# ]



# {
#     players.map(player => return <></>)
# }
