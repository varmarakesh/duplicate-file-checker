from fileUtil import fileUtil
import pprint

target_dir_path = '/Users/rakesh.varma/dev/**/*.py'
f = fileUtil(path = target_dir_path)
files = f.findAllFiles()
result = f.findDuplicateFilesBySize(files = files)
result = f.findDuplicateFilesByChecksum(files = reduce(lambda a,b:a+b, result.values()))

pprint.pprint(result)

