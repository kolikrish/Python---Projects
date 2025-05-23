import qrcode

upi_id = input('Enter Your UPI ID: ')

# Generate UPI URLs
upi_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# Generate QR codes
phonepe_qr = qrcode.make(upi_url)
paytm_qr = qrcode.make(upi_url)
google_pay_qr = qrcode.make(upi_url)

# Save QR code images
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

# Display QR codes
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

