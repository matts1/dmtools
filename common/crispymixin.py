from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset
from django.core.urlresolvers import reverse
from django.forms import ModelForm


class CrispyMixin(object):
    pre_text = ''
    post_text = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        if hasattr(self, 'name'):
            self.helper.form_action = reverse(self.name)
        self.helper.layout = Layout(
            Fieldset(self.pre_text) if self.pre_text else None,
            *self.crispy_fields(),
            Fieldset(self.post_text) if self.post_text else None,
            FormActions(
                Submit('save_changes', getattr(self, 'title', 'Save changes')),
            )
        )
        pass

    def crispy_fields(self):
        return self.fields.keys()


class CrispyForm(CrispyMixin, ModelForm):
    pass