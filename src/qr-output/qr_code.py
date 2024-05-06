import segno


def read_url(content: str) -> str:
   if  content.startswith("https"):
        print("Your URL is Correct " , content)
        return  content
   else:
        print("Your URL is incorrect", content)
        return None 

   
def convert_url_into_qr_code(url: str):
     
   qrcode = segno.make(url, error='h')
# The current directory should now contain the `qr.svg` file.
   qrcode.save('qr_code_project.svg', scale=4)




                      

                      