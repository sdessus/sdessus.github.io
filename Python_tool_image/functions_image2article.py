import os
from pathlib import *
# from IPTCInfo3 import *
import exifread
from datetime import datetime
import time

def im2art(ImFilePath,ArticlePath):
	ImFile = Path(ImFilePath)
	Article = Path(ArticlePath)
	# Testing arguments
	if not os.path.exists(ImFilePath):
		print ('The image file does not exist')
		return
	elif not os.path.exists(ArticlePath):
		print ('The article file does not exist')
		return
	elif (PureWindowsPath(ArticlePath).suffix != '.md'):
		print ('Your article should be Markdown (.md) file')
		return
		
	# Open article
	ArticleFile = open(ArticlePath)
	ArticleLine = ArticleFile.readlines()
	
	# Found emplacement on article
	BlockStartLine = 0
	for line in range(len(ArticleLine)) :
		if (ArticleLine[line] == '<div class="galleria" style="margin:auto">\n'):
			BlockStartLine = line
			break
	
	ArticleFile.close()
	
	# Right proper statement on article
	
	if (BlockStartLine == 0):
		ArticleFile = open(ArticlePath, 'a')	
		# Upper block statement
		ArticleFile.write('\n\n<div class="galleria" style="margin:auto">\n')
		
		# Writing at the end of the file
		ArticleFile.write('    <img src="images/%s">\n' % (ImFile.parts[-2] + '/' + ImFile.name))
		ArticleFile.write('<\div>\n')
		
		# Lower block statement
		LowerBlock = ['<script>\n', '\t(function() { \n', "            Galleria.loadTheme('https://cdnjs.cloudflare.com/ajax/libs/galleria/1.5.7/themes/classic/galleria.classic.min.js');\n", "            Galleria.run('.galleria');\n", '        }());\n', '</script>\n']
		ArticleFile.writelines(LowerBlock)
		
	else:
		BlockEndLine = 0
		for line in range(BlockStartLine,len(ArticleLine)-1):
			if (ArticleLine[line] == '<\\div>\n') and (ArticleLine[line+1] == '<script>\n'):
				BlockEndLine = line
				break
		if BlockEndLine == 0 :
			print ('La fin du block d''insertion d''image n''a pas été trouvé')
			return
		ArticleFile = open(ArticlePath, 'w')
		# insert newline in existing bloc
		ArticleLine.insert(BlockEndLine,'    <img src="images/%s">\n' % (ImFile.parts[-2] + '/' + ImFile.name))
		# Rewrite the article
		ArticleFile.writelines(ArticleLine)
	
	# Close file
	ArticleFile.close()

def TestImExt(ImFilePath):
	ImFile = Path(ImFilePath)
	
	#Testing the argument
	if not ImFile.is_absolute():
		print('Image folder path should be absolute')
		return
	elif not ImFile.exists():
		print('The image folder does not exist')
		return
	elif not ImFile.is_file():
		print('The image file should not be a folder')
		return
	
	if not ImFile.suffix.islower():
		ImFile.rename(ImFile.with_suffix(ImFile.suffix.lower()))
	
def fold2art(ImFolderPath,ArticlePath):
	ImFolder = Path(ImFolderPath)
	Article = Path(ArticlePath)
	
	# Testing Arguments
	if not ImFolder.is_absolute():
		print('Image folder path should be absolute')
		return
	elif not ImFolder.exists():
		print('The image folder does not exist')
		return
	elif not ImFolder.is_dir():
		print('The image folder is not a folder')
		return
	
	if not Article.is_absolute():
		print('Article path should be absolute')
		return
	elif not Article.exists():
		print('The article does not exist')
		return
	elif not Article.is_file():
		print('The article should be a file (not a folder)')
		return
	
	ImList = os.listdir(ImFolderPath)	
	for image in range(len(ImList)):
		TestImExt(ImFolder / ImList[image])
		im2art(ImFolder / ImList[image],ArticlePath)
		
def get_files_by_date(directory):
	Folder = Path(directory)
	FileList = os.listdir(Folder)
	FileListDated = []
	for fnum in range(len(FileList)):
		# FileListDated.insert(fnum, (os.path.getmtime(Folder / FileList[fnum]),FileList[fnum]))
		FileListDated.insert(fnum, (GetImDateShot(Folder / FileList[fnum]).strftime('%y%m%d-%H%M%S') ,FileList[fnum]))
	FileListDated.sort()
	# print(FileListDated)
	return  [fname for s,fname in FileListDated]
	
