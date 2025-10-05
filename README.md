# TUGAS 2 - PENGOLAHAN CITRA DIGITAL

**Nama:** Jhosua Armando Putra Panjaitan  
**NIM:** 2305541067  
**Mata Kuliah:** Pengolahan Citra Digital

## Deskripsi Tugas

Implementasi operasi-operasi dasar pengolahan citra:

1. **Operasi Pengurangan Citra** (Image Subtraction)
2. **Operasi Blending Citra** (Image Blending)
3. **Operasi Boolean** (AND, OR, XOR, NOT)
4. **Motion Detection** (Bonus)

## Struktur Project

### 📁 Source Code (Python)

```
├── main_program.py              # Program utama dengan menu
├── operasi_pengurangan.py       # Modul pengurangan citra
├── operasi_blending.py          # Modul blending citra
├── operasi_boolean.py           # Modul operasi boolean
├── motion_detection.py          # Modul motion detection
├── input_output.py              # Modul I/O dan visualisasi
└── requirements.txt             # Dependencies
```

### 📂 Output Results (33 files total)

```
hasil_pengolahan/
├── 1_pengurangan_citra/    (9 files)  - |A-B|, konstanta 100, konstanta 150
├── 2_operasi_boolean/      (12 files) - AND, OR, XOR, NOT
├── 3_motion_detection/     (3 files)  - Frame differencing
└── 4_blending_citra/       (9 files)  - α=0.3, 0.5, 0.7
```

### 📄 Documentation

- `LAPORAN_TUGAS2_PCD_SIMPLE.md` - Laporan lengkap dengan analisis

## Cara Menjalankan

### 🚀 Setup Environment

1. **Clone atau download project**

   ```bash
   cd "path/to/project/folder"
   ```

2. **Buat virtual environment (opsional tapi disarankan)**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # atau
   source .venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### ▶️ Menjalankan Program

1. **Jalankan program utama**

   ```bash
   python main_program.py
   ```

2. **Pilih operasi dari menu**
   ```
   📋 PILIH OPERASI:
   1. Operasi Pengurangan Citra
   2. Operasi Blending Citra
   3. Operasi Boolean (AND, OR, XOR, NOT)
   4. Motion Detection
   5. Demo Lengkap (Semua Operasi)
   6. Keluar
   ```

### 📖 Panduan Penggunaan

#### **Operasi 1: Pengurangan Citra**

- Pilih menu **1**
- Pilih sumber gambar:
  - **1** = Gunakan gambar sample built-in (direkomendasikan)
  - **2** = Upload gambar dari file
  - **3** = Buat gambar sintetis
- Program akan melakukan 3 operasi:
  - `|A - B|` (pengurangan absolut)
  - `(A - B) + 100` (dengan konstanta 100)
  - `(A - B) + 150` (dengan konstanta 150)
- Hasil disimpan di: `hasil_pengolahan/1_pengurangan_citra/`

#### **Operasi 2: Blending Citra**

- Pilih menu **2**
- Program otomatis menggunakan gambar sample
- Melakukan blending dengan 3 nilai alpha:
  - α=0.3 (30% A + 70% B)
  - α=0.5 (50% A + 50% B)
  - α=0.7 (70% A + 30% B)
- Hasil disimpan di: `hasil_pengolahan/4_blending_citra/`

#### **Operasi 3: Boolean**

- Pilih menu **3**
- Pilih sumber gambar seperti operasi 1
- Program melakukan 4 operasi boolean:
  - **AND** (irisan)
  - **OR** (gabungan)
  - **XOR** (perbedaan eksklusif)
  - **NOT** (inversi)
- Hasil disimpan di: `hasil_pengolahan/2_operasi_boolean/`

#### **Operasi 4: Motion Detection**

- Pilih menu **4**
- Program membuat frame sintetis secara otomatis
- Mendeteksi pergerakan menggunakan frame differencing
- Hasil disimpan di: `hasil_pengolahan/3_motion_detection/`

#### **Demo Lengkap (Disarankan)**

- Pilih menu **5**
- Program menjalankan semua operasi secara otomatis
- Menghasilkan 33 file dalam 4 kategori folder
- Total waktu eksekusi: ~10-15 detik

