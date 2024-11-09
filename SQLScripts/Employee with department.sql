select xmlelement(
   "Employee",
   xmlforest(e.first_name as "FirstName",
   e.last_name as "LastName",
   d.department_name as "DepartmentName")
)
  from employees e
  join departments d
on e.department_id = d.department_id;