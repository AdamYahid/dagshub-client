import enum
import logging
from dataclasses import dataclass
from typing import Any, List, Union, Optional

from .datapoint import Datapoint  # noqa
from .query_result import QueryResult  # noqa

logger = logging.getLogger(__name__)


@dataclass
class Metadata:
    key: str
    value: Any


autogenerated_columns = {
    "path",
    "datapoint_id",
    "dagshub_download_url",
}


class IntegrationStatus(enum.Enum):
    VALID = "VALID"
    INVALID_CREDENTIALS = "INVALID_CREDENTIALS"
    MISSING = "MISSING"


class PreprocessingStatus(enum.Enum):
    READY = "READY"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    UNKNOWN = ""  # TODO: delete once it's returned consistently


class DatasourceType(enum.Enum):
    BUCKET = "BUCKET"
    REPOSITORY = "REPOSITORY"
    CUSTOM = "CUSTOM"


class MetadataFieldType(enum.Enum):
    BOOLEAN = "BOOLEAN"
    INTEGER = "INTEGER"
    FLOAT = "FLOAT"
    STRING = "STRING"
    BLOB = "BLOB"


@dataclass
class MetadataFieldSchema:
    name: str
    valueType: MetadataFieldType
    multiple: bool


@dataclass
class DatasourceResult:
    id: Union[str, int]
    name: str
    rootUrl: str
    integrationStatus: IntegrationStatus
    preprocessingStatus: PreprocessingStatus
    type: DatasourceType
    metadataFields: Optional[List[MetadataFieldSchema]]


@dataclass
class DatasetResult:
    id: Union[str, int]
    name: str
    datasource: DatasourceResult
    datasetQuery: str
