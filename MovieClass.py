class Customer:
    def __init__(self,name,email,moviesrented=None,finesowed=0.0):
        self.__customerName = name 
        self.__customerEmail = email
        self.__customermoviesrented = moviesrented if moviesrented else[]
        self.__customerfinesowed = finesowed

    @property
    def customername(self):
        return self.__customerName

    @customername.setter
    def customername(self, changeName):
        self.__customerName = changeName

    @property
    def customeremail(self):
        return self.__customerEmail

    @customeremail.setter
    def customeremail(self , changeEmail):
        self.__customerEmail = changeEmail

    @property
    def customermoviesrented(self):
        return self.__customermoviesrented

    @customermoviesrented.setter
    def customermoviesrented(self , changemoviesrented):
        self.__customermoviesrented = changemoviesrented

    @property
    def customerfinesowed(self):
        return self.__customerfinesowed

    @customerfinesowed.setter
    def customerfinesowed(self , changefinesowed):
        self.__customerfinesowed = changefinesowed