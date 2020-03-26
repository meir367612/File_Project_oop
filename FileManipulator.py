from Pdf import PdfFile
from Word import WordFile
from Video import VideoFile
from Picture import ImageFile

from FileSystemManager import FileSystemManager,AllFiles


class FileManipulator:

    def Add(self,File1,File2):
        if type(File1) == type(File2):
            New_name = File1.name+" & "+File2.name
            New_content = File1.content + " & "+File2.content
            New_who_created = File1.who_created + " & " + File2.who_created
            New_description = File1.description + " & " + File2.description
            New_file_size = File1.file_size + File2.file_size
            New_File = (New_name,New_content,New_who_created,New_description,New_file_size)
            print( type(New_File))
            AllFiles.append(New_File)
            print("The Files is conected" + str(New_File))

    def clone(self,File,Number):
        File.content = File.content*Number
        return File

