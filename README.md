# steg
#
# steganography (n) the art of concealing messages within nonsecret data, 
#                   secret writing.
#
# usage: steg [-h] [-c] [-m TEXT] [-o OUT] [-z {0,1,2,3,4,5,6,7,8,9}] image
#
# steg takes an ASCII string of characters, assumes ASCII is an 8 bit code, and 
# (more or less) encodes that binary information in the least signficiant bit of
# the three color channels of a PNG image created from your supplied image.
# Visually it is very hard to notice a difference from the input image.
#
# Note: the message is only concealed, if someone knows it's there, it is very 
# easy to read. The hidden message is prefixed with 'magic bytes' and null 
# terminated, making it relatively easy to spot a pattern in PNGs with hidden
# messages.
#
# **DO NOT USE** this software in any situation where your life depends on
# secret messages; missionaries, dissidents and political prisoners, that means
# you. This is a demonstration program for fun.
