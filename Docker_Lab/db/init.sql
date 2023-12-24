CREATE DATABASE customers;
USE customers;


CREATE TABLE customers_data (
  customers_name VARCHAR(50),
  total_purchases INT
);


INSERT INTO customers_data
  (customers_name, total_purchases)
VALUES
  ('Amit Khanna', 2500),
  ('Anjali Gupta', 3000);