__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '18/03/21'

from django import forms
from django.contrib.auth import get_user_model
from amlit.models.organisation import Organisation, UserOrganisation
from civitas.models.community import Community

User = get_user_model()


class OrganisationForm(forms.ModelForm):
    community_code = forms.ModelChoiceField(
        Community.objects.all()
    )

    class Meta:
        model = Organisation
        fields = ('name', 'description', 'owner', 'community_code')

    def __init__(self, *args, **kwargs):
        super(OrganisationForm, self).__init__(*args, **kwargs)
        if self.instance:
            try:
                community = Community.objects.get(
                    code=self.instance.community_code)
                self.fields['community_code'].initial = community
                self.initial['community_code'] = community
            except Community.DoesNotExist:
                pass

    def clean(self):
        cleaned_data = self.cleaned_data
        community = cleaned_data.get('community_code', None)
        if community:
            cleaned_data['community_code'] = community.code
        return cleaned_data


class UserOrganisationForm(forms.ModelForm):
    class Meta:
        model = UserOrganisation
        fields = ('id', 'user', 'organisation', 'role')
