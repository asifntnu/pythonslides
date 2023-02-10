import image

img = image.Image('Asif\\Desktop\\pythonslides\\test.gif')
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,15)   # setDelay(0) turns off animation
#hello test
for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)
#make some changes
        newred = 255 - p.getRed()
        newgreen = 255 - p.getGreen()
        newblue = 255 - p.getBlue()

        newpixel = image.Pixel(newred, newgreen, newblue)

        img.setPixel(col, row, newpixel)
        img.draw(win)
img.draw(win)
win.exitonclick()
#this is first feature
