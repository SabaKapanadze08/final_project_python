from flask import render_template, redirect
from forms import ContactForm,RegisterForm, LoginForm, ReviewForm, ServiceForm
from ext import app, db
from models import services_item, ContactMessage,User, Review
from flask_login import login_user, logout_user, current_user, login_required

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        
        contact_message = ContactMessage(name=form.name.data, email=form.email.data, message=form.message.data)
        db.session.add(contact_message)
        db.session.commit()

    return render_template("contact.html", form=form)

@app.route("/reviews")
def reviews():
    user_reviews = Review.query.all()
    return render_template("reviews.html", reviews=user_reviews)

@app.route("/delete_review/<int:review_id>")
@login_required  
def delete_review(review_id):
    if current_user.role != "Admin" :
        return redirect("/")
    
    review = Review.query.get(review_id)

    db.session.delete(review)
    db.session.commit()

    return redirect("/reviews")


@app.route('/add_review', methods=['GET', 'POST'])
def add_review():
    form = ReviewForm()

    if form.validate_on_submit():
        author_name = form.author_name.data
        author_initials = form.author_initials.data
        rating = form.rating.data
        message = form.message.data
        
        new_review = Review(author_name=author_name, author_initials=author_initials, rating=rating, message=message)
        
        db.session.add(new_review)
        db.session.commit()
        return redirect("reviews")
    
    return render_template('add_review.html', form=form)

@app.route("/signin", methods=["GET", "POST"])
def signin():

    if current_user.is_authenticated:
       return redirect("/")

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
    return render_template("signin.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    
    if current_user.is_authenticated:
        redirect("/")

    form = RegisterForm()
    if form.validate_on_submit():
        existing_user_email = User.query.filter(User.email == form.email.data).first()
        existing_user_username = User.query.filter(User.username == form.username.data).first()
        
        if existing_user_email:
            form.email.errors.append("Email is already in use. Please use a different email.")
        
        if existing_user_username:
            form.username.errors.append("Username is already in use. Please use a different username.")

        if not form.email.errors and not form.username.errors:

            new_user = User(email=form.email.data, username=form.username.data, password=form.password.data, role=form.role.data)
            db.session.add(new_user)
            db.session.commit()
    
    return render_template("signup.html", form=form)

@app.route("/services")
def services():
    services_item_list=services_item.query.all()
    return render_template("services.html", services=services_item_list)


@app.route("/add_services", methods=["GET", "POST"])
@login_required
def add_services():
    if current_user.role != "Admin" :
        return redirect("/")
    
    form = ServiceForm()
    if form.validate_on_submit():
        new_service = services_item(name=form.name.data, price=form.price.data, image=form.image.data)
        if form.image.data:
            image = form.image.data
            image.save(f"{app.root_path}\static\{image.filename}")
            new_service.image = image.filename
        db.session.add(new_service)
        db.session.commit()
        return redirect("/services")    

    return render_template("add_services.html", form=form)


@app.route("/delete_service/<int:items_id>")
@login_required  
def delete_service(items_id):
    if current_user.role != "Admin" :
        return redirect("/")
    
    service = services_item.query.get(items_id)

    db.session.delete(service)
    db.session.commit()

    return redirect("/services")


@app.route("/product/<int:service_id>")
def products(service_id):
    service_item=services_item.query.filter_by(id=service_id).first()
    return render_template("product.html", products=service_item)