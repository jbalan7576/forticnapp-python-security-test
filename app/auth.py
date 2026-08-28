import hashlib


def authenticate(username, password):
    # INTENTIONALLY VULNERABLE: CWE-327 Weak Cryptography
    password_hash = hashlib.md5(password.encode()).hexdigest()

    if username == "admin" and password_hash == "21232f297a57a5a743894a0e4a801fc3":
        return True

    return False