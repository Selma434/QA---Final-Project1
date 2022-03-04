from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError

# create location form
class CreateLocationForm(FlaskForm):
    country = StringField('Which country is the Tourist site located in?', validators=[DataRequired(), Length(min=2,max=50)])
    city = StringField('Which city is the Tourist site located in?', validators=[DataRequired(), Length(min=2,max=40)])
    submit = SubmitField("Submit location")

# create site form
class CreateSiteForm(FlaskForm):
    site_name = StringField('Which Tourist site did you visit?', validators=[DataRequired()])
    favourite_part = StringField('What was your favourite part of the visit?', validators=[DataRequired()])
    location_id = SelectField("Select city in which the site is located:", choices=[], validators=[DataRequired()])
    submit = SubmitField("Submit Site")

# update site form
class UpdateSiteForm(FlaskForm):
    site_name = StringField('Which Tourist site did you visit?', validators=[DataRequired(), Length(min=2,max=50)])
    favourite_part = StringField('What did you most enjoy about the visit?', validators=[DataRequired(), Length(min=2,max=200)])
    location_id = SelectField("Select city in which the site is located:", choices=[], validators=[DataRequired()])
    submit = SubmitField("Update Site")
