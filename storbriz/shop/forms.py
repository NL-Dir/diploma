from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from .models import Order


class UserRegisterForm(UserCreationForm):
    """
    Переопределенная форма регистрации пользователей
    """

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы регистрации
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs.update({"placeholder": 'Логин'})
            self.fields['email'].widget.attrs.update({"placeholder": 'Email'})
            self.fields['first_name'].widget.attrs.update({"placeholder": 'Имя'})
            self.fields['last_name'].widget.attrs.update({"placeholder": 'Фамилия'})
            self.fields['password1'].widget.attrs.update({"placeholder": 'Придумайте пароль'})
            self.fields['password2'].widget.attrs.update({"placeholder": 'Повторите пароль'})
            self.fields[field].widget.attrs.update(
                {"class": "input form__input  authorization-input window-input _req ",
                 "autocomplete": "off"})


class UserUpdateForm(ModelForm):
    """
    Переопределенная форма регистрации пользователей
    """

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs.update({"placeholder": 'Логин'})
            self.fields['email'].widget.attrs.update({"placeholder": 'Email'})
            self.fields['first_name'].widget.attrs.update({"placeholder": 'Имя'})
            self.fields['last_name'].widget.attrs.update({"placeholder": 'Фамилия'})
            self.fields[field].widget.attrs.update(
                {"class": "input form__input  authorization-input window-input _req ",
                 "autocomplete": "off"})


TIME_CHOICES = (
    (1, '9:00 - 21:00'),
    (1, '9:00 - 15:00'),
    (1, '15:00 - 21:00'),
    (1, '9:00 - 13:00'),
    (1, '13:00 - 17:00'),
    (1, '17:00 - 21:00'),
)


class OrderCreateForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['street'].widget.attrs.update({"placeholder": 'Улица'})
            self.fields['building'].widget.attrs.update({"placeholder": 'дом'})
            self.fields['flat'].widget.attrs.update({"placeholder": 'квартира'})
            self.fields['time_period'] = forms.ChoiceField(choices=TIME_CHOICES, widget=forms.RadioSelect())
            self.fields['total'].widget = forms.HiddenInput()
            self.fields['user'].widget = forms.HiddenInput()
            self.fields['date'].widget = forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
            self.fields['status'].widget = forms.HiddenInput()
            self.fields['goods'].widget.attrs.update({"style": 'background-color: red;'})
            self.fields[field].widget.attrs.update({"class": "form-delivery__input input window-input _req",
                                                    "autocomplete": "off"})
