import random

from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'generatorApp/index.html'

    def get_context_data(self):
        context = super(Index, self).get_context_data()
        context['password'] = generate_pass(request=self.request)
        return context


def generate_pass(request):
    characters = list('qwertyuiopasdfghjklzxcvbnm')

    if request.GET.get('uppercase'):
        characters.extend('QWERTYUIOPASDFGHJKLZXCVBNM')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*()')
    if request.GET.get('numbers'):
        characters.extend('0123456789')

    password = ''
    for x in range(int(request.GET.get('length', 12))):
        password += random.choice(characters)

    return password
