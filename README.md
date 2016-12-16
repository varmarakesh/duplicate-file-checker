duplicate-file-checker implements an easy to consume python API to determine the duplicate files (by content) in a given directory path.
#Steps to Install and Run.

1. Clone the git repository.

    ```
    git clone https://github.com/varmarakesh/duplicate-file-checker
    ```

2. Run the solution after changing the target_dir_path variable in the run.py
    ```
        cd duplicate-file-checker/duplicate-file-checker
        python run.py
    ```
3. To run the unit tests.
    ```
        python -m unittest -v tests
    ```
#Compatability
    This was tested on mac osx and ubuntu linux 14 (on python 2.7)
    All libraries that were used in the project come as a part of python standard library. There is no need to separately install other libs.