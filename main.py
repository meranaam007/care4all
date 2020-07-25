from ElderFolk import ElderFolk
from YoungFolk import YoungFolk
from profile import User

elder1 = ElderFolk('e1', "Ramfal", 73, "seeker")
elder1.setFunds(7000)

elder2 = ElderFolk('e2', "LalaRam", 78, "seeker")
elder2.setFunds(7000)

elder3 = ElderFolk('e3', "Dharmbeer", 76, "seeker")
elder3.setFunds(7000)

elder4 = ElderFolk('e4', "Kanwarsingh", 81, "seeker")
elder4.setFunds(7000)

elder5 = ElderFolk('e5', "Khattar", 84, "seeker")
elder5.setFunds(7000)

# elder6 = ElderFolk('e6', "Manohar", 76, "seeker")
# elder6.setFunds(7000)

# elder7 = ElderFolk('e7', "Ramu", 82, "seeker")
# elder7.setFunds(7000)

# elder8 = ElderFolk('e8', "Master", 77, "seeker")
# elder8.setFunds(7000)

# elder9 = ElderFolk('e9', "LalSingh", 80, "seeker")
# elder9.setFunds(7000)

# elder10 = ElderFolk('e10', "Subasher", 71, "seeker")
# elder10.setFunds(7000)

# elder11 = ElderFolk('e11', "Surendra", 70, "seeker")
# elder11.setFunds(7000)

# elder12 = ElderFolk('e12', "Chaudhary", 69, "seeker")
# elder12.setFunds(7000)

# elder13 = ElderFolk('e13', "Dharma", 79, "seeker")
# elder13.setFunds(7000)

# elder14 = ElderFolk('e14', "Pyarelal", 75, "seeker")
# elder14.setFunds(7000)

# elder15 = ElderFolk('e15', "Dharma", 82, "seeker")
# elder15.setFunds(7000)

young1 = YoungFolk('y1','Mohan',25,'provider')
young2 = YoungFolk('y2','Suchitra',26,'provider')
young3 = YoungFolk('y3','Raani',29,'provider')
young4 = YoungFolk('y4','Sudesh',22,'provider')
young5 = YoungFolk('y5','Nikhil',24,'provider')

# elder1.setAvailabilty(False)
# elder2.setAvailabilty(False)
# elder3.setAvailabilty(False)
# elder4.setAvailabilty(False)
# elder5.setAvailabilty(False)
# elder8.setAvailabilty(False)
# elder14.setAvailabilty(False)

young1.register("abc@gmail.com","912345678")
if young1.login("abc@gmail.com","912345678"):

    res = young1.applyForService(elder2)
    if res:
        elder2.setApproveFolk(True)
        if not young1.setOlideTakenCareOf(elder2):
            young1.setSalary(1200)
            elder2.setFunds(-1200)
            elder2.setAvailabilty(False)

    res = young1.applyForService(elder1)
    if res:
        elder1.setApproveFolk(True)
        if not young1.setOlideTakenCareOf(elder1):
            young1.setSalary(1200)
            elder1.setFunds(-1200)
            elder1.setAvailabilty(False)

    res = young1.applyForService(elder3)
    if res:
        elder3.setApproveFolk(True)
        if not young1.setOlideTakenCareOf(elder3):
            young1.setSalary(1200)
            elder3.setFunds(-1200)
            elder3.setAvailabilty(False)

    res = young1.applyForService(elder5)
    if res:
        elder5.setApproveFolk(True)
        if not young1.setOlideTakenCareOf(elder5):
            young1.setSalary(1200)
            elder5.setFunds(-1200)
            elder5.setAvailabilty(False)

    res = young1.applyForService(elder4)
    if res:
        elder4.setApproveFolk(True)
        if not young1.setOlideTakenCareOf(elder4):
            young1.setSalary(1200)
            elder4.setFunds(-1200)
            elder4.setAvailabilty(False)

    young1.setRating(4.5)
    young1.setRating(5)
    young1.setRating(4)
    young1.setRating(4.3)
    young1.setReview("Best")

    print(young1.getOlideTakenCareof())
    print(young1.getSalary())
    print(young1.finalRating())

young2.register("xyz@gmail.com","912345678")
if young2.login("xyz@gmail.com","912345678"):
    res = young2.applyForService(elder4)
    if res:
        elder4.setApproveFolk(True)
        if not young2.setOlideTakenCareOf(elder4):
            young2.setSalary(1200)
            elder4.setFunds(-1200)
            elder4.setAvailabilty(False)

    print(young2.getOlideTakenCareof())
    print(young2.getSalary())