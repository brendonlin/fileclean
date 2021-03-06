import os
import shutil
from abc import ABC, abstractclassmethod
from . import PathNotFoundError


class Worker(ABC):
    def __init__(self, fromFilepath, toPath, pattern):
        self.fromFilepath = fromFilepath
        self.toPath = toPath
        self.pattern = pattern

    @abstractclassmethod
    def work(self):
        pass

    def isExists(self):
        if isinstance(self.toPath, str) and os.path.exists(self.toPath):
            fileList = os.listdir(self.toPath)
            basename = os.path.basename(self.fromFilepath)
            return basename in fileList
        else:
            raise PathNotFoundError


class DeleteWorker(Worker):
    def work(self):
        os.remove(self.fromFilepath)


class CopyWorker(Worker):
    def work(self):
        if not self.isExists():
            shutil.copy(self.fromFilepath, self.toPath)


class MoveWorker(Worker):
    def work(self):
        if not self.isExists():
            shutil.move(self.fromFilepath, self.toPath)


def selectWorker(command):
    workers = {"delete": DeleteWorker, "copy": CopyWorker, "move": MoveWorker}
    return workers.get(command)
