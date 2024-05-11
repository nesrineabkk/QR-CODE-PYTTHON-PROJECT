from typing import Union

from urllib.parse import urlparse

import segno


def read_url(content: str) -> Union[str, None]:
   if content.startswith('https'):
        print('Your URL is correct ' , content)
        return  content
   
   print('Your URL is incorrect ', content)
   return None 

def convert_url_into_qr_code(url: str):
    qr_code = segno.make(url)

    parsed_url = urlparse(url)
   
    # The current directory should now contain the `qr.svg` file.
    qr_code.save(f'qr_output/qr_{parsed_url.hostname}.svg', scale=4)
