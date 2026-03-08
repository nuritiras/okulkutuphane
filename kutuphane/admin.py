from django.contrib import admin
from .models import Yazar, Biyografi, Kategori, Kitap

# 1. Temel Kayıt Yöntemi
# Modelleri en sade haliyle admin paneline ekleriz
admin.site.register(Yazar)
admin.site.register(Biyografi)
admin.site.register(Kategori)

# 2. Özelleştirilmiş Kayıt Yöntemi (Dekoratör ile)
# Kitap modeli daha detaylı olduğu için onu özel bir sınıfla yönetelim
@admin.register(Kitap)
class KitapAdmin(admin.ModelAdmin):
    # Paneldeki listede hangi sütunlar görünsün?
    list_display = ('baslik', 'yazar') 
    
    # Sağ tarafa kategoriye göre filtreleme menüsü ekle
    list_filter = ('kategoriler',)     
    
    # Üst tarafa kitap başlığına göre arama yapabilen bir arama çubuğu ekle
    search_fields = ('baslik',)