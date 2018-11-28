import os
from pathlib import *

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
		ArticleFile = open(ArticlePath, 'w')
		# insert newline in existing bloc
		ArticleLine.insert(BlockStartLine+1,'    <img src="images/%s">\n' % (ImFile.parts[-2] + '/' + ImFile.name))
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

	print('Avec quel dossier d''images voulez-vous le remplir ?')
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

	fold2art(ImFolder,Article)
