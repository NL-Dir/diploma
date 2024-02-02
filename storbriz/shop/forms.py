from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


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
