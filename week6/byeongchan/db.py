import pickle


class Db:
    __DATA_FILE_NAME = "db_data.dat"
    __score_db = None

    @classmethod
    def filename(cls):
        return cls.__DATA_FILE_NAME

    @classmethod
    def reload(cls):

        try:

            with open(cls.__DATA_FILE_NAME, 'rb') as f:
                try:
                    cls.__score_db = pickle.load(f)
                except FileNotFoundError:  # when dbfile is empty
                    print("Empty DB: ", cls.__DATA_FILE_NAME)
                else:
                    print("Open DB: ", cls.__DATA_FILE_NAME)

        except FileNotFoundError:  # when dbfile doesn't exist
            print("New DB: ", cls.__DATA_FILE_NAME)

    @classmethod
    def update(cls):
        with open(cls.__DATA_FILE_NAME, 'wb') as f:
            pickle.dump(cls.__score_db, f)

    @classmethod
    def add(cls, name: str, score: int, age: int):
        cls.__score_db.append({"NAME": name, "SCORE": score, "AGE": age})

    @classmethod
    def delete(cls, name: str):
        records = cls.find(name)
        for rec in records:
            cls.__score_db.remove(rec)

    @classmethod
    def find_all(cls):
        return cls.__score_db

    @classmethod
    def find(cls, name: str):
        return list(filter(lambda r: r["NAME"] == name, cls.__score_db))

    @classmethod
    def inc(cls, name: str, amount: int):
        records = cls.find(name)
        cls.delete(name)
        for rec in records:
            rec["SCORE"] += amount
        cls.__score_db += records

    @classmethod
    def marshall(cls, sortkey: str = "NAME", name=None):
        msg = ""
        data = cls.find(name) if name else cls.__score_db
        sorted_records = sorted(data, key=lambda person: person[sortkey])
        for record in sorted_records:
            for attr in sorted(record):
                msg += "%s=%s " % (attr, record[attr])
            msg.rstrip()
            msg += "\n"
        return msg


if __name__ == '__main__':
    Db.reload()
    print(Db.find_all())

    print(Db.update())
