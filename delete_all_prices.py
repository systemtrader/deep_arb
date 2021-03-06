from scripts.downloader.databaseMgr import *
from scripts.utility import *
class DeleteModule():
    def __init__(self):
        self.conn = sqlite3.connect("prices.db")
        self.cursor = self.conn.cursor()
    def deleteRun(self):
        res = q("SELECT name FROM sqlite_master WHERE type='table';")
        i=1
        tot = len(res)

        for r in res:
            pr("DELETE COMPLETION: " + str(round(i/tot * 100,4)) + "%")
            if r == "distances":
                continue
            self.cursor.execute("DROP TABLE %s" % r)
            self.conn.commit()
            i += 1
        print("DELETE COMPLETION: 100.0000%")

if __name__ == '__main__':
    d = DeleteModule()
    d.deleteRun()