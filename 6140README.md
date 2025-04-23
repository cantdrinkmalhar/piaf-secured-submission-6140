# PIAF Secured Version

This repository contains the security-hardened version of the PIAF (Pour IA Francophone) web application, modified for academic vulnerability assessment and secure deployment.

## Security Fixes Applied

- ✅ **CSRF Protection** : CSRF tokens were added to all needed forms like **login.html** and **signup.html** performing state-changing actions including password changes.
- ✅ **XSS Mitigation** : Output escaping enabled in all the required templates i.e. **acc_active_email.html** and **password_reset_email.html**
- ✅ **Cookie Hardening** : Secure cookie flags (`HttpOnly`, `Secure`, `SameSite`) configured, changes were made initially in the production **settings.py** moving to **views.py** then connected it to **urls.py** both under api directory, finally configured the main app **urls.py** to imply the changes 
- ✅ **Password Security** : Strong password validation rules were added in the files like **tests.py** and **create_admin.py** using Django's built-in validators to prevent weak password usage.
- ✅ **Debug Mode Disabled** : `DEBUG = False` is now enforced in production **settings.py** to prevent internal data leaks.
- ✅ **Open Redirect Fix** : Redirects using the `?next=` parameter in the **views.py** are now validated using Django’s `url_has_allowed_host_and_scheme()` to prevent redirecting users to external domains.

## To Run Locally
Ensure Docker and Docker Compose are installed. Then:

docker-compose up --build

## Structure
Core Django app: piaf/

Settings and middleware configured in: piaf/src/settings.py

Templates updated for escaping and CSRF in: piaf/src/authentification/templates
