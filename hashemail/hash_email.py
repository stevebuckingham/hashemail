from hashlib import sha256


class HashEmail(object):

    def __init__(self, email, section_1_start=1, section_1_length=5, section_2_start=10, section_2_length=5):
        """
        Details required for double hashing an email using SHA256.
        :param email: Email address to hash
        :param section_1_start: 1 based start position for the first section of double hash
        :param section_1_length: Length of first section of double hash
        :param section_2_start: 1 based start position for the second section of double hash
        :param section_2_length: Length of second section of double hash
        """
        self.raw_email = None
        self._email = None
        self.email = email
        self.section_1_start = section_1_start
        self.section_1_length = section_1_length
        self.section_2_start = section_2_start
        self.section_2_length = section_2_length

    @property
    def email(self):
        """Email address that is being hashed"""
        return self._email

    @email.setter
    def email(self, emailaddress):
        """
        Change the email address to hash
        :param emailaddress: New email address to hash
        :return: False
        """
        lower_email = emailaddress.lower()
        self._email = lower_email
        self.raw_email = emailaddress

    def hash_value(self):
        """
        Function to double hash the email address using section settings from class.
        :return: Hex digest of double hashed email address
        """
        source = self.email.lower()
        initial = sha256(source.encode('utf-8')).hexdigest()
        interim = (initial[self.section_1_start - 1:(self.section_1_length - (self.section_1_start - 1))]
                   + initial
                   + initial[self.section_2_start:(self.section_2_length - (self.section_2_start - 1))]).encode('utf-8')
        final = sha256(interim).hexdigest()
        return final
