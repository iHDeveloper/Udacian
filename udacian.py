class Udacian: 
    def __init__(self, name, city, enrollment, nanodegree, status):
        self.name = name
        self.city = city
        self.enrollment = enrollment
        self.nanodegree = nanodegree
        self.status = status
    def __str__(self):
        return "{} is enrolled in {} studying {} in {} {} with {}, he/she is {}".format(
            self.name,
            self.city,
            self.nanodegree,
            self.enrollment[0],
            self.enrollment[1],
            self.enrollment[2],
            self.status
        )

enrollment = ( 'Sat', 'am', 'Ms. Lujuain' )
udacian = Udacian('Mohammed', 'Riyadh', enrollment, 'FSND', 'on tracking')
print(udacian)