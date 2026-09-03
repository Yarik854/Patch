#jwt - json web token, получаемый после успешной аутентификации
import os #читатьт окружение
from datetime import datetime, timedelta, timezone #срок жизни токена

import jwt #создание токена
from dotenv import load_dotenv #загрузка переменных из .env 

from fastapi import Depends, HTTPException 
from fastapi.security import OAuth2PasswordBearer #авторизация через bearer токен

from sqlalchemy.orm import Session 
from pwdlib import Password, PasswordHash #хэширование пароля

from database import get_db 
from models import User 

load_dotenv() #ЗАГРУЗКА ПЕРЕМЕННЫХ ОКРУЖЕНИЯ 

SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-me-32-bytes-min')

ALGORITHM = os.getenv('ALGORITHM', 'HS256')
ACCESS_TOKEN_EXPIRE_MINUTES = 30

password_hash = PasswordHash.recomended()

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl='api/users/login'
)