from django.contrib import admin
from .models import Category,Customer,Product,Order,Profile
from django.contrib.auth.models import User



# Register your models here.
#admin.site.register(Category)
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name',)  # Display the name field in the list view



admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)


#mix profile and user info

class ProfileInLine(admin.StackedInline):
    model= Profile

    #extend user model

class UserAdmin(admin.ModelAdmin):
    model = User
    fields =["username","first_name","last_name","email"]
    inlines = [ProfileInLine]

#unregister old signup
admin.site.unregister(User)
#re-register
admin.site.register(User,UserAdmin) 