import qrcode
import qrcode.constants

# Cria uma instância de QRCode com as configurações especificadas
qr = qrcode.QRCode(
    version=5,  # Define a versão do QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Define o nível de correção de erro
    box_size=9,  # Define o tamanho de cada caixa do QR Code
    border=3  # Define a largura da borda
)

# Adiciona os dados ao QR Code
qr.add_data("https://senhoralgodao.com.br/")
qr.make(fit=True)  # Ajusta o QR Code para se ajustar aos dados

# Gera a imagem do QR Code com as cores especificadas
imagem = qr.make_image(fill_color="Purple", back_color="white")
# Salva a imagem gerada em um arquivo
imagem.save("QRSrAlgodão.jpg")