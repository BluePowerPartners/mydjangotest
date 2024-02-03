from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field, Div
from crispy_forms.bootstrap import PrependedText, AppendedText

from django.utils.safestring import mark_safe

class Customuserform(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password1'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password2'}))
    class Meta:
        model=User
        fields = ['username','email','password1','password2']



class ApplyLeave(forms.Form):
    GEEKS_CHOICES =( 
    ("WFH", "Work From Home"), 
    ("LV", "Leave") 
) 
    type=forms.ChoiceField(choices = GEEKS_CHOICES)
    wfhdate=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Select Dates'}))
    wfhdate1=forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder':'Select Dates'}))
    selected_date = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'datetimepicker-input','id':'datepicker',
                                                            'data-target':'#datepicker','placeholder':'Pick the multiple dates'}))

    def __init__(self, *args, **kwargs):
        super(ApplyLeave, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class  = 'form-horizontal'
        # self.helper.label_class = 'col-sm-3'
        # self.helper.field_class = 'col-md-6'
        self.helper.layout = Layout(
            Row(
                Column('type', css_class='form-group col-md-6 mb-0')
            ),
            Row(
                Column('wfhdate', css_class='form-group col-md-6 mb-0')
            ),
            Row(
                Column('wfhdate1', css_class='form-group col-md-6 mb-0')
            ),
            Row(Column(
            AppendedText('selected_date',
                mark_safe('<i class="bi bi-calendar"></i>'),
                placeholder='Select a date'
                
            ),css_class='form-group col-md-8 mb-0')),
            Submit('submit', 'Submit')
        )
