# como remover fundo de imagens com Python

uma das principais ferramentas utilizadas no design é a remoção de fundo para a criação de artes. [neste código](https://github.com/claysfx/remove_background/blob/main/remove_background.ipynb) de poucas linhas, você conseguirá fazer essa remoção de forma automatizada.

---

1. instale as seguintes bibliotecas:
 * Pillow/PIL: biblioteca que adiciona suporte à abertura e gravação de imagens
``` bash
pip install pillow
```

 * Rembg: ferramenta para a remoção de "backgrounds"
``` bash
pip install rembg
```
---
2. importe as funcionalidades das bibliotecas:
``` bash
from PIL import Image
from rembg import remove
```
---
3. utilize **Image.open()** para aplicar a imagem em uma variável:
``` bash
img = Image.open('local_do_arquivo\nome_do_arquivo.png')
```
---
4. utilize **remove()** para remover o fundo da imagem:
``` bash
img_semfundo = remove(img)
```
---
5. após a finalização, baixe a imagem utilizando **save()**
``` bash
img_semfundo.save('local_do_arquivo\nome_do_novo_arquivo.png')
```
---
imagem anterior:
<p float="left">
 <img src="https://github.com/claysfx/remove_background/blob/main/Curva-Concepts-C300-Staggered-Ford-Mustang-Wheels-1.jpg" width="400" />
</p>
imagem após a remoção:
<p float="left">
 <img src="https://github.com/claysfx/remove_background/blob/main/imagem_sem_fundo.png" width="400" />
</p>

---
para conhecer mais sobre as bibliotecas utilizadas, acesse: [Pillow/PIL](https://pypi.org/project/Pillow/) / [Rembg](https://github.com/danielgatis/rembg)
