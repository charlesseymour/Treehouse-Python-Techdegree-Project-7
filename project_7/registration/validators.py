from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _, ngettext

import re


class UpperAndLowerValidator:

    def validate(self, password, user=None):
        if not (re.search(r'[A-Z]', password) and
                re.search(r'[a-z]', password)):
            raise ValidationError(
                _("Password lacks upper and/or lower case letter"),
                code='password_lacks_upper_or_lower',
            )

    def get_help_text(self):
        return _('''Your password must have at least one upper-case \
        and one lower-case letter.''')


class DigitValidator:

    def validate(self, password, user=None):
        if not re.search(r'[0-9]', password):
            raise ValidationError(
                _("Password lacks at least one digit"),
                code='password_lacks_digit',
            )

    def get_help_text(self):
        return _("Your password must have at least one digit from 0-9.")


class CurrentValidator:

    def validate(self, password, user=None):
        if not user:
            return

        if user.check_password(password):
            raise ValidationError(
                _("New password must be different than current password"),
                code='password_not_different',
            )

    def get_help_text(self):
        return _("The password must be different than the current password.")


class UserNameValidator:

    def validate(self, password, user=None):
        if not user:
            return

        if user.username.lower() in password.lower():
            raise ValidationError(
                _("Password cannot contain username"),
                code='password_contains_username',
            )

        if hasattr(user, 'account'):
            if user.account.first_name.lower() in password.lower():
                raise ValidationError(
                    _("Password cannot contain first name"),
                    code='password_contains_first_name',
                )

            if user.account.last_name.lower() in password.lower():
                raise ValidationError(
                    _("Password cannot contain last name"),
                    code='password_contains_last_name',
                )

    def get_help_text(self):
        return _("Password cannot contain username, first name, or last name.")


class SpecialCharValidator:

    def validate(self, password, user=None):

        if not re.search(r'[@#\$]', password):
            raise ValidationError(
                _('''Password must contain at least one of the following: \
                  @, #, $'''),
                code='password_no_specialchar',
            )

    def get_help_text(self):
        return _("Password must contain at least one of @, #, or $.")
