from django.db import models
from django.utils.translation import gettext_lazy as _

USER_TYPES = (
    ('ADMIN', 'Admin'),
    ('REGULAR', 'Regular'),
)

HISTORY_TYPES = (
    ('POST', 'Post'),
    ('MESSAGE', 'Message'),
)

SOCIAL_PLATFORMS = (
    ('FACEBOOK', 'Facebook'),
    ('TWITTER', 'Twitter')
)

MESSAGE_TYPES = (
    ('EMAIL', 'Email'),
    ('SMS', 'Sms')
)
