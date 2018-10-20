class Udacian: 
    def __init__(self, name, city, enrollment, nanodegree, status):
        self.name = name
        self.city = city
        self.enrollment = enrollment
        self.nanodegree = nanodegree
        self.status = status
    def __str__(self):
        return "{} is enrolled in {} studying {} in {} with {}, he/she is {}".format(
            self.name,
            self.city,
            self.nanodegree,
            self.enrollment[0],
            self.enrollment[1],
            self.status
        )

udacian = Udacian('Mohammed', 'Riyadh', ( 'Sat am', 'Ms. Lujuain' ), 'FSND', 'on tracking')
print(udacian)