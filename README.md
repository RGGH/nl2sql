```sudo apt update```
```sudo apt install mysql-server```

```sudo systemctl start mysql```

```mysql -u root -p```

```CREATE DATABASE your_database;```

    
    ```CREATE TABLE customers (
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
    ```

    ```INSERT INTO customers (name, email) VALUES
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com');
    
    INSERT INTO orders (customer_id, amount) VALUES
    (1, 99.99),
    (2, 149.49);
    ```
    
          FOREIGN KEY (customer_id) REFERENCES customers(id)
      );```

