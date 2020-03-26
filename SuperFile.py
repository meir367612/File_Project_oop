class SuperFile:
    def __init__(self, name:str, content:str,who_created:str,description:str,file_size:int):
        self.name = name
        self.content = content
        self.who_created = who_created
        self.description = description
        self.file_size = file_size
    def __str__(self):
        return "name is {} content is {} who_created is {} description is {} file_size is {}"\
            .format(self.name, self.content,self.who_created,self.description,self.file_size)