def RenameImInFolder(dir):
	Folder = Path(dir)
	# print(os.listdir(Folder))
	ImListSorted = get_files_by_date(Folder)
	# print(ImListSorted)
	for fnum in range(len(ImListSorted)):
		ImFile = Path(Folder / ImListSorted[fnum])
		ImName = ImFile.parts[-2] + '_%s.jpg' % str(fnum).rjust(2,'0')
		print(ImName)
		print(ImFile)
		if ImFile.with_name(ImName).exists():
			# ImFile.with_name(ImName).rename(ImFile.with_name(ImName).parent.joinpath(ImFile.with_name(ImName).stem + '_bis' + ImFile.with_name(ImName).suffix))
			ImFile.rename(ImFile.parent.joinpath('Torename' + ImFile.name))
		else:
			ImFile.rename(ImFile.with_name(ImName))
	
	# Clean up
	ImList = os.listdir(Folder)
	for fnum in range(len(ImList)):
		ImFile = Path(Folder / ImList[fnum])
		RemovePrefixIm(ImFile)
	
	# Check
	ImListRenamed = os.listdir(Folder)
	print(ImListRenamed)
	
def RemovePrefixIm(ImFilePath):
	ImFile = Path(ImFilePath)
	if 'Torename' in ImFile.name:
		ImName = ImFile.name[8:len(ImFile.name)]
		ImFile.rename(ImFile.with_name(ImName))
		
def GetImDateShot(ImFilePath):
	ImFile = Path(ImFilePath)
	OpenIm = open(ImFile, 'rb')
	ImExifData = exifread.process_file(OpenIm)
	print(ImFile)
	# print(ImExifData.get('EXIF DateTimeOriginal'))
	if (ImExifData.get('EXIF DateTimeOriginal') != None):
		ImDateShot = datetime.strptime(str(ImExifData.get('EXIF DateTimeOriginal')),'%Y:%m:%d %H:%M:%S')
	else:
		ImDateShot = datetime.strptime(str(time.strftime("%Y:%m:%d %H:%M:%S",time.gmtime(os.path.getmtime(ImFile)))),'%Y:%m:%d %H:%M:%S')
		# print(datetime.strptime(str(time.strftime("%Y:%m:%d %H:%M:%S",time.gmtime(os.path.getmtime(ImFile)))),'%Y:%m:%d %H:%M:%S'))
	# print (ImDateShot)
	return(ImDateShot)
		
def GetImComment(ImFilePath):
	ImFile = Path(ImFilePath)
	
	# Récupération des données EXIF
	OpenIm = open(ImFile, 'rb')
	ImExifData = exifread.process_file(OpenIm)
	OpenIm.close()
	
	# Test de l'existence d'un commentaire
	if (ImExifData.get('Image XPComment') == None):
		print("L'image ne possède pas de commentaire")
		return('')
	
	# print(ImExifData.get('Image XPComment'))
	# print(ImExifData['Image XPComment'].values)
	
	# Récupération du commentaire
	ByteComment = ImExifData['Image XPComment'].values
	StrComment = DecodeXPComment(ByteComment)
	print(StrComment)
	return(StrComment)
	
def DecodeXPComment(ByteComment):
	StrByteComment = str(ByteComment).strip('[ 0, 0, 0]').split(', 0, ') # maintenant c'est une liste de caractère seul
	IntComment = StrByteComment
	for ch in range(len(StrByteComment)): # boucle pour convertir les chaîne de caractère en entier
		IntComment[ch] = int(StrByteComment[ch])
	# print(IntComment)
	StrComment = "".join(map(chr, IntComment)) # création de la chaine de caractère à partir de la liste d'entier
	# print(StrComment)
	return(StrComment)
		
# def AddLegend(ImFilePath,legend):
	# info = IPTCInfo(ImFilePath)
	# print(info)
	
