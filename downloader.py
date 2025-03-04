import yt_dlp
import instaloader
import os
from datetime import datetime


# Função para criar pasta única para cada link com data e hora
def create_folder(prefix):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    folder_name = f"{prefix}_{timestamp}"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name


# Função para baixar vídeos do YouTube
def download_youtube_video(url):
    try:
        print(f"Baixando vídeo para o link: {url}")
        folder = create_folder("YouTube")
        ydl_opts = {
            'format': 'best',
            'outtmpl': f'{folder}/%(title)s.%(ext)s',  # Caminho da pasta criada
            'quiet': False
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Download concluído em: {folder}")
    except Exception as e:
        print(f"Erro ao baixar vídeo: {e}")


# Função para baixar mídia do Instagram
def download_instagram_media(url):
    try:
        loader = instaloader.Instaloader()
        shortcode = url.split('/')[-2]
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        folder = create_folder(post.owner_username)
        loader.download_post(post, target=folder)
        print(f"Download concluído em: {folder}")
    except Exception as e:
        print(f"Erro ao baixar mídia: {e}")


if __name__ == "__main__":
    opcoes = {1: "YOUTUBE", 2: "INSTAGRAM"}
    for chave, valor in opcoes.items():
        print(f"[{chave}] {valor}")
    escolha = int(input("ESCOLHA UMA OPCAO: "))
    
    match escolha:
        case 1:
            url = input("Digite o link do vídeo do YouTube: ")
            download_youtube_video(url)
        case 2:
            url = input("Digite o link da postagem do Instagram: ")
            download_instagram_media(url)
        case _:
            print("Opção inválida!")
