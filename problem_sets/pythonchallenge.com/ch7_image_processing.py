"http://www.pythonchallenge.com/pc/def/oxygen.html"
# image = Image.open(requests.get(url, stream=True).raw)
import re
from PIL import Image

# url = "http://www.pythonchallenge.com/pc/def/oxygen.png"
# import requests
# from io import BytesIO
# from PIL import Image
# img = Image.open(BytesIO(requests.get(url)).content))

# Open an image file
img = Image.open("./Oxygen.png")
# get just the row with gray colours
pixel = img.getpixel((x, img.height / 2))
gray_row = [pixel for x in range(img.width)]
# the color sizes are 7 pixels, manually counted.. although first one is 5
# check every 7th item
gray_row = gray_row[::7]

# Get the red component of each color since each color is grayscale
# pixel stored as [r,g,b,a]
ord_list = [r for r, g, b, a in gray_row if r == g == b]
print(ord_list)
content = "".join(map(chr, ord_list))
nums = nums = re.findall("\d+", content)
ints = map(int, nums)
print("".join(map(chr, ints)))


# gray_row = [(115, 115, 115, 255), (115, 115, 115, 255), (115, 115, 115, 255), (115, 115, 115, 255), (115, 115, 115, 255), (109, 109, 109, 255), (109, 109, 109, 255), (109, 109, 109, 255), (109, 109, 109, 255), (109, 109, 109, 255), (109, 109, 109, 255), (109, 109, 109, 255), (97, 97, 97, 255), (97, 97, 97, 255), (97, 97, 97, 255), (97, 97, 97, 255), (97, 97, 97, 255), (97, 97, 97, 255), (97, 97, 97, 255), (114, 114, 114, 255), (114, 114, 114, 255), (114, 114, 114, 255), (114, 114, 114, 255), (114, 114, 114, 255), (114, 114, 114, 255), (114, 114, 114, 255), (116, 116, 116, 255), (116, 116, 116, 255), (116, 116, 116, 255), (116, 116, 116, 255), (116, 116, 116, 255), (116, 116, 116, 255), (116, 116, 116, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (103, 103, 103, 255), (103, 103, 103, 255), (103, 103, 103, 255), (103, 103, 103, 255), (103, 103, 103, 255), (103, 103, 103, 255), (103, 103, 103, 255), (117, 117, 117, 255), (117, 117, 117, 255), (117, 117, 117, 255), (117, 117, 117, 255), (117, 117, 117, 255), (117, 117, 117, 255), (117, 117, 117, 255), (121, 121, 121, 255), (121, 121, 121, 255), (121, 121, 121, 255), (121, 121, 121, 255), (121, 121, 121, 255), (121, 121, 121, 255), (121, 121, 121, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (121, 121, 121, 255), (121, 121, 121, 255), (121, 121, 121, 255), (121, 121, 121, 255), (121, 121, 121, 255), (121, 121, 121, 255), (121, 121, 121, 255), (111, 111, 111, 255), (111, 111, 111, 255), (111, 111, 111, 255), (111, 111, 111, 255), (111, 111, 111, 255), (111, 111, 111, 255), (111, 111, 111, 255), (117, 117, 117, 255), (117, 117, 117, 255), (117, 117, 117, 255), (117, 117, 117, 255), (117, 117, 117, 255), (117, 117, 117, 255), (117, 117, 117, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (109, 109, 109, 255), (109, 109, 109, 255), (109, 109, 109, 255), (109, 109, 109, 255), (109, 109, 109, 255), (109, 109, 109, 255), (109, 109, 109, 255), (97, 97, 97, 255), (97, 97, 97, 255), (97, 97, 97, 255), (97, 97, 97, 255), (97, 97, 97, 255), (97, 97, 97, 255), (97, 97, 97, 255), (100, 100, 100, 255), (100, 100, 100, 255), (100, 100, 100, 255), (100, 100, 100, 255), (100, 100, 100, 255), (100, 100, 100, 255), (100, 100, 100, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (105, 105, 105, 255), (105, 105, 105, 255), (105, 105, 105, 255), (105, 105, 105, 255), (105, 105, 105, 255), (105, 105, 105, 255), (105, 105, 105, 255), (116, 116, 116, 255), (116, 116, 116, 255), (116, 116, 116, 255), (116, 116, 116, 255), (116, 116, 116, 255), (116, 116, 116, 255), (116, 116, 116, 255), (46, 46, 46, 255), (46, 46, 46, 255), (46, 46, 46, 255), (46, 46, 46, 255), (46, 46, 46, 255), (46, 46, 46, 255), (46, 46, 46, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (116, 116, 116, 255), (116, 116, 116, 255), (116, 116, 116, 255), (116, 116, 116, 255), (116, 116, 116, 255), (116, 116, 116, 255), (116, 116, 116, 255), (104, 104, 104, 255), (104, 104, 104, 255), (104, 104, 104, 255), (104, 104, 104, 255), (104, 104, 104, 255), (104, 104, 104, 255), (104, 104, 104, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (110, 110, 110, 255), (110, 110, 110, 255), (110, 110, 110, 255), (110, 110, 110, 255), (110, 110, 110, 255), (110, 110, 110, 255), (110, 110, 110, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (120, 120, 120, 255), (120, 120, 120, 255), (120, 120, 120, 255), (120, 120, 120, 255), (120, 120, 120, 255), (120, 120, 120, 255), (120, 120, 120, 255), (116, 116, 116, 255), (116, 116, 116, 255), (116, 116, 116, 255), (116, 116, 116, 255), (116, 116, 116, 255), (116, 116, 116, 255), (116, 116, 116, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (108, 108, 108, 255), (108, 108, 108, 255), (108, 108, 108, 255), (108, 108, 108, 255), (108, 108, 108, 255), (108, 108, 108, 255), (108, 108, 108, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (118, 118, 118, 255), (118, 118, 118, 255), (118, 118, 118, 255), (118, 118, 118, 255), (118, 118, 118, 255), (118, 118, 118, 255), (118, 118, 118, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (101, 101, 101, 255), (108, 108, 108, 255), (108, 108, 108, 255), (108, 108, 108, 255), (108, 108, 108, 255), (108, 108, 108, 255), (108, 108, 108, 255), (108, 108, 108, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (105, 105, 105, 255), (105, 105, 105, 255), (105, 105, 105, 255), (105, 105, 105, 255), (105, 105, 105, 255), (105, 105, 105, 255), (105, 105, 105, 255), (115, 115, 115, 255), (115, 115, 115, 255), (115, 115, 115, 255), (115, 115, 115, 255), (115, 115, 115, 255), (115, 115, 115, 255), (115, 115, 115, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (91, 91, 91, 255), (91, 91, 91, 255), (91, 91, 91, 255), (91, 91, 91, 255), (91, 91, 91, 255), (91, 91, 91, 255), (91, 91, 91, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (53, 53, 53, 255), (53, 53, 53, 255), (53, 53, 53, 255), (53, 53, 53, 255), (53, 53, 53, 255), (53, 53, 53, 255), (53, 53, 53, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (54, 54, 54, 255), (54, 54, 54, 255), (54, 54, 54, 255), (54, 54, 54, 255), (54, 54, 54, 255), (54, 54, 54, 255), (54, 54, 54, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (51, 51, 51, 255), (51, 51, 51, 255), (51, 51, 51, 255), (51, 51, 51, 255), (51, 51, 51, 255), (51, 51, 51, 255), (51, 51, 51, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (52, 52, 52, 255), (52, 52, 52, 255), (52, 52, 52, 255), (52, 52, 52, 255), (52, 52, 52, 255), (52, 52, 52, 255), (52, 52, 52, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (48, 48, 48, 255), (53, 53, 53, 255), (53, 53, 53, 255), (53, 53, 53, 255), (53, 53, 53, 255), (53, 53, 53, 255), (53, 53, 53, 255), (53, 53, 53, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (54, 54, 54, 255), (54, 54, 54, 255), (54, 54, 54, 255), (54, 54, 54, 255), (54, 54, 54, 255), (54, 54, 54, 255), (54, 54, 54, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (44, 44, 44, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (32, 32, 32, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (50, 50, 50, 255), (50, 50, 50, 255), (50, 50, 50, 255), (50, 50, 50, 255), (50, 50, 50, 255), (50, 50, 50, 255), (50, 50, 50, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (49, 49, 49, 255), (93, 93, 93, 255), (93, 93, 93, 255), (93, 93, 93, 255), (93, 93, 93, 255), (93, 93, 93, 255), (93, 93, 93, 255), (93, 93, 93, 255), (93, 93, 93, 255), (114, 112, 71, 255), (112, 110, 69, 255), (110, 108, 67, 255), (103, 100, 59, 255), (98, 95, 54, 255), (101, 98, 55, 255), (109, 105, 60, 255), (107, 100, 58, 255), (101, 92, 51, 255), (106, 97, 58, 255), (108, 99, 60, 255), (102, 94, 57, 255), (99, 91, 54, 255), (97, 87, 51, 255), (94, 82, 44, 255), (95, 83, 45, 255), (98, 86, 48, 255), (97, 84, 49, 255), (95, 82, 47, 255), (97, 83, 46, 255), (99, 85, 46, 255)]
# ord_list = [115, 109, 97, 114, 116, 32, 103, 117, 121, 44, 32, 121, 111, 117, 32, 109, 97, 100, 101, 32, 105, 116, 46, 32, 116, 104, 101, 32, 110, 101, 120, 116, 32, 108, 101, 118, 101, 108, 32, 105, 115, 32, 91, 49, 48, 53, 44, 32, 49, 49, 48, 44, 32, 49, 49, 54, 44, 32, 49, 48, 49, 44, 32, 49, 48, 51, 44, 32, 49, 49, 52, 44, 32, 49, 48, 53, 44, 32, 49, 49, 54, 44, 32, 49, 50, 49, 93]
# num = ['105', '110', '116', '101', '103', '114', '105', '116', '121']
# content = smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
# integrity


"""
RUBY

require 'chunky_png'
require 'set'

# Open the image
image = ChunkyPNG::Image.from_file('Oxygen.png')

# Get the row with gray colors
gray_row = (0...image.width).map { |x| image[x, image.height / 2] }

# Check every 7th item
gray_row = gray_row.each_slice(7).map(&:first)

# Get the red component of each color (assuming the image is grayscale)
ord_list = gray_row.map { |color| ChunkyPNG::Color.r(color) }

# Convert the list of ASCII values to characters
content = ord_list.map(&:chr).join

# Extract numbers from the string
nums = content.scan(/\d+/)

# Convert the numbers to ASCII values and then to characters
result = nums.map(&:to_i).map(&:chr).join

puts result

"""
