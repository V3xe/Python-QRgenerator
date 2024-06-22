
from QRmanage import QRcreator


def main() -> None:
    link: str = input('Provide text, link or path to make to qr code -> ')

    qr = QRcreator(link)
    qr.run()


if __name__ == '__main__':
    main()