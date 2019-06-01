stirngs on the binary gives "XOR-Challenge.c"
which is a big hint.

The "hash" function does some pretty complex lifting and shifting but using looking at it in a decompiler
like retdec we can see that basically the operations cancel out and all that happens is a kind of xor operation

so we use xortool to try to find the key.

we put the encrypted puffer at 0x601060 of length 210 (cmp in loc_4006a2) into a separate file and run xortool on it
It tells us that with key length 13 there i a high change of printable text. hooray!

then we grep for he19 in the results and indeed we find some valuable informaiton:


A variant gives us:



ESC1!#o,
c ng;2 >oyou f un-s %* hidd*n /?5*u he19bEh? y4:yJ-3d6S-+^]l^Xa

'T'e ^Q^\^Fm perat r   t(7treme#y *<9  n as . c&>$"!ent i! m&!1m,omple7 c #<(=s. Byoit:68+c usin( ai0;#<tant =ep,2 $!g k

with the key: xortool_out/6831.out;+d?\x10w1th_!4n-

As we know the key has length 13 it will repeat and if we can guess missing characters in the plaintext we can try to find the part of the
key that needs to be changed in order to create the correct key in the output.
We aim for the missing "e" in "hidden" just before the gibberish before he19

By flipping one char at a time we reveal more and more of the plain text and can guess new candidates.

In the end the key turns out to be: "x0r_w1th_n4nd" and reveals the solution:

root@bigigloo:/ctf# echo 'x0r_w1th_n4nd' | ./decryptor
Enter Password: Hello,
congrats you found the hidden flag: he19-Ehvs-yuyJ-3dyS-bN8U.

'The XOR operator is extremely common as a component in more complex ciphers. By itself, using a constant repeating key, a simple XOR cipher can trivially be broken using frequency analysis. If the content of any message can be guessed or otherwise known then the key can be revealed.'
(https://en.wikipedia.org/wiki/XOR_cipher)

'An XOR gate circuit can be made from four NAND gates. In fact, both NAND and NOR gates are so-called "universal gates" and any logical function can be constructed from either NAND logic or NOR logic alone. If the four NAND gates are replaced by NOR gates, this results in an XNOR gate, which can be converted to an XOR gate by inverting the output or one of the inputs (e.g. with a fifth NOR gate).'


Which in turn gives some interesting information!
