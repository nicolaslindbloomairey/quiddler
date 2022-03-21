import pygame.image as image
import csv

IMAGE_DICT = {}

base_folder = "images/version2/"
image_extension = ".png"

letters = []
with open("data/quiddler_cards.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        letters.append(row["Card"])

IMAGE_DICT["template"] = image.load("images/template.png")
IMAGE_DICT["back"] = image.load(base_folder + "back" + image_extension)
for L in letters:
    IMAGE_DICT[L] = image.load(base_folder + L + image_extension)

#IMAGE_DICT["A"] = image.load("images/version1/A.png")
#IMAGE_DICT["B"] = image.load("images/version1/B.png")
#IMAGE_DICT["C"] = image.load("images/version1/C.png")
#IMAGE_DICT["D"] = image.load("images/version1/D.png")
#IMAGE_DICT["E"] = image.load("images/version1/E.png")
#IMAGE_DICT["F"] = image.load("images/version1/F.png")
#IMAGE_DICT["G"] = image.load("images/version1/G.png")
#IMAGE_DICT["H"] = image.load("images/version1/H.png")
#IMAGE_DICT["I"] = image.load("images/version1/I.png")
#IMAGE_DICT["J"] = image.load("images/version1/J.png")
#IMAGE_DICT["K"] = image.load("images/version1/K.png")
#IMAGE_DICT["L"] = image.load("images/version1/L.png")
#IMAGE_DICT["M"] = image.load("images/version1/M.png")
#IMAGE_DICT["N"] = image.load("images/version1/N.png")
#IMAGE_DICT["O"] = image.load("images/version1/O.png")
#IMAGE_DICT["P"] = image.load("images/version1/P.png")
#IMAGE_DICT["Q"] = image.load("images/version1/Q.png")
#IMAGE_DICT["R"] = image.load("images/version1/R.png")
#IMAGE_DICT["S"] = image.load("images/version1/S.png")
#IMAGE_DICT["T"] = image.load("images/version1/T.png")
#IMAGE_DICT["U"] = image.load("images/version1/U.png")
#IMAGE_DICT["V"] = image.load("images/version1/V.png")
#IMAGE_DICT["W"] = image.load("images/version1/W.png")
#IMAGE_DICT["X"] = image.load("images/version1/X.png")
#IMAGE_DICT["Y"] = image.load("images/version1/Y.png")
#IMAGE_DICT["Z"] = image.load("images/version1/Z.png")
#IMAGE_DICT["CL"] = image.load("images/version1/CL.png")
#IMAGE_DICT["ER"] = image.load("images/version1/ER.png")
#IMAGE_DICT["IN"] = image.load("images/version1/IN.png")
#IMAGE_DICT["QU"] = image.load("images/version1/QU.png")
#IMAGE_DICT["TH"] = image.load("images/version1/TH.png")
