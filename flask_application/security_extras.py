from flask.ext.security.forms import RegisterForm, Required, TextField, _datastore, get_message, ValidationError


def unique_username(form, field):
    if _datastore.find_user(username=field.data) is not None:
        msg = get_message('EMAIL_ALREADY_ASSOCIATED', email=field.data)[0]
        raise ValidationError(msg)
        
class ExtendedRegisterForm(RegisterForm):
    username = TextField('Username', [Required(), unique_username])