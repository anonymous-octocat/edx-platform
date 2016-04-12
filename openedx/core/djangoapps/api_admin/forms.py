"""Forms for API management."""
from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

from openedx.core.djangoapps.api_admin.models import ApiAccessRequest


class ApiAccessRequestForm(forms.ModelForm):
    """Form to request API access."""
    terms_of_service = forms.BooleanField()

    class Meta(object):
        model = ApiAccessRequest
        fields = ('company_name', 'website', 'company_address', 'reason', 'terms_of_service')
        labels = {
            'company_name': _('Company Name'),
            'company_address': _('Company Address'),
            'reason': _('Describe what your application does.'),
        }
        help_texts = {
            'reason': None,
            'website': _("The URL of your company's website."),
            'company_name': _('The name of your company.'),
            'company_address': _('The contact address of your company.'),
        }
        widgets = {
            'company_address': forms.Textarea()
        }

    def __init__(self, *args, **kwargs):
        # Get rid of the colons at the end of the field labels.
        kwargs.setdefault('label_suffix', '')
        super(ApiAccessRequestForm, self).__init__(*args, **kwargs)

        self.fields['terms_of_service'].label = mark_safe(
            # Translators: link_start and link_end are HTML tags for a
            # link to the terms of service. platform_name is the name of
            # this Open edX installation.
            _('{link_start}{platform_name} API Terms of Service{link_end}').format(
                platform_name=settings.PLATFORM_NAME,
                link_start='<a href="{url}">'.format(url=reverse('api-tos')),
                link_end='</a>',
            )
        )
