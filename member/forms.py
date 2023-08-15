from django import forms 
from member.models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member 
        fields = ['userid', 'password', 'username','work','wdate']
        labels = {'userid':'아이디', 
                  'username':'이름',
                  'password':'패스워드',
                  'work':'분류',
                  'wdate':'생성일'}
