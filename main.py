from PIL import Image

# red = Image.open('monro_red.jpg')
# green = Image.open('monro_green.jpg')
# blue = Image.open('monro_blue.jpg')

image = Image.open('monro.jpg')
red, green, blue = image.split()

# red.save('monro_red.jpg')
# green.save('monro_green.jpg')
# blue.save('monro_blue.jpg')

scale = 100

red_croped = red.crop((scale, 0, red.width, red.height))
blue_croped = blue.crop((scale / 2, 0, blue.width - scale / 2, blue.height))

# red_croped.save('monro_red_croped.jpg')
# blue_croped.save('monro_blue_croped.jpg')

# red_croped = Image.open('monro_red_croped.jpg')
# blue_croped = Image.open('monro_blue_croped.jpg')

image = Image.blend(red_croped, blue_croped, 0.3)

image.save('monro_mixed.jpg')

# print(image.width)
# print(image.height)
# print(image.mode)
