from src.admin_views.base import SecureModelView

class UserAdminView(SecureModelView):
    can_create = False
    can_edit = False
    can_delete = False