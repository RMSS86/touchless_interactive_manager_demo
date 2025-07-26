
declare @fullName_ varchar(50) = '125487'
SELECT 
	Employee_ID
	, ISNULL(First_Name,'')+ ' ' +ISNULL(Last_Name,'') as NAME_
	from 
	iCAT_TIM_Employee where  Employee_ID = @fullName_



select * from iCAT_TIM_Employee order by Employee_ID

select Employee_ID from iCAT_TIM_Employee order by Employee_ID
select ISNULL(First_Name,'')+ ' ' +ISNULL(Last_Name,'') as NAME_ from iCAT_TIM_Employee order by Employee_ID
select Face_Encoding from iCAT_TIM_Employee order by Employee_ID

select * from iCAT_Item
INSERT INTO iCAT_TIM_Employee(Employee_ID,First_Name,Last_Name,Account_ID,Position_Account_ID,Face_Encoding )values()

	/*select * from iCAT_TIM_Employee


declare @fullName varchar(50)
declare @First_Name varchar(50)
declare @Last_Name varchar(50)

select @First_Name = ( select First_Name from iCAT_TIM_Employee where Employee_ID = '125487')
select @Last_Name = ( select Last_Name from iCAT_TIM_Employee where Employee_ID = '125487')

select @fullName = (@First_Name + ' ' + @Last_Name)  
*/

CREATE PROCEDURE [dbo].[ixSP_Existing_TIM_Agent_checker] (@Agent_ nvarchar(100))

AS
begin 

IF EXISTS(SELECT 1 FROM iCAT_TIM_Employee WITH(NOLOCK)
          WHERE Employee_ID = @Agent_)
    BEGIN
        select 'RE' as Record, Employee_ID  from iCAT_TIM_Employee where Employee_ID= @Agent_

    END
ELSE
    BEGIN
        select 'RDNE' as Record

    END
end


exec ixSP_Existing_TIM_Agent_checker '129999'