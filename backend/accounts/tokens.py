from django.contrib.auth.tokens import PasswordResetTokenGenerator


class TokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        """
        We are overriding the method because we dont want to include the users password in the hash
        """
        login_timestamp = '' if user.last_login is None else user.last_login.replace(microsecond=0, tzinfo=None)
        return str(user.id) + str(user.reset_salt) + str(timestamp) + str(login_timestamp)


token_generator = TokenGenerator()
