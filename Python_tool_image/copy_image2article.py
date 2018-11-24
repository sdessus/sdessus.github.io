import os
import pathlib

# Imlist = os.listdir(ImPath)

def im2art(ImFile,Article):
# Testing arguments
	if not os.path.exists(ImFile):
		print ('The image file does not exist')
		return
	elif not os.path.exists(Article):
		print ('The article file does not exist')
		return
	elif (pathlib.PurePosixPath(Article).suffix != '.md'):
		print ('Your article should be Markdown (.md) file')
		return
		
	# Open article
	ArticleFile = open(Article)
	print(ArticleFile)
	ArticleLine = ArticleFile.readline()
	ArticleFile.close()
	print(len(ArticleLine))
	print (ArticleLine)
	
	# Found emplacement on article
	BlockStartLine = 0
	for line in ArticleLine:
		print (line)
		if (line == '<div class="galleria" style="margin:auto">'):
			BlockStartLine = line
		break
	
	print (BlockStartLine)
		
	
	# Right proper statement on article