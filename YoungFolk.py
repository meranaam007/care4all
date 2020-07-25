from profile import User
from ElderFolk import ElderFolk

class YoungFolk(User):
    YoungFolks = []

    @classmethod
    def updateYoung(cls, young):
        cls.YoungFolks.append(young)

    def __init__(self, id, name, age, role):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__role = role
        self.__oldieCount = 0
        self.__oldieTakingCareof = []
        self.__salary = 0
        self.__rating = 0
        self.__review = []
        self.__ratingCount = 0
        YoungFolk.updateYoung(self)
    
    def setRating(self, rating):
        self.__rating += rating
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

    def applyForService(self, elder):
        if not elder.getAvailabilty():
            print("Not available")
            return False
        print("Thank you for applying")
        return True

    def setOldieCount(self, count):
        self.__oldieCount += count
    
    def getOldieCount(self):
        return self.__oldieCount
    
    def setOlideTakenCareOf(self, elder):
        if elder.getAvailabilty() and elder.getApproveFolk() and self.getOldieCount() < 4:
            self.__oldieTakingCareof.append(elder.getName())
            self.setOldieCount(1)
        elif elder.getApproveFolk() and self.__oldieCount >= 4:
            print("A limit for 4 oldones already exceeded")
            return True

    def getOlideTakenCareof(self):
        return self.__oldieTakingCareof
    
    def setSalary(self, salary):
        self.__salary += salary

    def getSalary(self):
        return self.__salary