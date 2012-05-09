import sys
import string #fixed typo was using
rot13 = string.maketrans( \
	"ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", \
	"NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
print string.translate(sys.argv[1], rot13)
