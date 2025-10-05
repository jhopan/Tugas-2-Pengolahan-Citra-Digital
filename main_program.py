"""
PROGRAM UTAMA - Pengolahan Citra     print("📋 PILIH OPERASI:")
    print("1. Operasi Pengurangan Citra")
    print("2. Operasi Blending Citra")
    print("3. Operasi Boolean (AND & OR)")
    print("4. Motion Detection"        for nama_operasi in operasi_list:
            if nama_operasi in hasil_boolean:
                data = hasil_boolean[nama_operasi]
                kategori_nama = f"3_boolean_{nama_operasi}" if nama_operasi == 'and' else f"4_boolean_{nama_operasi}"
                simpan_perbandingan_dengan_stats(
                    hasil_boolean['binary1']['image'], 
                    data['image'],
                    f"demo_{nama_operasi}",
                    "Demo Binary A",
                    data['title'],
                    stats_binary,
                    data['stats'],
                    kategori_nama
                )"5. Demo Lengkap (Semua Operasi)")
    print("6. Keluar")
    print("-"*60)
Tugas 2: Operasi Pengurangan Citra dan Boolean

Nama: Jhosua Armando Putra Panjaitan
NIM: 2305541067

STRUKTUR MODULAR:
├── operasi_pengurangan.py - Operasi pengurangan citra
├── operasi_boolean.py     - Operasi boolean
├── motion_detection.py    - Deteksi pergerakan
├── input_output.py        - Input/Output & visualisasi
└── main_program.py        - Program utama (file ini)
"""

# Import semua modul yang sudah dipisah
from operasi_pengurangan import demo_pengurangan_citra, hitung_statistik_dasar
from operasi_boolean import demo_operasi_boolean, hitung_statistik_biner
from operasi_blending import OperasiBlending
from motion_detection import demo_motion_detection
from input_output import (
    pilih_input_gambar, 
    simpan_perbandingan_dengan_stats,
    hitung_total_file_output,
    muat_gambar_sample
)

def tampilkan_header():
    """Menampilkan header program"""
    print("\n" + "="*60)
    print("🎯 PENGOLAHAN CITRA DIGITAL - TUGAS 2 (MODULAR)")
    print("   Operasi: Pengurangan, Blending, Boolean AND & OR")
    print("   Nama: Jhosua Armando Putra Panjaitan")
    print("   NIM: 2305541067")
    print("="*60)

def tampilkan_menu_utama():
    """Menampilkan menu utama"""
    print("\n📋 PILIH OPERASI:")
    print("1. Operasi Pengurangan Citra")
    print("2. Operasi Blending Citra")
    print("3. Operasi Boolean (AND, OR, XOR, NOT)")
    print("4. Motion Detection")
    print("5. Demo Lengkap (Semua Operasi)")
    print("6. Keluar")
    print("-"*60)

def proses_pengurangan_citra():
    """Memproses operasi pengurangan citra"""
    print("\n🔄 OPERASI PENGURANGAN CITRA")
    
    # Pilih input gambar
    img1, img2 = pilih_input_gambar()
    if img1 is None or img2 is None:
        print("❌ Operasi dibatalkan")
        return
    
    # Statistik gambar asli
    stats_asli = hitung_statistik_dasar(img1)
    
    # Demo operasi pengurangan
    hasil_operasi = demo_pengurangan_citra(img1, img2)
    
    # Simpan hasil
    print("\n💾 Menyimpan hasil operasi pengurangan...")
    for nama_operasi, data in hasil_operasi.items():
        simpan_perbandingan_dengan_stats(
            img1, data['image'], 
            f"pengurangan_{nama_operasi}",
            "Gambar A (Original)", 
            data['title'],
            stats_asli, 
            data['stats'],
            kategori="1_pengurangan_citra"
        )
    
    print(f"✅ Operasi pengurangan selesai! File disimpan: {len(hasil_operasi)*3} file")

