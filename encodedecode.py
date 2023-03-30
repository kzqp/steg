from PIL import Image

bytes = []
bits = 0

def encode(binary, image):
    with Image.open(image) as img:
        if len(binary) > img.width * img.height * 3:
            print("Your image file is not large enough to hide your text.")
        else:
            b, x, y, i, j = 0, 0, 0, 0, 0
            while b < len(binary):
                if x == img.width:
                    x = 0
                    y += 1
                color = img.getpixel((x,y))
                cl = list(color)
                while i < 3:
                    if b < len(binary):
                        bi = bin(color[i])[2:].zfill(8)
                        c = bi[:-1] + binary[b]
                        cl[i] = int(c, 2)
                        b += 1
                        i += 1
                        j += 1
                    else:
                        break
                img.putpixel((x,y), tuple(cl))

                i = 0
                x += 1
            img.save("tmp.png", compress_level=9)
            return(0)

def nulterminated(bit):
    global bits

    if len(bytes) < 8:
        bytes.insert(8, bit)
        bits += 1
        return False
    else:
        if bytes.count('0') == 8 and bits % 8 == 0:
            return True
        elif bits % 8 == 0:
            bytes.clear()
            bytes.insert(8, bit)
            bits += 1
            return False
        else:
            bytes.insert(8, bit)
            bits += 1
            return False
    
def decode(image):
    binary = ''
    with Image.open(image) as img:
        x, y, i = 0, 0, 0
        while y < img.height:
            while x < img.width:
                color = img.getpixel((x,y))
                while i < 3:
                    b = bin(color[i])[-1]
                    binary += b
                    if nulterminated(b):
                        return(binary)
                    i += 1
                i = 0
                x += 1
            y += 1
            x = 0
            
def write(image):
    with Image.open(image) as img:
        img.save("copy.png", compress_level=9)
