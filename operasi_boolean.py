"""
Module untuk Operasi Boolean
Berisi semua fungsi terkait operasi boolean pada gambar biner
"""

import cv2
import numpy as np

def binarisasi_gambar(image, threshold=127):
    """
    Mengkonversi gambar grayscale menjadi biner
    
    Args:
        image: Array numpy gambar grayscale
        threshold: Nilai threshold (default: 127)
        
    Returns:
        tuple: (gambar_biner, threshold_used)
    """
    try:
        _, binary = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
        return binary, threshold
    except Exception as e:
        print(f"❌ Error binarisasi: {e}")
        return None, threshold

def operasi_and(img1, img2, threshold=127):
    """
    Operasi boolean AND pada dua gambar
    
    Args:
        img1, img2: Array numpy gambar grayscale
        threshold: Threshold untuk binarisasi
        
    Returns:
        tuple: (hasil_and, stats_dict)
    """
    try:
        # Binarisasi gambar
        binary1, _ = binarisasi_gambar(img1, threshold)
        binary2, _ = binarisasi_gambar(img2, threshold)
        
        if binary1 is None or binary2 is None:
            return None, None
        
        # Operasi AND
        hasil = cv2.bitwise_and(binary1, binary2)
        
        # Statistik
        stats = hitung_statistik_biner(hasil, "A AND B", threshold)
        stats['Logika'] = 'Irisan (∩)'
        
        return hasil, stats
        
    except Exception as e:
        print(f"❌ Error operasi AND: {e}")
        return None, None

def operasi_or(img1, img2, threshold=127):
    """
    Operasi boolean OR pada dua gambar
    
    Args:
        img1, img2: Array numpy gambar grayscale
        threshold: Threshold untuk binarisasi
        
    Returns:
        tuple: (hasil_or, stats_dict)
    """
    try:
        # Binarisasi gambar
        binary1, _ = binarisasi_gambar(img1, threshold)
        binary2, _ = binarisasi_gambar(img2, threshold)
        
        if binary1 is None or binary2 is None:
            return None, None
        
        # Operasi OR
        hasil = cv2.bitwise_or(binary1, binary2)
        
        # Statistik
        stats = hitung_statistik_biner(hasil, "A OR B", threshold)
        stats['Logika'] = 'Gabungan (∪)'
        
        return hasil, stats
        
    except Exception as e:
        print(f"❌ Error operasi OR: {e}")
        return None, None

def operasi_xor(img1, img2, threshold=127):
    """
    Operasi boolean XOR pada dua gambar
    
    Args:
        img1, img2: Array numpy gambar grayscale
        threshold: Threshold untuk binarisasi
        
    Returns:
        tuple: (hasil_xor, stats_dict)
    """
    try:
        # Binarisasi gambar
        binary1, _ = binarisasi_gambar(img1, threshold)
        binary2, _ = binarisasi_gambar(img2, threshold)
        
        if binary1 is None or binary2 is None:
            return None, None
        
        # Operasi XOR
        hasil = cv2.bitwise_xor(binary1, binary2)
        
        # Statistik
        stats = hitung_statistik_biner(hasil, "A XOR B", threshold)
        stats['Logika'] = 'Selisih Simetris (⊕)'
        
        return hasil, stats
        
    except Exception as e:
        print(f"❌ Error operasi XOR: {e}")
        return None, None

def operasi_not(img1, threshold=127):
    """
    Operasi boolean NOT pada gambar
    
    Args:
        img1: Array numpy gambar grayscale
        threshold: Threshold untuk binarisasi
        
    Returns:
        tuple: (hasil_not, stats_dict)
    """
    try:
        # Binarisasi gambar
        binary1, _ = binarisasi_gambar(img1, threshold)
        
        if binary1 is None:
            return None, None
        
        # Operasi NOT
        hasil = cv2.bitwise_not(binary1)
        
        # Statistik
        stats = hitung_statistik_biner(hasil, "NOT A", threshold)
        stats['Logika'] = 'Komplemen (¬)'
        
        return hasil, stats
        
    except Exception as e:
        print(f"❌ Error operasi NOT: {e}")
        return None, None

def hitung_statistik_biner(binary_image, operation_name="", threshold=127):
    """
    Menghitung statistik untuk gambar biner
    
    Args:
        binary_image: Array numpy gambar biner
        operation_name: Nama operasi
        threshold: Nilai threshold yang digunakan
        
    Returns:
        dict: Dictionary statistik
    """
    try:
        white_pixels = np.count_nonzero(binary_image)
        total_pixels = binary_image.size
        black_pixels = total_pixels - white_pixels
        
        return {
            'Pixel Putih': white_pixels,
            'Pixel Hitam': black_pixels,
            'Persentase Putih': (white_pixels / total_pixels) * 100,
            'Threshold': f'{threshold}/255',
            'Operasi': operation_name,
            'Ukuran': f'{binary_image.shape[1]}x{binary_image.shape[0]}'
        }
    except Exception as e:
        print(f"❌ Error menghitung statistik biner: {e}")
        return {}

def demo_operasi_boolean(img1, img2, threshold=127):
    """
    Demo lengkap semua operasi boolean
    
    Args:
        img1, img2: Array numpy gambar grayscale
        threshold: Threshold untuk binarisasi
        
    Returns:
        dict: Dictionary berisi semua hasil operasi
    """
    print("🔄 Demo Operasi Boolean...")
    
    results = {}
    
    # Binarisasi gambar asli
    binary1, _ = binarisasi_gambar(img1, threshold)
    binary2, _ = binarisasi_gambar(img2, threshold)
    
    if binary1 is None or binary2 is None:
        print("❌ Gagal melakukan binarisasi")
        return results
    
    # Statistik gambar biner asli
    stats_binary1 = hitung_statistik_biner(binary1, "Binary A", threshold)
    stats_binary2 = hitung_statistik_biner(binary2, "Binary B", threshold)
    
    results['binary1'] = {
        'image': binary1,
        'stats': stats_binary1,
        'title': 'Binary A (Threshold 127)'
    }
    
    results['binary2'] = {
        'image': binary2,
        'stats': stats_binary2,
        'title': 'Binary B (Threshold 127)'
    }
    
    # 1. Operasi AND
    print("  1️⃣ Operasi AND")
    hasil_and, stats_and = operasi_and(img1, img2, threshold)
    if hasil_and is not None:
        results['and'] = {
            'image': hasil_and,
            'stats': stats_and,
            'title': 'A AND B (Irisan)'
        }
    
    # 2. Operasi OR
    print("  2️⃣ Operasi OR")
    hasil_or, stats_or = operasi_or(img1, img2, threshold)
    if hasil_or is not None:
        results['or'] = {
            'image': hasil_or,
            'stats': stats_or,
            'title': 'A OR B (Gabungan)'
        }
    
    # 3. Operasi XOR
    print("  3️⃣ Operasi XOR")
    hasil_xor, stats_xor = operasi_xor(img1, img2, threshold)
    if hasil_xor is not None:
        results['xor'] = {
            'image': hasil_xor,
            'stats': stats_xor,
            'title': 'A XOR B (Selisih Simetris)'
        }
    
    # 4. Operasi NOT
    print("  4️⃣ Operasi NOT")
    hasil_not, stats_not = operasi_not(img1, threshold)
    if hasil_not is not None:
        results['not'] = {
            'image': hasil_not,
            'stats': stats_not,
            'title': 'NOT A (Komplemen)'
        }
    
    print("✅ Demo operasi boolean selesai!")
    return results