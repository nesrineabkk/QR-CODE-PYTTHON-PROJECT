import qrcode
import svgwrite
import os

class QRGenerator:
    
    def __init__(self, url: str):
        self.url = url