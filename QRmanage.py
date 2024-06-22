import segno
import uuid
import os
from typing import Callable
from sys import platform
class QRcreator:
    def __init__(self,text_to_code:str):
        self._text_to_code = text_to_code


    def _gather_requirements(self) -> dict:
        anwsers: dict = {}
        print('Asked questions will specify how qr code will look')

        q1 = input('Do you want to create random name for qr code? [y/n]')
        if q1.lower() == 'y':
            anwsers['q1'] = str(uuid.uuid4())+'.png'
        elif q1.lower() == 'n':
            q1 = input('Provide name to qr code -> ')
            anwsers['q1'] = q1+'.png'

        q2 = input('Input set scale of qr code in pixels -> ')
        anwsers['q2'] = q2

        q3 = input('Do you want to set border to qr code? [y/n]')
        if q3.lower() == 'y':
            q3 = input('Provide size of border -> ')
            anwsers['q3'] = int(q3)
        elif q3.lower() == 'n':
            anwsers['q3'] = ''
            print('Border won\'t be added')

        q4 = input('Provide path to save qr code -> ')
        anwsers['q4'] = q4

        return anwsers

    def _prepare_qr(self,requirements: dict) -> None:
        print('Creating QR code...')
        try:
            qrcode = segno.make_qr(self._text_to_code)
            if requirements['q3'] != '':
                qrcode.save(
                    os.path.join(str(requirements['q4']), str(requirements['q1'])),
                    scale=requirements['q2'],
                    border=requirements['q3']
                )
            else:
                qrcode.save(
                    os.path.join(str(requirements['q4']), str(requirements['q1'])),
                    scale=requirements['q2']
                )

            print('QR created...')
        except FileNotFoundError as e:
            print(f'Path to save file not found -> {requirements['q4']}')
    def run(self):
        requirements: dict = self._gather_requirements()
        self._prepare_qr(requirements)
