Background:
I am a manufacturing engineer, not a programmer. However, I like to study the program. In my daily job, I have to deal with different kinds of Excel files. And I know some VBA, so I have created some Marco in Excel to open and read several check list.
But the excel Marco user form run very slow, because every time when I run the Marco it have to open another big size Excel file as check list database. 
I decided to abandon my Excel Marco, and 
restart with the hot language Python. 

Purpose:
Build a better maintenance, faster check list with Python. 

Basic Feature:
	1. Checking items in the user interface is load from database.  
	2. Has version control for every check point modify, new add, del.
	3. User review each checking items, select "Pass", "Violated", "N/A".
		a. If "Pass"  , jump to next item.
		b. If "Violated", require to input more detail in a textbox.  Better to have attachment (Photo, document attached)
		c. If "N/A", also jump to next item.
		d. All the selection and  "Violated" textbox input content store in an area, where can overall review.
	4. Separate two groups. One is administer, another is normal user. The administer can edit/add/remove the checking items. 

Plan to use module:
	• Openpyxl
	• OS
	• Others..

Some problem I meet:
Use website frame, like Django  or other GUI module to implement the check list interface???
