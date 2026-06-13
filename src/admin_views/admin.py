from src.admin_views.base import SecureModelView


class AdminAdminView(SecureModelView):
    can_create = True
    can_edit = True
    can_delete = True

