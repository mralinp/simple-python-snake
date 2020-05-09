def save(name, score):
    file = open("./db.db", "a")
    file.write(name+":"+str(score))
    file.write("\n")
    file.close()
def load():
    buff = [""]
    try:
        file = open("./db.db", "r")
        buff = file.readlines()
        file.close()
    except :
        file = open("./db.db", "w+")
        file.write("")
        file.close()
    return buff
    
if __name__ == '__main__':
    save("hassan", 4000)
    save("mohammad", 3050)
    save("ali", 1230)
    print(load())
    