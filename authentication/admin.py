from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.forms import ModelForm

from .models import User


class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ('email', 'username')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    list_display = ('email', 'username')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password', 'username',)}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'username', 'is_superuser', 'is_staff', 'is_active')}
            ),
        )

    filter_horizontal = ()


admin.site.register(User, CustomUserAdmin)

