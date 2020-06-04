from django import forms


class PivotForm(forms.Form):
    stock_items_id = forms.IntegerField(required = True, disabled = True, show_hidden_initial = True)
    prev_closing_price = forms.CharField(label = '전일 종가', required = True)
    prev_high_price = forms.IntegerField(label = '전일 고가(↑)', required = True)
    prev_low_price = forms.IntegerField(label = '전일 저가(↓)', required = True)
