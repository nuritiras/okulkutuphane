from django.shortcuts import render, redirect, get_object_or_404
from .forms import KitapForm
from .models import Kitap

# CREATE: Yeni Kitap Ekleme
def kitap_ekle(request):
    if request.method == 'POST':
        form = KitapForm(request.POST)
        if form.is_valid(): # Veriler kurallara uygun mu?
            form.save() # Hem kitabı hem de çoklu ilişkileri otomatik kaydeder!
            return redirect('kitap_listesi') # Başarılıysa yönlendir
    else:
        # GET isteği ise boş form göster
        form = KitapForm()
    
    return render(request, 'kutuphane/kitap_form.html', {'form': form})

# UPDATE: Mevcut Kitabı Güncelleme
def kitap_duzenle(request, kitap_id):
    # İlgili kitabı bul, yoksa 404 hatası ver
    kitap = get_object_or_404(Kitap, id=kitap_id)
    
    # instance=kitap diyerek formun içinin dolu gelmesini sağlıyoruz
    if request.method == 'POST':
        form = KitapForm(request.POST, instance=kitap)
        if form.is_valid():
            form.save()
            return redirect('kitap_listesi')
    else:
        form = KitapForm(instance=kitap)
        
    return render(request, 'kutuphane/kitap_form.html', {'form': form})

# READ: Kitapları Listeleme (Ana Sayfa)
def kitap_listesi(request):
    # Veritabanındaki tüm kitapları çekiyoruz
    kitaplar = Kitap.objects.all()
    return render(request, 'kutuphane/kitap_listesi.html', {'kitaplar': kitaplar})

# DELETE: Kitap Silme İşlemi
def kitap_sil(request, kitap_id):
    kitap = get_object_or_404(Kitap, id=kitap_id)
    
    # Silme işlemi her zaman güvenlik için POST isteği ile yapılmalıdır!
    if request.method == 'POST':
        kitap.delete()
        return redirect('kitap_listesi')
        
    # GET isteği gelirse onay sayfasını göster
    return render(request, 'kutuphane/kitap_sil_onay.html', {'kitap': kitap})