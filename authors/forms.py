import re

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        ),
            code='invalid'
        )


class RegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Your username')
        add_placeholder(self.fields['email'], 'Your e-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: John')
        add_placeholder(self.fields['last_name'], 'Ex.: Doe')
        add_placeholder(self.fields['password'], 'Type your password')
        add_placeholder(self.fields['password2'], 'Repeat your password')

    username = forms.CharField(
        label='Username',
        help_text=(
            'Username mus have letters, number or one of those @.+-_. '
            'the length shoud between 4 and 150 characters'),
        error_messages={
            'required': 'esse campo não pode ficar vazio',
            'min_length': 'Username must have at least 4 characters',
            'max_length': 'Username must have have less than 150 characters'
        },
        min_length=4,
        max_length=150,

    )
    first_name = forms.CharField(
        error_messages={'required': 'Write your first name'},
        label='First name'
    )

    last_name = forms.CharField(
        error_messages={'required': 'Write your last name'},
        label='Last name'
    )

    email = forms.EmailField(
        error_messages={'required': 'E-mail is required'},
        label='E-mail',
        help_text='The e-mail must be valid',

    )

    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Sua senha',
        error_messages={
            'required': 'Password must not be empty',
        },
        validators=[strong_password]
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Confirme sua senha',
        error_messages={
            'required': 'Please, repeat your password',
        },
    )

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'email',
                  'password',
                  ]

        # exclude = ['first_name']

        labels = {
            'username': 'Usuario',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail',
            'password': 'Senha',
        }

        widgets = {
            'first_name': forms.TextInput(),
            'password': forms.PasswordInput(),
        }

    def clean_password(self):
        data = self.cleaned_data.get('password')

        if 'atenção' in data:
            raise ValidationError(
                'Não digite %(value)s no campo password',
                code='invalid',
                params={'value': 'atenção'}
            )

        return data

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'User e-mail is already in use', code='invalid',
            )

        return email

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                'Password and confirmation must be equal',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [
                    password_confirmation_error,
                ],
            })
