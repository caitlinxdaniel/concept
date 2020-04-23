from django.contrib import admin

# Register your models here.
from .models import Phrase, Concept, Token

admin.site.register(Phrase)
admin.site.register(Concept)
admin.site.register(Token)
