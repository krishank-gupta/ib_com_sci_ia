from passlib.context import CryptContext

pwd_config = CryptContext(schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds = 30000
)

def hash_password(entered_password):
    return pwd_config.hash(entered_password)

def check_password(entered_password, hashed):
    return pwd_config.verify(entered_password, hashed)

def get_charities_usernames(db_table):
    charities = []
    for i in db_table:
        charities.append(i.username)
    return charities

def validation(data, datatype):
    return None
