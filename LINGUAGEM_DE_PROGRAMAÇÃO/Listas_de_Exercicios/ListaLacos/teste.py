from PIL import Image
 
# Lista de caracteres do mais escuro para o mais claro
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
 
def redimensionar_imagem(imagem, nova_largura=100):
    largura_original, altura_original = imagem.size
    proporcao = altura_original / largura_original / 1.65
    nova_altura = int(nova_largura * proporcao)
    return imagem.resize((nova_largura, nova_altura))
 
def cinza(imagem):
    return imagem.convert("L")
 
def pixels_para_ascii(imagem):
    pixels = imagem.getdata()
    return "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
 
def converter_para_ascii(caminho_imagem, nova_largura=100):
    try:
        imagem = Image.open(caminho_imagem)
    except Exception as e:
        print("Erro ao abrir a imagem:", e)
        return
   
    imagem = redimensionar_imagem(imagem, nova_largura)
    imagem_cinza = cinza(imagem)
   
    string_ascii = pixels_para_ascii(imagem_cinza)
    largura_linha = imagem_cinza.width
   
    # Divide a string ascii no tamanho da largura da linha
    imagem_ascii = "\n".join([string_ascii[i:(i + largura_linha)] for i in range(0, len(string_ascii), largura_linha)])
    print(imagem_ascii)
 
# Insira o caminho da sua imagem aqui
converter_para_ascii("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLbZ4imzNFQ3i8X67iXA_7o2hndreU_wD4QD5RzOE4UVYVaK1R-C1_MA23&s=10")