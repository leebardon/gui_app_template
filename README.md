DATA SOURCE  - Qlikview 
Process for obtaining Qlikview spreadsheets (paraphrased from email sent by Peter Fisk)
1.	Open QlikView. 
a.	On Dashboard Tab select “exclude NERC” green button and select the Faculty/Prof service for the data. 
b.	Now switch to main tab then select the 8 main courses that we report on. Note  Visitor, BB User and IDM are all auto selected so no need to change. 
c.	Download lower table  data (highest scores) - this is then called “student Training Record” (note scores will be changing to dates). (spreadsheet 3 above)
d.	Next we use the “Completed” option and change to NO and then download the data from table “Health and safety” (top table) as this forms the ‘not completed’  spread sheet. (spreadsheet 1 above)
e.	From then on its just a matter of changing the Faculty/prof service on the dashboard each time renaming as we save. 

2.	…filter the training record spreadsheet on Display Screen Equipment(DSE) self assessment and select all scores from 40 upwards and copy paste into new spreadsheet called DSE at risk users. (spreadsheet 2 above)

NOTE from Lee: We will not download spreadsheets for each faculty individually – just a single download, the app will process accordingly to save manual legwork. No need to select specific faculty – just 1 spreadsheet for 
NOTE: The original version of the app had a module for obtaining currently active users from ldap. This has been removed, as it can be selected in Qlikview. It also includes functions for selecting ‘not completed’ – these will also be removed, as ban be done in qlikview. 

The 8 courses they report on (use ctrl-click to select in ‘Course Content Item’ , Main tab):
1.	5 step risk assessment
2.	Computer workstation setup
3.	DSE – user self assessment
4.	Fire awareness
5.	H&S Induction
6.	Manual Handling of Loads
7.	Slips, trips and falls
8.	Stress awareness course V1







THINGS TO DO - core functionality
Red – needs done
Amber – nice to have 
Green – done 

•	Python backend: 
o	Clean and process Qlikview excel spreadsheets
o	Filter results by faculty and department
o	Filter results by required scores
o	Generate three separate spreadsheets per department
o	Change saving location of output from local desktop to SharePoint
o	Add functions to email SharePoint link to email list (H&S to provide) 

•	GUI frontend (PyQT5 and PySide2)
o	Build interface for adding qlikview spreadsheets to the program
o	(H&S will only have to download 2 spreadsheets total, not 2 spreadsheets for each subdepartment as they were doing before) 
o	Ensure user has suitable instructions for naming input qlikview files 
	Program uses 2 input spreadsheets downloaded from qlikview - “student_records.xlsx” and “not_completed.xlsx”. Must be saved as file type xlsx and contain the string ‘records’ and ‘complete’ in filename at present. Check that this is clear in user instructions.
	Ultimately, a ‘help’ button could be added? That binds to an instructions ‘page’. See GuiController.py for examples (using pyqt5 and pyside2)

•	Create desktop icon  – see FrontPage - py2exe.org  and python - How to set a window icon with PyQt5? - Stack Overflow 

Maintenance 
•	Robust Error Handling (see comments in code)
•	Logging system (use system implemented in Collab-2-Panotpo)
•	Unit tests

To Run
•	NOTE – Built in VSCode on windows. Not sure if it will run in WSL, probably not linux box. 

Currently uses conda for env, and setup.py to build src and generate .exe files etc (see healthy_safety/health_safety)
•	Install deps – still not entirely sure with doing this in windows, think you need to install from anaconda prompt (navigate to project root and run conda install env.yaml)
•	Build -> run python setup.py build  to set src file structure. Code changes wont be picked up by the  build after this. During dev, use:
•	DEV  in project root, using windows cmd terminal thing, run python setup.py dev

•	run from GuiController.py (python -m src/Controllers/GuiController.py) or using vscode
