The QR code is a lie
When we look at the jpg itself, we can see that there is data behind the end of the jpg

daubsi@bigigloo:/tmp$ hexdump -C modernart.jpg | grep "ff d9"
00011350  ff d9 07 06 05 ff c4 00  14 01 01 00 00 00 00 00  |................|
00022620  b2 8f ff d9 0a 20 e2 96  84 e2 96 84 e2 96 84 e2  |..... ..........|
daubsi@bigigloo:/tmp$ vi dump
daubsi@bigigloo:/tmp$ cat dump | xxd -r -p

 ▄▄▄▄▄▄▄  ▄ ▄▄ ▄▄▄▄▄▄▄
 █ ▄▄▄ █ ▄█▀█▄ █ ▄▄▄ █
 █ ███ █  ▀▄▀▄ █ ███ █
 █▄▄▄▄▄█ ▄ ▄ █ █▄▄▄▄▄█
 ▄▄▄ ▄▄▄▄██▄█▀▄▄   ▄
 ▄█▄▀▄▄▄█▀▄▀ ▄ ▀ ▄▀▀▀▄
 ▀█▄█ ▀▄█▀   ▄ █ ▄▀ ▄
 ▄▄▄▄▄▄▄ █▀▄█ █▄█ ▀▀
 █ ▄▄▄ █ ██▄█▀█▄█▀▀▄ █
 █ ███ █ ▄ ▀ ▄ ▀▀▄█▀▀▄
 █▄▄▄▄▄█ █▀█ ▄ █▀  █▀█
daubsi@bigigloo:/tmp$

This QR code translates to "AES-128", so there's apparently some sort of encryption involved
When we "strings" the binary we come across these 2 interesting strings:

root@bigigloo:/ssd# strings -n 20 /tmp/modernart.jpg
(E7EF085CEBFCE8ED93410ACF169B226A)
(KEY=1857304593749584)


We can decode this using Cyberchef into the plaintext "Ju5t_An_1mag3"
