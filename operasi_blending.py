"""
Modul Operasi Blending Citra
Nama: Jhosua Armando Putra Panjaitan
NIM: 2305541067
Mata Kuliah: Pengolahan Citra Digital

Modul ini berisi implementasi operasi blending (pencampuran) dua citra
dengan menggunakan weighted average untuk menghasilkan transisi yang smooth.
"""

import numpy as np
import cv2
from input_output import (
    muat_gambar_sample,
    simpan_perbandingan_dengan_stats
)

class OperasiBlending:
    def __init__(self):
        """Inisialisasi class"""
        pass
    
    def dapatkan_citra_sample(self):
        """Mendapatkan citra sample untuk testing"""
        return muat_gambar_sample()
    
    def blending_citra(self, img1, img2, alpha=0.5):
        """
        Melakukan operasi blending pada dua citra
        
        Formula: Hasil = α × A + (1-α) × B
        
        Parameters:
        - img1: Citra pertama (A)
        - img2: Citra kedua (B) 
        - alpha: Faktor blending (0.0 - 1.0)
        
        Returns:
        - result: Citra hasil blending
        """
        
        # Pastikan kedua citra memiliki ukuran yang sama
        if img1.shape != img2.shape:
            img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
        
        # Konversi ke float untuk mencegah overflow
        img1_float = img1.astype(np.float64)
        img2_float = img2.astype(np.float64)
        
        # Operasi blending: α×A + (1-α)×B
        result_float = alpha * img1_float + (1 - alpha) * img2_float
        
        # Clamp nilai ke range [0, 255] dan konversi kembali ke uint8
        result = np.clip(result_float, 0, 255).astype(np.uint8)
        
        return result
    
    def hitung_statistik_blending(self, img1, img2, result, alpha):
        """
        Menghitung statistik untuk operasi blending
        
        Parameters:
        - img1, img2: Citra input
        - result: Citra hasil blending
        - alpha: Faktor blending yang digunakan
        
        Returns:
        - stats_asli: Statistik citra input
        - stats_hasil: Statistik citra hasil
        """
        
        stats_asli = {
            'Mean A': f"{np.mean(img1):.2f}",
            'Mean B': f"{np.mean(img2):.2f}",
            'Std A': f"{np.std(img1):.2f}",
            'Std B': f"{np.std(img2):.2f}",
            'Alpha (α)': f"{alpha:.1f}",
            'Beta (1-α)': f"{1-alpha:.1f}"
        }
        
        # Verifikasi linear combination
        expected_mean = alpha * np.mean(img1) + (1-alpha) * np.mean(img2)
        actual_mean = np.mean(result)
        
        stats_hasil = {
            'Mean Result': f"{actual_mean:.2f}",
            'Expected Mean': f"{expected_mean:.2f}",
            'Mean Error': f"{abs(actual_mean - expected_mean):.4f}",
            'Std Dev': f"{np.std(result):.2f}",
            'Max': f"{np.max(result)}",
            'Min': f"{np.min(result)}",
            'Blend Ratio': f"{int(alpha*100)}% A + {int((1-alpha)*100)}% B"
        }
        
        return stats_asli, stats_hasil
    
    def demo_blending_alpha(self, img1, img2, alpha, nama_operasi, kategori):
        """
        Demo operasi blending dengan alpha tertentu
        
        Parameters:
        - img1, img2: Citra input
        - alpha: Faktor blending
        - nama_operasi: Nama untuk file output
        - kategori: Kategori folder
        """
        
        print(f"  🎨 Blending dengan α={alpha} ({int(alpha*100)}% A + {int((1-alpha)*100)}% B)")
        
        # Operasi blending
        result = self.blending_citra(img1, img2, alpha)
        
        # Hitung statistik
        stats_asli, stats_hasil = self.hitung_statistik_blending(img1, img2, result, alpha)
        
        # Simpan hasil perbandingan
        simpan_perbandingan_dengan_stats(
            img1, result, 
            nama_operasi,
            f"Citra A (Weight={alpha:.1f})", 
            f"Blended Result ({int(alpha*100)}% A + {int((1-alpha)*100)}% B)",
            stats_asli, stats_hasil,
            "hasil_pengolahan", kategori
        )
    
    def demo_blending(self, kategori="4_blending_citra"):
        """
        Demo lengkap operasi blending dengan berbagai nilai alpha
        
        Parameters:
        - kategori: Nama folder untuk menyimpan hasil
        """
        
        print("🔄 Demo Operasi Blending...")
        
        # Dapatkan citra sample
        img1, img2 = self.dapatkan_citra_sample()
        
        # Berbagai nilai alpha untuk demonstrasi
        alpha_configs = [
            (0.3, "blend_30"),
            (0.5, "blend_50"), 
            (0.7, "blend_70")
        ]
        
        # Demo setiap konfigurasi alpha
        for alpha, nama in alpha_configs:
            self.demo_blending_alpha(img1, img2, alpha, nama, kategori)
        
        print("✅ Demo blending selesai!")
        print(f"💾 Disimpan: {kategori}/ (9 file)")

if __name__ == "__main__":
    # Test standalone
    print("🧪 Testing Operasi Blending...")
    blending = OperasiBlending()
    blending.demo_blending("test_blending")
    print("✅ Test selesai!")