from django import forms

class PasswordForm(forms.Form):
    password_length = forms.IntegerField()
    qubits_number = forms.IntegerField()
