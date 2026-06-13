from flask import redirect, url_for, render_template, request
from flask_admin import AdminIndexView, expose
from flask_login import current_user, login_user, logout_user
from flask_admin.contrib.sqla import ModelView

from src.admin_views.forms import LoginForm
from src.models.admin import Admin as AdminModel


class SecureModelView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('admin.login'))


class SecureIndexView(AdminIndexView):

    def is_accessible(self):
        return (
            current_user.is_authenticated
            or request.endpoint in ('admin.login', 'admin.logout')
        )

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('.login'))

    @expose('/login', methods=('GET', 'POST'))
    def login(self):
        form = LoginForm()
        if form.validate_on_submit():
            admin = AdminModel.query.filter_by(
                name=form.username.data
            ).first()

            if admin and admin.password == form.password.data:
                login_user(admin, remember=True)
                return redirect(url_for('admin.index'))

        return render_template('login.html', form=form)

    @expose('/logout')
    def logout(self):
        logout_user()
        return redirect('/admin')

