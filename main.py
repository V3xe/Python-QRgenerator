import segno
import uuid

class QRmaker:
    def __init__(self,link: str,uuid: uuid,scale: int) -> None:
        self._link = link
        self._uuid = uuid
        self._scale = scale
    #Creating QR code, provide link to website
    def create_code(self):
        qrcode = segno.make_qr(self._link)
        qrcode.save(
            str(self._uuid)+'.png',
            scale=self._scale
        )
def main() -> None:
    link: str = input('Please provide link to change to qr code: ')

    qr = QRmaker(link,uuid.uuid4(),5)
    qr.create_code()
    print('QR generated..')


if __name__ == '__main__':
    main()