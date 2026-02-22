from django.contrib import admin

from core.models import (
    Member,
)

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.forms import UserCreationForm
from django import forms

User = get_user_model()
admin.site.unregister(User)

class MemberInline(admin.StackedInline):
    model = Member
    max_num = 1
    can_delete = False
    required = True
    verbose_name_plural = "Membership Details"
    fieldsets = (
        (None, {
            "fields": (
                "contact_email",
                "game_name",
                "address",
                "city",
                "state",
                "zip",
                "country",
                "chapter",
            )
        }),
    )


class FullUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

        

class UserAdmin(DefaultUserAdmin):
    add_form = FullUserCreationForm
    inlines = (MemberInline,)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'first_name', 'last_name',
                'password1', 'password2', 'is_active', 'is_staff'
            ),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    ordering = ('username',)

admin.site.register(User, UserAdmin)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    
    # prevent members from being created in the MemberAdmin
    def has_add_permission(self, request):
        return False


    fields = ( 
        'user',
        'chapter',
        'game_name',
        'contact_email', 
        'address',
        'city',
        'state',
        'zip',
        'country'
    )
    readonly_fields = (
        'user',
    )