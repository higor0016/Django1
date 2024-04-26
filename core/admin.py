from django.contrib import admin

# Register your models here.
from .models import Produto, Cliente

class ProdudoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


class ClienteAdmin(admin.ModelAdmin):
    list_display=('nome', 'sobrenome', 'email')

admin.site.register(Produto, ProdudoAdmin)
admin.site.register(Cliente, ClienteAdmin)