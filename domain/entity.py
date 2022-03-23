class Entity:

    #current_id = 0

    def __init__(self, id_entity):
        self.__id_entity = id_entity
        #self.__id_entity = Entity.current_id
        #Entity.current_id += 1

    @property
    def id_entity(self):
        return self.__id_entity

    @id_entity.setter
    def id_entity(self, id_ent):
        self.__id_entity = id_ent
