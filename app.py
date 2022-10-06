#Import
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

#Config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydata.db'
db = SQLAlchemy(app)

#Schema

class Leagues(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String)
    country = db.Column(db.String)
    level = db.Column(db.String)
    teams = db.relationship('Teams', backref = 'all_teams')

class Teams(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String)
    city = db.Column(db.String)
    manager = db.Column(db.String)
    leagues = db.Column(db.ForeignKey('leagues.id'))
    players = db.relationship('Players', backref = 'all_players')

class Players(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String)
    position = db.Column(db.String)
    age = db.Column(db.String)
    teams = db.Column(db.ForeignKey('teams.id'))

# Database Exectutable
db.create_all()

d1 = Leagues(id=1, name='Premier League', country='England', level='1') 
d2 = Leagues(id=2, name='Ligue 1', country='France', level='1') 
d3 = Leagues(id=3, name='Bundesliga', country='Germany', level='1') 
d4 = Leagues(id=4, name='La Liga', country='Spain', level='1') 
d5 = Leagues(id=5, name='Eredivisie', country='Holland', level='1')
db.session.add(d1)
db.session.add(d2) 
db.session.add(d3) 
db.session.add(d4) 
db.session.add(d5) 
db.session.commit()
c1 = Teams(id=1, name='Man City', city='Manchester', manager='manager', leagues=1) 
c2 = Teams(id=2, name='Chealsea', city='London', manager='manager', leagues=1) 
c3 = Teams(id=3, name='Bayern Munich', city='Berlin', manager='manager', leagues=3) 
c4 = Teams(id=4, name='Dortmund', city='Dortmund', manager='manager', leagues=3) 
c5 = Teams(id=5, name='PSG', city='Paris', manager='manager', leagues=2) 
c6 = Teams(id=6, name='AS Monaco', city='Monaco', manager='manager', leagues=2) 
c7 = Teams(id=7, name='Real Madrid', city='Madrid', manager='manager', leagues=4) 
c8 = Teams(id=8, name='Marseille', city='Marseille', manager='manager', leagues=2) 
c9 = Teams(id=9, name='PSV', city='Eindhoven', manager='manager', leagues=5) 
c10 = Teams(id=10, name='Ajax', city='Ajax', manager='manager', leagues=5) 
db.session.add(c1) 
db.session.add(c2) 
db.session.add(c3) 
db.session.add(c4) 
db.session.add(c5) 
db.session.add(c6) 
db.session.add(c7) 
db.session.add(c8) 
db.session.add(c9) 
db.session.add(c10) 
db.session.commit()
s1 = Players(id=1, name='name', position ='CAM', age='28', teams=4) 
s2 = Players(id=2, name='name', position ='CAM', age='25', teams=2) 
s3 = Players(id=3, name='name', position ='CAM', age='24', teams=1) 
db.session.add(s1) 
db.session.add(s2) 
db.session.add(s3) 
db.session.commit()

#Routes
@app.route('/') 
def home(): 
    return ('Hello') 

# CRUD
@app.route('/add')
def add():
    new_team = Teams(name="New Team", city='City', manager='manager')
    db.session.add(new_team)
    db.session.commit()
    return "Added new team to database"

@app.route('/read')
def read():
    teams = Teams.query.all()
    teams_string = ""
    for team in teams:
        teams_string += "<br>"+ team.name + team.city + team.manager
    return teams_string

@app.route('/update/<name>')
def update(name):
    first_team = Teams.query.first()
    first_team.name = name
    db.session.commit()
    return first_team.name
    
@app.route('/leagues') 
def leagues(): 
    return render_template("leagues.html") 

@app.route('/teams') 
def course(): 
    return render_template("teams.html") 

if __name__ == '__main__': app.run(debug=True, host='0.0.0.0', port=8001)
