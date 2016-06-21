from flask import (Blueprint,
                   redirect,
                   render_template,
                   request,
                   url_for)
from flask_user import (current_user,
                        login_required,
                        roles_accepted)
from appname.database import db
from appname.main.forms import UserProfileForm

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('main/index.html')


@main.route('/user/profile', methods=['GET', 'POST'])
@login_required
def user_profile():
    # Initialize form
    form = UserProfileForm(request.form, current_user)

    # Process valid POST
    if request.method == 'POST' and form.validate():
        # Copy form fields to user_profile fields
        form.populate_obj(current_user)

        # Save user_profile
        db.session.commit()

        # Redirect to home page
        return redirect(url_for('main.home'))

    # Process GET or invalid POST
    return render_template('main/user_profile.html',
                           form=form)


@main.route("/restricted")
@login_required
def restricted():
    return render_template('main/restricted.html')


# The Admin page is accessible to users with the 'admin' role
@main.route('/admin')
@roles_accepted('admin')  # Limits access to users with the 'admin' role
def admin():
    return render_template('main/admin.html')
