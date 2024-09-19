import qrcode

from PIL import Image

def generate_qr_code(data, file_name):
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=5,
        )
        
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        try:
            logo = Image.open("logo.png")
            basewidth = 70
            wpercent = (basewidth / float(logo.size[0]))
            hsize = int((float(logo.size[1]) * float(wpercent)))
            logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
            
            img = img.convert("RGBA")
            logo = logo.convert("RGBA")
            
            pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
            
            img.paste(logo, pos, logo)
            
        except FileNotFoundError:
            print("Logo file not found")
        except  Exception as e:
            print("Error with logo processing: ", e)
            
        img.save(file_name + ".png")
        
    except Exception as e:
        print("Error with QR code generation: ", e)
        
        

if __name__ == "__main__":
    try:
        data = input("Enter data to encode: ")
        file_name = input("Enter file name: ")
        
        generate_qr_code(data, file_name)
    except Exception as e:
        print("Error: ", e)
            