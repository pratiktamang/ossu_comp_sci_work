# import urllib.request

# BASE_URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
# NOTHING = "?nothing="
# num = "12345"
# progress = "."
# increment = True

# url = BASE_URL + NOTHING + num


# def print_progress(progress, increment):
#     if len(progress) <= 30 and increment:
#         progress += "."
#     elif len(progress) > 30:
#         increment = False

#     if not increment:
#         if len(progress) > 1:
#             # Remove the last character
#             progress = progress[:-1]
#         else:
#             # Reset the increment when progress is back to 1 dot
#             increment = True

#     print(progress)
#     return progress, increment


# while True:
#     content = str(urllib.request.urlopen(url).read())
#     next_num = content.split("'")[1].split(" ")[-1]

#     if next_num.isdigit():
#         num = next_num
#         url = BASE_URL + NOTHING + num
#     elif next_num == "going.":
#         num = str(int(num) / 2)
#         url = BASE_URL + NOTHING + num
#     else:
#         print(content)
#         break

#     progress, increment = print_progress(progress, increment)

# # peak

import requests

BASE_URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
num = "12345"

while True:
    response = requests.get(f"{BASE_URL}?nothing={num}")
    content = response.text
    print(content)

    if "and the next nothing is" in content:
        num = content.split()[-1]
    elif "Divide by two" in content:
        num = str(int(num) // 2)
    else:
        break


# Ruby

# require 'net/http'
# require 'uri'

# BASE_URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
# NOTHING_PARAM = "?nothing="
# num = "12345"

# def fetch_content(url)
#   uri = URI(url)
#   response = Net::HTTP.get_response(uri)
#   response.body if response.is_a?(Net::HTTPSuccess)
# end

# while true
#   url = BASE_URL + NOTHING_PARAM + num
#   content = fetch_content(url)

#   puts content

#   if content.include?('Divide by two')
#     num = (num.to_i / 2).to_s
#   elsif content =~ /and the next nothing is (\d+)/
#     num = $1
#   else
#     break
#   end
# end
