# Website Kementerian Haji dan Umroh Kota Salatiga

Website statis layanan haji Kota Salatiga. HTML, CSS, dan JavaScript tanpa framework, npm, database, atau proses build. Seluruh aset disertakan agar situs bisa dibuka secara offline (tautan ke layanan pusat tetap membutuhkan internet).

## Buka di komputer
1. Ekstrak ZIP.
2. Buka `dist/index.html` dengan Chrome, Edge, atau Firefox.
3. Pilihan lain: dari folder proyek jalankan `python -m http.server 8000 --directory dist`, lalu buka `http://localhost:8000`.

## File yang diedit
- `dist/content.js`: nama instansi, kontak, jam layanan, headline, isi panduan, visi, misi, FAQ, dan tautan pusat.
- `dist/styles.css`: warna, ukuran huruf, jarak, dan tampilan responsif. Warna utama berada pada `:root`.
- `dist/app.js`: komponen header/footer, halaman beranda, tugas dan fungsi, sejarah, kontak, dan interaksi dialog. Cari fungsi `home`, `vision`, `duties`, `history`, atau `contact`.
- `dist/index.html`: halaman Beranda.
- `dist/tugas-dan-fungsi.html`: halaman Tugas dan Fungsi.
- `dist/visi-misi.html`: halaman Visi Misi.
- `dist/sejarah.html`: halaman Sejarah.
- `dist/kontak.html`: halaman Kontak.
- `dist/assets/logo-kemenhaj.png`: logo asli yang diberikan pengguna.
- `dist/assets/hero-haji.png`: ilustrasi hero hasil generasi AI; bukan foto dokumentasi kantor.

## Mengisi kontak
Buka `dist/content.js`, lalu lengkapi objek `contact`:
```
contact: {
  address: 'Alamat resmi kantor',
  phone: 'Nomor telepon resmi',
  whatsapp: '628xxxxxxxxxx',
  email: 'Email resmi',
  mapsUrl: 'https://...'
}
```
WhatsApp memakai kode negara 62. Isi hanya URL HTTPS terpercaya. Tombol WhatsApp dan peta muncul otomatis setelah kolomnya terisi. Data ini ditampilkan secara publik jika website dipublikasikan.

## Deploy sendiri
Tidak ada build command. Folder publik / publish directory: `dist`.

### Hosting cPanel
Unggah **isi** folder `dist` ke `public_html` atau folder domain tujuan. Pastikan `index.html` langsung berada di folder tersebut.

### Hosting website statis
Unggah folder `dist` ke layanan hosting statis yang Anda gunakan. Jika diminta build command, kosongkan. Jika diminta output directory, gunakan `dist`. Semua tautan internal relatif sehingga dapat dipasang di subfolder.

### GitHub Pages
Gunakan isi `dist` sebagai root branch publikasi, atau salin isi `dist` ke folder `docs` dan atur Pages untuk folder tersebut. Tidak memerlukan backend.

## Status fitur
- Lima menu utama sesuai permintaan: Beranda, Tugas dan Fungsi, Visi Misi, Sejarah, Kontak.
- Empat panduan layanan terbuka sebagai dialog, dilengkapi daftar berkas dan accordion ketentuan. Tidak ada checkbox, cetak, atau unduh checklist.
- FAQ bisa diperluas. Menu ponsel dapat dibuka dan ditutup. Dialog mendukung tombol Escape.
- Cek porsi membuka layanan pusat. Tidak mengakses API atau menyimpan nomor porsi.
- Tidak ada reservasi antrean, pengiriman formulir, atau backend aktif.
- Instagram, WhatsApp, email, dan Google Maps memakai tautan dari pengguna. Alamat berupa tautan lokasi. Konten tugas, sejarah, dan misi lokal masih draf untuk pembahasan, bukan rumusan resmi yang disahkan.
- Jadwal: Senin–Kamis 07.30–16.00 WIB; Jumat 07.30–16.30 WIB.
- Kartu Umrah & Haji Khusus dan section Informasi & Edukasi tidak ditampilkan.

## Sebelum digunakan sebagai portal resmi
Ganti naskah profil draf dengan dokumen kantor yang disahkan, verifikasi seluruh persyaratan dan tautan, serta gunakan domain instansi. Top bar dan penanda presentasi di footer telah dihapus. Setiap HTML sengaja memakai meta `noindex,nofollow` untuk prototipe; sesuaikan saat publikasi resmi.

## Referensi desain
https://haji.go.id/profil/visi-misi — header putih, aksen emas, kartu putih, kartu visi emas, dan tipografi sans-serif.

## Membuat ulang ZIP
Jalankan `python3 package-source.py` dari folder proyek setelah mengedit. Paket ZIP akan diperbarui; tautan source code tidak ditampilkan di footer website. ZIP tidak membawa token, Git, atau konfigurasi akun hosting.

## Validasi yang dilakukan
Pemeriksaan sintaks JavaScript, file halaman/aset, navigasi desktop, empat panduan, accordion ketentuan, penghapusan checkbox/tombol, dan tautan kontak melalui browser. CSS memiliki breakpoint ponsel dan tablet; pengujian perangkat fisik tetap dianjurkan sebelum rilis resmi.

## Pembaruan layanan
Persyaratan pendaftaran mengikuti isi situs simulasi milik pengguna: https://simulasi-haji-reguler-salatiga.lacynook8.chatgpt.site/ (source commit 4286f7106412ee809cc14fd957a8e6ec8376246c). Dokumen kependudukan dibedakan dari berkas setelah proses bank.

Ketentuan pendaftaran dan pelimpahan dicocokkan dengan PMHU 6 Tahun 2026 yang diberikan pengguna. Pembatalan mengacu PMHU 3 Tahun 2025 Pasal 14–19; mutasi embarkasi Pasal 64. Daftar mutasi tetap diberi penjelasan sebagai berkas persiapan awal karena kebutuhan administrasi disesuaikan dengan alasan dan kantor asal/tujuan.

Referensi teks PMHU 3: https://peraturan.go.id/files/permen-haji-umrah-no-3-tahun-2025.pdf ; salinan teks pembanding https://pasal.id/peraturan/permen/permen-haji-umrah-no-3-tahun-2025 .
