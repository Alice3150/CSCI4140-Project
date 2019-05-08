import tensorflow as tf
from flask import Flask, render_template, request, url_for, redirect, flash, make_response, session
from wtforms import SubmitField
import os
import datetime
from pymongo import MongoClient

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from werkzeug import secure_filename

import sys
sys.path.append("model")
import evaluate as transfer

# Create app
app = Flask(__name__)

app.secret_key = "secret key"

# please set the following CONSTANTS before running application
# PROJECT_PATH = 'E:\\Alice\\project\\CSCI4140-Project\\'
# APP_PATH = 'E:\\Alice\\project\\CSCI4140-Project\\deployment\\'

PROJECT_PATH = '/mnt/d/Study/opensourse/CSCI4140-Project/'
APP_PATH = '/mnt/d/Study/opensourse/CSCI4140-Project/deployment/'

# la_muse_ckpt = PROJECT_PATH + 'model_styles\\la_muse.ckpt'
# rain_princess_ckpt = PROJECT_PATH + 'model_styles\\rain_princess.ckpt'
# scream_ckpt = PROJECT_PATH + 'model_styles\\scream.ckpt'
# udnie_ckpt = PROJECT_PATH + 'model_styles\\udnie.ckpt'
# wave_ckpt = PROJECT_PATH + 'model_styles\\wave.ckpt'
# wreck_ckpt = PROJECT_PATH + 'model_styles\\wreck.ckpt'

la_muse_ckpt = PROJECT_PATH + 'model_styles/la_muse.ckpt'
rain_princess_ckpt = PROJECT_PATH + 'model_styles/rain_princess.ckpt'
scream_ckpt = PROJECT_PATH + 'model_styles/scream.ckpt'
udnie_ckpt = PROJECT_PATH + 'model_styles/udnie.ckpt'
wave_ckpt = PROJECT_PATH + 'model_styles/wave.ckpt'
wreck_ckpt = PROJECT_PATH + 'model_styles/wreck.ckpt'

# Connect to the database
# Please specify your database
client = MongoClient("mongodb+srv://csci4140:csci4140@esocluster-90004.mongodb.net/admin")
db = client.projdb

class ImageForm(FlaskForm):
    # input image
    image= FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'PNG', 'jpeg'], 'Images only!')
    ])

    # Submit button
    submit = SubmitField("Transfer")

