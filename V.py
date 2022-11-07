import qrcode
ls=[]
img=[]
for i in range(2):

    n=input("enter name")
    a=input("adress")
    ph=input("phno")

    ls=[n,a,ph]
    print (ls)
    img.append(ls)
    
j=0 
for i in img:
    j+=1
    a=str(j)
    im = qrcode.make(i)
    type(im)  # qrcode.image.pil.PilImage
    im.save(a+".png")