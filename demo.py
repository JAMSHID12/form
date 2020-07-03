class Result:
    def mark(self,pysics,chemistry,maths):
        self.pysics = pysics
        self.chemistry = chemistry
        self.maths = maths

    def percent(self):
        percent = (self.pysics + self.maths + self.chemistry ) * 100 / 300
        if percent > 70:
            print("greater")
        else:
            print("less")
        return percent


    def check_grade(self,grade):
        self.grade = grade
        if grade == "A":
            print("A grade")
        elif grade == "B":
            print("B grade")
        elif grade == "C":
            print("C grade")






x = Result()
x.mark(67, 96, 78)
x.check_grade("A")
print(x.percent())