# Home page
@app.route("/", methods=['GET', 'POST'])
def home():
    """Home page of app with form"""
    # Create form
    screamForm = ImageForm(prefix="screamForm")
    laMuseForm = ImageForm(prefix="laMuseForm")
    rainPrincessForm = ImageForm(prefix="rainPrincessForm")
    udnieForm = ImageForm(prefix="udnieForm")
    waveForm = ImageForm(prefix="waveForm")
    wreckForm = ImageForm(prefix="wreckForm")

    if screamForm.validate_on_submit() and screamForm.image.data:
        image = screamForm.image.data
        current_time_str = datetime.datetime.now().strftime("%I%M%p%B%d%Y")
        filename = secure_filename(current_time_str + image.filename)
        # img_path = APP_PATH + 'static\\images'
        img_path = APP_PATH + 'static/images'
        file_path = os.path.join(
            img_path, filename
        )
        image.save(file_path)
        args = ['--checkpoint', scream_ckpt, '--in-path', file_path, '--out-path', img_path]
        transfer.main(args)
        scream_file_url = '/static/images/' + filename

        if 'username' in session:
            _username = session['username']
            _user = db.Users.find_one({'name':_username})
            _image = db.Images.insert_one({'filename':filename, 'name':_user.get('_id'), 'fileurl':scream_file_url})
            image_id = _image.inserted_id
            db.Users.update_one({'name': _username}, {'$push': {'images': image_id}})
        
        return redirect(url_for('display', image_src=filename))

    else:
        scream_file_url = None

    if laMuseForm.validate_on_submit() and laMuseForm.image.data:
        image = laMuseForm.image.data
        current_time_str = datetime.datetime.now().strftime("%I%M%p%B%d%Y")
        filename = secure_filename(current_time_str + image.filename)
        # img_path = APP_PATH + 'static\\images'
        img_path = APP_PATH + 'static/images'
        file_path = os.path.join(
            img_path, filename
        )
        image.save(file_path)
        args = ['--checkpoint', la_muse_ckpt, '--in-path', file_path, '--out-path', img_path]
        transfer.main(args)
        laMuse_file_url = '/static/images/' + filename

        if 'username' in session:
            _username = session['username']
            _user = db.Users.find_one({'name':_username})
            _image = db.Images.insert_one({'filename':filename, 'name':_user.get('_id'), 'fileurl':laMuse_file_url})
            image_id = _image.inserted_id
            db.Users.update_one({'name': _username}, {'$push': {'images': image_id}})
            
        return redirect(url_for('display', image_src=filename))

    else:
        laMuse_file_url = None

    if rainPrincessForm.validate_on_submit() and rainPrincessForm.image.data:
        image = rainPrincessForm.image.data
        current_time_str = datetime.datetime.now().strftime("%I%M%p%B%d%Y")
        filename = secure_filename(current_time_str + image.filename)
        # img_path = APP_PATH + 'static\\images'
        img_path = APP_PATH + 'static/images'
        file_path = os.path.join(
            img_path, filename
        )
        image.save(file_path)
        args = ['--checkpoint', rain_princess_ckpt, '--in-path', file_path, '--out-path', img_path]
        transfer.main(args)
        rainPrincess_file_url = '/static/images/' + filename

        if 'username' in session:
            _username = session['username']
            _user = db.Users.find_one({'name':_username})
            _image = db.Images.insert_one({'filename':filename, 'name':_user.get('_id'), 'fileurl':rainPrincess_file_url})
            image_id = _image.inserted_id
            db.Users.update_one({'name': _username}, {'$push': {'images': image_id}})
        
        return redirect(url_for('display', image_src=filename))

    else:
        rainPrincess_file_url = None

    if udnieForm.validate_on_submit() and udnieForm.image.data:
        image = udnieForm.image.data
        current_time_str = datetime.datetime.now().strftime("%I%M%p%B%d%Y")
        filename = secure_filename(current_time_str + image.filename)
        # img_path = APP_PATH + 'static\\images'
        img_path = APP_PATH + 'static/images'
        file_path = os.path.join(
            img_path, filename
        )
        image.save(file_path)
        args = ['--checkpoint', udnie_ckpt, '--in-path', file_path, '--out-path', img_path]
        transfer.main(args)
        udnie_file_url = '/static/images/' + filename

        if 'username' in session:
            _username = session['username']
            _user = db.Users.find_one({'name':_username})
            _image = db.Images.insert_one({'filename':filename, 'name':_user.get('_id'), 'fileurl':udnie_file_url})
            image_id = _image.inserted_id
            db.Users.update_one({'name': _username}, {'$push': {'images': image_id}})

        return redirect(url_for('display', image_src=filename))

    else:
        udnie_file_url = None

    if waveForm.validate_on_submit() and waveForm.image.data:
        image = waveForm.image.data
        current_time_str = datetime.datetime.now().strftime("%I%M%p%B%d%Y")
        filename = secure_filename(current_time_str + image.filename)
        # img_path = APP_PATH + 'static\\images'
        img_path = APP_PATH + 'static/images'
        file_path = os.path.join(
            img_path, filename
        )
        image.save(file_path)
        args = ['--checkpoint', wave_ckpt, '--in-path', file_path, '--out-path', img_path]
        transfer.main(args)
        wave_file_url = '/static/images/' + filename

        if 'username' in session:
            _username = session['username']
            _user = db.Users.find_one({'name':_username})
            _image = db.Images.insert_one({'filename':filename, 'name':_user.get('_id'), 'fileurl':wave_file_url})
            image_id = _image.inserted_id
            db.Users.update_one({'name': _username}, {'$push': {'images': image_id}})
        
        return redirect(url_for('display', image_src=filename))

    else:
        wave_file_url = None

    if wreckForm.validate_on_submit() and wreckForm.image.data:
        image = wreckForm.image.data
        current_time_str = datetime.datetime.now().strftime("%I%M%p%B%d%Y")
        filename = secure_filename(current_time_str + image.filename)
        # img_path = APP_PATH + 'static\\images'
        img_path = APP_PATH + 'static/images'
        file_path = os.path.join(
            img_path, filename
        )
        image.save(file_path)
        args = ['--checkpoint', wreck_ckpt, '--in-path', file_path, '--out-path', img_path]
        transfer.main(args)
        wreck_file_url = '/static/images/' + filename
        
        if 'username' in session:
            _username = session['username']
            _user = db.Users.find_one({'name':_username})
            _image = db.Images.insert_one({'filename':filename, 'name':_user.get('_id'), 'fileurl':wreck_file_url})
            image_id = _image.inserted_id
            db.Users.update_one({'name': _username}, {'$push': {'images': image_id}})
        
        return redirect(url_for('display', image_src=filename))

    else:
        wreck_file_url = None
    
    loginMessage = "<a class='nav-link active' href='signup'>Sign up / Login</a>"

    if 'username' in session:
        # loginUrl = "#"
        # loginMessage = session['username']
        _username = session['username']
        _user = db.Users.find_one({'name':_username})
        avatar_url = _user['avatar_url']
        loginMessage = "<a class='nav-link active' href='album'><img id='avatar' src="+avatar_url+" width='30' height='30'></a>" + \
                            "<a class='nav-link active' href='logout'>Logout</a>"

    return render_template('index.html', 
        screamForm=screamForm, scream_file_url=scream_file_url, 
        laMuseForm=laMuseForm, laMuse_file_url=laMuse_file_url,
        rainPrincessForm=rainPrincessForm, rainPrincess_file_url=rainPrincess_file_url,
        udnieForm=udnieForm, udnie_file_url=udnie_file_url,
        waveForm=waveForm, wave_file_url=wave_file_url,
        wreckForm=wreckForm, wreck_file_url=wreck_file_url,
        loginMessage=loginMessage)

