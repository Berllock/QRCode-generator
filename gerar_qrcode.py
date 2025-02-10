import qrcode
import qrcode.constants

# Cria uma instância de QRCode com as configurações especificadas
qr = qrcode.QRCode(
    version=5,  # Define a versão do QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Define o nível de correção de erro
    box_size=9,  # Define o tamanho de cada caixa do QR Code
    border=3  # Define a largura da borda
)

# Requere a entrada de dados do QR Code
qr_Data = input("Insira o dado para o QRCode: ")
# Requere o nome e formato do arquivo que será gerado
qr_Name = input("Insira o nome do arquivo e formato: ")

# Adiciona os dados ao QR Code
qr.add_data(qr_Data)
qr.make(fit=True)  # Ajusta o QR Code para se ajustar aos dados

# Gera a imagem do QR Code com as cores especificadas
imagem = qr.make_image()
# Salva a imagem gerada em um arquivo
imagem.save(qr_Name)