print '{0}, {1}, {2}'.format('a', 'b', 'c')
print '{2}, {1}, {0}'.format('a', 'b', 'c')
print '{2}, {1}, {0}'.format(*'abc')      # unpacking argument sequence
print '{0}{1}{0}'.format('abra', 'cad')   # arguments' indices can be repeated
print 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')

coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print 'Coordinates: {latitude}, {longitude}'.format(**coord)
c = 3-5j
print ('The complex number {0} is formed from the real part {0.real} '
'and the imaginary part {0.imag}.').format(c)



print "Kaal:{0} {1} ".format(9+2/14*2,"kg")


class Point(object):
     def __init__(self, x, y):
         self.x, self.y = x, y
     def __str__(self):
         return 'Point({self.x}, {self.y})'.format(self=self)

print str(Point(4, 2))

kaal= 5*7/2+2*3
print "Kaal:{0} {1}".format(kaal,"kg")



