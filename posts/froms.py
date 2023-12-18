from django import forms


class AddPost(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea())
    category = forms.ChoiceField(choices={(0, 'sport'),
                                          (1, 'beauty'),
                                          (2, 'health'),
                                          })
