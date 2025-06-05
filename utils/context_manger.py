"""Manages how the context is stored and retrieved from the redis cache/the database"""

from models import ContextData, ContextQuery, ContextResponse

class FetchContext():
    def __init__(self, query: ContextQuery, response: ContextResponse):
        pass

    def search_redis(self)-> bool:
        pass

    def search_db(self)-> bool:
        pass

    def get_cache(self)-> ContextResponse:
        pass

    def get_db(self)-> ContextResponse:
        pass

    def get_context(self)-> ContextResponse:
        if self.check_redis(self.query):
            self.response = self.get_cache(self.query)
        else: 
            self.response = self.get_db(self.query)
        return self.response
    
class UpdateContext():
    def __init__(self, data: ContextData, status: bool):
        pass

    def update_cahe(self):
        pass

    def update_db(self):
        pass

    def update(self):
        self.update_redis(self.data)
        self.update_db(self.data)