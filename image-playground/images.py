from PIL import Image,ImageFilter

#img = Image.open('./Images/Pikachu.jpg')

# Blur
#blur_img = img.filter(ImageFilter.BLUR)
#blur_img.save("./convert_images/blur.png",'png')

# Convert to gray
#gray_img = img.convert('L')
#gray_img.save("./convert_images/grey.png",'png')
#gray_img.show()

# rotate images
#rotate_img = img.convert('L')
#rotate_img = rotate_img.rotate(90)
#rotate_img.save("./convert_images/rotate.png",'png')

# resize image
#resize_img = img.convert('L')
#resize_img = resize_img.resize((500, 500))
#resize_img.save("./convert_images/resize.png",'png')

# crop
#crop_img = img.convert('L')
#box = (100,100,400,400)
#region = crop_img.crop(box)
#region.save("./convert_images/crop.png",'png')

# thumbnail
imge = Image.open('./Images/developer.jpg')
imge.thumbnail((400,200))
imge.save('./convert_images/thumbnail_img.png','png')