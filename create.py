from flask import Flask
from models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgres://wcwlejqqgupljr:cd578524384fe50128b92d5def7359e4041ad0cda58189dc53eb4331005d43a5@ec2-3-216-92-193.compute-1.amazonaws.com:5432/d5dlf9grtpdmbk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
