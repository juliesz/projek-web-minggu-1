# SIMANTAP — QA & Application Discovery Documentation Hub

Selamat datang di repositori dokumentasi **Application Discovery, Reverse Engineering, dan Quality Assurance (QA) Baseline** untuk sistem aplikasi **SIMANTAP (Sistem Informasi Manajemen & Transaksi Pertanian)**.

Dokumentasi ini disusun secara adaptif dan terstruktur berdasarkan kondisi aktual kode sumber, basis data MySQL (`simantap2_db`), serta antarmuka visual yang beroperasi pada server lokal, mengikuti kaidah skill `application-discovery-qa-documentation`.

---

## 📁 Struktur Direktori Folder QA

```text
QA/
├── data/
│   └── discovery.json                           # Metadata penemuan sistem terstruktur (JSON format)
├── diagrams/
│   ├── architecture.mmd                         # Diagram arsitektur MVC, Middleware, dan Database Tier
│   ├── user-journey.mmd                         # Pemetaan perjalanan pengguna lintas role
│   ├── order-checkout-process.mmd               # Alur proses belanja, ongkir Haversine, & submit order
│   ├── kasir-verification-flow.mmd              # Alur verifikasi bukti bayar & update status kasir
│   ├── password-reset-workflow.mmd              # Alur permohonan & resolusi reset kata sandi
│   └── erd.mmd                                  # Entity Relationship Diagram (8 tabel database relasional)
├── documents/
│   ├── SIMANTAP_Application_Discovery_Report.docx   # Laporan lengkap penemuan sistem & screenshot tersemat
│   ├── SIMANTAP_Functional_Specification.docx       # Spesifikasi kebutuhan fungsional & aturan validasi
│   └── SIMANTAP_QA_Requirement_Specification.docx   # Spesifikasi kebutuhan pengujian & handover QA
├── screenshots/
│   ├── PAGE_PUB_01_HOME.png                     # Tangkapan layar katalog beranda publik
│   ├── PAGE_PUB_02_LOGIN.png                    # Tangkapan layar formulir login multi-role
│   ├── PAGE_PUB_03_REGISTER.png                 # Tangkapan layar registrasi pelanggan
│   ├── PAGE_PUB_04_FORGOT_PASSWORD.png          # Tangkapan layar form pengajuan lupa password
│   ├── PAGE_PUB_05_CHECKOUT.png                 # Tangkapan layar form checkout & koordinat
│   ├── PAGE_PUB_06_PAYMENT.png                  # Tangkapan layar instruksi pembayaran & upload bukti
│   ├── PAGE_PUB_07_MY_ORDERS.png                # Tangkapan layar pelacakan pesanan saya
│   ├── PAGE_KAS_01_DASHBOARD.png                # Tangkapan layar dashboard operasional kasir
│   ├── PAGE_KAS_02_PESANAN.png                  # Tangkapan layar daftar pesanan masuk kasir
│   ├── PAGE_KAS_03_RIWAYAT.png                  # Tangkapan layar buku riwayat transaksi kasir
│   ├── PAGE_ADM_01_DASHBOARD.png                # Tangkapan layar dashboard finansial & stok admin
│   ├── PAGE_ADM_02_PRODUK.png                   # Tangkapan layar manajemen produk & foto
│   ├── PAGE_ADM_03_SUPPLIER.png                 # Tangkapan layar manajemen data supplier
│   ├── PAGE_ADM_04_PEMBELIAN.png                # Tangkapan layar pencatatan pembelian supplier (restock)
│   ├── PAGE_ADM_05_PENGGUNA.png                 # Tangkapan layar manajemen pengguna & hak akses
│   ├── PAGE_ADM_06_TRANSAKSI.png                # Tangkapan layar audit transaksi penjualan admin
│   ├── PAGE_ADM_07_LAPORAN.png                  # Tangkapan layar buku kas keuangan & ekspor PDF
│   └── PAGE_ADM_08_PASSWORD_REQUEST.png         # Tangkapan layar manajemen tiket reset password
├── scripts/
│   └── capture_screens.py                       # Skrip otomatisasi Playwright untuk capture screenshot
├── spreadsheets/
│   ├── SIMANTAP_Feature_Inventory.xlsx          # Inventaris lengkap 38 fitur dengan input, proses, & output
│   ├── SIMANTAP_Role_Permission_Matrix.xlsx     # Matriks otorisasi hak akses (Public, Pelanggan, Kasir, Admin)
│   ├── SIMANTAP_QA_Test_Scenarios.xlsx          # 38 skenario uji positif, negatif, batas, dan keamanan
│   └── SIMANTAP_Data_Dictionary.xlsx            # Kamus data lengkap 8 tabel database MySQL
├── skill-application-discovery-qa-documentation.md
├── skill-QA Engineer.md
└── README.md                                    # Panduan dan indeks dokumen (berkas ini)
```

---

## 📌 Ringkasan Eksekutif Hasil Discovery

