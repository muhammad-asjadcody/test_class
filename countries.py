class česko():
    def capital(self):
        print("Praha je hlavní město České republiky")

    def language(self):
        print("Česky je nejpoužívanější jazyk v ČR")

    def type(self):
        print("Čzech republic is a developed country")

class AMERICA():
    def capital(self):
        print("Washinton D.C. is the capital of USA")
    def language(self):
        print("English is the primary language in the US")
    def type(self):
        print("USA is a developed country")

obj_ČESKO = česko()
obj_US = AMERICA()

for country in (obj_ČESKO, obj_US):
    country.capital()
    country.language()
    country.type()
