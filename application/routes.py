from application import app, db
from application.models import Locations, TouristSites
from application.forms import CreateLocationForm, CreateSiteForm, UpdateSiteForm
from flask import render_template, redirect, url_for, request

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    locations = Locations.query.all()
    sites = TouristSites.query.all()

    return render_template('home.html', locations=locations, sites=sites)

@app.route('/create/location', methods=['GET', 'POST'])
def create_location():
    form = CreateLocationForm()

    if form.validate_on_submit():
        location = Locations(country=form.country.data, city=form.city.data)
        db.session.add(location)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('create-location.html', form=form)
 
    
@app.route('/create/site', methods=['GET', 'POST'])
def create_site():
    form = CreateSiteForm()
    locations = Locations.query.all()

    for location_id in locations:
        form.location_id.choices.append(
            (f"{location_id.id}", f"{location_id.city}")
        )
    
    if form.validate_on_submit():
        site = TouristSites(site_name=form.site_name.data, favourite_part=form.favourite_part.data, location_id=form.location_id.data)
        db.session.add(site)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('create-site.html', form=form, locations=locations)


@app.route('/update/site/<id>', methods=['GET', 'POST'])
def updatesite(id):
    form = UpdateSiteForm()
    site = TouristSites.query.filter_by(id=id).first()
    locations = Locations.query.all()

    for location_id in locations:
        form.location_id.choices.append(
            (f"{location_id.id}", f"{location_id.city}")
        )

    if request.method == 'GET':
        form.site_name.data = site.site_name
        form.favourite_part.data = site.favourite_part
        form.location_id.data = site.location_id
        return render_template('update.html', form=form)

    else: 
        if form.validate_on_submit():
            site.site_name = form.site_name.data
            site.favourite_part = form.favourite_part.data
            site.location_id = form.location_id.data
            db.session.commit()
            return redirect(url_for('home'))


@app.route('/delete/<id>', methods=['GET', 'POST'])
def deletesite(id):
    site = TouristSites.query.filter_by(id=id).first()
    db.session.delete(site)
    db.session.commit()
    return redirect(url_for('home'))