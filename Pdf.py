from SuperFile import SuperFile


class PdfFile(SuperFile):
    def __init__(self, name:str, content:str,who_created:str,description:str,file_size:int):
        SuperFile.__init__(self,name,content,who_created,description,file_size)


    def __str__(self):
        s = SuperFile.__str__(self)
        return s