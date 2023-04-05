import rsa

def code(messange):
    (_pub, _priv) = rsa.newkeys(1024)
    message = messange.encode('utf8')

    crypto = rsa.encrypt(message, _pub)

    message = rsa.decrypt(crypto, _priv)
    return message.decode('utf8'), crypto
