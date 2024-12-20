import os
import typing as tp
from dataclasses import dataclass


@dataclass(frozen=True)
class WorkerConfig:
    DEVICE: tp.Literal["cuda", "cpu"] = os.getenv("DEVICE", "cpu")
    MODEL_NAME: str = os.getenv("WHISPER_MODEL_NAME", "tiny")
    DOWNLOAD_ROOT: str = os.getenv("DOWNLOAD_ROOT", "/cache")
    PIKA_HOST = os.getenv("PIKA_HOST", "localhost")
    PIKA_PORT = int(os.getenv("PIKA_PORT", "5672"))
    PIKA_USER = os.getenv("PIKA_USER", "rmuser")
    PIKA_PASS = os.getenv("PIKA_PASS", "rmpassword")
    PIKA_QUEUE = os.getenv("PIKA_QUEUE", "task_queue")


@dataclass(frozen=True)
class ObjectStorageConfig:
    PATH: str = os.getenv("OBJECT_STORAGE_PATH", "/object_storage")


worker_config = WorkerConfig()
object_storage_config = ObjectStorageConfig()
