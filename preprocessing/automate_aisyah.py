import pandas as pd
import os

def preprocess_data(file_path):
    # 1. Membaca data mentah (Raw Data)
    # Dataset Heart Disease biasanya menggunakan koma (,), bukan titik koma (;)
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} tidak ditemukan!")
        return

    df = pd.read_csv(file_path) # Default sep=','
    
    # 2. Preprocessing: Penanganan Missing Values (PENTING untuk Skor Tinggi)
    # Mengisi kolom numerik dengan mean
    df = df.fillna(df.mean(numeric_only=True))
    
    # Mengisi kolom kategorikal (object) dengan modus
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].fillna(df[col].mode()[0])
    
    # 3. Target Engineering (Biner)
    # Mengubah target 'num' menjadi 0 (sehat) dan 1 (sakit)
    df['num'] = df['num'].apply(lambda x: 1 if x > 0 else 0)

    # 4. Encoding: Mengubah teks menjadi angka agar siap dilatih
    df_clean = pd.get_dummies(df, drop_first=True)
    
    # 5. Menyiapkan folder output
    # Folder harus sesuai dengan struktur yang diminta: namadataset_preprocessing
    output_dir = 'preprocessing/heart_disease_preprocessing'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # 6. Menyimpan hasil ke CSV baru
    output_file = f"{output_dir}/heart_disease_clean.csv"
    df_clean.to_csv(output_file, index=False)
    
    print("-" * 30)
    print(f"STATUS: OTOMASI SUKSES!")
    print(f"File siap latih: {output_file}")
    print(f"Jumlah baris & kolom: {df_clean.shape}")
    print("-" * 30)

if __name__ == "__main__":
    # Path dataset di VS Code kamu
    raw_data_path = 'heart_disease_uci_raw/heart_disease_uci.csv'
    preprocess_data(raw_data_path)