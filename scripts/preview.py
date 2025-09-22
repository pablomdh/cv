import fitz  # PyMuPDF
from PIL import Image

# Input y output en la carpeta "output"
pdf_path = "output/Pablo_Dubourdieu_CV.pdf"
preview_path = "output/preview.png"

# Abrir el PDF
doc = fitz.open(pdf_path)
page = doc[0]  # primera página

# Generar imagen (150 dpi recomendado para preview en README)
pix = page.get_pixmap(dpi=150)
img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

# Guardar preview
img.save(preview_path)
