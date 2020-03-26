from Pdf import PdfFile
from Word import WordFile
from Video import VideoFile
from Picture import ImageFile

AllFiles=[]

class FileSystemManager:
    def __init__(self,Size):
        self.Size = Size



    def AddFile(self, File):
        # print(vars(File))
        if File.file_size > self.Size:
            print("You over the maximum size! ")
        else:
            for i  in AllFiles:
                if i.name == File.name:
                    print("This file is already exist! ")
                    return False
            AllFiles.append(File)




    def DeleteFile(self,Name):
        for i in AllFiles:
            if i.name == Name:
                AllFiles.remove(i)
                print("File removed succesfuly")



    def GetFile(self,Type=None):

        if not Type:
             print(AllFiles)

        else:
            print("cxcx")
            print(Type)
            return


