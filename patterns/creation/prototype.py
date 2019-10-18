#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


class Prototype():
    
    value = 'default'

    def clone(self, **attrs):
        obj_self = self
        obj = self.__class__()
        print(f"obj_self: {type(obj_self)}, obj: {type(obj)}")
        obj.__dict__.update(attrs)
        return obj


class PrototypeDispatcher():
    def __init__(self):
        self._objects = {}

    def get_objects(self):
        return self._objects

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]


def main():
    dispatcher = PrototypeDispatcher()
    prototype = Prototype()

    _value = {'username': 'Leejini', 'password': 'foo!'}
    default = prototype.clone()
    dict_prototype = prototype.clone(value=_value, type='dictionary')
    json_prototype = prototype.clone(value=json.dumps(_value), type='json')

    dispatcher.register_object('dict_data', dict_prototype)
    dispatcher.register_object('json_data', json_prototype)
    dispatcher.register_object('default', default)

    print([{n:type(p.value)} for n, p in dispatcher.get_objects().items()])

if __name__ == '__main__':
    main()
