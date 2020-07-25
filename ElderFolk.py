from profile import User

class ElderFolk(User):
    elderFolks = []

    @classmethod
    def updateElders(cls, elder):
        cls.elderFolks.append(elder)

    def __init__(self, id, name, age, role):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__role = role
        self.__isAvailable = True
        self.__allocateFunds = 0
        self.__approveFolk = False  
        self.__rating = 0
        self.__review = []
        self.__ratingCount = 0
        ElderFolk.updateElders(self)
    
    def setRating(self, rating):
        self.__rating = rating
        self.__ratingCount += 1

    def getRating(self):
        return self.__rating
    
    def finalRating(self):
        self.__rating = self.getRating()/self.__ratingCount
        return self.__rating

    def setReview(self, review):
        self.__review.append(review)

    def getReview(self):
        return self.__review

    def getRole(self):
        return self.__role
    
    def getName(self):
        return self.__name

    def getId(self):
        return self.__id
    
    def getAge(self):
        return self.__age

    def setAvailabilty(self, availabilty):
        self.__isAvailable = availabilty
    
    def getAvailabilty(self):
        return self.__isAvailable
    
    def setFunds(self, fund):
        self.__allocateFunds += fund
    
    def getFunds(self):
        return self.__allocateFunds
    
    def setApproveFolk(self, approve):
        self.__approveFolk = approve
    
    def getApproveFolk(self):
        return self.__approveFolk