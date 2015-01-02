from django.forms import ModelForm
from cart.models import Order
from captcha.fields import CaptchaField


class OrderForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Order
        exclude = ['order_date',
                   'order_confirmed',
                   'order_delivered',
                   'order_products',
                   'order_code',
                   'order_sum']
