from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by')
    search_fields = ('title', 'content')
    list_filter = ('created_by',)
    fields = ('title', 'content', 'created_by')
    readonly_fields = ('created_by',)  # To prevent modification of creator field

    # Optionally, you could add more configurations as needed
    def get_readonly_fields(self, request, obj=None):
        if not obj:  # If object is not created yet (new object)
            return self.readonly_fields
        return self.readonly_fields

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'date_of_birth', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_of_birth')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'date_of_birth', 'profile_photo')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
