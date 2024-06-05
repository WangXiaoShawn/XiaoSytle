from django import forms
from .models import Account, UserProfile


class RegistrationForm(forms.ModelForm): # 表单里的字段自动映射到模型里的字段
    #forms.CharField 是一个字符字段，用于表示文本输入。
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control', #class 添加CSS类名，使其符合Bootstrap样式。
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = Account #model = Account： 表单基于 Account 模型。
        #表单包含并仅包含 Account 模型中的这些字段。
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def clean(self):#clean 方法是 Django 表单类中的一个特殊方法，它允许你在表单的字段验证完成之后进行额外的验证。
        cleaned_data = super(RegistrationForm, self).clean()#这行代码调用了父类的 clean 方法，获取所有已经通过字段验证的数据。
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)#确保父类的初始化过程得以执行。这一步很重要，因为它设置了表单字段及其初始值。
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name' #在Django表单中，widget.attrs 是一个用于设置表单字段HTML属性的字典。
        #通过 widget.attrs，你可以为表单字段添加或修改各种HTML属性，例如 placeholder、class、id、style 等。这些属性将在表单渲染为HTML时应用到对应的HTML标签上，从而影响表单字段的外观和行为。
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last Name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        for field in self.fields:#这段代码的目的是为表单中的每个字段统一添加一个CSS类form-control。这种做法常用于使用前端框架（如Bootstrap）时，以确保表单字段的样式一致。让我们详细解释这段代码的意义和作用。
            self.fields[field].widget.attrs['class'] = 'form-control'


class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone_number')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)
    class Meta:
        model = UserProfile
        fields = ('address_line_1', 'address_line_2', 'city', 'state', 'country', 'profile_picture')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
