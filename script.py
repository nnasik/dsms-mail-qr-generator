import qrcode
from PIL import Image, ImageDraw, ImageFont

qr_no = 35
file_name_1 = qr_no

link = "https://dsms.koralaipattuwest.ds.gov.lk/mail/view/"
a4 = Image.new('RGB', (2481, 3507), color = 'white')
# get a font
fnt = ImageFont.truetype("C:/Windows/Fonts/Calibri.ttf", 40)

for i in range(1,49):
    
    img = qrcode.make(link+str(qr_no))
    
    #img = img.copy()
    # get a drawing context
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((0,0,410,409),radius=20, fill=None, outline=None, width=1)

    # draw multiline text
    d.multiline_text((90, 380), "DSMS Mail : " + str(qr_no), font=fnt)
    
    a4.paste(img, (((i-1)%6)*410+10, (((i-1)//6)*410)+((i-1)//6)*20))
    qr_no+=1

a4.save(str(file_name_1)+"-"+str(qr_no-1)+"_A4.png")







