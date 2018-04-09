## Hash Email

### Simple function to double hash an email address.

A simple function to double hash an email.

Hashes an email address and then rehashes it using parts of the hash value.

This mechanism is not suitable for storing passwords.

### Example

```python
from hashemail.hash_email import HashEmail

emailhash = HashEmail("test@example.com")
email.hash_value()

```

Additional options:

- section_1_start: 1 based start position for the first section of double hash
- section_1_length: Length of first section of double hash
- section_2_start: 1 based start position for the second section of double hash
- section_2_length: Length of second section of double hash