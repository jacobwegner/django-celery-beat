from django.core import management

import pytest


@pytest.mark.django_db()
class test_CheckMigrations:
    def test_migrations_check(self):
        management.call_command("makemigrations", check=True, dry_run=True)
