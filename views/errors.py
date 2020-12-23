from flask import Blueprint, redirect, render_template, url_for, flash

from views.models import login_manager

errors = Blueprint(
    'errors',
    __name__,
    template_folder= 'templates'
)

@login_manager.unauthorized_handler
def unauthorized():
    flash('Please Log In to access the page.','danger')
    return redirect(url_for('auth.login'))


def page_not_found(d):
    return render_template('errors/404_error.html'),404