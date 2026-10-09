Select employee_id from Employees where (salary<30000) and manager_id NOT IN (
Select employee_id from Employees) order by employee_id