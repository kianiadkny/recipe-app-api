'''
Django command to wait for the pgsql database to be ready
'''
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    ''' Django command to wait for database to be ready'''

    def handle(self, *args, **options):
        '''Entry point for command'''
        self.stdout.write('Waiting for postgres database ...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable,waiting for 1 second')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available for use!'))
