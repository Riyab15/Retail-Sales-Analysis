

CREATE DATABASE RetailSalesDB;

USE RetailSalesDB;



CREATE TABLE retail_sales (
    InvoiceNo VARCHAR(20),
    StockCode VARCHAR(20),
    Description TEXT,
    Quantity INT,
    InvoiceDate DATETIME,
    UnitPrice FLOAT,
    CustomerID INT,
    Country VARCHAR(100)
);


-- Check Missing Customer IDs

SELECT *
FROM retail_sales
WHERE CustomerID IS NULL;

-- Remove Missing Values

DELETE FROM retail_sales
WHERE CustomerID IS NULL;

-- Check Duplicate Records

SELECT InvoiceNo,
       StockCode,
       COUNT(*) AS DuplicateCount
FROM retail_sales
GROUP BY InvoiceNo, StockCode
HAVING COUNT(*) > 1;

-- Remove Negative Quantities

DELETE FROM retail_sales
WHERE Quantity <= 0;

-- Remove Negative Prices

DELETE FROM retail_sales
WHERE UnitPrice <= 0;



ALTER TABLE retail_sales
ADD COLUMN TotalSales FLOAT;

UPDATE retail_sales
SET TotalSales = Quantity * UnitPrice;

-- Total Records

SELECT COUNT(*) AS TotalRecords
FROM retail_sales;

-- Total Revenue

SELECT SUM(TotalSales) AS TotalRevenue
FROM retail_sales;

-- Average Order Value

SELECT AVG(TotalSales) AS AvgOrderValue
FROM retail_sales;



SELECT Description,
       SUM(Quantity) AS QuantitySold
FROM retail_sales
GROUP BY Description
ORDER BY QuantitySold DESC
LIMIT 10;


SELECT Country,
       SUM(TotalSales) AS Sales
FROM retail_sales
GROUP BY Country
ORDER BY Sales DESC
LIMIT 10;



SELECT CustomerID,
       SUM(TotalSales) AS Spending
FROM retail_sales
GROUP BY CustomerID
ORDER BY Spending DESC
LIMIT 10;



SELECT MONTH(InvoiceDate) AS Month,
       SUM(TotalSales) AS Sales
FROM retail_sales
GROUP BY Month
ORDER BY Month;

-

SELECT YEAR(InvoiceDate) AS Year,
       SUM(TotalSales) AS Sales
FROM retail_sales
GROUP BY Year
ORDER BY Year;


-- Country Wise Customers

SELECT Country,
       COUNT(DISTINCT CustomerID) AS Customers
FROM retail_sales
GROUP BY Country
ORDER BY Customers DESC;

-- Product Revenue

SELECT Description,
       SUM(TotalSales) AS Revenue
FROM retail_sales
GROUP BY Description
ORDER BY Revenue DESC
LIMIT 10;

-- Customer Frequency

SELECT CustomerID,
       COUNT(DISTINCT InvoiceNo) AS TotalOrders
FROM retail_sales
GROUP BY CustomerID
ORDER BY TotalOrders DESC;




-- Best Selling Product

SELECT Description,
       SUM(Quantity) AS TotalSold
FROM retail_sales
GROUP BY Description
ORDER BY TotalSold DESC
LIMIT 1;

-- Highest Revenue Country

SELECT Country,
       SUM(TotalSales) AS Revenue
FROM retail_sales
GROUP BY Country
ORDER BY Revenue DESC
LIMIT 1;

-- Most Valuable Customer

SELECT CustomerID,
       SUM(TotalSales) AS Revenue
FROM retail_sales
GROUP BY CustomerID
ORDER BY Revenue DESC
LIMIT 1;

