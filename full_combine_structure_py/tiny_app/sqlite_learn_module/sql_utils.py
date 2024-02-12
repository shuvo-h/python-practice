import bcrypt

def make_password_hash(plain_text_password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_text_password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def check_hashed_password(plain_text_password, hashed_password):
    # Hash the plain text password using the same salt as the hashed password
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password.encode('utf-8'))

