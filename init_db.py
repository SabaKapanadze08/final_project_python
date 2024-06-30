from ext import app,db
from models import services_item, ContactMessage, User


with app.app_context():
    db.create_all()

    admin_user = User("admin@gmail.com", "Admin", "Admin123!", "Admin")
    db.session.add(admin_user)
    db.session.commit()