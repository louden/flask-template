# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>


from flask import redirect, render_template, render_template_string, Blueprint
from flask import request, url_for
from flask_user import current_user, login_required, roles_accepted
from app import app, db
from app.core.models import UserProfileForm, SubscribeForm
import stripe

core_blueprint = Blueprint('core', __name__, url_prefix='/')


# The Home page is accessible to anyone
@core_blueprint.route('')
def home_page():
    form = SubscribeForm()
    return render_template('core/home_page.html', form=form)


# The User page is accessible to authenticated users (users that have logged in)
@core_blueprint.route('user')
@login_required  # Limits access to authenticated users
def user_page():
    return render_template('core/user_page.html')


# The Admin page is accessible to users with the 'admin' role
@core_blueprint.route('admin')
@roles_accepted('admin')  # Limits access to users with the 'admin' role
def admin_page():
    return render_template('core/admin_page.html')


@core_blueprint.route('user/profile', methods=['GET', 'POST'])
@login_required
def user_profile_page():
    # Initialize form
    form = UserProfileForm(request.form, current_user)

    # Process valid POST
    if request.method == 'POST' and form.validate():
        # Copy form fields to user_profile fields
        form.populate_obj(current_user)

        # Save user_profile
        db.session.commit()

        # Redirect to home page
        return redirect(url_for('core.home_page'))

    # Process GET or invalid POST
    return render_template('core/user_profile_page.html',
                           form=form)

@core_blueprint.route('create_subscription', methods=['POST'])
def create_subscription():
    stripe.api_key = app.config['STRIPE_SECRET_KEY']
    
    # Get the incomming details
    email = request.form['stripeEmail'] # NEEDS TO BE VERIFIED
    token = request.form['stripeToken']

    # Try to create customer with Stripe
    try:
        stripe.Customer.create(
          email=email,
          source=token,
          plan='weekly_box'
        )
    except:
        # If the cutomer creation fails on stripe's end, stop
        return('Failure')
    try

    # Create the new user
    user = User(email=email,
                first_name=first_name,
                last_name=last_name,
                password=app.user_manager.hash_password(password),
                active=True,
                confirmed_at=datetime.utcnow())

    # Save to DB
    db.session.commit()
    
    return('Success')

# Register blueprint
app.register_blueprint(core_blueprint)