### 📁 Hasil Output

Setiap operasi menghasilkan 3 file per hasil:

- `*_comparison.jpg` - Perbandingan visual dengan statistik
- `*_original.jpg` - Gambar asli
- `*_result.jpg` - Gambar hasil operasi

**Total output: 33 files dalam struktur terorganisir**

### 🔧 Troubleshooting

**Error: ModuleNotFoundError**

```bash
pip install opencv-python numpy matplotlib scikit-image
```

**Error: Permission denied**

- Pastikan folder tidak read-only
- Jalankan terminal sebagai administrator

**Program tidak merespons**

- Tekan `Ctrl+C` untuk menghentikan
- Restart dan coba lagi

**Gambar tidak muncul**

- Install backend matplotlib: `pip install tkinter`
- Atau gunakan mode headless (file tetap tersimpan)

## Features

- ✅ **Modular Architecture** - Code terorganisir dalam 5 modul terpisah
- ✅ **Auto File Organization** - Output otomatis tersimpan dalam folder berkategori
- ✅ **Statistical Analysis** - Analisis kuantitatif untuk setiap operasi
- ✅ **Visual Comparison** - Side-by-side comparison dengan statistik
- ✅ **Error Handling** - Penanganan error yang robust
- ✅ **Sample Images** - Built-in sample images untuk testing
- ✅ **Multiple Input Sources** - File upload, sample, atau synthetic images
- ✅ **Comprehensive Documentation** - Laporan lengkap dan README detail

## Penjelasan Teknis

### 🔬 Algoritma yang Diimplementasikan

#### **1. Operasi Pengurangan Citra**

```python
# Pengurangan Absolut
result = |A - B|

# Dengan Konstanta
result = (A - B) + konstanta
```

- **Tujuan:** Change detection, background subtraction
- **Output:** Highlight perbedaan struktural antar citra
- **Aplikasi:** Motion detection, medical imaging, surveillance

#### **2. Operasi Blending**

```python
# Linear Combination
result = α × A + (1-α) × B
```

- **Parameter α:** 0.0-1.0 (blend factor)
- **Tujuan:** Image morphing, artistic effects, watermarking
- **Keunggulan:** Smooth transition, mathematical precision

#### **3. Operasi Boolean**

```python
AND: pixel = A & B      # Irisan (intersection)
OR:  pixel = A | B      # Gabungan (union)
XOR: pixel = A ^ B      # Perbedaan eksklusif
NOT: pixel = ~A         # Inversi (complement)
```

- **Input:** Binary images (0/255)
- **Tujuan:** Segmentasi, masking, region extraction
- **Validasi:** OR - AND = XOR (set theory)

#### **4. Motion Detection**

```python
# Frame Differencing
diff = |frame1 - frame2|

# Thresholding
binary = diff > threshold

# Morphological Cleanup
cleaned = opening(closing(binary))
```

- **Pipeline:** Differencing → Thresholding → Morphological operations
- **Output:** Binary mask menunjukkan area pergerakan

### 📊 Struktur Data Output

Setiap operasi menghasilkan struktur data konsisten:

```python
{
    'image': numpy_array,           # Hasil operasi
    'title': 'Deskripsi Operasi',  # Judul untuk visualisasi
    'stats': {                     # Statistik kuantitatif
        'Mean': float,
        'Std Dev': float,
        'Max': int,
        'Min': int,
        # ... statistik spesifik operasi
    }
}
```

### 🎯 Use Cases dan Aplikasi

| Operasi              | Use Case                                 | Domain Aplikasi                                           |
| -------------------- | ---------------------------------------- | --------------------------------------------------------- |
| **Pengurangan**      | Change detection, Background subtraction | Medical imaging, Surveillance, Satellite imagery          |
| **Blending**         | Image morphing, Artistic composition     | Digital art, Film VFX, UI/UX design                       |
| **Boolean**          | Object segmentation, Region extraction   | Computer vision, Medical analysis, Quality control        |
| **Motion Detection** | Movement tracking, Security monitoring   | Surveillance systems, Sports analysis, Traffic monitoring |

### 🔍 Contoh Workflow

