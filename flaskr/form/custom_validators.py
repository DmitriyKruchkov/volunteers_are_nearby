from wtforms import ValidationError


def file_ext_validator(ext):
    message = f'Расширение аватара должно быть: {', '.join(ext)}'

    def _length(form, field):
        if field.data.filename and field.data.filename.split(".")[-1] not in ext:
            raise ValidationError(message)

    return _length
