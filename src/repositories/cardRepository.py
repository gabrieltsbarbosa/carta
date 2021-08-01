cartas_db = {}


class Repo():
    def get(id = 0):
        if id != 0:
            for i in cartas_db:
                if i == id:
                    return cartas_db[id], 200
        
            return "", 404

        cartas = []
        for i in cartas_db:
            cartas.append(cartas_db[i])
        return cartas

    
    def insert(package):
        id = len(cartas_db) + 1
        carta = {
            id:{
                'id': id,
                'nome': package['nome'],
                'endereco': package['endereco'],
                'texto':package['texto']
            }
        }
        cartas_db.update(carta)
        return carta[id], 201

    def update(id, package):
        carta = cartas_db[id]
        carta[package['item']] = package['content']
        return cartas_db[id], 200

    def delete(id):
        try:
            cartas_db.pop(int(id))
            return "Carta deletada com sucesso", 200

        except:
            return "Error", 404

    

    


