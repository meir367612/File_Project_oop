from SuperFile import SuperFile


class VideoFile(SuperFile):
    def __init__(self, name:str, content:str,who_created:str,description:str,file_size:int):
        SuperFile.__init__(self, name, content, who_created, description, file_size)
        self.__duration = duration

    def __str__(self):
        s = SuperFile.__str__(self)
        s += " duration is {}".format(self.__duration)
        return s


