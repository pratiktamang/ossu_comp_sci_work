# http://www.pythonchallenge.com/pc/def/channel.html

import os
import pdb

# directory = "./ch6_unzip_files/Now There Are Pairs/"
# comments = []

# for filename in os.listdir(directory):
#     file_path = os.path.join(directory, filename)
#     if os.path.isfile(file_path):
#         f = open(file_path, "r")
#         line = f.readline()
#         if not line.startswith("Next nothing is "):
#             comments.append(line)
#             print("-----")
#             print(line)
#             print("-----")
# ans = zip(comments)
# print(list(ans))

import zipfile


def hint():
    comments = []
    num = "90052"
    zipped_file = zipfile.ZipFile("./ch6_zip_file.zip")

    while True:
        file = num + ".txt"
        content = zipped_file.read(file).decode("utf-8")
        comments.append(zipped_file.getinfo(file).comment.decode("utf-8"))
        if content.startswith("Next nothing is "):
            num = content.split(" ")[-1]
        else:
            break
    print("".join(comments))


hint()

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
