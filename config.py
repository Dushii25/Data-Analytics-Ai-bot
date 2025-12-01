# config.py

# ========================
# PostgreSQL Database Config
# ========================
DBCONFIG = {
    "host": "localhost",        # e.g. "localhost" or your DB server
    "port": 5432,               # default PostgreSQL port
    "database": "data_analytics_db",  # change to your DB name
    "user": "postgres",         # change to your DB user
    "password": "7906258537" # change to your DB password
}

# ========================
# Admin Credentials
# ========================
# Used in admin.py for login
ADMIN_USERNAME = "admin"        # change as you like
ADMIN_PASSWORD = "admin123"     # change as you like

# ========================
# App Settings (optional)
# ========================
APP_NAME = "Data Analytics Bot"
APP_WELCOME_MESSAGE = "Welcome to Data Analytics Bot!"
