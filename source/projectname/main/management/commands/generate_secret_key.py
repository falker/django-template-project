# -*- coding: utf-8 -*-
import random
from django.core.management import BaseCommand, CommandError
from django.db.models import get_apps

class Command(BaseCommand):

    def handle(self, *args, **options):
        if len(args) > 0:
            raise CommandError('Command takes no arguments (%s given)' % len(args))

        symbols = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        secret_key = ''.join([random.SystemRandom().choice(symbols) for i in range(50)])

        print "Your secret key is '{}'".format(secret_key)
