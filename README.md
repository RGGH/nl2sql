```sudo apt update```
```sudo apt install mysql-server```

```sudo systemctl start mysql```

```mysql -u root -p```

```CREATE DATABASE employees;```

```https://dev.mysql.com/doc/employee/en/employees-installation.html```


  ❯ uv run main2.py 
  INFO:__main__:Usable Tables: ['departments', 'dept_emp', 'dept_manager', 'employees', 'salaries', 'titles']
  INFO:__main__:Table: departments
  INFO:__main__:  Column: dept_no | Type: CHAR(4)
  INFO:__main__:  Column: dept_name | Type: VARCHAR(40)
  INFO:__main__:Table: dept_emp
  INFO:__main__:  Column: emp_no | Type: INTEGER
  INFO:__main__:  Column: dept_no | Type: CHAR(4)
  INFO:__main__:  Column: from_date | Type: DATE
  INFO:__main__:  Column: to_date | Type: DATE
  INFO:__main__:Table: dept_manager
  INFO:__main__:  Column: emp_no | Type: INTEGER
  INFO:__main__:  Column: dept_no | Type: CHAR(4)
  INFO:__main__:  Column: from_date | Type: DATE
  INFO:__main__:  Column: to_date | Type: DATE
  INFO:__main__:Table: employees
  INFO:__main__:  Column: emp_no | Type: INTEGER
  INFO:__main__:  Column: birth_date | Type: DATE
  INFO:__main__:  Column: first_name | Type: VARCHAR(14)
  INFO:__main__:  Column: last_name | Type: VARCHAR(16)
  INFO:__main__:  Column: gender | Type: ENUM
  INFO:__main__:  Column: hire_date | Type: DATE
  INFO:__main__:Table: salaries
  INFO:__main__:  Column: emp_no | Type: INTEGER
  INFO:__main__:  Column: salary | Type: INTEGER
  INFO:__main__:  Column: from_date | Type: DATE
  INFO:__main__:  Column: to_date | Type: DATE
  INFO:__main__:Table: titles
  INFO:__main__:  Column: emp_no | Type: INTEGER
  INFO:__main__:  Column: title | Type: VARCHAR(50)
  INFO:__main__:  Column: from_date | Type: DATE
  INFO:__main__:  Column: to_date | Type: DATE
  INFO:__main__:Dialect: mysql
  INFO:__main__:Usable Tables: ['departments', 'dept_emp', 'dept_manager', 'employees', 'salaries', 'titles']
  INFO:__main__:Table Info: 
  CREATE TABLE departments (
  	dept_no CHAR(4) NOT NULL, 
  	dept_name VARCHAR(40) NOT NULL, 
  	PRIMARY KEY (dept_no)
  )DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_0900_ai_ci
  
  /*
  3 rows from departments table:
  dept_no	dept_name
  d009	Customer Service
  d005	Development
  d002	Finance
  */
  
  
  CREATE TABLE dept_emp (
  	emp_no INTEGER NOT NULL, 
  	dept_no CHAR(4) NOT NULL, 
  	from_date DATE NOT NULL, 
  	to_date DATE NOT NULL, 
  	PRIMARY KEY (emp_no, dept_no), 
  	CONSTRAINT dept_emp_ibfk_1 FOREIGN KEY(emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE, 
  	CONSTRAINT dept_emp_ibfk_2 FOREIGN KEY(dept_no) REFERENCES departments (dept_no) ON DELETE CASCADE
  )DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_0900_ai_ci
  
  /*
  3 rows from dept_emp table:
  emp_no	dept_no	from_date	to_date
  10001	d005	1986-06-26	9999-01-01
  10002	d007	1996-08-03	9999-01-01
  10003	d004	1995-12-03	9999-01-01
  */
  
  
  CREATE TABLE dept_manager (
  	emp_no INTEGER NOT NULL, 
  	dept_no CHAR(4) NOT NULL, 
  	from_date DATE NOT NULL, 
  	to_date DATE NOT NULL, 
  	PRIMARY KEY (emp_no, dept_no), 
  	CONSTRAINT dept_manager_ibfk_1 FOREIGN KEY(emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE, 
  	CONSTRAINT dept_manager_ibfk_2 FOREIGN KEY(dept_no) REFERENCES departments (dept_no) ON DELETE CASCADE
  )DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_0900_ai_ci
  
  /*
  3 rows from dept_manager table:
  emp_no	dept_no	from_date	to_date
  110022	d001	1985-01-01	1991-10-01
  110039	d001	1991-10-01	9999-01-01
  110085	d002	1985-01-01	1989-12-17
  */
  
  
  CREATE TABLE employees (
  	emp_no INTEGER NOT NULL, 
  	birth_date DATE NOT NULL, 
  	first_name VARCHAR(14) NOT NULL, 
  	last_name VARCHAR(16) NOT NULL, 
  	gender ENUM('M','F') NOT NULL, 
  	hire_date DATE NOT NULL, 
  	PRIMARY KEY (emp_no)
  )DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_0900_ai_ci
  
  /*
  3 rows from employees table:
  emp_no	birth_date	first_name	last_name	gender	hire_date
  10001	1953-09-02	Georgi	Facello	M	1986-06-26❯ uv run main2.py 
INFO:__main__:Usable Tables: ['departments', 'dept_emp', 'dept_manager', 'employees', 'salaries', 'titles']
INFO:__main__:Table: departments
INFO:__main__:  Column: dept_no | Type: CHAR(4)
INFO:__main__:  Column: dept_name | Type: VARCHAR(40)
INFO:__main__:Table: dept_emp
INFO:__main__:  Column: emp_no | Type: INTEGER
INFO:__main__:  Column: dept_no | Type: CHAR(4)
INFO:__main__:  Column: from_date | Type: DATE
INFO:__main__:  Column: to_date | Type: DATE
INFO:__main__:Table: dept_manager
INFO:__main__:  Column: emp_no | Type: INTEGER
INFO:__main__:  Column: dept_no | Type: CHAR(4)
INFO:__main__:  Column: from_date | Type: DATE
INFO:__main__:  Column: to_date | Type: DATE
INFO:__main__:Table: employees
INFO:__main__:  Column: emp_no | Type: INTEGER
INFO:__main__:  Column: birth_date | Type: DATE
INFO:__main__:  Column: first_name | Type: VARCHAR(14)
INFO:__main__:  Column: last_name | Type: VARCHAR(16)
INFO:__main__:  Column: gender | Type: ENUM
INFO:__main__:  Column: hire_date | Type: DATE
INFO:__main__:Table: salaries
INFO:__main__:  Column: emp_no | Type: INTEGER
INFO:__main__:  Column: salary | Type: INTEGER
INFO:__main__:  Column: from_date | Type: DATE
INFO:__main__:  Column: to_date | Type: DATE
INFO:__main__:Table: titles
INFO:__main__:  Column: emp_no | Type: INTEGER
INFO:__main__:  Column: title | Type: VARCHAR(50)
INFO:__main__:  Column: from_date | Type: DATE
INFO:__main__:  Column: to_date | Type: DATE
INFO:__main__:Dialect: mysql
INFO:__main__:Usable Tables: ['departments', 'dept_emp', 'dept_manager', 'employees', 'salaries', 'titles']
INFO:__main__:Table Info: 
CREATE TABLE departments (
	dept_no CHAR(4) NOT NULL, 
	dept_name VARCHAR(40) NOT NULL, 
	PRIMARY KEY (dept_no)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_0900_ai_ci

/*
3 rows from departments table:
dept_no	dept_name
d009	Customer Service
d005	Development
d002	Finance
*/


CREATE TABLE dept_emp (
	emp_no INTEGER NOT NULL, 
	dept_no CHAR(4) NOT NULL, 
	from_date DATE NOT NULL, 
	to_date DATE NOT NULL, 
	PRIMARY KEY (emp_no, dept_no), 
	CONSTRAINT dept_emp_ibfk_1 FOREIGN KEY(emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE, 
	CONSTRAINT dept_emp_ibfk_2 FOREIGN KEY(dept_no) REFERENCES departments (dept_no) ON DELETE CASCADE
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_0900_ai_ci

/*
3 rows from dept_emp table:
emp_no	dept_no	from_date	to_date
10001	d005	1986-06-26	9999-01-01
10002	d007	1996-08-03	9999-01-01
10003	d004	1995-12-03	9999-01-01
*/


CREATE TABLE dept_manager (
	emp_no INTEGER NOT NULL, 
	dept_no CHAR(4) NOT NULL, 
	from_date DATE NOT NULL, 
	to_date DATE NOT NULL, 
	PRIMARY KEY (emp_no, dept_no), 
	CONSTRAINT dept_manager_ibfk_1 FOREIGN KEY(emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE, 
	CONSTRAINT dept_manager_ibfk_2 FOREIGN KEY(dept_no) REFERENCES departments (dept_no) ON DELETE CASCADE
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_0900_ai_ci

/*
3 rows from dept_manager table:
emp_no	dept_no	from_date	to_date
110022	d001	1985-01-01	1991-10-01
110039	d001	1991-10-01	9999-01-01
110085	d002	1985-01-01	1989-12-17
*/


CREATE TABLE employees (
	emp_no INTEGER NOT NULL, 
	birth_date DATE NOT NULL, 
	first_name VARCHAR(14) NOT NULL, 
	last_name VARCHAR(16) NOT NULL, 
	gender ENUM('M','F') NOT NULL, 
	hire_date DATE NOT NULL, 
	PRIMARY KEY (emp_no)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_0900_ai_ci

/*
3 rows from employees table:
emp_no	birth_date	first_name	last_name	gender	hire_date
10001	1953-09-02	Georgi	Facello	M	1986-06-26
10002	1964-06-02	Bezalel	Simmel	F	1985-11-21
10003	1959-12-03	Parto	Bamford	M	1986-08-28
*/


CREATE TABLE salaries (
	emp_no INTEGER NOT NULL, 
	salary INTEGER NOT NULL, 
	from_date DATE NOT NULL, 
	to_date DATE NOT NULL, 
	PRIMARY KEY (emp_no, from_date), 
	CONSTRAINT salaries_ibfk_1 FOREIGN KEY(emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_0900_ai_ci

/*
3 rows from salaries table:
emp_no	salary	from_date	to_date
10001	60117	1986-06-26	1987-06-26
10001	62102	1987-06-26	1988-06-25
10001	66074	1988-06-25	1989-06-25
*/


CREATE TABLE titles (
	emp_no INTEGER NOT NULL, 
	title VARCHAR(50) NOT NULL, 
	from_date DATE NOT NULL, 
	to_date DATE, 
	PRIMARY KEY (emp_no, title, from_date), 
	CONSTRAINT titles_ibfk_1 FOREIGN KEY(emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_0900_ai_ci

/*
3 rows from titles table:
emp_no	title	from_date	to_date
10001	Senior Engineer	1986-06-26	9999-01-01
10002	Staff	1996-08-03	9999-01-01
10003	Senior Engineer	1995-12-03	9999-01-01
*/
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
INFO:__main__:Generated SQL Query: SELECT e.first_name, e.last_name
FROM employees e
ORDER BY e.hire_date
LIMIT 1;
INFO:__main__:Query Result:
INFO:__main__:('Margareta', 'Markovitch')
~/python/nl2sql/src/nl2sql employees

  10002	1964-06-02	Bezalel	Simmel	F	1985-11-21
  10003	1959-12-03	Parto	Bamford	M	1986-08-28
  */
  
  
  CREATE TABLE salaries (
  	emp_no INTEGER NOT NULL, 
  	salary INTEGER NOT NULL, 
  	from_date DATE NOT NULL, 
  	to_date DATE NOT NULL, 
  	PRIMARY KEY (emp_no, from_date), 
  	CONSTRAINT salaries_ibfk_1 FOREIGN KEY(emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE
  )DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_0900_ai_ci
  
  /*
  3 rows from salaries table:
  emp_no	salary	from_date	to_date
  10001	60117	1986-06-26	1987-06-26
  10001	62102	1987-06-26	1988-06-25
  10001	66074	1988-06-25	1989-06-25
  */
  
  
  CREATE TABLE titles (
  	emp_no INTEGER NOT NULL, 
  	title VARCHAR(50) NOT NULL, 
  	from_date DATE NOT NULL, 
  	to_date DATE, 
  	PRIMARY KEY (emp_no, title, from_date), 
  	CONSTRAINT titles_ibfk_1 FOREIGN KEY(emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE
  )DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_0900_ai_ci
  
  /*
  3 rows from titles table:
  emp_no	title	from_date	to_date
  10001	Senior Engineer	1986-06-26	9999-01-01
  10002	Staff	1996-08-03	9999-01-01
  10003	Senior Engineer	1995-12-03	9999-01-01
  */
  INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
  INFO:__main__:Generated SQL Query: SELECT e.first_name, e.last_name
  FROM employees e
  ORDER BY e.hire_date
  LIMIT 1;
  INFO:__main__:Query Result:
  INFO:__main__:('Margareta', 'Markovitch')
  ~/python/nl2sql/src/nl2sql employees

# Margareta', 'Markovitch
![image](https://github.com/user-attachments/assets/df4ed021-4c6c-4e17-9e66-210af841d64a)
