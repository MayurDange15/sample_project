from django import forms
from first_app.models import Seq

# Default form for this application
class HomeForm(forms.Form):
    # input field for this form
    post = forms.CharField()
