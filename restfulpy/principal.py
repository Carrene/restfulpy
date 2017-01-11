
from itsdangerous import TimedJSONWebSignatureSerializer
from nanohttp import settings


class JwtPrincipal:

    def __init__(self, payload):
        self.payload = payload

    @classmethod
    def create_serializer(cls):
        return TimedJSONWebSignatureSerializer(
            settings.jwt.secret,
            expires_in=settings.jwt.max_age,
            algorithm_name=settings.jwt.algorithm
        )

    def encode(self):
        return self.create_serializer().dumps(self.payload)

    @classmethod
    def decode(cls, encoded):
        if encoded.startswith('Bearer '):
            encoded = encoded[7:]
        payload = cls.create_serializer().loads(encoded)
        return cls(payload)

    def is_in_roles(self, *roles):
        if 'roles' in self.payload:
            if set(self.payload['roles']).intersection(roles):
                return True
        return False

    @property
    def email(self):
        return self.payload.get('email')

    @property
    def session_id(self):
        return self.payload.get('sessionId')

    @property
    def id(self):
        return self.payload.get('id')
