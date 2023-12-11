import requests
from tqdm import tqdm
import os
import zipfile
import webbrowser

print("Autore: Christopher Zonta")
print("Email: czonta1996@outlook.it\n") 
print("Questo script intende avviare allo studio delle basi di QGIS, attraverso il sito https://download.qgis.org/downloads/data/ che fornisce esercitazioni e vari materiali di studio. Questo script scaricherà dapprima il modulo delle esercitazioni da questo sito, ossia una ZIP file chiamata training_manual_exercise_data.zip da 300 MB, poi la estrae nella stessa folder dove è presente questo script ed esegue il file example.qgs assumendo che abbiate già installato QGIS nel computer. Infine, qualora non bastasse, aprirà il QGIS Training Manual, permettendo di consultare l'indice delle Informazioni.")
def download_file(url, destination_path):
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # Dimensione dei blocchi di download (1 KB)
        progress_bar = tqdm(total=total_size, unit='B', unit_scale=True)

        with open(destination_path, 'wb') as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)

        progress_bar.close()

        print(f"Download completato. File salvato in: {destination_path}")
    else:
        print(f"Errore nel download. Status code: {response.status_code}")

if __name__ == "__main__":
    url = "https://download.qgis.org/downloads/data/training_manual_exercise_data.zip"
    destination_path = "training_manual_exercise_data.zip"

    download_file(url, destination_path)
    
def extract_zip(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        total_files = len(zip_ref.infolist())
        progress_bar = tqdm(total=total_files, unit='file')

        for file_info in zip_ref.infolist():
            zip_ref.extract(file_info)
            progress_bar.update(1)

        progress_bar.close()


    os.system("cd exercise_data & example.qgs")

if __name__ == "__main__":
    zip_file = "training_manual_exercise_data.zip"

    # Estrai l'archivio
    extract_zip(zip_file)
    
    url = "https://docs.qgis.org/testing/en/docs/training_manual/"
    webbrowser.open(url)

    print("Fatto, buon lavoro e buono studio. Tifo per te.")
