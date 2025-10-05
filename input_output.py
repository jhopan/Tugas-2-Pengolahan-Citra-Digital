"""
Module untuk Input/Output dan Visualisasi
Berisi fungsi-fungsi untuk memuat gambar dan menyimpan hasil
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import data
import os
from tkinter import filedialog, messagebox
import tkinter as tk

def buat_folder_hasil(nama_folder="hasil_pengolahan"):
    """
    Membuat folder untuk menyimpan hasil dengan subfolder berdasarkan kategori
    
    Args:
        nama_folder: Nama folder yang akan dibuat
        
    Returns:
        str: Path folder yang dibuat
    """
    try:
        # Buat folder utama
        if not os.path.exists(nama_folder):
            os.makedirs(nama_folder)
            print(f"📁 Folder '{nama_folder}' telah dibuat")
        
        # Buat subfolder berdasarkan kategori
        subfolders = [
            "1_pengurangan_citra",
            "2_operasi_boolean", 
            "3_motion_detection",
            "4_blending_citra"
        ]
        
        for subfolder in subfolders:
            subfolder_path = os.path.join(nama_folder, subfolder)
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)
                print(f"📂 Subfolder '{subfolder}' telah dibuat")
        
        return nama_folder
    except Exception as e:
        print(f"❌ Error membuat folder: {e}")
        return None

def muat_gambar_sample():
    """
    Memuat gambar sample dari skimage
    
    Returns:
        tuple: (img1, img2) atau (None, None) jika gagal
    """
    try:
        print("🔄 Memuat gambar sample...")
        img1 = data.camera()  # Gambar kamera
        img2 = data.coins()   # Gambar koin
        
        # Resize agar ukuran sama
        img1 = cv2.resize(img1, (300, 300))
        img2 = cv2.resize(img2, (300, 300))
        
        print("✅ Berhasil memuat gambar sample")
        return img1, img2
        
    except Exception as e:
        print(f"❌ Error memuat gambar sample: {e}")
        return None, None

def input_gambar_dari_file():
    """
    Input gambar dari file menggunakan dialog
    
    Returns:
        tuple: (img1, img2) atau (None, None) jika gagal
    """
    try:
        print("📂 Pilih gambar pertama...")
        root = tk.Tk()
        root.withdraw()
        
        # Pilih gambar pertama
        file1 = filedialog.askopenfilename(
            title="Pilih Gambar Pertama",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
        )
        if not file1:
            print("❌ Tidak ada gambar dipilih")
            return None, None
        
        # Pilih gambar kedua
        print("📂 Pilih gambar kedua...")
        file2 = filedialog.askopenfilename(
            title="Pilih Gambar Kedua",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
        )
        if not file2:
            print("❌ Tidak ada gambar kedua dipilih")
            return None, None
        
        # Baca gambar
        img1 = cv2.imread(file1, cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(file2, cv2.IMREAD_GRAYSCALE)
        
        if img1 is None or img2 is None:
            print("❌ Error membaca gambar")
            return None, None
        
        # Resize agar ukuran sama
        height = min(img1.shape[0], img2.shape[0], 400)
        width = min(img1.shape[1], img2.shape[1], 400)
        
        img1 = cv2.resize(img1, (width, height))
        img2 = cv2.resize(img2, (width, height))
        
        print("✅ Berhasil memuat gambar dari file")
        return img1, img2
        
    except Exception as e:
        print(f"❌ Error input gambar: {e}")
        return None, None

def buat_gambar_sintetis():
    """
    Membuat gambar sintetis untuk demonstrasi
    
    Returns:
        tuple: (img1, img2) gambar sintetis
    """
    try:
        print("🎨 Membuat gambar sintetis...")
        
        # Gambar 1: Bentuk geometris
        img1 = np.zeros((300, 300), dtype=np.uint8)
        cv2.rectangle(img1, (50, 50), (150, 150), 255, -1)  # Kotak putih
        cv2.circle(img1, (200, 200), 40, 128, -1)  # Lingkaran abu-abu
        
        # Gambar 2: Bentuk geometris berbeda
        img2 = np.zeros((300, 300), dtype=np.uint8)
        cv2.circle(img2, (100, 100), 50, 255, -1)  # Lingkaran putih
        cv2.rectangle(img2, (180, 180), (280, 280), 192, -1)  # Kotak abu-abu
        
        print("✅ Berhasil membuat gambar sintetis")
        return img1, img2
        
    except Exception as e:
        print(f"❌ Error membuat gambar sintetis: {e}")
        return None, None

def tampilkan_gambar_input(img1, img2, title1="Gambar A", title2="Gambar B"):
    """
    Menampilkan gambar input secara berdampingan
    
    Args:
        img1, img2: Array numpy gambar
        title1, title2: Judul untuk masing-masing gambar
    """
    try:
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        
        axes[0].imshow(img1, cmap='gray')
        axes[0].set_title(title1, fontsize=12, fontweight='bold')
        axes[0].axis('off')
        
        axes[1].imshow(img2, cmap='gray')
        axes[1].set_title(title2, fontsize=12, fontweight='bold')
        axes[1].axis('off')
        
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print(f"❌ Error menampilkan gambar: {e}")

def simpan_perbandingan_dengan_stats(img_asli, img_hasil, filename_base, 
                                   title_asli, title_hasil, stats_asli, stats_hasil,
                                   folder_output="hasil_pengolahan", kategori=""):
    """
    Menyimpan perbandingan gambar dengan statistik dalam layout balanced
    
    Args:
        img_asli, img_hasil: Gambar asli dan hasil
        filename_base: Base filename untuk save
        title_asli, title_hasil: Judul gambar
        stats_asli, stats_hasil: Dictionary statistik
        folder_output: Folder untuk menyimpan hasil
        kategori: Kategori operasi (pengurangan/boolean/motion)
    """
    try:
        # Pastikan folder output ada
        buat_folder_hasil(folder_output)
        
        # Tentukan subfolder berdasarkan kategori
        if kategori:
            output_path = os.path.join(folder_output, kategori)
            # Pastikan folder kategori ada
            if not os.path.exists(output_path):
                os.makedirs(output_path)
                print(f"📂 Subfolder '{kategori}' telah dibuat")
        else:
            output_path = folder_output
        
        # Buat figure dengan layout balanced 2x2
        fig = plt.figure(figsize=(14, 10))
        gs = fig.add_gridspec(2, 2, height_ratios=[3, 2], hspace=0.3, wspace=0.2)
        
        # Gambar asli (atas kiri)
        ax1 = fig.add_subplot(gs[0, 0])
        ax1.imshow(img_asli, cmap='gray')
        ax1.set_title(title_asli, fontsize=14, fontweight='bold', color='blue', pad=15)
        ax1.axis('off')
        
        # Gambar hasil (atas kanan)
        ax2 = fig.add_subplot(gs[0, 1])
        ax2.imshow(img_hasil, cmap='gray')
        ax2.set_title(title_hasil, fontsize=14, fontweight='bold', color='red', pad=15)
        ax2.axis('off')
        
        # Statistik asli (bawah kiri)
        ax3 = fig.add_subplot(gs[1, 0])
        ax3.axis('off')
        stats_text_asli = format_stats_text("STATISTIK ASLI", stats_asli)
        ax3.text(0.5, 0.95, stats_text_asli, fontsize=11,
                transform=ax3.transAxes, va='top', ha='center', family='monospace',
                bbox=dict(boxstyle="round,pad=0.5", facecolor="lightblue", alpha=0.8))
        
        # Statistik hasil (bawah kanan)
        ax4 = fig.add_subplot(gs[1, 1])
        ax4.axis('off')
        stats_text_hasil = format_stats_text("STATISTIK HASIL", stats_hasil)
        ax4.text(0.5, 0.95, stats_text_hasil, fontsize=11,
                transform=ax4.transAxes, va='top', ha='center', family='monospace',
                bbox=dict(boxstyle="round,pad=0.5", facecolor="lightcoral", alpha=0.8))
        
        # Simpan file
        plt.subplots_adjust(left=0.05, right=0.95, top=0.92, bottom=0.08, hspace=0.3, wspace=0.2)
        plt.savefig(f"{output_path}/{filename_base}_comparison.jpg",
                   dpi=150, bbox_inches='tight', pad_inches=0.2)
        plt.close()
        
        # Simpan gambar individual
        cv2.imwrite(f"{output_path}/{filename_base}_original.jpg", img_asli)
        cv2.imwrite(f"{output_path}/{filename_base}_result.jpg", img_hasil)
        
        print(f"💾 Disimpan: {kategori}/{filename_base}_comparison.jpg")
        
    except Exception as e:
        print(f"❌ Error menyimpan perbandingan: {e}")

def format_stats_text(title, stats_dict):
    """
    Format dictionary statistik menjadi text per baris
    
    Args:
        title: Judul statistik
        stats_dict: Dictionary statistik
        
    Returns:
        str: Text yang sudah diformat
    """
    text = f"{title}:\n"
    for key, value in stats_dict.items():
        if isinstance(value, float):
            text += f"{key}: {value:.2f}\n"
        else:
            text += f"{key}: {value}\n"
    return text

def tampilkan_menu_input():
    """
    Menampilkan menu pilihan input gambar
    """
    print("\n📁 PILIH SUMBER GAMBAR:")
    print("1. Gunakan gambar sample (built-in)")
    print("2. Input gambar dari file")
    print("3. Buat gambar sintetis")
    print("4. Kembali ke menu utama")
    print("-"*40)

def pilih_input_gambar():
    """
    Menu interaktif untuk memilih sumber gambar
    
    Returns:
        tuple: (img1, img2) atau (None, None) jika batal
    """
    while True:
        tampilkan_menu_input()
        pilihan = input("👉 Pilih sumber gambar (1-4): ").strip()
        
        if pilihan == '1':
            img1, img2 = muat_gambar_sample()
            if img1 is not None and img2 is not None:
                tampilkan_gambar_input(img1, img2)
                return img1, img2
        
        elif pilihan == '2':
            img1, img2 = input_gambar_dari_file()
            if img1 is not None and img2 is not None:
                tampilkan_gambar_input(img1, img2)
                return img1, img2
        
        elif pilihan == '3':
            img1, img2 = buat_gambar_sintetis()
            if img1 is not None and img2 is not None:
                tampilkan_gambar_input(img1, img2)
                return img1, img2
        
        elif pilihan == '4':
            return None, None
        
        else:
            print("❌ Pilihan tidak valid!")

def hitung_total_file_output(folder_output="hasil_pengolahan"):
    """
    Menghitung total file output yang dihasilkan
    
    Args:
        folder_output: Folder yang akan dihitung
        
    Returns:
        int: Jumlah file output
    """
    try:
        if not os.path.exists(folder_output):
            return 0
        
        files = [f for f in os.listdir(folder_output) if f.endswith(('.jpg', '.png', '.bmp'))]
        return len(files)
        
    except Exception as e:
        print(f"❌ Error menghitung file: {e}")
        return 0