| Atribut Proyek | Informasi Aktual Terverifikasi |
| :--- | :--- |
| **Nama Aplikasi** | SIMANTAP (Sistem Informasi Manajemen & Transaksi Pertanian) |
| **Kategori Sistem** | Point of Sale (POS), Inventory & E-Commerce Web Application |
| **Teknologi Utama** | Laravel 11.x, PHP 8.3/8.5, MySQL (`simantap2_db`), Tailwind CSS, DomPDF |
| **Model Hak Akses** | 3 Peran: `pelanggan` (Customer), `kasir` (Cashier), `admin` (Administrator) |
| **Jumlah Modul** | 8 Modul Fungsional |
| **Jumlah Halaman** | 19 Halaman UI Unik |
| **Jumlah Fitur Terverifikasi** | 38 Fitur Utama Teruji |
| **Jumlah Tabel Database** | 8 Tabel Utama dengan Integritas Foreign Key Relasional |
| **Lingkungan Uji** | Local Server (`http://127.0.0.1:8000`) |

---

## 🔄 Matriks Keterlacakan (Traceability Matrix)

Alur keterlacakan menghubungkan seluruh artefak penemuan ke pengujian:

$$\text{Project} \longrightarrow \text{Module} \longrightarrow \text{Page} \longrightarrow \text{Feature} \longrightarrow \text{QA Requirement} \longrightarrow \text{Test Scenario} \longrightarrow \text{Screenshot Evidence}$$

| Modul | Halaman Utama | Fitur Kunci | QA Requirement | Skenario Uji | Bukti Screenshot |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **MOD_01: E-Commerce** | `/`, `/checkout`, `/orders/payment` | FEAT_001 s/d FEAT_008 | REQ_001 s/d REQ_008 | TC_001 s/d TC_008 | `PAGE_PUB_01` s/d `PAGE_PUB_07` |
| **MOD_02: Autentikasi** | `/login`, `/register`, `/forgot-password` | FEAT_009 s/d FEAT_012 | REQ_009 s/d REQ_012 | TC_009 s/d TC_015 | `PAGE_PUB_02` s/d `PAGE_PUB_04` |
| **MOD_03: Kasir POS** | `/kasir/dashboard`, `/kasir/pesanan`, `/kasir/riwayat` | FEAT_013 s/d FEAT_019 | REQ_013 s/d REQ_019 | TC_016 s/d TC_021 | `PAGE_KAS_01` s/d `PAGE_KAS_03` |
| **MOD_04: Master Data** | `/admin/dashboard`, `/admin/produk`, `/admin/supplier` | FEAT_020 s/d FEAT_028 | REQ_020 s/d REQ_028 | TC_022 s/d TC_027 | `PAGE_ADM_01` s/d `PAGE_ADM_03` |
| **MOD_05: Pembelian** | `/admin/pembelian` | FEAT_029, FEAT_030 | REQ_029, REQ_030 | TC_028 | `PAGE_ADM_04` |
| **MOD_06: Transaksi** | `/admin/transaksi` | FEAT_031, FEAT_032 | REQ_031, REQ_032 | TC_031 | `PAGE_ADM_06` |
| **MOD_07: Keuangan** | `/admin/laporan`, `/admin/laporan/export/pdf` | FEAT_033 s/d FEAT_036 | REQ_033 s/d REQ_036 | TC_029 s/d TC_031 | `PAGE_ADM_07` |
| **MOD_08: Akun & Tiket**| `/admin/pengguna`, `/admin/password-request` | FEAT_037, FEAT_038 | REQ_037, REQ_038 | TC_032 s/d TC_034 | `PAGE_ADM_05`, `PAGE_ADM_08` |
| **Security & RBAC** | Seluruh Route Tertutup (`role:admin`, `role:kasir,admin`) | RBAC Isolation | REQ_SEC_01 s/d 04 | TC_035 s/d TC_038 | Flash redirect & HTTP 403 |

---

## 🚀 Panduan Serah Terima (Handover to QA Automation)

Dokumentasi ini siap digunakan oleh **Website QA Automation Architect** (`skill-QA Engineer.md`):

1. **Jalankan Aplikasi Target**: Pastikan web server aktif pada port 8000 (`php artisan serve --port=8000`) dan database MySQL aktif di Laragon.
2. **Gunakan Baseline Skenario**: Buka berkas `QA/spreadsheets/SIMANTAP_QA_Test_Scenarios.xlsx` untuk mengeksekusi test case `TC_001` hingga `TC_038`.
3. **Akun Pengujian Terverifikasi**:
   - **Administrator**: `username: admin` | `role: admin`
   - **Kasir**: `username: kasir` | `role: kasir`
   - **Pelanggan**: `username: Canny@gmail.com` | `role: pelanggan`
4. **Pustaka Otomasi**: Menggunakan Playwright Chromium (`QA/scripts/capture_screens.py` dapat dikembangkan lebih lanjut untuk assertion otomatis).
