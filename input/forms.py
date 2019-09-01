'''from django import forms
from input.models import Good
from import_export.forms import ImportForm, ConfirmImportForm

class GoodImportForm(ImportForm):
    good = forms.ModelChoiceField(
        queryset=Good.objects.all(),
        required=True)
		
class GoodConfirmImportForm(ConfirmImportForm):
    good = forms.ModelChoiceField(
        queryset=Good.objects.all(),
        required=True)'''