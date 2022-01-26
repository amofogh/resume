from django import forms


class contact_us_form(forms.Form):
    name = forms.CharField(max_length=100, required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی', 'class': 'form-control'}))
    email = forms.EmailField(max_length=150, required=True,
                             widget=forms.EmailInput(attrs={'placeholder': 'ایمیل', 'class': 'form-control'}))
    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'متن پیام', 'class': 'form-control', 'rows': '4'}))
