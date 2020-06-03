
--Once you have a complete database, do the following:

--1. List the following details of each employee: employee number, last name, first name, sex, and salary.
select e.emp_no as "Employee number"
	,e.last_name as "last name"
	,e.first_name as "first name"
	,e.sex as "Gender"
	, cast(s.salaries as money) as Salary
from employees e
	inner join salaries s on
		s.emp_no = e.emp_no;

--2. List first name, last name, and hire date for employees who were hired in 1986.
select e.first_name as "first name"
	,e.last_name as "last name"
	,e.hire_date as "hire date"
from employees e
where
	EXTRACT(YEAR FROM hire_date) = '1986';
	
--3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.
select dm.dept_no as "Department Number"
	,d.dept_name as "Department Name"
	,e.emp_no as "Manager employee number"
	,e.first_name as "Manager first name"
	,e.last_name as "Manager last name"
from dept_manager dm
	inner join departments d on 
		d.dept_no = dm.dept_no
	inner join employees e on
		e.emp_no = dm.emp_no;
		
--4. List the department of each employee with the following information: employee number, last name, first name, and department name.
select e.emp_no as "Employee number"
	,e.last_name as "Employee last name"
	,e.first_name as "Employee first name"
	,d.dept_name as "Department name"
from employees e
	inner join dept_emp de on
		de.emp_no = e.emp_no
	inner join departments d on
		d.dept_no = de.dept_no;

--5. List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."
select first_name as "Employee first name"
	,last_name as "Employee last name"
	,sex as "Gender"
from employees
where first_name = 'Hercules'
	and upper(last_name) like 'B%';
	
--6. List all employees in the Sales department, including their employee number, last name, first name, and department name.
select e.emp_no as "Employee number"
	,last_name as "Employee last name"
	,first_name as "Employee first name"
	,d.dept_name as "Department name"
from employees e
	inner join dept_emp de on
		de.emp_no = e.emp_no
	inner join departments d on
		d.dept_no = de.dept_no;
		
--7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
select e.emp_no as "Employee number"
	,last_name as "Employee last name"
	,first_name as "Employee first name"
	,d.dept_name as "Department name"
from employees e
	inner join dept_emp de on
		de.emp_no = e.emp_no
	inner join departments d on
		d.dept_no = de.dept_no
		and d.dept_name in ('Sales','Development');
		
--8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
select last_name as "Last name"
	,count(last_name) as "Frequency count"
from employees
group by last_name
order by count(last_name) desc;