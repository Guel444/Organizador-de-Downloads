import shutil
from config import PASTA_DOWNLOADS, TIPOS_ARQUIVOS


def mapear_arquivos():
    resultado = {pasta: [] for pasta in TIPOS_ARQUIVOS}

    for arquivo in PASTA_DOWNLOADS.iterdir():
        if not arquivo.is_file() or not arquivo.suffix:
            continue

        extensao = arquivo.suffix.lower().lstrip('.')

        for pasta, extensoes in TIPOS_ARQUIVOS.items():
            if extensao in extensoes:
                resultado[pasta].append(arquivo)
                break

    return resultado


def organizar(arquivos_mapeados):
    for pasta, arquivos in arquivos_mapeados.items():
        if not arquivos:
            continue

        destino = PASTA_DOWNLOADS / pasta
        destino.mkdir(exist_ok=True)

        for arquivo in arquivos:
            shutil.move(arquivo, destino / arquivo.name)
