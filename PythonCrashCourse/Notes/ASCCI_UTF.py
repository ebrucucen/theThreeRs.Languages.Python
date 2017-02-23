ASCII :maps 128 chars: ==> requires 8 only!
    95 chars: [A-Z(26),a-z(26),0-9(10),punctions($?&)]
    33 chars: space, tab, linefeed(33)

    A= 65= 01000001
    B= 66= 01000010
    C= 67= 01000011
    D= 68= 01000100
10011111 in binary
in decimal(base 10): 2**7,2**4,2**3,2**2,2**1,2**0=128+16+8+4+2+1=159
in octal(base 8): 8**2, 8**1, 8**0 =  237
in hexadecimal(base 16):16**1,16**0= 9[15]=9F
[0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F] 

UTF-8: requires 8,16,24, 32 bits (1-4 octets)...
[Any ASCII is valid UTF-8]

First 128 Unicode codepoints, U+0000 - U+007F ==[ASCII]use 8 bits.
Next 1920 Unicode codepoints, U+0080 - U+07FF ==[Latin+close]use 16 bits.
Other 63487 Unicode codepoints, U+0800 - U+FFFF 
[==>[[256*8]=2048] ==== 
    [[65535] 1*15 [=15]+ 16*15 [=240]+ 256*15 [=3840] + 4096*15 [=61440]]
Basic Multilungial Plane


source: http://kunststube.net/encoding/
