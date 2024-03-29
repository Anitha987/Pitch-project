from flask_login import login_required,current_user
from flask import render_template,request,redirect,url_for,abort
from ..models import User,Pitch,Category,Comment,Vote
from .forms import UpdateProfile,PitchForm,CategoryForm,CommentForm
from ..import db,photos
from . import main 
@main.route('/')
def index():
  '''
  view root page function that returns the index page and its data
  '''
  # category = Category.query.all()
  category = Category.get_categories()

  return render_template('index.html',category = category)
@main.route('/add/category',methods=['GET','POST'])
@login_required
def new_category():
  '''
  viewnew group route function that returns a page with a formto create a category
  '''
  form = CategoryForm()
  if form.validate_on_submit():
    name = form.name.data
    new_category= Category(name=name)
    new_category.save_category()
    return redirect(url_for('.index'))
  title = 'New category'
  return render_template('new_category.html',Category_form=form,title=title)
    
@main.route('/categories/<int:id>')    
def category(id):
  category =Category.query.get(id)
  pitches = Pitch.query.filter_by(category=id).all()
  return render_template('category.html',pitches=pitches,category=category)

@main.route('/categories/view_pitch/add/<int:id>',methods=['GET','POST'])
@login_required
def new_pitch(id):
  '''
  function to check pitches form and from the fields
  '''
  form = PitchForm()
  category= Category.query.filter_by(id=id).first()
  if category is None:
    abort(404)
  if form.validate_on_submit():
    content = form.content.data
    new_pitch= Pitch(content=content,category=category.id,user_id=current_user.id)
    new_pitch.save_pitch()
    return redirect(url_for('.category',id=category.id))
  title='New Pitch'
  return render_template('new_pitch.html',title=title,pitch_form = form,category = category)
@main.route('/categories/view_pitch/<int:id>',methods=['GET','POST'])
@login_required
def view_pitch(id):
  '''
  function htat returns a single pitch for comment to be added
  '''
  print (id)
  pitches=Pitch.query.get(id)
  if pitches is None:
    abort(404)
  comment=Comments.get_comments(id)
  return return_template('pitch.html',pitches=pitches,comment=comment,category_id=id)
@main.route('/user/<uname>')
def profile(uname):
  user = User.query.filter_by(username = uname).first()

  if user is None:
    abort(404)
  return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
  user = User.query.filter_by(username = uname).first()
  if user is None:
    abort(404)
  form = UpdateProfile()
  if form.validate_on_submit():
      user.bio = form.bio.data
      db.session.add(user)
      db.session.commit()
      return redirect(url_for('.profile',uname=user.username))
  return render_template('profile/update.html',form =form)  


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
  user = User.query.filter_by(username = uname).first()
  if 'photo' in request.files:
      filename = photos.save(request.files['photo'])
      path = f'photos/{filename}'
      user.profile_pic_path = path
      db.session.commit()
  return redirect(url_for('main.profile',uname=uname))        

