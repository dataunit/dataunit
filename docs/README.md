Introduction
------------
DataUnit is a framework that makes it easy to write and execute automated unit tests for data integration code (aka ETL).   

It uses a spreadsheet-based Microsoft Excel template as its main user interface, into which users enter their test information, such as the job metadata, as well as their unit test data as rows and columns.  

The framework then uses that information to run the code being tested, comparing the expected results to the actual results, and reporting the outcome (pass/fail) of the tests being that were run. 

Test Workbook Data Model
------------------------
The Test Workbook is main user interface and way in which users can enter tests, test commands and test data.  

The Data Model for the Test Workbook is described below.  In general, each sheet within the Test Workbook is represented by an entity in the model.  As the Test Workbook is the container for all the other entities, it is represented as having a relationship to entities, even though there is no direct data element linking those entities.

[Example of a Test Workbook](test_case_workbook.v3.xlsx)

* The **Test Workbook** is a container for a set of **Tests**.
* A separate **Test Runner** is used to execute the **Tests** contained in a **Workbook**.  The **Workbook** could be passed to the **Test Runner** as a command-line argument.
* A **Workbook** can have one or more **Tests** as well as one or more **Settings**.   
* **Settings** control the behavior of the **Workbook** and **Tests** that are run by the **Test Runner**.
* Each **Test** can have one or more **Test Commands** which in turn can have one or more **Parameters**.  
* **Tests** can also have **Variables** which can be defined to share values and settings across multiple tests.  
* **Variables** are resolved to their value at the time a test is run, and the values of **Variables** can change as **Tests** are run.  (We may want to make an option of making a Variable static so that it is read-only).  This is main mechanism for Tests to share information.  An example of a Variable would be `INPUT_DATA_DIRECTORY`.   This could be used in setting one of the **Test Command Parameters** for a **Test Command** that reads data from a file directory.  
An example of a Setting is `VariableStartDelimiter` and `VariableEndDelimiter`.  These would be used by the **Test Runner** to detect the presence of **Variables** specified in **Test Command Parameters**, or in the other sheets.  So, for instance if you specified a `VariableStartDelimiter=“${“` and `VariableEndDelimiter=”}”`, then you could use Variables in your Test Command Parameters such as `${INPUT_DATA_DIRECTORY}`, which would then be resolved to its value.
* There are several worksheets that are hidden that are used for driving the user interface.  Borrowing from the Python convention of using underscores to prefix private variables, these worksheets are prefixed by underscores.  The **_commands** sheet is a lookup of the list of Test Commands, and the **_command_parameters** contains parameters associated with the _commands.

![Data Model](docs/DataUnit_ERD.png)