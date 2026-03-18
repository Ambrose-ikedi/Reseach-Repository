from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from .models import Research
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    research = Research.query.all()
    return render_template('home.html', research=research)

@main.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        filepath = os.path.join('app/uploads', filename)
        file.save(filepath)

        new_research = Research(
            title=request.form['title'],
            author=request.form['author'],
            category=request.form['category'],
            filename=filename
        )
        db.session.add(new_research)
        db.session.commit()

        return redirect(url_for('main.home'))

    return render_template('upload.html')

@main.route('/search')
def search():
    query = request.args.get('q')
    results = Research.query.filter(Research.title.contains(query)).all() if query else []
    return render_template('search.html', results=results)
