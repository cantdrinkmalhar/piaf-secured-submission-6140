from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Render the password_reset_email.html template'

    def handle(self, *args, **kwargs):
        # Get a user (replace with an actual user from your database)
        user = User.objects.first()

        if not user:
            self.stdout.write(self.style.ERROR('No users found in the database.'))
            return

        # Generate the password reset token
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        # Context data for the template
        context = {
            'user': user,
            'protocol': 'http',
            'domain': 'localhost:8000',
            'uid': uid,
            'token': token,
        }

        # Render the template
        email_content = render_to_string('password_reset_email.html', context)
        self.stdout.write(email_content)
