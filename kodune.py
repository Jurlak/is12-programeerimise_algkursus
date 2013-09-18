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

class Point(object):
     def __init__(self, x, y):
         self.x, self.y = x, y
     def __str__(self):
         return 'Point({self.x}, {self.y})'.format(self=self)

print str(Point(4, 2))

coord = (3, 5)
print'X: {0[0]};  Y: {0[1]}'.format(coord)

print "repr() shows quotes: {0!r}; str() doesn't: {1!s}".format('test1', 'test2')

print '{0:<30}'.format('left aligned')

print '{0:>30}'.format('right aligned')

print '{0:^30}'.format('centered')

print '{0:*^30}'.format('centered')  # use '*' as a fill char

print '{0:+f}; {0:+f}'.format(3.14, -3.14)  # show it always

print '{0: f}; {0: f}'.format(3.14, -3.14)  # show a space for positive numbers

print '{0:-f}; {0:-f}'.format(3.14, -3.14)  # show only the minus -- same as '{0:f}; {0:f}'

print "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)

print "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)


points = 19.5
total = 22
print 'Correct answers: {0:.2%}.'.format(points/total)

import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print'{0:%Y-%m-%d %H:%M:%S}'.format(d)



