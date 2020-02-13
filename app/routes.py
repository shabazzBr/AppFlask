def load(app):
    from app.home import home
    app.register_blueprint(home)

    from app.auth import auth
    app.register_blueprint(auth)