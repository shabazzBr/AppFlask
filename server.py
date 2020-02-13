from app import create_app, db
import os
from app.models import User
from flask_migrate import Migrate

app = create_app(os.environ["FLASK_ENV"])
Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(
        app=app,
        db=db,
        User=User
    )

if __name__ == '__main__':
    app.run(debug=True, port=3000, host="0.0.0.0")