def InsertLegend2Art(ImFilePath, ArticlePath):
	# def : insert le commentaire d'une image en légende dans l'article
	# inputs : ImFilePath = chemin de l'image dont le commentaire doit être inséré
	# 		   ImFilePath = chemin de l'article dans lequel le commentaire doit être inséré
	
	# Création des objects "Path" pour manipulation
	ImFile = Path(ImFilePath)
	# Test si l'image contient un commentaire
	if(GetImComment(ImFilePath) == ''):
		print("L'image %s ne contient pas de commentaire" % ImFile.name)
		return
	
	# Lecture de l'article et récupération en list des lignes
	ArticleFile = open(ArticlePath)
	ArticleLines = ArticleFile.readlines()
	ArticleFile.close()
	
	# Reconnaitre la ligne correspondant à l'image
	ImLine = -1
	for line in range(len(ArticleLines)) :
		if (ImFile.name in ArticleLines[line]):
			ImLine = line
			break
	
	# Test si aucune ligne n'a été trouvée
	if(ImLine == -1):
		print("La ligne correspondant à l'image %s selectionnée n'a pas été trouvé dans l'article. Veuillez vérifier les arguments" % ImFile.name)
		return
	
	# Test si une légende existe déjà -> pas capable de gérer ça pour le moment
	if('data-description' in ArticleLines[line]):
		print("Une légende existe déjà pour l'image %s. Veuillez la supprimer pour mettre à jour la légende" % ImFile.name)
		return
		
	# Insérer la légende dans la ligne
	ArticleLines[ImLine] = ArticleLines[ImLine][0:len(ArticleLines[ImLine])-2] + ' data-description="%s">\n' % GetImComment(ImFilePath)
	
	# Rewrite the article
	ArticleFile = open(ArticlePath, 'w')
	ArticleFile.writelines(ArticleLines)
	ArticleFile.close()
	
def InsertLegendFolder2Art(ImFolderPath, ArticlePath):
	# def : insert les commentaires des images du dossier en legend dans l'article
	# inputs : ImFolder = chemin du dossier d'image dont les commentaire doivent être insérés
	# 		   ImFilePath = chemin de l'article dans lequel les commentaires doit être inséré	
	ImFolder = Path(ImFolderPath)
	Article = Path(ArticlePath)
	
	# Testing Arguments
	if not ImFolder.is_absolute():
		print('Image folder path should be absolute')
		return
	elif not ImFolder.exists():
		print('The image folder does not exist')
		return
	elif not ImFolder.is_dir():
		print('The image folder is not a folder')
		return
	
	if not Article.is_absolute():
		print('Article path should be absolute')
		return
	elif not Article.exists():
		print('The article does not exist')
		return
	elif not Article.is_file():
		print('The article should be a file (not a folder)')
		return
	
	# On récupère la liste de ttes les images du dossier
	ImList = os.listdir(ImFolderPath)
	
	# On parcourt la liste d'image en appliquant la fonction d'insertion de légende pour chaque image
	for fnum in range(len(ImList)):
		ImFile = Path(ImFolder / ImList[fnum])
		InsertLegend2Art(ImFile, Article)
	
def DoTheMagic():
	BlogContentPath = Path('C:\Blog_TDM\content')

	print('Quel article voulez-vous remplir ?')
	ArticlePath = input()
	Article = Path(ArticlePath)

	# Testing Input
	if not Article.is_absolute():
		Article = BlogContentPath / Article
		print(Article)

	if not Article.exists():
		print('The article does not exist')
		return
	elif not Article.is_file():
		print('The article should be a file (not a folder)')
		return

	print("Avec quel dossier d'images voulez-vous le remplir ?")
	ImFolderPath = input()
	ImFolder = Path(ImFolderPath)

	# Testing input
	if not ImFolder.is_absolute():
		ImFolder = BlogContentPath / 'images' / ImFolder
		print(Article)
		
	if not ImFolder.exists():
		print('The image folder does not exist')
		return
	elif not ImFolder.is_dir():
		print('The image folder is not a folder')
		return
	
	RenameImInFolder(ImFolder)
	fold2art(ImFolder,Article)
	
	print("Voulez-vous ajouter des légendes aux images ? O/N")
	LegendOn = input()
	
	if(LegendOn.lower() == 'o'):
		InsertLegendFolder2Art(ImFolder,Article)
