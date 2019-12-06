from django.forms import ModelForm
from .models import Project, Message

class MessageModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].label = ''
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Leave your comment here please', 'id':'typefield', 'style': 'font-size: 18px;font-family: Arial, Helvetica, sans-serif;'})

    class Meta:
        model = Message
        fields = ['message']

class PostModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Name of the project',})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email for contacting you',})
        self.fields['details'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Small description of the model',})
        self.fields['image'].widget.attrs.update({'class': 'form-control',})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Leave a brief description of your project here please',})
    
    class Meta:
        model = Project
        fields = ('name','email','details', 'image','description')