import mysql.connector
import binascii

# We traverse the DB and collecting all the objects, all hierarchies are connected via a parent-child or PID-ID relationship.
# At first I walked all the books and addresses and was looking for some outstanding things but I had
# a feeling that it would be the PNGs (of course) where the flag would be hidden
# Walking the PNGs was easy as well. Every record held a part of the PNG (a chunk) and had to be written to a binary file
# literally one after the other (the contents in the DB were b64-encoded. One particular thing was that an IDAT record could
# have subrecords AS WELL, connecting as usual via PID-ID reference
# When all the files are collected we can see that "A strange car.png" is actually our flag egg.


category_ids = {}

def handlePNGs():
	p_pid = category_ids['galery'][0]
	mycursor.execute(lookup, { 'pid': p_pid})
	myresult = mycursor.fetchall()
	pngs={}

	# Actually we only need to look for the PNG called "A strange car.png"
	for x in myresult:
		pngs[x[0]]=[x[0],x[1],bytearray.fromhex(x[2]).decode(),{}]

	for k in pngs.keys():
		query = "SELECT hex(id), ord, type, HEX(FROM_BASE64(Value)) FROM Thing WHERE HEX(PID)=%(pid)s ORDER BY ORD"
		mycursor.execute(query, {'pid': k})
		myresult = mycursor.fetchall()
		with open(pngs[k][2]+'.png', 'wb') as fout:
			for x in myresult:
				if x[3] != None:
					fout.write(binascii.unhexlify(''.join(x[3])))
				else: # Sub container
					query2 = "SELECT ord, type, HEX(FROM_BASE64(Value)) FROM Thing WHERE HEX(PID)=%(container)s ORDER BY ORD"
					mycursor2.execute(query2, {'container': x[0]})
					myresult2 = mycursor2.fetchall()
					for y in myresult2:
						fout.write(binascii.unhexlify(''.join(y[2])))
		fout.close()



def handleBooks():
	print("Handling books")
	b_pid = category_ids['bookshelf'][0]
	print(b_pid)
	lookup = "SELECT HEX(ID) AS ID, TYPE, HEX(VALUE) AS VALUE, HEX(PID) as PID FROM Thing WHERE type='book'"
	mycursor.execute(lookup, {'pid': b_pid})
	myresult = mycursor.fetchall()
	books={}
	for x in myresult:
		#books[x[0]]=[x[0],x[1],bytearray.fromhex(x[2]).decode(),{}]
		books[x[0]]=[x[0],x[1],x[2],x[3],{}]

#	for k in books.keys():
#		print(k,books[k])
	# Get book details
	bookdetails = "select hex(id),type,value,hex(pid) from Thing where type like 'book.%'"
	mycursor.execute(bookdetails)
	myresult = mycursor.fetchall()

	for x in myresult:
		pid = x[3]
		value = x[2]
		atype = x[1]
		abook = books[pid]
		abook[4][atype]=value

	for k in books.keys():
		b = books[k][4]
		print("Language: {0}\nURL: {1}\nAuthor: {2}\nTitle: {3}\nYear: {4}\nISBN: {5}\n\n".format(b["book.language"],b["book.url"],b["book.author"],b["book.title"],b["book.year"],b["book.isbn"]))

def handleAdresses():
	ab_pid = category_ids['addressbook'][0]

	mycursor.execute(lookup, { 'pid': ab_pid })

	myresult = mycursor.fetchall()

	addresses={}

	for x in myresult:
	#       print(x)
	        addresses[x[0]]=[x[0],x[1],bytearray.fromhex(x[2]).decode(),{}]

	#for k in addresses.keys():
	#       print(k)

	addressdetails = "select hex(id),type,value,hex(pid) from Thing where type LIKE 'address.%'"
	mycursor.execute(addressdetails)
	myresult = mycursor.fetchall()

	for x in myresult:
	        pid = x[3]
	        value = x[2]
	        atype = x[1]
	        arecord=addresses[pid]
	        arecord[3][atype]=value

	for k in addresses.keys():
	        ad = addresses[k][3]
	        print("Address-ID: {0}\nGender: {1}\nPhone: {2}\nAge: {3}\nPicture: {4}\nFruit: {5}\nAbout: {6}Name: {7}\nEMail: {8}\nCompany: {9}\nAddress: {10}\nGUID: {11}\nEyeColor: {12}\nRegistered: {13}\nGreeting: {14}\n\n".format(addresses[k][0],ad["address.gender"],ad["address.phone"],ad["address.age"],ad["address.picture"],ad["address.favoriteFruit"],ad["address.about"], ad["address.name"], ad["address.email"], ad["address.company"], ad["address.address"],ad["address.guid"],ad["address.eyeColor"],ad["address.registered"],ad["address.greeting"]))



mydb = mysql.connector.connect(host='192.168.0.1',user='he19',passwd='he19',db='he19thing')
mycursor = mydb.cursor()
mycursor2 = mydb.cursor()
mycursor.execute("SELECT HEX(ID) AS ID, TYPE, HEX(VALUE) AS VALUE, HEX(PID) AS PID FROM Thing WHERE PID IS NULL;")
myresult = mycursor.fetchall()
for x in myresult:
	r = myresult[0]
root_id=r[0]
#print(root_id)
lookup = "SELECT HEX(ID) AS ID, TYPE, HEX(VALUE) AS VALUE, HEX(PID) as PID FROM Thing WHERE HEX(PID)=%(pid)s"
mycursor.execute("SELECT HEX(ID) AS ID, TYPE, HEX(VALUE) AS VALUE FROM Thing WHERE HEX(PID)='{0}'".format(root_id))
myresult = mycursor.fetchall()

for x in myresult:
  category_ids[x[1]]=[x[0],x[1],bytearray.fromhex(x[2]).decode()]


handlePNGs()