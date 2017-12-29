HTTP_CONNECTOR = 0
FILE_CONNECTOR = 1
DIRECTORY_CONNECTOR = 2
MBOX_CONNECTOR = 3
from frtcore.resource_connector import ResourceConnectorFactory
from frtcore.resource_connector import HttpResourceConnector
from frtcore.resource_connector import FileResourceConnector
from frtcore.resource_connector import DirectoryResourceConnector
from frtcore.resource_connector import MBoxResouceConnector
from frtcore.resource_cache import ResourceCache
from frtcore.resource import Resource
from frtcore.dictionary import TransformableDict
from frtcore.dictionary import SaveableLoadableDict
from frtcore.dictionary import JSONTransformableDictEncoder
