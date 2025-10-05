"""
Module untuk Operasi Pengurangan Citra
Berisi semua fungsi terkait pengurangan gambar
"""

import cv2
import numpy as np

def pengurangan_absolut(img1, img2):
    """
    Operasi pengurangan absolut |A - B|
    
    Args:
        img1, img2: Array numpy gambar grayscale
        
    Returns:
        tuple: (hasil_gambar, statistik_dict)
    """
    try:
        # Pastikan ukuran sama
        if img1.shape != img2.shape:
            raise ValueError("Ukuran gambar harus sama")
        
        # Operasi pengurangan absolut
        hasil = cv2.absdiff(img1, img2)
        
        # Hitung statistik
        stats = {
            'Mean': float(np.mean(hasil)),
            'Std Dev': float(np.std(hasil)),
            'Max': int(np.max(hasil)),
            'Min': int(np.min(hasil)),
            'Total Pixels': int(hasil.size),
            'Pixels >0': int(np.count_nonzero(hasil)),
            'Persen Diff': (np.count_nonzero(hasil) / hasil.size) * 100
        }
        
        return hasil, stats
        
    except Exception as e:
        print(f"❌ Error dalam pengurangan absolut: {e}")
        return None, None

def pengurangan_dengan_konstanta(img1, img2, konstanta=100):
    """
    Operasi (A - B) + K dengan handling underflow
    
    Args:
        img1, img2: Array numpy gambar grayscale
        konstanta: Nilai konstanta yang ditambahkan (default: 100)
        
    Returns:
        tuple: (hasil_gambar, statistik_dict)
    """
    try:
        # Pastikan ukuran sama
        if img1.shape != img2.shape:
            raise ValueError("Ukuran gambar harus sama")
        
        # Konversi ke int16 untuk mencegah underflow
        temp = img1.astype(np.int16) - img2.astype(np.int16) + konstanta
        
        # Clip ke range [0, 255] dan convert ke uint8
        hasil = np.clip(temp, 0, 255).astype(np.uint8)
        
        # Hitung statistik
        stats = {
            'Mean': float(np.mean(hasil)),
            'Std Dev': float(np.std(hasil)),
            'Max': int(np.max(hasil)),
            'Min': int(np.min(hasil)),
            'Total Pixels': int(hasil.size),
            'Konstanta': konstanta,
            'Range': f'[{np.min(hasil)}, {np.max(hasil)}]'
        }
        
        return hasil, stats
        
    except Exception as e:
        print(f"❌ Error dalam pengurangan dengan konstanta: {e}")
        return None, None

def hitung_statistik_dasar(image):
    """
    Menghitung statistik dasar gambar
    
    Args:
        image: Array numpy gambar
        
    Returns:
        dict: Dictionary berisi statistik dasar
    """
    try:
        return {
            'Mean': float(np.mean(image)),
            'Std Dev': float(np.std(image)),
            'Max': int(np.max(image)),
            'Min': int(np.min(image)),
            'Total Pixels': int(image.size)
        }
    except Exception as e:
        print(f"❌ Error menghitung statistik: {e}")
        return {}

def demo_pengurangan_citra(img1, img2):
    """
    Demo lengkap operasi pengurangan citra
    
    Args:
        img1, img2: Array numpy gambar grayscale
        
    Returns:
        dict: Dictionary berisi semua hasil operasi
    """
    print("🔄 Demo Operasi Pengurangan Citra...")
    
    results = {}
    
    # 1. Pengurangan Absolut
    print("  1️⃣ Pengurangan Absolut |A - B|")
    hasil_abs, stats_abs = pengurangan_absolut(img1, img2)
    if hasil_abs is not None:
        results['absolut'] = {
            'image': hasil_abs,
            'stats': stats_abs,
            'title': 'Pengurangan Absolut |A - B|'
        }
    
    # 2. Pengurangan dengan Konstanta
    print("  2️⃣ Pengurangan dengan Konstanta (A - B) + 100")
    hasil_const, stats_const = pengurangan_dengan_konstanta(img1, img2, 100)
    if hasil_const is not None:
        results['konstanta'] = {
            'image': hasil_const,
            'stats': stats_const,
            'title': 'Pengurangan (A - B) + 100'
        }
    
    # 3. Variasi konstanta lain
    print("  3️⃣ Pengurangan dengan Konstanta (A - B) + 150")
    hasil_const2, stats_const2 = pengurangan_dengan_konstanta(img1, img2, 150)
    if hasil_const2 is not None:
        results['konstanta2'] = {
            'image': hasil_const2,
            'stats': stats_const2,
            'title': 'Pengurangan (A - B) + 150'
        }
    
    print("✅ Demo pengurangan citra selesai!")
    return results