from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mybd.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    detail = db.Column(db.String(140))
    # date = db.Column(db.DateTime, nullable=False)
        

@app.route('/', methods=['GET', 'POST'])
def toppage():
    if request.method == 'GET':
        posts = Post.query.all()
        return render_template('toppage.html', posts=posts)
    else:
        title = request.form.get('title')
        detail = request.form.get('detail')
        new_post = Post(title=title, detail=detail)

        db.session.add(new_post)
        db.session.commit()
        return redirect('/')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/detail/<int:id>')
def read(id):
    post = Post.query.get(id)
    return render_template('detail.html', post=post)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    post = Post.query.get(id)
    if request.method == 'GET':
        return render_template('update.html', post=post)
    else:
        post.title = request.form.get('title')
        post.detail = request.form.get('detail')

        db.session.commit()
        return redirect('/')


@app.route('/delete/<int:id>')
def delete(id):
    post = Post.query.get(id)

    db.session.delete(post)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
   app.run() 