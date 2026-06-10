import yt_dlp
import os
import webbrowser
from datetime import datetime


DOWNLOAD_DIR = "downloads"


def telecharger(url, dossier=DOWNLOAD_DIR):

    if not os.path.exists(dossier):
        os.makedirs(dossier)

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n====================================")
    print("      VIDEO DOWNLOADER PRO V2")
    print("====================================")
    print("Date :", date)
    print("URL  :", url)
    print("------------------------------------\n")

    options = {
        "outtmpl": f"{dossier}/%(uploader)s/%(title)s.%(ext)s",

        # vidéo + audio best quality
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",

        # IMPORTANT: compat TikTok / réseaux sociaux
        "ignoreerrors": True,
        "noplaylist": False,

        # images / thumbnails
        "writethumbnail": True,
        "write_all_thumbnails": True,

        # logs visibles
        "quiet": False,
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

        print("\n✔ Téléchargement terminé avec succès")

        # OUVERTURE AUTOMATIQUE DE LA GALERIE
        ouvrir_galerie(dossier)

    except Exception as e:
        print("\n❌ ERREUR :", str(e))


def ouvrir_galerie(dossier):
    """
    Ouvre automatiquement le dossier de téléchargement = galerie locale
    """

    path = os.path.abspath(dossier)
    print("\n📁 Ouverture galerie :", path)

    try:
        webbrowser.open(path)
    except:
        os.startfile(path)


if __name__ == "__main__":

    print("====================================")
    print("     VIDEO DOWNLOADER UNIVERSEL")
    print("====================================\n")

    while True:

        lien = input("Colle le lien (ou 'exit') : ").strip()

        if lien.lower() == "exit":
            print("Fermeture du programme...")
            break

        if lien:
            telecharger(lien)
        else:
            print("⚠️ Aucun lien fourni")