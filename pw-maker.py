import db_controller

db = db_controller.Db_Controller(0)
# db.insert("did it work?")
# print db.get_pw("John")
# db.save_pw("Margo", "Facebook", "abcabc")
print db.get_pw("Margo", "Facebook")