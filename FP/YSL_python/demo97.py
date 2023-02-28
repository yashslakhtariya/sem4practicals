class CEO:
    cmpny = "Haribol!"
    mnthly_incm = 643216008
    bonus = 6432160

    # To use function as variable for object, 'getter method' is used
    # Syntax : @property
    @property
    def Incm(self):
        return self.mnthly_incm + self.bonus

    # To set value of variable (function -> variable by getter method), 'setter' method is used
    # Syntax : @methodname.setter
    @Incm.setter
    def Incm(self, var):
        self.bonus = var - self.Incm


ysl = CEO()
ysl.Incm = 6432161612
print(ysl.Incm)
print(ysl.bonus)
