# Flask Template

This is a flask template based on the [Flask Foundation](https://github.com/JackStouffer/Flask-Foundation).  I have added Flask-User and Stripe support to the template for use on my own projects.

I have also reorganized the structure to have models and forms that pertain to a particular blueprint in the folder for that blueprint.

# Changes to Make

When you start a new project with this template, you will need to touch several files, in addition to the content that you add.  These are outlined below. 

## Assets

- appname/assets.py: This file names several css and javascript files that get bundled together and minified.  You will need to edit the names to your specific needs.

## Blueprints

- appname/__init__.py: As new blueprints are added to the application, they need to be registered in the `create_app()` function.  See the example for `main`.

## Error Handling Pages

- appname/templates/{401, 404, 500}.html: These files are basic error messages.  Update them to your application
- appname/__init__.py: If you add more error handling templates, they need to be registered in the `register_errorhandlers()` function.

## Settings

- appname/settings.py: This file contains all of the settings for the application.  

## User Pages

- appname/templates/{common, flask_user}/*: These pages have templates that overide the default Flask-User templates that are based on Bootstrap.  If you want to use the defaults, delete these folders.  Otherwise, edit them as desired.

# TODO

- Update tests
- Add Stripe