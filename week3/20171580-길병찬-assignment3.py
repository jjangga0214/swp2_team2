import pickle
import functools

db_file_name = 'test3_4.dat'


def read_score_db():
    scdb = []

    try:
        with open(db_file_name, 'rb') as f:
            try:
                scdb = pickle.load(f)
            except FileNotFoundError:  # when dbfile is empty
                print("Empty DB: ", db_file_name)
            else:
                print("Open DB: ", db_file_name)
#
    except FileNotFoundError:  # when dbfile doesn't exist
        print("New DB: ", db_file_name)

    return scdb


# write the data into person db
def write_score_db(scdb):
    with open(db_file_name, 'wb') as f:
        pickle.dump(scdb, f)


def do_score_db(scdb):
    while True:
        input_str = input("Score DB > ").strip()

        if input_str.strip() == "":
            continue

        parsed_input = input_str.split(" ")
        cmd = parsed_input[0].lower()

        if cmd == 'add':
            if len(parsed_input) != 4:
                print("add 의 인자는 이름, 나이, 성적 순서대로 단 3개이어야 합니다.")
                continue

            try:
                age = int(parsed_input[2])
                score = int(parsed_input[3])
                if age < 0 or score < 0:
                    raise ValueError()
            except ValueError:
                print("나이 또는 성적은 0 이상의 정수이어야 합니다.")
            else:
                record = {'Name': parsed_input[1], 'Age': age, 'Score': score}
                scdb.append(record)

        elif cmd == 'del':
            if len(parsed_input) != 2:
                print("del 의 인자는 이름 단 1개이어야 합니다.")
                continue

            for i in reversed(range(len(scdb))):
                if scdb[i]['Name'] == parsed_input[1]:
                    del scdb[i]

        elif cmd == "find":
            if len(parsed_input) != 2:
                print("find 의 인자는 이름 단 1개이어야 합니다.")
                continue

            record = find_by_field(scdb, "Name", parsed_input[1])
            print_record(record)

        elif cmd == "inc":
            if len(parsed_input) != 3:
                print("inc 의 인자는 순서대로 이름과 성적 단 2개이어야 합니다.")
                continue

            try:
                amount = int(parsed_input[2])
            except ValueError:
                print("더하거나 뺄 성적은 정수이어야 합니다.")
            else:
                for record in find_by_field(scdb, "Name", parsed_input[1]):
                    record["Score"] += amount

        elif cmd == 'show':
            if len(parsed_input) > 2:
                print("show 의 인자는 0개 또는 필드 1개이어야 합니다.")
                continue

            sort_key = 'Name' if len(parsed_input) == 1 else parsed_input[1]
            try:
                print_score_db(scdb, sort_key)
            except InvalidFieldError:
                print("찾으려는 필드가 존재하지 않습니다.")

        elif cmd == 'quit':
            print("saving now...")
            write_score_db(scdb)
            print("bye")
            break

        else:
            print("Invalid command: " + parsed_input[0])


def print_record(record):
    for attr in sorted(record):
        print(attr + "=" + str(record[attr]), end=" ")
    print()


def print_score_db(scdb, keyname):
    try:
        sorted_records = sorted(scdb, key=lambda person: person[keyname])
    except KeyError:
        raise InvalidFieldError()

    for p in sorted_records:
        print_record(p)


def find_by_field(scdb, field_name, field_val):
    return filter(lambda p: p[field_name] == field_val, scdb)

class InvalidFieldError(Exception):
    pass

score_db = read_score_db()
do_score_db(score_db)
