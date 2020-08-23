from PIL import Image
from PIL import ImageFilter

img=Image.open('./images/charmander.jpg')
print (img.size)

gray_image=img.convert('L')
gray_image.thumbnail((200,200))
gray_image.save('gray.png','png')