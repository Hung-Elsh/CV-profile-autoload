import pytesseract
from PIL import Image
from pdf2image import convert_from_bytes
from io import BytesIO

class TesseractHeplperPDFScan():

    def __init__(self, b64string):
        self.string_pdf = b64string
        self.extracted_information = ""
        self.string_image = b64string 

    def __conver_to_jpg(self):
        try:
            pdf_pages = convert_from_bytes(BytesIO.open(self.string_pdf)) 
            pdf_pages.save('converted.jpg', 'JPEG')
            return True
        except Exception:
        
            return False
        

    def __reading_jpg(self, is_pdf=False):
        if is_pdf:
            try:
                self.extracted_information = str(((pytesseract.image_to_string(Image.open('./converted_images/converted.jpg'), lang='vie'))))
                return True
            except Exception:
                self.extracted_information = str(((pytesseract.image_to_string(Image.open(BytesIO(self.string_pdf)), lang='vie'))))
            else:
                return False
        else:
            try:
                self.extracted_information = str(((pytesseract.image_to_string(Image.open(BytesIO(self.string_image)), lang='vie'))))
            except Exception:
                return False
        
    def Scann_pdf(self):
        is_pdf = self.__conver_to_jpg()
        read_sucess = self.__reading_jpg(is_pdf)
        if read_sucess:
            return self.extracted_information
        else:
            return False
    
    def Scann_image(self):
        self.__reading_jpg(False)
        return self.extracted_information


if __name__ == '__main__':
    ts = TesseractHeplperPDFScan('./converted_images/mau-cong-van-de-nghi-1-e1577117362136.jpg')
    ts.Scann_image()
    print(ts.extracted_information)
    f = open('ext.txt', 'w')
    f.write(ts.extracted_information)
    f.close()
