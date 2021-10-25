from tracky.tracker import Tracker


class MyDict(dict):
    def __init__(self, data: list, *arg, **kw):
        super(MyDict, self).__init__(*arg, **kw)
        self.__assign__(data)

    def __assign__(self, data: dict):
        for key, value in data.items():
            if type(value) is int:
                self[key] = MyInt(value)
            elif type(value) is float:
                self[key] = MyFloat(value)
            elif type(value) is bool:
                # self[key] = myBool(value)
                self[key] = value
            elif type(value) is str:
                self[key] = MyStr(value)
            elif type(value) is dict:
                self[key] = MyDict(value)
            elif type(value) is list:
                self[key] = MyList(value)
            elif type(value) is None:
                self[key] = None
            else:
                raise Exception(f"Found unknown data type: {type(value)}")

    def __len__(self):
        Tracker.track()
        return super().__len__()

    
    def __iter__(self):
        Tracker.track()
        return super().__iter__()


class MyList(list):
    def __init__(self, data: list, *arg, **kw):
        super(MyList, self).__init__(*arg, **kw)
        self.__assign__(data)

    def __assign__(self, data: list):
        for obj in data:
            if type(obj) is int:
                self.append(MyInt(obj))
            elif type(obj) is float:
                self.append(MyFloat(obj))
            elif type(obj) is bool:
                # self.append(myBool(obj))
                self.append(obj)
            elif type(obj) is str:
                self.append(MyStr(obj))
            elif type(obj) is dict:
                self.append(MyDict(obj))
            elif type(obj) is list:
                self.append(MyList(obj))
            elif type(obj) is None:
                self.append(None)
            else:
                raise Exception(f"Found unknown data type: {type(obj)}")

    def __len__(self):
        Tracker.track()
        return super().__len__()

    def __iter__(self):
        Tracker.track()
        return super().__iter__()


class MyStr(str):
    def __new__(cls, *args, **kw):
        return str.__new__(cls, *args, **kw)

    def __len__(self):
        Tracker.track()
        return super().__len__()

    def __iter__(self):
        Tracker.track()
        return super().__iter__()


class MyInt(int):
    def __new__(cls, *args, **kw):
        return int.__new__(cls, *args, **kw)

    


class MyFloat(float):
    def __new__(cls, *args, **kw):
        return float.__new__(cls, *args, **kw)

def getMyCollection(data, args):
    Tracker.init(args)
    # JSON object
    if type(data) is dict:
        return MyDict(data)
    # JSON array
    elif type(data) is list:
        return MyList(data)
    else:
        raise Exception(f"Found unknown data type: {type(data)}")
