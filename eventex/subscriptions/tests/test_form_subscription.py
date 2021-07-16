from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """CPF must only accept digits."""
        form = self.make_validated_form(cpf='ABCD5678910')
        #self.assertListEqual(['cpf'], list(form.errors))
        #self.assertFormErrorMessage(form, 'cpf', 'CPF deve conter apenas números.')
        self.assertFormErrorCode(form, 'cpf', 'digits')
    
    def test_cpf_has_11_digits(self):
        """CPF must contain eleven digits"""
        form = self.make_validated_form(cpf='1234')
        #self.assertListEqual(['cpf'], list(form.errors))
        #self.assertFormErrorMessage(form, 'cpf', 'CPF deve conter 11 dígitos.')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_name_must_be_capitalized(self):
        form = self.make_validated_form(name='RAFIC Farah')
        self.assertEqual('Rafic Farah', form.cleaned_data.get('name'))

    def test_email_is_optional(self):
        """Email is optional."""
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        """Phone is optional."""
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        """Email and Phone are optional, but one must be informed."""
        form = self.make_validated_form(email='', phone='')
        self.assertListEqual(['__all__'], list(form.errors))

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors.get(field)
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def assertFormErrorMessage(self, form, field, msg):
        # Obsoleto
        errors = form.errors
        errors_list= errors[field]
        self.assertListEqual([msg], errors_list)

    def make_validated_form(self, **kwargs):
        valid = dict(name='Rafic Farah', cpf='12345678910',
                    email='rafic@farah.com', phone='21-998366404')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()

        return form