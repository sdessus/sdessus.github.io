import os
import sys
from Npp import notepad # import it first!

filePathSrc="C:\Blog_TDM\comments_blog_tdm\comments" # Path to the folder with files to convert
for root, dirs, files in os.walk(filePathSrc):
    for fn in files: 
        if fn[-4:] == '.yml': # Specify type of the files
            notepad.open(root + "\\" + fn)      
            notepad.runMenuCommand("Encoding", "Convert to ANSI")
            # notepad.save()
            # if you try to save/replace the file, an annoying confirmation window would popup.
            notepad.saveAs("{}{}".format(fn[:-4], '_ansi.yml')) 
            notepad.close()