# Risk reyestri

Bal = ehtimal (1-5) × təsir (1-5). Yüksək: 15+, Orta: 8-14, Aşağı: 7 və aşağı.

| № | Risk | Aktiv | Əvvəl (E×T) | Tədbir | Sonra (E×T) | Status |
|---|---|---|---|---|---|---|
| R1 | Admin parolu brauzer kodunda açıq idi, hər kəs görə bilərdi | CampTrade admin paneli | 5×5 = **25** | Giriş Supabase Auth-a köçürüldü, kodda parol yoxdur | 1×5 = **5** | Düzəldildi |
| R2 | Bazada "allow all" qaydası: hər kəs məhsul və blogu silə/dəyişə bilərdi | CampTrade verilənlər bazası | 5×5 = **25** | Yazma yalnız giriş etmiş admin-ə verildi, qeydiyyat bağlandı | 1×4 = **4** | Düzəldildi |
| R3 | ImgBB açarı kodda açıq, kimsə onunla şəkil yükləyib limiti bitirə bilər | ImgBB hesabı | 4×2 = **8** | Planlanır: açarı yeniləmək, yükləməni serverə köçürmək | 4×2 = **8** | Açıq |
| R4 | Blog mətni `innerHTML` ilə səhifəyə yazılır (XSS). Admin hesabı ələ keçsə zərərli kod yerləşdirilə bilər | CampTrade blog səhifəsi | 3×4 = **12** | Yazma artıq yalnız admin-dədir. Planlanır: mətni təmizləyən kitabxana əlavə etmək | 2×4 = **8** | Qismən azaldılıb |
| R5 | Admin hesabının parolu oğurlanır və ya 2FA yoxdur | Supabase, Netlify, GitHub hesabları | 3×5 = **15** | Uzun unikal parol, 2FA aktiv etmək, qeydiyyatın bağlanması | 2×5 = **10** | Yoxlanılır |
| R6 | Şifrələmə parolunun itməsi, fayl bərpa olunmur | SecureVault parolu | 3×4 = **12** | Parolu parol meneceridə saxlamaq | 1×4 = **4** | Azaldılıb |
| R7 | Supabase secret açarı GitHub-a düşür | SecureVault `.env` | 3×5 = **15** | `.env` `.gitignore`-dadır, `git check-ignore` ilə yoxlanılıb | 1×5 = **5** | Azaldılıb |
| R8 | Bucket təsadüfən public olur | SecureVault `vault` bucket | 2×4 = **8** | Bucket private-dir. Public olsa belə fayl AES-256 ilə şifrəlidir | 1×2 = **2** | Azaldılıb |
| R9 | Sayt məlumatları itir, avtomatik ehtiyat nüsxə yoxdur | CampTrade cədvəlləri | 3×4 = **12** | CSV ilə əl ehtiyat nüsxəsi. Planlanır: müntəzəm export | 2×4 = **8** | Qismən azaldılıb |
| R10 | Köhnə admin parolu Git tarixçəsində qalır | CampTrade GitHub repo | 2×2 = **4** | Köhnə parol artıq işləmir, çünki giriş Supabase-dədir | 1×1 = **1** | Qəbul edilib |

## Nəticə

Ən yüksək risklər (R1, R2, 25 bal) real şəkildə düzəldildi. Qalan açıq riskləri (R3, R4, R5, R9) növbəti dövrdə həll etmək planlanır.