@app.route('/signup', methods=['POST', 'GET'])
def signup(name=None):
    error = ""
    count = 0

    if request.method == 'POST':
        _name = request.form['inputUsername']
        _password = request.form['inputPassword']
        _rpassword = request.form['repeatPassword']
        users = db.Users.find({'name':_name})

        for u in users:
            count += 1

        if count != 0:
            error="Username already exists!"
        elif _password != _rpassword:
            error="password not coincident!"
        else:
            db.Users.insert({'name':_name, 'password':_password, 'images':[], 'avatar_url':'/static/avatar/default.jpg'})
            flash('You were successfully signed up')
            return redirect(url_for('login'))

    return render_template('signup.html', name=name, error=error)

@app.route('/login', methods=['POST', 'GET'])
def login(name=None):
    error = ""

    if request.method == 'POST':
        _name = request.form['inputUsername']
        _password = request.form['inputPassword']
        user = db.Users.find_one({'name':_name}, {'password':_password})

        if user == None:
            error = "Username not exist!"
        elif user['password'] != _password:
            error = "Password incorrect!"
        else:
            session['username'] = _name
            return redirect(url_for('home'))

    return render_template('login.html', name=name, error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

#only implement album to display, not main page to display
#also not the user profile
@app.route("/display/<image_src>", methods=['post','get'])
def display(image_src=None):
    image_src = "/static/images/" + image_src
    return render_template('display.html',image_src = image_src)

@app.route("/album/")
def album():
    #replace with database imgs
    #only for testing
    imgs = ["/static/styles/la_muse.jpg","/static/styles/la_muse.jpg","/static/styles/la_muse.jpg",
            "/static/styles/rain_princess.jpg","/static/styles/star.jpg","/static/styles/the_scream.jpg",
            "/static/styles/the_scream.jpg","/static/styles/rain_princess.jpg","/static/styles/star.jpg"]
    return render_template('album.html',imgs=imgs)

if __name__ == "__main__":
    print(("* Loading model and Flask starting server..."
           "please wait until server has fully started"))
    # Run app
    app.run(host="0.0.0.0", port=80)
