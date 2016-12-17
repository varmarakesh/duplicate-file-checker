# -*- coding: utf-8 -*-
import glob
import os
import hashlib

class fileUtil:

    def __init__(self, path):
        self.path = path

    def __remove_non_duplicates(self, results):
        """
        Removes key-value pairs that have only one element in the value list.
        :param results: Dictionary contains key and values where value is a list.
        :return:
        """
        for key in results.keys():
            if len(results[key]) == 1:
                del results[key]
        return results

    def __findDuplicateFilesByAttributes(self, files, func):
        """
        Finds duplicates by attribute (checksum or filesize) and groups them into a dictionary
        :param files:
        :param func:
        :return:
        """
        res = {}
        for file in files:
            size = getattr(self, func)(file)
            if size in res.keys():
                res[size].append(file)
            else:
                res[size] = [file]
        return self.__remove_non_duplicates(results = res)

    def checkSum(self, file):
        """
        Computes the md5 hash of the file
        :param file: full file path
        :return: md5 hash
        """
        return hashlib.md5(open(file, 'rb').read()).hexdigest()

    def fileSize(self, file):
        """
        Computes the size the file
        :param file: full file path
        :return: file size
        """
        return os.path.getsize(file)

    def findAllFiles(self):
        """
        Retrieves a list of all files in the input directory, recursively.
        :return: list of all files
        """
        return [filename for filename in glob.iglob(self.path)]

    def findDuplicateFilesBySize(self, files):
        """
        Finds duplicate files by file size and groups them into a dictionary. Key is the filesize and value is the list of filepaths.
        :param files: list of file paths
        :return: Dictionary that contains the grouping.
        """
        return self.__findDuplicateFilesByAttributes(files, 'fileSize')

    def findDuplicateFilesByChecksum(self, files):
        """
        Finds duplicate files by checksum and groups them into a dictionary. Key is the filesize and value is the list of filepaths.
        :param files: list of file paths
        :return: Dictionary that contains the grouping.
        """
        return self.__findDuplicateFilesByAttributes(files, 'checkSum')

