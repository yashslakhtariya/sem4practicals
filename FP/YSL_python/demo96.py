class CEO:
    cmpny = "Haribol!"
    mnthly_incm = 643216008
    bonus = 6432160

    # To use function as variable for object, 'getter method' is used using
    @property
    def Incm(self):
        return self.mnthly_incm + self.bonus


ysl = CEO()
print(ysl.Incm)
