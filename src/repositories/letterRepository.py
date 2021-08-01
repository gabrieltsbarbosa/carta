letters_db = {}


class Repo():
    def get(id = 0):
        if id != 0:
            for i in letters_db:
                if i == id:
                    return letters_db[id], 200
        
            return "", 404

        letters = []
        for i in letters_db:
            letters.append(letters_db[i])
        return letters

    
    def insert(package):
        id = len(letters_db) + 1
        letter = {
            id:{
                'id': id,
                'name': package['name'],
                'adress': package['adress'],
                'txt':package['txt']
            }
        }
        letters_db.update(letter)
        return letter[id], 201

    def update(id, package):
        letter = letters_db[id]
        letter[package['item']] = package['content']
        return letters_db[id], 200

    def delete(id):
        try:
            letters_db.pop(int(id))
            return "Sucess", 200

        except:
            return "Error", 404

    

    


