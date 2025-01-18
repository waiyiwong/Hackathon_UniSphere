from django.apps import AppConfig
import logging

class UserAccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_account'

    def ready(self):
        import user_account.signals



# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def login(username, password):
    # ... login logic ...
    if login_successful:
        logging.info(f'User {username} logged in successfully.')
    else:
        logging.warning(f'Failed login attempt for user {username}.')

def update_profile(user_id, new_profile_data):
    # ... profile update logic ...
    logging.info(f'Profile updated for user ID {user_id}.')
