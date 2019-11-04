from django.forms import Form, ModelForm

from agent.models import Customer


class AgentForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ['deleted']
