### Question 1:
- (a) When dividing the total sum of the `order_amount` by the number of orders we do indeed get an AOV of $3145.13. However, this value is misleading as it is the average value per _order_ and not per item sold. Customers regularly buy up to 8 sneakers per order, but the user with the `user_id` 607, frequently orders 2000 sneakers at a time.
- (b) I would report the Average Value per Ordered Item rather than Average Order Value. This will give a better sense for how much the customers are paying for each sneaker, rather than the average value per checkout. If we wanted, we could still report the AOV but I would segregate the data by filtering out people who order an amount of items over a certain threshold. We could then get a separate AOV for the _small quantity buyers_, and for the _bulk buyers_.
- (c) If we calculate the Average Value per Ordered Item we would get a value of $357.92.
  - (extra. If we take the Average Order Value of orders under 10 items we a get a value of $754.09)

### Question 2:

(a) The following query gets `54` orders shipped by _Speedy Express_.
```sql
SELECT Count(*)
FROM Orders
WHERE ShipperID = (
    SELECT ShipperID
    FROM Shippers
    WHERE ShipperName = "Speedy Express");
```

(b) We get the the last name of the employee with the most orders as `Peacock`.
```sql
Select LastName
From Employees
WHERE EmployeeID = (
    Select EmployeeID
    From Orders
    GROUP BY EmployeeID
    ORDER BY COUNT(EmployeeID) DESC
    LIMIT 1);
```

(c) We get the most common product ordered from customers in Germany as `Gorgonzola Telino`.
```sql
SELECT ProductName
FROM Products
WHERE ProductID = (
    SELECT OrderDetails.ProductID
    FROM Customers
    INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID
    INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
    WHERE Customers.Country = "Germany"
    GROUP BY OrderDetails.ProductID
    ORDER BY COUNT(OrderDetails.ProductID) DESC
    LIMIT 1);
```