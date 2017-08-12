# coding=utf-8
from django import forms
from myapp.models import Book,Author

TOPIC_CHOICES= (('level1','好评'),('level2','中评'),('level3','差评'))


class RemarkForm(forms.Form):
    subject = forms.CharField(max_length = 100,label = '标题')
    mail = forms.EmailField(label = '邮件')
    topic = forms.ChoiceField(choices = TOPIC_CHOICES,label = '评价')
    message = forms.CharField(label = '内容',widget = forms.Textarea)
    cc_myself = forms.BooleanField(required = False,label = '订阅')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book  #直接使用models中的类book，
        fields = ('title','author','publisher')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        labels = {
            'first_name':'名字',
            'last_name':'姓',
            'email':'邮箱',
        }
