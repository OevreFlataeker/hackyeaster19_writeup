When we pan around using the mouse we don't see anything special.
However using the cursor keys we see that there are other movements possible.
We're able to traverse the outer bounds of the sphere and inside we see smth that vaguely looks like an object made of mirrors...
In one corner we're able to identify smth that might look like one of the sync boxes of a QR code ( :-/ )

But it is all distorted and looking at the virtual center of the scene.
So we need to edit the Javascript/HTML source code!

Using the information provided at:
https://stackoverflow.com/questions/2558346/how-do-you-edit-javascript-in-the-browser

We're able to create a local "overwrite" version of the disco2.html file.
Here we do the following changes:

Line 123: Change "color: 0x111111", to "color: 0x000000" (Make it black)
Line 132: Comment out that line, virtually hiding the sphere itself
Line 143: "mirrorTile.lookAt(center)" --> Comment out that line
Between line 140 and line 141 add the following line: "if (Math.abs(m[0])>275 || Math.abs(m[1])>275 || Math.abs(m[2])>60 ) continue;"
This line virtually filters all the mirrors away that were placed on the sphere, leaving only the QR code mirrors left to be painted!

When we now reload the html file, we immediately see the QR code in it's full beauty. Rotating it by 180° and looking slightly between the sides of the bridge,
the QR code scanner should now be able to recognize the QR code:

https://zxing.org/w/decode.jspx gives:
he19-r5pN-YIRp-2cyh-GWh8

