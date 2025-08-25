import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'geliştirme-icin-gecici-gizli-anahtar'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://neondb_owner:npg_waAFtTN5C2Kg@ep-billowing-base-a2g0zhr8-pooler.eu-central-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
    SQLALCHEMY_TRACK_MODIFICATIONS = False