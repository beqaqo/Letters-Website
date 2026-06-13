import os
from uuid import uuid4

from markupsafe import Markup
from flask_admin.form import ImageUploadField

from src.admin_views.base import SecureModelView
from src.config import Config

class PhotoAdminView(SecureModelView):
    def _image(view, context, model, name):
        return Markup(
            f'<img src="/static/uploads/{model.img}" width="100">'
        )

    def gen_name(obj, file_data):
        filename, ext = os.path.splitext(file_data.filename)
        return f'{uuid4()}{ext}'

    column_formatters = {
        'img': _image,
    }

    form_extra_fields = {
        'img': ImageUploadField(
            base_path=Config.UPLOAD_PATH,
            namegen=gen_name,
        )
    }



