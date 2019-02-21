import os

with open(os.environ.get('JWT_PRIVATE_KEY_PATH'), "rb") as key_file:
    private_key = key_file.read()

with open(os.environ.get('JWT_PUBLIC_KEY_PATH'), "rb") as key_file:
    public_key = key_file.read()

SECRET_KEY = os.environ.get('SECRET_KEY')
