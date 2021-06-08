Create database MyFitBot
Go

Use MyFitBot

Create table dbo.User_Profile(
Profile_Id int,
First_Name varchar(50),
Last_Name varchar(50),
Email varchar(50),
Gender char(1),
DOB date,
Current_Weight decimal(5,2),
Height int,
Goal_Weight decimal(5,2),
Daily_Net_Calorie_Goal int,
CONSTRAINT pk_user_profile PRIMARY KEY (Profile_Id)
)

Create table dbo.Diet_Log(
Diet_Log_Id INTEGER,
Profile_Id int,
Log_Date datetime,
Meal varchar(50),
Food_Name varchar(50),
Calorie_Per_Unit int,
Quantity int,
CONSTRAINT pk_diet_log PRIMARY KEY (Diet_Log_Id)
--,CONSTRAINT fk_diet_log_profile_id FOREIGN KEY (Profile_Id) REFERENCES User_Profile(Profile_Id)
)

Create table dbo.Exercise_Log(
Exercise_Id int,
Profile_Id int,
Log_Date datetime,
Exercise_Name varchar(50),
Calories_Burned int,
Description varchar(255)
CONSTRAINT pk_exercise_log PRIMARY KEY (Exercise_Id),
--CONSTRAINT fk_exercise_log_profile_id FOREIGN KEY (Profile_Id) REFERENCES User_Profile(Profile_Id)
)

--Delete from dbo.Exercise_Log
--Delete from dbo.Diet_Log
--Delete from dbo.User_Profile

INSERT INTO dbo.User_Profile(Profile_Id,First_Name,Last_Name,Email,Gender,DOB,Current_Weight,Height,Goal_Weight,Daily_Net_Calorie_Goal) 
VALUES 
(1,'Christel','Russen','crussen0@businessweek.com','F','1/25/1997',162.4,62,145,1500)
,(2,'Kieth','McCully','kmccully4@theguardian.com','M','8/27/1991',179.9,69,165,1700);

INSERT INTO dbo.Exercise_Log(Exercise_Id,Profile_Id,Log_Date,Exercise_Name,Calories_Burned,Description) 
VALUES
(1,1,'2018-02-15 08:49:09','Walk',55,'Commute to work')
,(2,2,'2018-02-15 12:55:02','Walk (1 mile)',95,'Walk around the lake after lunch')
,(3,1,'2018-02-15 16:55:34','Walk',55,'Commute from work')
,(4,1,'2018-02-16 08:45:06','Walk',55,'Commute to work')
,(5,2,'2018-02-16 12:56:43','Walk (1 mile)',95,'Walk around the lake after lunch')
,(6,1,'2018-02-16 16:54:15','Walk',55,'Commute from work')
,(7,1,'2018-02-16 17:22:24','Jog (2 miles)',170,'Jog on the treadmill')
,(8,2,'2018-02-16 17:34:58','Workout',245,'Workout at the gym');

INSERT INTO dbo.Diet_Log(Diet_Log_Id,Profile_Id,Log_Date,Meal,Food_Name,Calorie_Per_Unit,Quantity) VALUES
 (1,2,'2018-02-15 07:15:45','Breakfast','Bagel with Cream Cheese',436,1)
,(2,2,'2018-02-15 07:15:45','Breakfast','Coffee with Cream (16 oz)',55,1)
,(3,1,'2018-02-15 08:30:18','Breakfast','Glazed Donut',190,2)
,(4,1,'2018-02-15 08:30:18','Breakfast','Coke (12 oz.)',150,1)
,(5,2,'2018-02-15 10:03:14','Snack','Trail Mix (.5 cup)',430,1)
,(6,2,'2018-02-15 12:16:13','Lunch','Hamburger',560,1)
,(7,2,'2018-02-15 12:16:13','Lunch','French Fries (100 oz.)',360,1)
,(8,2,'2018-02-15 12:16:13','Lunch','Coke (12 oz.)',150,1)
,(9,1,'2018-02-15 12:30:35','Lunch','Ham Sandwich',290,1)
,(10,1,'2018-02-15 12:30:35','Lunch','Potato Chips',150,1)
,(11,1,'2018-02-15 12:30:35','Lunch','Coke (12 oz.)',150,1)
,(12,1,'2018-02-15 12:30:35','Lunch','Chocolate Chip Cookie',78,2)
,(13,1,'2018-02-15 15:12:19','Snack','Coke (12 oz.)',150,1)
,(14,1,'2018-02-15 15:12:19','Snack','Chocolate Chip Cookie',78,1)
,(15,2,'2018-02-15 15:22:55','Snack','Candy Bar',130,1)
,(16,2,'2018-02-16 07:04:32','Breakfast','Coffee with Cream (16 oz.)',55,1)
,(17,2,'2018-02-16 07:04:32','Breakfast','Banana',100,1)
,(18,1,'2018-02-16 08:00:45','Breakfast','Apple',95,1)
,(19,1,'2018-02-16 08:00:45','Breakfast','Coffee',38,1)
,(20,2,'2018-02-16 10:15:22','Snack','Almonds (1 oz.)',120,1)
,(21,2,'2018-02-16 12:03:54','Lunch','Grilled Chicken (5 oz.)',450,1)
,(22,2,'2018-02-16 12:03:54','Lunch','Green Beans (1 cup)',30,1)
,(23,1,'2018-02-16 12:14:19','Lunch','Greek Salad',390,1)
,(24,1,'2018-02-16 14:08:34','Snack','Banana',100,1)
,(25,2,'2018-02-16 16:12:45','Snack','Almonds (1 oz.)',120,1)
,(26,2,'2018-02-15  17:43:08','Dinner','General Tso Chicken',650,1)
,(27,2,'2018-02-15  17:43:08','Dinner','Sweet Tea (12 oz.)',50,1)
,(28,1,'2018-02-15  18:30:57','Dinner','Steak (8 oz.)',680,1)
,(29,1,'2018-02-15  18:30:57','Dinner','Mashed Potatoes (1 cup)',215,1)
,(30,1,'2018-02-15  18:30:57','Dinner','Green Beans (1 cup)',30,1)
,(31,1,'2018-02-15  18:30:57','Dinner','Chocolate Chip Cookie',78,2)
,(32,1,'2018-02-15  18:30:57','Dinner','Red Wine (5 oz.)',150,2)
,(33,2,'2018-02-15  21:02:34','Snack','Chocolate Chip Cookie',78,3)
,(34,1,'2018-02-16  18:08:34','Dinner','Grilled Salmon (6 oz.)',340,1)
,(35,1,'2018-02-16  18:08:34','Dinner','Quinoa (.75 cup)',160,1)
,(36,1,'2018-02-16  18:08:34','Dinner','Red Wine (5 oz.)',150,1)
,(37,2,'2018-02-16  18:45:06','Dinner','Caesar Salad',320,1)
,(38,2,'2018-02-16  18:45:06','Dinner','Tomato Soup (1 cup)',280,1)
,(39,1,'2018-02-16  21:03:16','Snack','Granola Bar',132,1)
,(40,2,'2018-02-16  21:09:23','Snack','Grapes (1 cup)',230,1);

