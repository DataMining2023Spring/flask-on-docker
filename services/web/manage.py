from flask.cli import FlaskGroup

<<<<<<< HEAD
from project import app, db, User
=======
from project import app
>>>>>>> bcc15e2dc7991fdf2486b2282223e7564742319c


cli = FlaskGroup(app)


<<<<<<< HEAD
@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(User(email="michael@mherman.org"))
    db.session.commit()


=======
>>>>>>> bcc15e2dc7991fdf2486b2282223e7564742319c
if __name__ == "__main__":
    cli()

