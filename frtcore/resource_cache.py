import os
from frtcore import ResourceConnectorFactory
from frtcore import FileResourceConnector
from frtcore import FILE_CONNECTOR

class ResourceCache(object):
    def __init__(self, location, **kwargs):
        self.location = location
        self.cache_path, self.filename = os.path.split(self.location)

        self.connector = ResourceConnectorFactory.create_connector(self.location)
        if self.connector is None and self.filename:
            self.connector = FileResourceConnector(self.location)

        if (self.connector.type == FILE_CONNECTOR or
                self.connector.type == FILE_CONNECTOR) and \
            not os.path.isdir(self.cache_path):
            os.makedirs(self.cache_path)

    def exists(self):
        return self.connector.exists()

    def delete(self):
        if self.exists():
            self.connector.delete()

    def read_data(self):
        return self.connector.open().decode('string-escape').strip('"')

    def write(self, content):
        self.connector.write(content)
