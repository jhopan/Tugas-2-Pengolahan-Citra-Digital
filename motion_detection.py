"""
Module untuk Motion Detection
Berisi fungsi-fungsi untuk deteksi pergerakan antar frame
"""

import cv2
import numpy as np

def deteksi_motion_sederhana(frame1, frame2, threshold=30):
    """
    Deteksi motion sederhana menggunakan frame differencing
    
    Args:
        frame1, frame2: Array numpy frame gambar
        threshold: Threshold untuk deteksi motion
        
    Returns:
        tuple: (motion_mask, stats_dict)
    """
    try:
        # Pastikan ukuran sama
        if frame1.shape != frame2.shape:
            frame2 = cv2.resize(frame2, (frame1.shape[1], frame1.shape[0]))
        
        # Hitung perbedaan absolut
        diff = cv2.absdiff(frame1, frame2)
        
        # Apply threshold
        _, motion_mask = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)
        
        # Hitung statistik
        motion_pixels = np.count_nonzero(motion_mask)
        total_pixels = motion_mask.size
        motion_percentage = (motion_pixels / total_pixels) * 100
        
        stats = {
            'Motion Pixels': motion_pixels,
            'Total Pixels': total_pixels,
            'Motion %': motion_percentage,
            'Threshold': f'{threshold}/255',
            'Status': 'DETECTED' if motion_percentage > 1.0 else 'MINIMAL',
            'Method': 'Simple Differencing'
        }
        
        return motion_mask, stats
        
    except Exception as e:
        print(f"❌ Error deteksi motion sederhana: {e}")
        return None, None

def deteksi_motion_dengan_cleanup(frame1, frame2, threshold=30):
    """
    Deteksi motion dengan morphological cleanup
    
    Args:
        frame1, frame2: Array numpy frame gambar
        threshold: Threshold untuk deteksi motion
        
    Returns:
        tuple: (cleaned_motion_mask, stats_dict)
    """
    try:
        # Deteksi motion sederhana terlebih dahulu
        motion_mask, _ = deteksi_motion_sederhana(frame1, frame2, threshold)
        
        if motion_mask is None:
            return None, None
        
        # Morphological operations untuk cleanup noise
        kernel = np.ones((3,3), np.uint8)
        
        # Close operation: menghubungkan area yang berdekatan
        cleaned = cv2.morphologyEx(motion_mask, cv2.MORPH_CLOSE, kernel)
        
        # Open operation: menghilangkan noise kecil
        cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_OPEN, kernel)
        
        # Hitung statistik setelah cleanup
        motion_pixels = np.count_nonzero(cleaned)
        total_pixels = cleaned.size
        motion_percentage = (motion_pixels / total_pixels) * 100
        
        stats = {
            'Motion Pixels': motion_pixels,
            'Total Pixels': total_pixels,
            'Motion %': motion_percentage,
            'Threshold': f'{threshold}/255',
            'Status': 'DETECTED' if motion_percentage > 1.0 else 'MINIMAL',
            'Cleaned': 'Morphological',
            'Method': 'With Cleanup'
        }
        
        return cleaned, stats
        
    except Exception as e:
        print(f"❌ Error deteksi motion dengan cleanup: {e}")
        return None, None

def buat_frame_motion_demo():
    """
    Membuat frame demo untuk motion detection
    
    Returns:
        tuple: (frame1, frame2) untuk testing motion detection
    """
    try:
        # Frame 1: Scene statis
        frame1 = np.zeros((300, 300), dtype=np.uint8)
        cv2.rectangle(frame1, (50, 50), (150, 150), 128, -1)  # Kotak abu-abu
        cv2.circle(frame1, (200, 200), 30, 255, -1)  # Lingkaran putih
        
        # Frame 2: Scene dengan perubahan (simulasi motion)
        frame2 = frame1.copy()
        cv2.rectangle(frame2, (70, 70), (170, 170), 128, -1)  # Kotak bergeser
        cv2.circle(frame2, (180, 180), 30, 255, -1)  # Lingkaran bergeser
        cv2.rectangle(frame2, (250, 250), (290, 290), 192, -1)  # Objek baru
        
        print("✅ Frame demo motion detection berhasil dibuat")
        return frame1, frame2
        
    except Exception as e:
        print(f"❌ Error membuat frame demo: {e}")
        return None, None

