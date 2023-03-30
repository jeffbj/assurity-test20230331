# assurity-test20230331

This is a Python script for a technical assignment below:

> Using the API given below create an automated test with the listed acceptance criteria:
>
> **API** = https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false
>
> **Acceptance Criteria:**
> - Name = "Carbon credits"
> - CanRelist = true
> - The Promotions element with Name = "Gallery" has a Description that contains the text "Good position in category"
> 
> **Instructions:**
> - Your test needs to be written using a programming language of your choice (not a tool like SoapUI). Ensure you include a clear ReadMe
> - Submit your test to us in a format that lets us execute and review the code (it must be submitted in a public repository like Bitbucket or Github)
> - Your test must validate all the three acceptance criteria
> - Points will be awarded for meeting the criteria, style and the use of good practices and appropriate use of source control
> - We want to see your best work - no lazy coding or comments.


## Dependencies
This automated test written in Python requires the following depencencies to be installed:

* Python 3.x
* requests library
* unittest library


## Installation
To install the dependencies, run the following command:
```
pip install requests
```


## Usage
To run the test, execute the following command:
```
python -m unittest test_queryInfo.py
```
Run the script.The log messages will be displayed in the console.


## How it works
The setUp method is executed before each test case and sends a GET request to the API, saving the JSON response as an attribute of the TestApi instance.

Each test case validates a different aspect of the response. 
- The first test case `test_name` checks if the 'Name' attribute of the response is ***equal*** to an expected value. 
- The second test case `test_canRelist` checks if the 'CanRelist' attribute is ***true***. 
- The third test case `test_promotionsGalleryDescription` checks if the 'Description' attribute of the 'Gallery' promotion ***contains*** an expected value.

The logging module is used to add log messages at key points in the script, such as when a test case is running and when it passes or fails. This helps with debugging and understanding the flow of the script.

## Acceptance list of assignment
***1. Your test needs to be written using a programming language of your choice (not a tool like SoapUI). Ensure you include a clear ReadMe***
- [x] Test script is written in Python
- [x] The Outcome includes a clear ReadMe file(this file)

***2. Submit your test to us in a format that lets us execute and review the code (it must be submitted in a public repository like Bitbucket or Github)***
- [x] The outcome is submitted on Github
- [x] The test can be executed by following the README file
- [x] The code can be reviewed clearly on Github

***3. Your test must validate all the three acceptance criteria***
- [x] Three test cases validate all the three acceptance criteria
- [x] Test case `test_name` validates the acceptance cirteria `Name = "Carbon credits"`
- [x] Test case `test_canRelist` validates the acceptance cirteria `CanRelist = true`
- [x] Test case `test_promotionsGalleryDescription` validates the acceptance cirteria `The Promotions element with Name = "Gallery" has a Description that contains the text "Good position in category"`

***4. Points will be awarded for meeting the criteria, style and the use of good practices and appropriate use of source control***
- [x] The outcome meets the criteria
- [x] The outcome has good code style and engineering practices
- [x] The outcome uses git appropriately for source control 

***5. We want to see your best work - no lazy coding or comments.***
- [x] The test script includes comments and logs to aid in understanding, debugging and maintaining the script flow
