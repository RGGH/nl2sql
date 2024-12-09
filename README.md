```sudo apt update```
```sudo apt install mysql-server```

```sudo systemctl start mysql```

```mysql -u root -p```

```CREATE DATABASE employees;```

```https://dev.mysql.com/doc/employee/en/employees-installation.html```


  ❯ uv run main.py 
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
 

  INFO:__main__:Query Result:
  INFO:__main__:('Margareta', 'Markovitch')
  ~/python/nl2sql/src/nl2sql employees

# 'Margareta', 'Markovitch'
![image](https://github.com/user-attachments/assets/df4ed021-4c6c-4e17-9e66-210af841d64a)
