class Config:
    SECRET_KEY = "gcethub_secret_key"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Root%4012345@localhost/gcethub"

    SQLALCHEMY_TRACK_MODIFICATIONS = False