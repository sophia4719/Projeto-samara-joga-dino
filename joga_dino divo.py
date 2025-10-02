import os
import pyautogui as auto

CAMINHO_PASTA = os.getcwd()
print("caminho da pasta:", CAMINHO_PASTA )

CAMINHO_PASTA_IMAGENS = os.path.join(CAMINHO_PASTA,  ".\\automacao\\img")
print("caminho da pasta imagens:", CAMINHO_PASTA_IMAGENS)

lista_foto = os.listdir (CAMINHO_PASTA_IMAGENS)
print("conteudo da lista de foto:",lista_foto)

caminho_dino = os.path.join (CAMINHO_PASTA,".\\automaçao\\dino.png")

while True:
    for foto in lista_foto:
        caminho_da_foto = os.path.join (CAMINHO_PASTA_IMAGENS, foto)
    try:
        posicao_cacto = auto.locateOnScreen (caminho_da_foto, confidence=0.6)
        posicao_dino = auto.locateOnScreen (caminho_dino, confidence= 0.6)

    except:
        posicao_cacto = None

    else:
        print ("posiçao do cacto:", posicao_cacto.left) 
        print("posicao do dino:", posicao_dino.left)

        if posicao_cacto.left = posicao_dino.left <= 170:
            auto.press ("space")
            auto.keyDown ("space")