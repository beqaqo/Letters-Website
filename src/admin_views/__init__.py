from src.models import (
    User,
    Message,
    Photo,
    Statistic,
    Admin,
)
from src.admin_views.base import SecureIndexView
from src.admin_views.user import UserAdminView
from src.admin_views.message import MessageAdminView
from src.admin_views.photo import PhotoAdminView
from src.admin_views.statistic import StatisticAdminView
from src.admin_views.admin import AdminAdminView


def register_admin_views(admin_instance, db_session):
    admin_instance.add_view(UserAdminView(User, db_session, name='Users'))
    admin_instance.add_view(MessageAdminView(Message, db_session, name='Messages'))
    admin_instance.add_view(PhotoAdminView(Photo, db_session, name='Photos'))
    admin_instance.add_view(StatisticAdminView(Statistic, db_session, name='Statistics'))
    admin_instance.add_view(AdminAdminView(Admin, db_session, name='Admins', endpoint='admin_users'))
