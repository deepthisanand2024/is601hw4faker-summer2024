sunilvjn@VRINDAVAN:~/projects2024/hw4/myproject$ pytest --num_records=40
====================================================================================================== test session starts ======================================================================================================
platform linux -- Python 3.10.12, pytest-8.2.2, pluggy-1.5.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/sunilvjn/projects2024/hw4/myproject
configfile: pytest.ini
testpaths: tests
plugins: pylint-0.21.0, Faker-25.8.0, cov-5.0.0
collected 91 items                                                                                                                                                                                                              
sunilvjn@VRINDAVAN:~/projects2024/hw4/myproject$ pytest --num_records=50
====================================================================================================== test session starts ======================================================================================================
platform linux -- Python 3.10.12, pytest-8.2.2, pluggy-1.5.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/sunilvjn/projects2024/hw4/myproject
configfile: pytest.ini
testpaths: tests
plugins: pylint-0.21.0, Faker-25.8.0, cov-5.0.0
collected 60 items / 1 error                                                                                                                                                                                                    
==================================================================================================== short test summary info ====================================================================================================
ERROR tests/test_operations.py - ValueError: Error: Division by zero


Summary: Test failed for 50th record onwards. Adding the snapshot

