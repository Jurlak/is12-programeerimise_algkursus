print("{:.2f}".format(3.1415926))
print("{:+.2f}".format(3.1415926))
print("{:+.2f}".format(-1))
print("{:.0f}".format(2.71828))
print("{:0>2d}".format(5))
print("{:x<4d}".format(5))
print("{:x<4d}".format(10))
print("{:,}".format(1000000))
print("{:.2%}".format(0.25))
print("{:.2e}".format(1000000000))
print("{:10d}".format(13))
print("{:<10d}".format(13))
print("{:^10d}".format(13))

print("so much depends upon {}".format("a red wheel barrow"))
print("glazed with {} water beside the {} chickens".format("rain", "white"))

print(" {0} is better than {1} ".format("emacs", "vim"))
print(" {1} is better than {0} ".format("emacs", "vim"))


pi = 3.14159
print(" pi = %1.2f " % pi)

s1 = "cats"
s2 = "dogs"
print(" %s and %s living together" % (s1, s2))


madlib = " I {verb} the {object} off the {place} ".format(verb="took", object="cheese", place="table")
print madlib

str = "Oh {0}, {0}! wherefore art thou {0}?".format("Romeo")
print str

print("{0:d} - {0:x} - {0:o} - {0:b} ".format(21))

email_f = "Your email address was {email}".format
print(email_f(email="bob@example.com"))

print(" The {} set is often represented as {{0}} ".format("empty"))
