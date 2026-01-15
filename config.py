from pathlib import Path

PASTA_DOWNLOADS = Path.home() / 'Downloads'

TIPOS_ARQUIVOS = {
    'Imagens': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
    'Videos': ['mp4', 'avi', 'mov', 'mkv', 'flv', 'wmv', '3gp'],
    'Documentos': ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'txt', 'csv', 'odt', 'ods', 'odp'],
    'Arquivos Comprimidos': ['zip', 'rar', '7z', 'tar', 'gz', 'bz2'],
    'Músicas': ['mp3', 'wav', 'flac', 'aac', 'wma', 'ogg'],
    'Aplicativos': ['exe', 'msi', 'apk', 'dmg', 'app', 'ipa']
}

DRY_RUN = True