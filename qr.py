import qrcode as qr
link=input("enetr :")
img= qr.make(link)
img = qr.make(fill_color = 'red',back_color = 'white')
img.save("github.png")