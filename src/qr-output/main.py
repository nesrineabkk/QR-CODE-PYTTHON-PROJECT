from qr_code import read_url, convert_url_into_qr_code

def main():
   url = read_url(content='https://google.com')
   convert_url_into_qr_code(url=url)
if __name__ == '__main__':
   main()