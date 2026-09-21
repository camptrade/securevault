| № | Yoxlama | Əvvəl | Sonra | Qeyd |
|---|---|---|---|---|
| 1 | Kodda secret açar | Yaxşı | Yaxşı | Kodda yalnız `anon` açarı var (yoxlanılıb). ImgBB açarı kodda açıq qalır (risk reyestrində) |
| 2 | Admin parolunun yoxlanması | Problem | Düzəldildi | Parol koddan silindi, giriş Supabase Auth ilə serverdə yoxlanılır |
| 3 | Supabase RLS | Yaxşı | Yaxşı | blogs və products cədvəllərində aktivdir |
| 4 | Yazma icazələri | Problem | Düzəldildi | "allow all" silindi. Oxumaq hamıya, yazmaq yalnız giriş etmiş admin-ə. Giriş etməmiş sorğu 401 ilə bloklandı |
| 5 | Storage bucket-lər | Yaxşı | Yaxşı | Supabase Storage istifadə olunmur, şəkillər ImgBB-dədir |
| 6 | HTTPS | Yaxşı | Yaxşı | Netlify avtomatik HTTPS verir |
| 7 | Ehtiyat nüsxə | Bilmirəm | Əla | Cədvəllər CSV kimi endirilib. Avtomatik ehtiyat nüsxə yoxdur |