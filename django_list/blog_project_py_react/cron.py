# backup.py

import os
import subprocess
from django.core.management import call_command

def backup_database():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_root.settings')
    import django
    django.setup()  # Make sure Django is properly set up

    try:
        call_command('dbbackup', '--clean')
        print("Backup successful")
    except Exception as e:
        print(f"An error occurred: {e}")







if __name__ == "__main__":
    backup_database()
