import random
import string

from django.contrib.auth import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import CreateView

from userprofile.forms import NewAccountForm


# Create your views here.

class CreateNewAccount(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'location/location_form.html'
    form_class = NewAccountForm

    def get_success_url(self):
        psw = ''.join(random.SystemRandom().choice(string.ascii_uppercase +
                                                   string.ascii_lowercase +
                                                   string.digits + '!$%#@') for _ in range(8))

        if (user_instance := User.objects.filter(id=self.object.id)) and user_instance.exists():
            user_object = user_instance.first()
            user_object.set_password(psw)
            user_object.save()

            content = f"Buna ziua, \n " \
                    f"Date de autentificare sunt: \n username: {user_object.username} \n" \
                    f"parola: {psw}"

            msg_html = render_to_string('registration/invite_user.html', {'content_email': content})
            email = EmailMultiAlternatives(subject="Date contact platforma",
                                           body=content,
                                           from_email='contact@gmail.ro',
                                           to=[user_object.email])
            email.attach_alternative(msg_html, 'text/html')
            email.send()
        return reverse('location:lista_locatii')