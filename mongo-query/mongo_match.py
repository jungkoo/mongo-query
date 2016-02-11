# -*- coding: utf-8 -*-
class MongoMatch:
    def __init__(self, match={}):
        self._match = match
        self._type_map = {}

    def __and__(self, other):
        self._match.update(other)
        return self

    # def __or__(self, other):
    #     print self._match
    #     print other

    def __call__(self):
        return self._match

if __name__ == '__main__':
    m = MongoMatch()
    m &= {"title": 1}
    m &= {"name": "2"}

    print m()
