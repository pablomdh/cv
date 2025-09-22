from pdf2image import convert_from_path

pages = convert_from_path("Pablo_Dubourdieu_CV.pdf", dpi=150)
pages[0].save("preview.png", "PNG")
