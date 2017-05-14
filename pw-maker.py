import db_controller
import sys

db = db_controller.Db_Controller(0)
# db.insert("did it work?")
# print db.get_pw("John")
# db.save_pw("Margo", "Facebook", "abcabc")
print(sys.argv[1] + " " + sys.argv[2])
print(db.save_pw_from_strings(sys.argv[1], sys.argv[2]))