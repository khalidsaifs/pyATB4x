# API automation frame work
# python + request module + pytest + Allure Report.

'''
Rules for creating test cases.
1. Not all test cases are executed, only stable cases are automated.
2. Stable flows - regression suits.
    a. CRUD - create booking, update, delete, fetch.
3. ind end to end
4. create booking, update booking, delete and GET - 404

How can i automate?

1. python language
2. HOw to make a request - request module.
    a. HTTP methods - GET, POST, PUT,Patch and DELETE.
3. verify the response using pytest (used to verify and maintain test cases).
4. mostly we will automate 10-15 test cases.

'''

#  Pytest:
'''
It is a powerful testing framework using python and maintain my test cases.
It is widely used for execution of test cases. 

Rules:
1.we have to name the file name test_file_name.py
2.we have name teh method  as follwing 
        def test_main_name()
        def test_test_case_1():
3. You can add assertions:
        expected results == Actual results
        its will give the results in pass or fail.
4. F = fail
5. green dot - p - Pass.
6. you can mark your test using - @pytest.mark.name.
-m for marking in console.
-v for verbos for more info about results
-s for seeing the data 


'''