
```markdown
# 📚 Kütüphane Yönetim Sistemi - Django CRUD ve Model İlişkileri

Bu proje, Django web framework'ü kullanılarak **ilişkisel veritabanı mantığını (Bire Bir, Bire Çok, Çoka Çok)** ve temel **CRUD (Create, Read, Update, Delete)** operasyonlarını kavramak amacıyla geliştirilmiş kapsamlı bir eğitim uygulamasıdır.

## 🚀 Özellikler

- **Bire Bir İlişki (OneToOne):** Yazar ve Biyografisi bağlaması.
- **Bire Çok İlişki (ForeignKey):** Bir yazarın birden fazla kitabının olması.
- **Çoka Çok İlişki (ManyToMany):** Bir kitabın birden fazla kategoriye (Roman, Bilim Kurgu vb.) ait olabilmesi.
- **Django ModelForm Entegrasyonu:** Veri ekleme ve güncelleme işlemlerinin güvenli bir şekilde yapılması.
- **Modern Arayüz:** Tüm form ve listeleme sayfaları **Bootstrap 5** kullanılarak responsive (mobil uyumlu) ve şık bir tasarıma kavuşturulmuştur.

## 🛠️ Kullanılan Teknolojiler

- **Backend:** Python, Django
- **Frontend:** HTML5, Bootstrap 5 (CDN)
- **Veritabanı:** SQLite (Django varsayılanı)

## 📸 Ekran Görüntüleri

*(Buraya projenin çalıştığı sayfanın veya daha önce oluşturduğumuz kapak görselinin linkini ekleyebilirsin)*
![Proje Görseli](gorsel-linki-buraya-gelecek.jpg)

## 💻 Kurulum ve Çalıştırma (Local Environment)

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

**1. Projeyi klonlayın:**
```bash
git clone [https://github.com/KULLANICI_ADIN/kutuphane-sistemi.git](https://github.com/KULLANICI_ADIN/kutuphane-sistemi.git)
cd kutuphane-sistemi

```

**2. Sanal ortam (Virtual Environment) oluşturun ve aktifleştirin:**

```bash
# Windows için:
python -m venv env
env\Scripts\activate

# macOS/Linux için:
python3 -m venv env
source env/bin/activate

```

**3. Gerekli paketleri yükleyin:**

```bash
pip install django

```

**4. Veritabanı tablolarını oluşturun (Migration):**

```bash
python manage.py makemigrations
python manage.py migrate

```

**5. Geliştirme sunucusunu başlatın:**

```bash
python manage.py runserver

```

**6. Tarayıcıda görüntüleyin:**
Tarayıcınızı açın ve şu adrese gidin: `http://127.0.0.1:8000/`

---

> **Not:** Bu proje eğitim amaçlıdır. Form işlemleri, veritabanı ilişkileri ve Bootstrap entegrasyonu konularında bir rehber niteliği taşımaktadır.

```

Bu dosya ile projen artık tam anlamıyla bir "Açık Kaynak" portfolyo projesi haline geldi! 

```