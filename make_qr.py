
import qrcode

# آدرس عمومی اپلیکیشن Streamlit را اینجا قرار بده
url = "https://YOUR-APP-NAME.streamlit.app"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=4
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(
    fill_color="black",
    back_color="white"
)

img.save("rang_behesht_qr.png")

print("QR Code ساخته شد!")
