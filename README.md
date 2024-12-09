```sudo apt update```
```sudo apt install mysql-server```

```sudo systemctl start mysql```

```mysql -u root -p```

```CREATE DATABASE your_database;```

    
    CREATE TABLE customers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE orders (
        id INT AUTO_INCREMENT PRIMARY KEY,
        customer_id INT NOT NULL,
        amount DECIMAL(10, 2) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (customer_id) REFERENCES customers(id)
    );
    

    INSERT INTO customers (name, email) VALUES
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com');
    
    INSERT INTO orders (customer_id, amount) VALUES
    (1, 99.99),
    (2, 149.49);
    FOREIGN KEY (customer_id) REFERENCES customers(id)
      );

---
    3 rows from orders table:
    id	customer_id	amount	created_at
    1	1	99.99	2024-12-09 09:31:07
    2	2	149.49	2024-12-09 09:31:07
    */
    INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
    INFO:__main__:Generated SQL Query: SELECT `email` FROM `customers` WHERE `name` = 'Alice' LIMIT 1;
    INFO:__main__:Query Result:
    INFO:__main__:('alice@example.com',)
