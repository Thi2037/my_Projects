DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Task_manager_application',  # Database name
        'USER': 'your_mysql_user',  # Your MySQL username
        'PASSWORD': 'your_mysql_password',  # Your MySQL password
        'HOST': 'localhost',  # Change if MySQL is on a different host
        'PORT': '3306',  # MySQL default port
    }
}