If (Select count(*) from sys.views Where name = 'Daily_Goal_Review') = 1
	Drop view dbo.Daily_Goal_Review

EXEC('
Create View dbo.Daily_Goal_Review
As
Select 
u.Profile_Id
,u.First_Name
,u.Last_Name
,de.Snapshot_Date As Activity_Date
,de.Total_Calories_Consumed
,de.Total_Calories_Burned
,de.Net_Calories_Consumed
,u.Daily_Net_Calorie_Goal
,Case When u.Daily_Net_Calorie_Goal >= de.Net_Calories_Consumed
	Then ''Y''
	Else ''N''
	End ''Daily_Calorie_Goal_Met''
,Case When u.Daily_Net_Calorie_Goal >= de.Net_Calories_Consumed
	Then ''Great job '' + u.First_Name + ''! Keep up the hard work.''
	Else ''Good try '' + u.First_Name + ''. Maybe lay off the '' + de.High_Calorie_Food + '' next time.''
	End Motivational_Message
From dbo.User_Profile u 
Join
(
	Select 
	d.Profile_Id
	,d.Snapshot_Date
	,d.Total_Calories_Consumed
	,e.Total_Calories_Burned
	,d.Total_Calories_Consumed - e.Total_Calories_Burned As Net_Calories_Consumed
	,d.High_Calorie_Food
	FROM (
		Select 
		u.Profile_Id
		,Cast(d.Log_Date as Date) As Snapshot_Date
		,SUM(d.Calorie_Per_Unit*d.Quantity) As Total_Calories_Consumed
		,fd.Food_Name as High_Calorie_Food
		,fd.Total_Calorie
		From dbo.User_Profile u Join dbo.Diet_Log d 
			on u.Profile_Id = d.Profile_Id
		Left Outer Join (
			Select 
			Cast(Log_Date as Date) As Snapshot_Date,
			Profile_Id,
			Food_Name,
			ROW_NUMBER() Over (Partition By Profile_ID, Cast(Log_Date as Date) Order by (Calorie_Per_Unit*Quantity) desc) rnk,
			Calorie_Per_Unit*Quantity As Total_Calorie
			From dbo.Diet_Log
			) fd on u.Profile_Id = fd.Profile_Id and Cast(d.Log_Date as Date) = fd.Snapshot_Date and fd.rnk =1
		Group By
		u.Profile_Id
		,Cast(d.Log_Date as Date)
		,fd.Food_Name
		,fd.Total_Calorie
		) d Join (
		Select 
		u.Profile_Id
		,Cast(e.Log_Date as Date) As Snapshot_Date
		,SUM(e.Calories_Burned) As Total_Calories_Burned
		from dbo.User_Profile u Join dbo.Exercise_Log e 
			on u.Profile_Id = e.Profile_Id
		Group By
		u.Profile_Id
		,Cast(e.Log_Date as Date)
		) e on d.Profile_Id = e.Profile_Id and d.Snapshot_Date = e.Snapshot_Date
) de on u.Profile_Id = de.Profile_Id
')

--Select * from dbo.Daily_Goal_Review

--Create view for testing "Assert Datasets Equal" command
CREATE VIEW dbo.Diet_Log_Profile_Test AS
SELECT 
	dl.[Log_Date]
	,dl.[Meal]
	,dl.[Food_Name]
	,dl.[Calorie_Per_Unit]
	,dl.[Quantity]
	,up.First_Name
	,up.Last_Name
FROM [MyFitBot].[dbo].[Diet_Log] dl
INNER JOIN MyFitBot.dbo.User_Profile up
	ON up.Profile_Id = dl.Profile_Id
--WHERE up.First_Name = 'Christel' AND up.Last_Name = 'Russen'
;
