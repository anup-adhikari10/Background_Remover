from rembg import remove
from PIL import Image
input_path = 'anup.jpg'
output_path = 'clanup.png'
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
Image.open("clanup.png")