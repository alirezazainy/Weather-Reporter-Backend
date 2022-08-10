from passlib.context import CryptContext
from pydantic import BaseModel
# Passwords Hashing processor

# Passlib Cryptor model
pwd_cxt = CryptContext(schemes='bcrypt', deprecated='auto')


class Hash:
    """
    This Model Hashes password with bcrypt CryptContext Engine
    and Verify or Check the passwords

    Method 'bcrypt': Gives a plain password and returns a hashed password 
    Method 'verify': Gives a plain password and hashed password and check them same or not
    """
    @staticmethod
    def bcrypt(password):
        return pwd_cxt.hash(password)

    @staticmethod
    def verify(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password, hashed_password)
