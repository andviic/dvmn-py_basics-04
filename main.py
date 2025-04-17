from PIL import Image

image = Image.open('monro.jpg')
red, green, blue = image.split()
scale = 50

red_croped_1 = red.crop((scale, 0, red.width, red.height))
red_croped_2 = red.crop((scale / 2, 0, red.width - scale / 2, red.height))
red_chanel = Image.blend(red_croped_1, red_croped_2, 0.5)

blue_croped_1 = blue.crop((0, 0, blue.width - scale, blue.height))
blue_croped_2 = blue.crop((scale / 2, 0, blue.width - scale / 2, blue.height))
blue_chanel = Image.blend(blue_croped_1, blue_croped_2, 0.5)

green_chanel = green.crop((scale / 2, 0, green.width - scale / 2,
                           green.height))

final_image = Image.merge('RGB', (red_chanel, green_chanel, blue_chanel))
final_image.save('monro_final.jpg')
final_image.thumbnail((80, 80))
final_image.save('monro_avatar.jpg')
