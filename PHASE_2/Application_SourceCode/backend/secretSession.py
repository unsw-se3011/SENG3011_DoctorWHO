# source: https://gist.github.com/aescalana/7e0bc39b95baa334074707f73bc64bfe

from flask.sessions import SecureCookieSessionInterface
from itsdangerous import URLSafeTimedSerializer
SK_FSS = "d3AD7iNe"


class CookieSessionInterface(SecureCookieSessionInterface):
	def __init__(self, secret_key):
		self.secret_key = secret_key
	# Override method
	# Take secret_key instead of an instance of a Flask app
	def get_signing_serializer(self, secret_key):
		signer_kwargs = dict(
			key_derivation=self.key_derivation,
			digest_method=self.digest_method
		)
		return URLSafeTimedSerializer(secret_key, salt=self.salt,
		                              serializer=self.serializer,
		                              signer_kwargs=signer_kwargs)

def decodeFlaskCookie(cookieValue):
	csi = CookieSessionInterface(SK_FSS)
	signingSerializer = csi.get_signing_serializer(csi.secret_key)
	return signingSerializer.loads(cookieValue)

# Keep in mind that flask uses unicode strings for the
# dictionary keys
def encodeFlaskCookie(cookieDict):
	csi = CookieSessionInterface(SK_FSS)
	signingSerializer = csi.get_signing_serializer(csi.secret_key)
	return signingSerializer.dumps(cookieDict)
"""
if __name__=='__main__':
	sk = 'wow_so_very_secret_lmao'
	sessionDict = {"role":"Admin","username":"root"}
	cookie = encodeFlaskCookie(sk, sessionDict)
	print(cookie)
	decodedDict = decodeFlaskCookie(sk, cookie)
	assert sessionDict==decodedDict
"""
