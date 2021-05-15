2.2
CREATE TABLE CUSTOMERS(ID INT PRIMARY KEY,
                        FIRSTNAME VARCHAR(30),
                        LASTNAME VARCHAR(30));

2.4
CREATE TABLE ORDERS (ID INT PRIMARY KEY,
		PRODUCT_NAME VARCHAR(30),
		PRODUCT_PRICE FLOAT,
		DATE_ORDER DATE,
		ID_CUSTOMER INT);

2.5
CREATE TABLE ORDERS (ID INT PRIMARY KEY,
		PRODUCT_NAME VARCHAR(30),
		PRODUCT_PRICE FLOAT,
		DATE_ORDER DATE,
		ID_CUSTOMER INT);

3.1
SELECT * FROM CUSTOMERS
ORDER BY ID;

3.2
SELECT PRODUCT_NAME FROM ORDERS
ORDER BY PRODUCT_NAME ASC;

4.1
CREATE TABLE CUSTOMERS (id int primary key,
    firstname varchar(30),
    lastname varchar(30),
    ADDRESS VARCHAR(100));

CREATE TABLE ORDERS (ID INT primary key,
   PRODUCT_NAME VARCHAR(30),
   PRODUCT_PRICE FLOAT,
   DATE_ORDER DATE,
   ID_CUSTOMER INT,
   AMOUNT INT,
   FOREIGN KEY(ID_CUSTOMER) REFERENCES CUSTOMERS(id)
   ON DELETE CASCADE);

4.4
SELECT Orders.product_name, Customers.firstname, Customers.lastname
FROM Orders INNER JOIN Customers ON Orders.id_customer = Customers.id
WHERE address IS NULL OR address = ''
ORDER BY Orders.id;
