from flask import Blueprint, render_template, request, redirect, url_for
from marvel.forms import MarvelForm
from flask_login import login_required, current_user
from marvel.models import Marvel, MarvelSchema, db

site = Blueprint('site', __name__, template_folder='site_templates')
@site.route('/')
def home():
    return render_template('index.html')
    
@site.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    marvelform = MarvelForm()

    try:
        if request.method == 'POST' and marvelform.validate_on_submit():
            
            name = marvelform.name.data
            description = marvelform.description.data
            comics_appeared_in = marvelform.comics_appeared_in.data
            super_power = marvelform.super_power.data
            date_created = marvelform.date_created.data
            user_token = current_user.token
            marvel = Marvel(name, description, comics_appeared_in, super_power, date_created, user_token)
            db.session.add(marvel)
            db.session.commit()
            return redirect(url_for('site.profile')) 
    except:
        raise Exception('Character not created, please check your form and try again.')
    user_token = current_user.token
    marvels = Marvel.query.filter_by(user_token=user_token)
    return render_template('profile.html', form=marvelform, marvels=marvels)



   