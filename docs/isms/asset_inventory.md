# Aktiv reyestri (Asset Inventory)

| № | Aktiv | Harada durur | Həssaslıq | Niyə vacibdir |
|---|---|---|---|---|
| 1 | Müştəri siyahısı (demo fayl) | Kompüter, buludda şifrəli | Yüksək | Şəxsi məlumat ehtiva edir |
| 2 | Şifrələmə parolu | İstifadəçinin yaddaşı / parol meneceri | Çox yüksək | İtərsə fayl bərpa olunmur, sızarsa fayl açılır |
| 3 | Supabase secret açarı | `.env` faylı | Çox yüksək | Bucket-ə tam giriş verir |
| 4 | Supabase hesabı | Bulud | Yüksək | Bütün buluddakı fayllara giriş |
| 5 | Buluddakı şifrəli fayllar | Supabase Storage (`vault`) | Orta | Şifrəlidir, amma silinərsə itki olar |
| 6 | Mənbə kod | GitHub | Orta | Kodun itməsi və ya dəyişdirilməsi |
| 7 | GitHub hesabı | Bulud | Orta | Kodu dəyişdirmək mümkün olar |
| 8 | CampTrade admin paneli | Netlify | Yüksək | Saytın məhsullarını idarə edir, yalnız parolla qorunur |
| 9 | Trello board | Bulud | Aşağı | Layihə planı |