import qrcode as qr

def generate_qr_code(data, file_name):
    try:
        img = qr.make(data)
        img.save(file_name+".png")
    except Exception as e:  
        print("Error in generating QR code. Please try again.")
    
    
    
if __name__ == '__main__':
    try:    
        data = input("Enter the data to be stored in the QR code: ")
        file_name = input("Enter the name of the file to save the QR code: ")
        generate_qr_code(data, file_name)
        print("QR code generated successfully!")
    except Exception as e:
        print("Error in generating QR code. Please try again.")