import pickle

dbfilename = 'test3_4.dat'

def readScoreDB():
	try:
		fH = open(dbfilename, 'rb')
	except FileNotFoundError as e:
		print("New DB: ", dbfilename)
		return []

	scdb = []
	try:
		scdb =  pickle.load(fH)
	except:
		print("Empty DB: ", dbfilename)
	else:
		print("Open DB: ", dbfilename)
	fH.close()
	return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

def doScoreDB(scdb):
	while(True):
		inputstr = input("Score DB > ")
		if inputstr == "": continue
		parse = inputstr.split(" ")

		if parse[0] == 'add':
			record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
			scdb += [record]

		elif parse[0] == 'del':
			list_p = []
			count = 0
			for p in scdb:
				if p['Name'] == parse[1]:
					count += 1
					list_p.append(p)
			for p in list_p:
				scdb.remove(p)

		elif parse[0] == 'show':
			sortKey = 'Name' if len(parse) == 1 else parse[1]
			showScoreDB(scdb, sortKey)

		elif parse[0] == 'find':
			for li in scdb:
				if li['Name'] == parse[1]:
					for list_ in sorted(li):
						print(list_ + "=" + li[list_], end=' ')
					print()

		elif parse[0] == 'inc':
			for list in scdb:
				if list['Name'] == parse[1]:
					list['Score'] = int(list['Score'])
					list['Score'] += int(parse[2])

		elif parse[0] == 'quit':
			break
		else:
			print("Invalid command: " + parse[0])
			

def showScoreDB(scdb, keyname):
	for p in sorted(scdb, key=lambda person: person[keyname]):
		for attr in sorted(p):
			print(attr + "=" + str(p[attr]), end=' ')
		print()
	


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

