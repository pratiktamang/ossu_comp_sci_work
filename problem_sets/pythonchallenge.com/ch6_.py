# http://www.pythonchallenge.com/pc/def/channel.html
# import zipfile


# def hint():
#     comments = []
#     num = "90052"
#     zipped_file = zipfile.ZipFile("./ch6_zip_file.zip")

#     while True:
#         file = num + ".txt"
#         content = zipped_file.read(file).decode("utf-8")
#         comments.append(zipped_file.getinfo(file).comment.decode("utf-8"))
#         if content.startswith("Next nothing is "):
#             num = content.split(" ")[-1]
#         else:
#             break
#     print("".join(comments))


# hint()

# with regular expression
import zipfile, re

f = zipfile.ZipFile("./ch6_zip_file.zip")
print(f.read("readme.txt").decode("utf-8"))

num = "90052"

comments = []

while True:
    content = f.read(num + ".txt").decode("utf-8")
    comments.append(f.getinfo(num + ".txt").comment.decode("utf-8"))
    print(content)
    match = re.search("Next nothing is (\d+)", content)
    if match == None:
        break
    num = match.group(1)

print("".join(comments))


"""
****************************************************************
****************************************************************
**                                                            **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
**   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
**   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
**                                                            **
****************************************************************
 **************************************************************
"""

"""

RUBY

require 'zip'

def hint
  comments = []
  num = "90052"
  zipped_file = Zip::File.open("./ch6_zip_file.zip")

  while true
    file = num + ".txt"
    content = zipped_file.get_entry(file).get_input_stream.read
    comments << zipped_file.get_entry(file).comment
    if content.start_with?("Next nothing is ")
      num = content.split(" ").last
    else
      break
    end
  end
  puts comments.join
end

hint



"""
