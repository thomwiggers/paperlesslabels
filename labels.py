import AveryLabels
from reportlab.lib.units import mm, cm
from reportlab_qrcode import QRCodeImage


    # 123inkt 38x21,2
AveryLabels.labelInfo["123inkt ASN"] = (5, 13, (38.1*mm, 21.2*mm), (0.3*mm, 0), (10.0*mm, 10.3*mm))

startASN = 1

def render(c,x,y):
    global startASN
    barcode_value = f"ASN{startASN:05d}"
    startASN = startASN + 1

    qr = QRCodeImage(barcode_value, size=y*0.9)
    qr.drawOn(c,1*mm,y*0.05)
    c.setFont("Helvetica", 2*mm)
    c.drawString(y, (y-2*mm)/2, barcode_value)
    print(x)
    print(y)


label = AveryLabels.AveryLabel("123inkt ASN")
label.open( "paperlesslabels.pdf" )
label.render(render, 65 )
label.close()

