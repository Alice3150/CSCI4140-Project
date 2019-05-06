import tensorflow as tf
from flask import Flask, render_template, request, url_for, redirect
from wtforms import SubmitField
import os

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
PROJECT_PATH = 'E:\\Alice\\project\\photo_style_transfer\\'
APP_PATH = 'E:\\Alice\\project\\photo_style_transfer\\deployment\\'

la_muse_ckpt = PROJECT_PATH + 'model_styles\\la_muse.ckpt'
rain_princess_ckpt = PROJECT_PATH + 'model_styles\\rain_princess.ckpt'
scream_ckpt = PROJECT_PATH + 'model_styles\\scream.ckpt'
udnie_ckpt = PROJECT_PATH + 'model_styles\\udnie.ckpt'
wave_ckpt = PROJECT_PATH + 'model_styles\\wave.ckpt'
wreck_ckpt = PROJECT_PATH + 'model_styles\\wreck.ckpt'

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
        filename = secure_filename(image.filename)
        img_path = APP_PATH + 'static\\images'
        file_path = os.path.join(
            img_path, filename
        )
        image.save(file_path)
        args = ['--checkpoint', scream_ckpt, '--in-path', file_path, '--out-path', img_path]
        transfer.main(args)
        scream_file_url = '/static/images/' + filename
    else:
        scream_file_url = None

    if laMuseForm.validate_on_submit() and laMuseForm.image.data:
        image = laMuseForm.image.data
        filename = secure_filename(image.filename)
        img_path = APP_PATH + 'static\\images'
        file_path = os.path.join(
            img_path, filename
        )
        image.save(file_path)
        args = ['--checkpoint', la_muse_ckpt, '--in-path', file_path, '--out-path', img_path]
        transfer.main(args)
        laMuse_file_url = '/static/images/' + filename
    else:
        laMuse_file_url = None

    if rainPrincessForm.validate_on_submit() and rainPrincessForm.image.data:
        image = rainPrincessForm.image.data
        filename = secure_filename(image.filename)
        img_path = APP_PATH + 'static\\images'
        file_path = os.path.join(
            img_path, filename
        )
        image.save(file_path)
        args = ['--checkpoint', rain_princess_ckpt, '--in-path', file_path, '--out-path', img_path]
        transfer.main(args)
        rainPrincess_file_url = '/static/images/' + filename
    else:
        rainPrincess_file_url = None

    if udnieForm.validate_on_submit() and udnieForm.image.data:
        image = udnieForm.image.data
        filename = secure_filename(image.filename)
        img_path = APP_PATH + 'static\\images'
        file_path = os.path.join(
            img_path, filename
        )
        image.save(file_path)
        args = ['--checkpoint', udnie_ckpt, '--in-path', file_path, '--out-path', img_path]
        transfer.main(args)
        udnie_file_url = '/static/images/' + filename
    else:
        udnie_file_url = None

    if waveForm.validate_on_submit() and waveForm.image.data:
        image = waveForm.image.data
        filename = secure_filename(image.filename)
        img_path = APP_PATH + 'static\\images'
        file_path = os.path.join(
            img_path, filename
        )
        image.save(file_path)
        args = ['--checkpoint', wave_ckpt, '--in-path', file_path, '--out-path', img_path]
        transfer.main(args)
        wave_file_url = '/static/images/' + filename
    else:
        wave_file_url = None

    if wreckForm.validate_on_submit() and wreckForm.image.data:
        image = wreckForm.image.data
        filename = secure_filename(image.filename)
        img_path = APP_PATH + 'static\\images'
        file_path = os.path.join(
            img_path, filename
        )
        image.save(file_path)
        args = ['--checkpoint', wreck_ckpt, '--in-path', file_path, '--out-path', img_path]
        transfer.main(args)
        wreck_file_url = '/static/images/' + filename
    else:
        wreck_file_url = None

    return render_template('index.html', 
        screamForm=screamForm, scream_file_url=scream_file_url, 
        laMuseForm=laMuseForm, laMuse_file_url=laMuse_file_url,
        rainPrincessForm=rainPrincessForm, rainPrincess_file_url=rainPrincess_file_url,
        udnieForm=udnieForm, udnie_file_url=udnie_file_url,
        waveForm=waveForm, wave_file_url=wave_file_url,
        wreckForm=wreckForm, wreck_file_url=wreck_file_url)


if __name__ == "__main__":
    print(("* Loading model and Flask starting server..."
           "please wait until server has fully started"))
    # Run app
    app.run(host="0.0.0.0", port=80)
