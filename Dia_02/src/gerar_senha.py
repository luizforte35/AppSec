import secrets
import string

string.ascii_uppercase
string.digits
string.punctuation
string.ascii_lowercase

def gerar_senhas(length):
    
    secure_pass = secrets.choice(string.ascii_uppercase)
    secure_pass += secrets.choice(string.ascii_lowercase)
    secure_pass += secrets.choice(string.digits)
    secure_pass += secrets.choice(string.punctuation)
    for i in range(length - 4 ):
        secure_pass += secrets.choice(string.ascii_uppercase + string.digits + string.punctuation + string.ascii_lowercase)
    return secure_pass

senhas = []
senhas.append(gerar_senhas(12))
    