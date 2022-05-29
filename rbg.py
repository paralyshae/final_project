from PIL import Image
import numpy as np

# Open Image
evidence = Image.open('evidence\\Original\\IMG7.jpg')

# Show Image
evidence.show()

# Get RGB values at (x, y)
colors = evidence.getpixel((369, 170))

# Print RGB values
print (colors)

