# -*- coding: utf-8 -*-
import glob
import os
import hashlib
import pprint

class fileUtil:

    def __init__(self, path):
        self.path = path

    def __checksum(self, file):
        """
        Computes the md5 hash of the file
        :param file: full file path
        :return: md5 hash
        """
        return hashlib.md5(open(file, 'rb').read()).hexdigest()

    def __fileSize(self, file):
        """
        Computes the size the file
        :param file: full file path
        :return: file size
        """
        return os.path.getsize(file)


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
        res = {}
        for file in files:
            size = self.__fileSize(file)
            if size in res.keys():
                res[size].append(file)
            else:
                res[size] = [file]
        return self.__remove_non_duplicates(results = res)

    def findDuplicateFilesByChecksum(self, files):
        """
        Finds duplicate files by checksum and groups them into a dictionary. Key is the filesize and value is the list of filepaths.
        :param files: list of file paths
        :return: Dictionary that contains the grouping.
        """
        res = {}
        for file in files:
            size = self.__checksum(file)
            if size in res.keys():
                res[size].append(file)
            else:
                res[size] = [file]
        return self.__remove_non_duplicates(results = res)
