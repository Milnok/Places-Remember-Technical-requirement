from django import forms
from .models import Place


class PlaceForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(attrs={
                                "class": "form-control",
                                "placeholder": "Введите название места",
                                'style': 'font-size: 30px',
                            }))
    discription = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                'rows': '4',
                'style': 'font-size: 30px',
            }
        )
    )

    class Meta:
        model = Place
        fields = ('title', 'discription')
