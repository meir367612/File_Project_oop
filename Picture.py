from SuperFile import SuperFile


class ImageFile(SuperFile):
    def __init__(self, name:str, content:str,who_created:str,description:str,file_size:int):
        SuperFile.__init__(self, name, content, who_created, description, file_size)
        self.__image_dimensions = image_dimensions

    def __str__(self):
        s = SuperFile.__str__(self)
        s += " image_dimensions is {}".format(self.__image_dimensions)
        return s


