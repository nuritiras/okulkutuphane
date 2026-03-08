from django.db import models

class Yazar(models.Model):
    isim = models.CharField(max_length=100)

    def __str__(self):
        return self.isim

class Biyografi(models.Model):
    yazar = models.OneToOneField(Yazar, on_delete=models.CASCADE)
    detay = models.TextField()

# Kategori modelini Kitap'tan önce tanımlıyoruz ki Kitap onu tanıyabilsin
class Kategori(models.Model):
    isim = models.CharField(max_length=50)

    def __str__(self):
        return self.isim

class Kitap(models.Model):
    baslik = models.CharField(max_length=100)
    yazar = models.ForeignKey(Yazar, on_delete=models.CASCADE, related_name='kitaplar')
    
    # Çoka Çok ilişkiyi Kitap modeline taşıdık!
    kategoriler = models.ManyToManyField(Kategori, related_name='kitaplar')

    def __str__(self):
        return self.baslik