def analisis_motion_area(motion_mask):
    """
    Analisis area yang mengalami motion
    
    Args:
        motion_mask: Mask hasil deteksi motion
        
    Returns:
        dict: Informasi tentang area motion
    """
    try:
        # Cari contours (area motion)
        contours, _ = cv2.findContours(motion_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        if len(contours) == 0:
            return {
                'Motion Areas': 0,
                'Largest Area': 0,
                'Total Motion Area': 0
            }
        
        # Hitung area dari setiap contour
        areas = [cv2.contourArea(cnt) for cnt in contours]
        total_motion_area = sum(areas)
        largest_area = max(areas) if areas else 0
        
        return {
            'Motion Areas': len(contours),
            'Largest Area': int(largest_area),
            'Total Motion Area': int(total_motion_area),
            'Avg Area': int(total_motion_area / len(contours)) if contours else 0
        }
        
    except Exception as e:
        print(f"❌ Error analisis motion area: {e}")
        return {}

def demo_motion_detection():
    """
    Demo lengkap motion detection dengan berbagai metode
    
    Returns:
        dict: Dictionary berisi hasil demo motion detection
    """
    print("🔄 Demo Motion Detection...")
    
    results = {}
    
    # Buat frame demo
    frame1, frame2 = buat_frame_motion_demo()
    
    if frame1 is None or frame2 is None:
        print("❌ Gagal membuat frame demo")
        return results
    
    # Statistik frame asli
    stats_frame1 = {
        'Frame': 'Original',
        'Mean Intensity': float(np.mean(frame1)),
        'Std Dev': float(np.std(frame1)),
        'Max': int(np.max(frame1)),
        'Min': int(np.min(frame1)),
        'Type': 'Static Scene'
    }
    
    stats_frame2 = {
        'Frame': 'Modified', 
        'Mean Intensity': float(np.mean(frame2)),
        'Std Dev': float(np.std(frame2)),
        'Max': int(np.max(frame2)),
        'Min': int(np.min(frame2)),
        'Type': 'With Motion'
    }
    
    results['frame1'] = {
        'image': frame1,
        'stats': stats_frame1,
        'title': 'Frame 1 (Original)'
    }
    
    results['frame2'] = {
        'image': frame2,
        'stats': stats_frame2,
        'title': 'Frame 2 (With Motion)'
    }
    
    # 1. Motion Detection Sederhana
    print("  1️⃣ Motion Detection Sederhana")
    motion_simple, stats_simple = deteksi_motion_sederhana(frame1, frame2, 30)
    if motion_simple is not None:
        # Tambah analisis area
        area_info = analisis_motion_area(motion_simple)
        stats_simple.update(area_info)
        
        results['motion_simple'] = {
            'image': motion_simple,
            'stats': stats_simple,
            'title': 'Motion Detection (Simple)'
        }
    
    # 2. Motion Detection dengan Cleanup
    print("  2️⃣ Motion Detection dengan Cleanup")
    motion_cleaned, stats_cleaned = deteksi_motion_dengan_cleanup(frame1, frame2, 30)
    if motion_cleaned is not None:
        # Tambah analisis area
        area_info = analisis_motion_area(motion_cleaned)
        stats_cleaned.update(area_info)
        
        results['motion_cleaned'] = {
            'image': motion_cleaned,
            'stats': stats_cleaned,
            'title': 'Motion Detection (Cleaned)'
        }
    
    # 3. Variasi threshold
    print("  3️⃣ Motion Detection (Threshold 15)")
    motion_low, stats_low = deteksi_motion_dengan_cleanup(frame1, frame2, 15)
    if motion_low is not None:
        area_info = analisis_motion_area(motion_low)
        stats_low.update(area_info)
        
        results['motion_low_threshold'] = {
            'image': motion_low,
            'stats': stats_low,
            'title': 'Motion Detection (Low Threshold)'
        }
    
    print("✅ Demo motion detection selesai!")
    return results