import src.qr_code.qr_code as qr_code


def main():
   url = qr_code.read_url(content='https://google.com')
   qr_code.convert_url_into_qr_code(url=url)


if __name__ == '__main__':
    main()
