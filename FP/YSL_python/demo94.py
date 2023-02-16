# Class Methods

class CEO:
    company = "YSL Pvt. Ltd."
    mnthly_incm = 643216008
    location = "Vrindavana"

    # To change class variable value with object
    def chngMnthlyIncm(self, mi):
        self.__class__.mnthly_incm = mi

    # Same thing done above can be done by using classmethod
    # '@' is property decorator and has many uses
    @classmethod
    def chngMnthlyIncm2(self, mi):
        self.mnthly_incm = mi


ysl = CEO()
print(ysl.mnthly_incm)
ysl.chngMnthlyIncm(643216160)
ysl.chngMnthlyIncm2(643216160)
print(ysl.mnthly_incm)
print(CEO.mnthly_incm)