def proses_operasi_blending():
    """Memproses operasi blending"""
    print("\n🔄 OPERASI BLENDING")
    
    # Buat instance operasi blending
    blending = OperasiBlending()
    
    # Demo operasi blending
    blending.demo_blending("4_blending_citra")
    
    print("✅ Operasi blending selesai! File disimpan: 9 file")

def proses_operasi_boolean():
    """Memproses operasi boolean"""
    print("\n🔄 OPERASI BOOLEAN")
    
    # Pilih input gambar
    img1, img2 = pilih_input_gambar()
    if img1 is None or img2 is None:
        print("❌ Operasi dibatalkan")
        return
    
    # Demo operasi boolean
    hasil_operasi = demo_operasi_boolean(img1, img2)
    
    # Simpan hasil
    print("\n💾 Menyimpan hasil operasi boolean...")
    
    # Simpan gambar biner asli sebagai referensi
    if 'binary1' in hasil_operasi:
        stats_binary = hasil_operasi['binary1']['stats']
        
        # Simpan hasil operasi boolean - semua operasi dalam satu folder
        operasi_list = ['and', 'or', 'xor', 'not']
        for nama_operasi in operasi_list:
            if nama_operasi in hasil_operasi:
                data = hasil_operasi[nama_operasi]
                simpan_perbandingan_dengan_stats(
                    hasil_operasi['binary1']['image'], 
                    data['image'],
                    f"boolean_{nama_operasi}",
                    "Binary A (Original)",
                    data['title'],
                    stats_binary,
                    data['stats'],
                    kategori="2_operasi_boolean"
                )
    
    print(f"✅ Operasi boolean selesai! File disimpan: {len([k for k in hasil_operasi.keys() if k in ['and','or','xor','not']])*3} file")

def proses_motion_detection():
    """Memproses motion detection"""
    print("\n🔄 MOTION DETECTION")
    
    # Demo motion detection (menggunakan frame yang dibuat otomatis)
    hasil_operasi = demo_motion_detection()
    
    if not hasil_operasi:
        print("❌ Gagal melakukan motion detection")
        return
    
    # Simpan hasil
    print("\n💾 Menyimpan hasil motion detection...")
    
    # Simpan frame asli sebagai referensi
    if 'frame1' in hasil_operasi and 'motion_cleaned' in hasil_operasi:
        frame1_data = hasil_operasi['frame1']
        motion_data = hasil_operasi['motion_cleaned']
        
        simpan_perbandingan_dengan_stats(
            frame1_data['image'],
            motion_data['image'],
            "motion_detection",
            frame1_data['title'],
            motion_data['title'],
            frame1_data['stats'],
            motion_data['stats'],
            kategori="3_motion_detection"
        )
    
    # Simpan variasi lain jika ada
    variasi_list = ['motion_simple', 'motion_low_threshold']
    for nama_variasi in variasi_list:
        if nama_variasi in hasil_operasi and 'frame1' in hasil_operasi:
            data_variasi = hasil_operasi[nama_variasi]
            frame1_data = hasil_operasi['frame1']
            
            simpan_perbandingan_dengan_stats(
                frame1_data['image'],
                data_variasi['image'],
                nama_variasi,
                "Frame Original",
                data_variasi['title'],
                frame1_data['stats'],
                data_variasi['stats'],
                kategori="3_motion_detection"
            )
    
    print("✅ Motion detection selesai! File disimpan: 9 file")

