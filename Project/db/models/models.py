class Model:
    def __init__(self, line : str):
        pass

class RequestsModel(Model):
    def __init__(self, line):
        super().__init__(line)
        self.id = int(line[0])
        self.hard = line[1]
        self.help = line[2]
        self.department = line[3]
        self.comment = line[4]
        self.pick_flag = line[5]
        self.user_id = int(line[6])
        self.tech_id = int(line[7])



class UserModel(Model):
    def __init__(self, line):
        super().__init__(line)
        self.id = int(line[0])
        self.login = line[1]
        self.password = line[2]
        self.role = line[3]