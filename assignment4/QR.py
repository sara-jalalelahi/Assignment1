
import qrcode
container=input('enter text:'),'\n',input('enter adress:')
qr=qrcode.make(container)
qr.save('qrcode_assignment4.jpg')