def demo_lengkap():
    """Menjalankan demo lengkap semua operasi"""
    print("\n🎯 DEMO LENGKAP SEMUA OPERASI")
    print("Menggunakan gambar sample built-in untuk konsistensi...")
    
    # Load gambar sample
    img1, img2 = muat_gambar_sample()
    if img1 is None or img2 is None:
        print("❌ Gagal memuat gambar sample")
        return
    
    total_files_awal = hitung_total_file_output()
    
    # 1. Operasi Pengurangan
    print("\n1️⃣ OPERASI PENGURANGAN CITRA")
    stats_asli = hitung_statistik_dasar(img1)
    hasil_pengurangan = demo_pengurangan_citra(img1, img2)
    
    for nama_operasi, data in hasil_pengurangan.items():
        simpan_perbandingan_dengan_stats(
            img1, data['image'],
            f"demo_{nama_operasi}",
            "Sample Camera",
            data['title'],
            stats_asli,
            data['stats'],
            kategori="1_pengurangan_citra"
        )
    
    # 2. Operasi Boolean (Semua: AND, OR, XOR, NOT)
    print("\n2️⃣ OPERASI BOOLEAN (AND, OR, XOR, NOT)")
    hasil_boolean = demo_operasi_boolean(img1, img2)
    
    if 'binary1' in hasil_boolean:
        stats_binary = hasil_boolean['binary1']['stats']
        # Semua operasi boolean dalam satu folder
        operasi_list = ['and', 'or', 'xor', 'not']
        for nama_operasi in operasi_list:
            if nama_operasi in hasil_boolean:
                data = hasil_boolean[nama_operasi]
                simpan_perbandingan_dengan_stats(
                    hasil_boolean['binary1']['image'],
                    data['image'],
                    f"demo_boolean_{nama_operasi}",
                    "Binary Camera",
                    data['title'],
                    stats_binary,
                    data['stats'],
                    "hasil_pengolahan",
                    "2_operasi_boolean"
                )
    
    # 3. Motion Detection
    print("\n3️⃣ MOTION DETECTION")
    hasil_motion = demo_motion_detection()
    
    if hasil_motion:
        motion_list = ['motion_cleaned']  # Ambil satu yang terbaik saja
        for nama_motion in motion_list:
            if nama_motion in hasil_motion and 'frame1' in hasil_motion:
                data_motion = hasil_motion[nama_motion]
                frame1_data = hasil_motion['frame1']
                
                simpan_perbandingan_dengan_stats(
                    frame1_data['image'],
                    data_motion['image'],
                    f"demo_{nama_motion}",
                    "Demo Frame",
                    data_motion['title'],
                    frame1_data['stats'],
                    data_motion['stats'],
                    "hasil_pengolahan",
                    "3_motion_detection"
                )
    
    # 4. Operasi Blending (Terakhir)
    print("\n4️⃣ OPERASI BLENDING CITRA")
    blending = OperasiBlending()
    blending.demo_blending("4_blending_citra")
    
    # Hitung total file
    total_files_akhir = hitung_total_file_output()
    files_generated = total_files_akhir - total_files_awal
    
    print(f"\n🎉 DEMO LENGKAP SELESAI!")
    print(f"📁 Total file yang dihasilkan: {files_generated} file")
    print(f"📂 Lokasi: hasil_pengolahan/")
    print(f"📋 Operasi: Pengurangan, Blending, Boolean AND & OR, Motion Detection")

def main():
    """Fungsi utama program"""
    try:
        tampilkan_header()
        
        while True:
            try:
                tampilkan_menu_utama()
                pilihan = input("👉 Pilih operasi (1-6): ").strip()
                
                if pilihan == '1':
                    proses_pengurangan_citra()
                
                elif pilihan == '2':
                    proses_operasi_blending()
                
                elif pilihan == '3':
                    proses_operasi_boolean()
                
                elif pilihan == '4':
                    proses_motion_detection()
                
                elif pilihan == '5':
                    demo_lengkap()
                
                elif pilihan == '6':
                    total_files = hitung_total_file_output()
                    print(f"\n👋 Terima kasih telah menggunakan program!")
                    print(f"📁 Total file hasil: {total_files} file")
                    print(f"📂 Lokasi: hasil_pengolahan/")
                    break
                
                else:
                    print("❌ Pilihan tidak valid! Silakan pilih 1-6.")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Program dihentikan oleh user.")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                print("💡 Silakan coba lagi.")
                
    except ImportError as e:
        print(f"❌ Error import modul: {e}")
        print("💡 Pastikan semua file modul tersedia:")
        print("   - operasi_pengurangan.py")
        print("   - operasi_boolean.py") 
        print("   - motion_detection.py")
        print("   - input_output.py")
    except Exception as e:
        print(f"❌ Error tidak terduga: {e}")

if __name__ == "__main__":
    main()