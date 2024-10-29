import os
from PIL import Image

# с использованием библиотеки pillow производим вставку изображения поверх другого

filename = 'butterfly.png' # изображение, которое нужно вставлять поверх другого
im1 = Image.open(filename, 'r') # открытие изображения
filename1 = 'zakat_pole.jpg' # изображение поверх которого будет производится вставка другого изображения
im2 = Image.open(filename1, 'r') # открытие изображения
im1 = im1.resize((im1.width//6, im1.height//6)) # уменьшение размера изображения
text_img = Image.new('RGBA', (1000,600), (0, 0, 0, 0)) # создание нового файла
text_img.paste(im2, (0, 0)) # вставка фонового изображения
text_img.paste(im1, ((text_img.width - im1.width) // 2, (text_img.height - im1.height) // 2), mask=im1)
# вставка изображения поверх фонового с применением маски (для того чтобы убрать фон у вставляемого изоборажения
# и расположение изображения по центру фонового
text_img.show() # показать изображение

# отображение формата файла, размера файла, режим изображения
print(im1.format, im1.size, im1.mode)
print(im2.format, im2.size, im2.mode)
