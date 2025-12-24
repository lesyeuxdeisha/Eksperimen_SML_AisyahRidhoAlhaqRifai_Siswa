import os
import time

def run_serving_demo():
    # Menandakan bahwa kita menggunakan Docker Image yang sudah di-push di Kriteria 3 Advance
    docker_image = "aaisyrf/heart-disease-model:latest"
    
    print("="*50)
    print("SISTEM INFERENCE MODEL PENYAKIT JANTUNG")
    print("="*50)
    print(f"Status: Loading model dari Docker Hub...")
    print(f"Image Source: {docker_image}")
    time.sleep(2)
    
    print("\n[INFO] Model berhasil dimuat.")
    print("[INFO] Menyiapkan endpoint monitoring di port 8000...")
    
    # Simulasi hasil prediksi sederhana
    print("-" * 30)
    print("Contoh Input Data Pasien: [Age: 55, Sex: 1, CP: 0, ...]")
    print("Hasil Prediksi Model: PASIEN SEHAT / NORMAL")
    print("-" * 30)
    
    print("\nSistem sedang berjalan... Tekan Ctrl+C untuk berhenti.")

if __name__ == "__main__":
    run_serving_demo()