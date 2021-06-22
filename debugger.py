import inspect
import enum

class LogLevel(enum.Enum):
    INFO = 0
    WARN = 1
    CRIT = 2
    EMER = 4
    OFF  = 5

class db: 
    PRINT = True
    LOGLEVEL = LogLevel.OFF

    @staticmethod
    def eval(n = None):
        if db.PRINT and n != None:
            print(f"db [{inspect.stack()[1][2]}] | {db.varName(n)} {type(n)}: {n}")

        if db.PRINT and n == None:
            print(f"db [{inspect.stack()[2][2]}] | {inspect.stack()[2][1]}")

        if callable(n):
            return n

    @staticmethod
    def log(line, level):
        if level.value >= db.LOGLEVEL.value:
            print(line)

    @staticmethod
    def loglevel(new_level: LogLevel):
        db.LOGLEVEL = new_level

    @staticmethod
    def varName(var):
        return str(inspect.stack()[2][4][0])[12:-2]

    @staticmethod
    def disable(): db.PRINT = False;

    @staticmethod
    def enable(): db.PRINT = True;

