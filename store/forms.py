from django.forms import ModelForm
from store.models import Comment
from captcha.fields import CaptchaField


class CommentForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = ['comment_text']