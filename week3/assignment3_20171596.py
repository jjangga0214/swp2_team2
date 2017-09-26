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
        scdb = pickle.load(fH)

    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    for i in scdb:
        i['Age'] = int(i['Age'])
        i['Score'] = int(i['Score'])
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while True:
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        try:
            if parse[0] == 'add':
                record = {'Name': parse[1], 'Age': int(parse[2]), 'Score': int(parse[3])}
                scdb += [record]

            elif parse[0] == 'del':
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)

            elif parse[0] == 'show':
                sortKey = 'Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)

            elif parse[0] == 'quit':
                break

            elif parse[0] == 'find':
                for p in scdb:
                    if p['Name'] == parse[1]:
                        print(p)

            elif parse[0] == 'inc':
                for p in scdb:
                    if p['Name'] == parse[1]:
                        p['Score'] = p['Score'] + parse[2]

                    else:
                        print('It dosen\'t exist ', parse[1], '. Please type the name again')
                        continue

            else:
                print("Invalid command: " + parse[0])
        except:
                print('Type again')


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + str(p[attr]), end=' ')
        print()

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

