from django import forms
from .models import Kitap

class KitapForm(forms.ModelForm):
    class Meta:
        model = Kitap
        fields = ['baslik', 'yazar', 'kategoriler']
        
        # Etiketleri Türkçeleştirelim
        labels = {
            'baslik': 'Kitap Başlığı',
            'yazar': 'Yazar Seçimi',
            'kategoriler': 'Kategoriler'
        }
        
        # Bootstrap CSS sınıflarını (form-control, form-select) ekleyelim
        widgets = {
            'baslik': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Kitap adını giriniz...'
            }),
            'yazar': forms.Select(attrs={
                'class': 'form-select'
            }),
            'kategoriler': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input' # Checkbox'lar için Bootstrap sınıfı
            }),
        }