```bash
# 1. Setup environment
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt

# 2. Run demo lengkap (recommended)
python main_program.py
# Pilih: 5. Demo Lengkap (Semua Operasi)

# 3. Check results
ls hasil_pengolahan/
# Output: 4 folders dengan 33 files total

# 4. Analyze results
# Buka file *_comparison.jpg untuk melihat perbandingan visual
# Baca LAPORAN_TUGAS2_PCD_SIMPLE.md untuk analisis detail
```

## Technologies Used

### 🐍 **Python 3.13+**

- **Platform:** Cross-platform (Windows, Linux, macOS)
- **Minimum:** Python 3.8+
- **Recommended:** Python 3.13+ untuk performa optimal

### 📚 **Dependencies**

| Library          | Version                | Purpose                                     |
| ---------------- | ---------------------- | ------------------------------------------- |
| **OpenCV**       | `opencv-python>=4.8.0` | Core image processing operations            |
| **NumPy**        | `numpy>=1.24.0`        | Numerical computations dan array operations |
| **Matplotlib**   | `matplotlib>=3.7.0`    | Visualization dan plotting                  |
| **Scikit-image** | `scikit-image>=0.21.0` | Sample images dan additional tools          |

### 💾 **System Requirements**

**Minimum:**

- RAM: 4GB
- Storage: 50MB free space
- CPU: Any modern processor
- GPU: Not required (CPU-only)

**Recommended:**

- RAM: 8GB+ (untuk processing gambar besar)
- Storage: 100MB+ (untuk output files)
- CPU: Multi-core processor
- Display: 1920x1080+ (untuk visualisasi optimal)

### 🔧 **Installation Methods**

**Method 1: pip install (Standard)**

```bash
pip install opencv-python numpy matplotlib scikit-image
```

**Method 2: conda install (Anaconda users)**

```bash
conda install opencv numpy matplotlib scikit-image
```

**Method 3: requirements.txt (Project)**

```bash
pip install -r requirements.txt
```

### 🌟 **Advanced Features**

#### **Performance Optimization**

- **Vectorized Operations:** Menggunakan NumPy untuk operasi array yang cepat
- **Memory Management:** Efficient memory usage untuk gambar besar
- **Batch Processing:** Demo lengkap memproses multiple operations secara otomatis

#### **Error Handling**

- **Input Validation:** Validasi format dan ukuran gambar
- **File I/O Safety:** Penanganan error file tidak ditemukan atau permission denied
- **Graceful Degradation:** Program tetap berjalan meski ada error minor

#### **Extensibility**

- **Modular Design:** Mudah menambah operasi baru
- **Plugin Architecture:** Setiap operasi dalam modul terpisah
- **Configurable Output:** Folder dan naming conventions dapat disesuaikan

---

## 📋 **Project Summary**

| Aspect             | Details                                   |
| ------------------ | ----------------------------------------- |
| **Total Files**    | 44 files (11 source + 33 results)         |
| **Code Lines**     | ~1000+ lines across 5 modules             |
| **Operations**     | 4 major operations + statistical analysis |
| **Output Formats** | JPG images dengan comparison views        |
| **Documentation**  | README + Comprehensive report             |
| **Test Coverage**  | All operations tested dengan sample data  |

## 🎯 **Learning Outcomes**

✅ **Pemahaman Konsep:** Operasi fundamental pengolahan citra  
✅ **Implementasi:** Python programming dengan library image processing  
✅ **Modular Design:** Clean code architecture dan separation of concerns  
✅ **Data Analysis:** Statistical analysis dan quantitative evaluation  
✅ **Visualization:** Effective presentation of results  
✅ **Documentation:** Technical writing dan project documentation

## 🚀 **Future Enhancements**

Potential improvements untuk development selanjutnya:

- [ ] GUI interface menggunakan tkinter atau PyQt
- [ ] Real-time processing untuk webcam input
- [ ] Batch processing untuk multiple files
- [ ] Advanced filtering operations (Gaussian, Sobel, etc.)
- [ ] Performance benchmarking dan optimization
- [ ] Export ke format video (untuk motion detection)

---

**Developer:** Jhosua Armando Putra Panjaitan
