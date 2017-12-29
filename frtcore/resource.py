import json
from frtcore import ResourceCache
from frtcore import ResourceConnectorFactory
class Resource(object):

    def __init__(self, location, cache_location=None, tlsverify=True, resource_connector=None):

        self.location = location
        connector_args = {'tlsverify': tlsverify}

        if not resource_connector:
            self.connector = ResourceConnectorFactory.create_connector(location, **connector_args)
        else:
            self.connector = resource_connector

        if cache_location:
            self.cache = ResourceCache(cache_location)
        else:
            self.cache = None

        self.in_memory_data = None

    def configure_cache(self, cachepath):
        self.cache = ResourceCache(cachepath)

    def delete_cache(self):
        if self.cache:
            self.cache.delete()

    def cache_path(self):
        if self.cache:
            return self.cache.location
        return ''

    def update(self):
        if self.cache:
            self.cache.delete()

        data = self.connector.open()

        if self.cache:
            self.cache.write(data)
        return data

    def read(self):
        data = None
        if self.cache and self.cache.exists():
            data = self.cache.read_data()
        else:
            data = self.update()

        if isinstance(data, str):
            try:
                return json.loads(data)
            except ValueError:
                pass
        return data

    @property
    def connector_type(self):
        return self.connector.type

    @property
    def data(self):
        if not self.in_memory_data:
            self.in_memory_data = self.read()

        return self.in_memory_data