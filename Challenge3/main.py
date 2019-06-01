'''
require"base64"
puts"write some text and hit enter:"
input=gets.chomp                                                    # "a"
h=input.unpack('C'*input.length).collect{|x|x.to_s(16)}.join        # char to hex for each char, 61
ox='%#X'%h.to_i(16)                                                 # to 0X und uppercase, 0X61
x=ox.to_i(16)*['5'].cycle(101).to_a.join.to_i                       # create a number consisting of 5 101times after eachother and then multiply with the hexnumber 61 as dec-->
                                                                    # 5388888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888835
c=x.to_s(16).scan(/../).map(&:hex).map(&:chr).join                  # convert the number to a hex, then as a string, read 2 chars at a time, interpret as hex and print the chr of it

b=Base64.encode64(c)
puts"encrypted text:""#{b}"
'''


'''
#03
$ echo -n "K7sAYzGlYx0kZyXIIPrXxK22DkU4Q+rTGfUk9i9vA60C/ZcQOSWNfJLTu4RpIBy/27yK5CBW+UrBhm0=" | base64 -d | xxd -p | tr -d '\n'
2bbb006331a5631d246725c820fad7c4adb60e453843ead319f524f62f6f03ad02fd971039258d7c92d3bb8469201cbfdbbc8ae42056f94ac1866d

>>> print "%0x"%(0x2bbb006331a5631d246725c820fad7c4adb60e453843ead319f524f62f6f03ad02fd971039258d7c92d3bb8469201cbfdbbc8ae42056f94ac1866d/55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555)
6e3030625f7374796c655f63727970746f

$ echo -n 6e3030625f7374796c655f63727970746f | xxd -r -p
n00b_style_crypto
'''

output="K7sAYzGlYx0kZyXIIPrXxK22DkU4Q+rTGfUk9i9vA60C/ZcQOSWNfJLTu4RpIBy/27yK5CBW+UrBhm0="
# debased hex output:
# 2b bb 00 63 31 a5 63 1d 24 67 25 c8 20 fa d7 c4 ad b6 0e 45 38 43 ea d3 19 f5 24 f6 2f 6f 03 ad 02 fd 97 10 39 25 8d 7c 92 d3 bb 84 69 20 1c bf db bc 8a e4 20 56 f9 4a c1 86 6d

'''
2083061918366036933124777781776017495216833333333333333333333333333333333333333333333333333333333333312502714149672964002085555515573158381165
divide
by
55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
==
37495114530588664796246000071968314913903
to hex = 0x6e3030625f7374796c655f63727970746f

=n00b_style_crypto
'''

print("he19-YPkZ-ZZpf-nbYt-6ZyD")


