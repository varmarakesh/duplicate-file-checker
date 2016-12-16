import unittest
from fileUtil import fileUtil
import os

class test(unittest.TestCase):

    def setUp(self):
        self.f = fileUtil(path = os.getcwd()+'/*')
        self.files = self.f.findAllFiles()
        print self.files

    def test_findAllFiles(self):
        self.assertIsNotNone(self.files)

    def test_findDuplicateFilesBySize(self):
        #expecting no python files in the current directory have the same file size.
        result = self.f.findDuplicateFilesBySize(files = self.files)
        self.assertEqual(len(result),0)

    def test_findDuplicateFilesByChecksum(self):
        #expecting no python files in the current directory have the same checksum.
        result = self.f.findDuplicateFilesByChecksum(files = self.files)
        self.assertEqual(len(result),0)

