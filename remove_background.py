from PIL import Image #para abrir a imagem
from rembg import remove #para remover o fundo

#aplicando a imagem em uma varíavel
img = Image.open('local_do_arquivo\nome_do_arquivo.png')

#removendo o fundo da imagem
img_semfundo = remove(img)

#salvando a imagem
img_semfundo.save('local_do_arquivo\nome_do_novo_arquivo.png')