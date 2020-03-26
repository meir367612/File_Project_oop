from Pdf import PdfFile
from Word import WordFile
from Video import VideoFile
from Picture import ImageFile

from FileSystemManager import FileSystemManager
from FileManipulator import FileManipulator

def main():

    fileSystemManager = FileSystemManager(100)
    print(fileSystemManager)
    FileManipulator.Add(PdfFile("meir","lalal","sasasa","tryme",100),(PdfFile("meir","lalal","sasasa","tryme",100)),(PdfFile("meir","lalal","sasasa","tryme",100)))

    # for i in range(10):
    #     x=fileSystemManager.AddFile(PdfFile("pdf_{}".format(i), "pdf_{}_content".format(i),
    #                                   "noa", "try_file", 10))
    #     # fileSystemManager.DeleteFile("pdf_1")
    #
    # fileSystemManager.GetFile()
    # print(fileSystemManager)
    # allFiles = fileSystemManager.getFiles()
    # wordFiles = fileSystemManager.getFiles("Word")




main()