'''
The HF3 is stored in the session cookie, so we have to save it.
THen we "know" that it is a flask application. Per se, the cookies are only encoded not encrypted.
But there is a drop in replacement available which adds AES256 crypto
https://github.com/SaintFlipper/EncryptedSession
the following code is copy/pasted from encrypted_session.py


the key is given in the webpage when you walk the maze and end up in the top right corner


    <h2>Placeholder</h2>
    <code>[DEBUG]: app.crypto_key: timetoguessalasttime</code><br>
    <code>[ERROR]: Traceback (most recent call last): UnicodeDecodeError: 'utf-8' codec can't decode byte in
        position 1: invalid continuation byte</code>
    <br>
    <code>[DEBUG]: Flag added to session</code>


    So the key is timeto\x01guess\x03a\x03last\x07time

    Which is NOW 32 bits.. \x == 1 char 01 is the other chars

    you will also need pycryptodome und pycryptodomex
    when there are strxor errors, it might be because of a collision with pycrypto

'''


from werkzeug.datastructures import CallbackDict
from flask.sessions import SessionInterface, SessionMixin

from Crypto.Cipher import AES
import json
from json import JSONEncoder, JSONDecoder
import base64
import zlib

class BinaryAwareJSONDecoder(JSONDecoder):
    """
    Converts a json string, where binary data was converted into objects form
    using the BinaryAwareJSONEncoder, back into a python object.
    """

    def __init__(self):
            JSONDecoder.__init__(self, object_hook=self.dict_to_object)

    def dict_to_object(self, d):
        if '__type__' not in d:
            return d

        typ = d.pop('__type__')
        if typ == 'bytes':
            return base64.b64decode (bytes (d['b'], 'utf-8'))
        else:
            # Oops... better put this back together.
            d['__type__'] = typ
            return d


crypto_key = b'timeto\x01guess\x03a\x03last\x07time'

session_cookie= "u.B+wsjdtJ9AvDOX9YS3fHhPhlTg1HmZlQ3ADO+uBq7IQyQjqEXV/GtE4U/xLRVbSt/IDPlMvOgXuLzThKsHWVR9QznSU7xg50b1WnK+P/JXBB75xi0pyVWA+EzQFTPsVd1xCvUSdPoeE7TfjM7W2scr+P9fgTDwwXgCjQvKVjLYFnxNhheZqMZ+XYLJ5nt9u0FVvNGXPi4NaFaxbjG96LDA0U1XVAJGDNQGqSt0UCAX64lRWr3S6XNvzd3rboxch+Ck5YvFQ9A2qjY6wp7ujuA9M7sUMp8c5kvvknm0vHqFEYW6iFAR0d52It7Uxi8NTzaHbxp8Fr1qwGHHSu16xfYeV7iJm0ZA+ihOoTcj2HyL2dZXePm5NdeASY4VOcXg12nVv32ovfzYwx3uQoAtKzac9qtYyQWHYyj/+fX00VrEgUAFCuOHs8s6FESpVbIzYq4f5qSDvbtWTsKkOokp0hW+PIS078uyU09dOEDO6Ef0vQcBvPH79n5k9Bjf3KP4w7TF9KjbIqukA9CKX7Gpza9vEACBvZCeZ5Iq/Z0YVNmYBxcbzbZDd4IM6GHe/DpYhYO8mDxi5Zys+lR8d4bEId8psPX8GD/6/pY20zkSsD1WFVeERg+KVF9nzrXgKsA9Z758syArVcOoww017g209PEU4AKZjLWEzN3Jw0JGVfs6o8LkSey8BKQQ==.n7n5qF4jM63YG7+2TZMGqQ==.B2OnQIR1ur6PAucLXUHtXQ=="

itup = session_cookie.split(".")

is_compressed=False

ciphertext = base64.b64decode (bytes(itup[1], 'utf-8'))
mac = base64.b64decode (bytes(itup[2], 'utf-8'))
nonce = base64.b64decode (bytes(itup[3], 'utf-8'))

# Decrypt
cipher = AES.new (crypto_key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify (ciphertext, mac)

# Convert back to a dict and pass that onto the session
if is_compressed:
    data = zlib.decompress (data)
session_dict = json.loads (str (data, 'utf-8'), cls=BinaryAwareJSONDecoder)

print(session_dict)
