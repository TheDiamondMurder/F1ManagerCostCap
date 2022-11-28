import sqlite3

def run_script(option=""):
    con = sqlite3.connect("scripts/result/main.db")
    cursor = con.cursor()

    newCap = option.lower()

    cursor.execute("UPDATE Regulations_Enum_Changes SET CurrentValue = " + str(newCap) + " WHERE ChangeID = 3")
    print("Set cost cap to $"+ str(newCap))

    con.commit()
    con.close()


def get_description():
    return "Allows you to edit the cost cap. \n Just put the value of the cost cap you want.  \nAuthor: u/DiamondF1"

if __name__ == '__main__':
    run_script()