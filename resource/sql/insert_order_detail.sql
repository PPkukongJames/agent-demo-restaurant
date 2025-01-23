-- เพิ่มข้อมูลรายละเอียดของออเดอร์ลงในตาราง OrderDetails
INSERT INTO OrderDetails (OrderID, MenuID, Quantity)
VALUES
-- Order 1-5
(1, 1, 2), -- Pizza x2
(1, 2, 1), -- Spaghetti Carbonara x1
(2, 3, 2), -- Grilled Chicken x2
(2, 4, 1), -- Beef Steak x1
(3, 5, 3), -- Salmon Teriyaki x3
(3, 6, 2), -- Caesar Salad x2
(4, 7, 2), -- Garlic Bread x2
(4, 8, 1), -- Spring Rolls x1
(5, 9, 1), -- Tomato Soup x1
(5, 10, 2), -- Stuffed Mushrooms x2

-- Order 6-10
(6, 11, 1), -- Ice Cream x1
(6, 12, 1), -- Cheesecake x1
(7, 13, 2), -- Brownies x2
(7, 14, 1), -- Tiramisu x1
(8, 15, 1), -- Fruit Salad x1
(8, 16, 2), -- Espresso x2
(9, 17, 2), -- Cappuccino x2
(9, 18, 1), -- Iced Lemon Tea x1
(10, 19, 1), -- Smoothie x1
(10, 20, 2), -- Orange Juice x2

-- Order 11-15
(11, 1, 1), -- Pizza x1
(11, 2, 1), -- Spaghetti Carbonara x1
(12, 3, 1), -- Grilled Chicken x1
(12, 4, 2), -- Beef Steak x2
(13, 5, 1), -- Salmon Teriyaki x1
(13, 6, 1), -- Caesar Salad x1
(14, 7, 2), -- Garlic Bread x2
(14, 8, 1), -- Spring Rolls x1
(15, 9, 1), -- Tomato Soup x1
(15, 10, 1), -- Stuffed Mushrooms x1

-- Order 16-20
(16, 11, 2), -- Ice Cream x2
(16, 12, 1), -- Cheesecake x1
(17, 13, 1), -- Brownies x1
(17, 14, 1), -- Tiramisu x1
(18, 15, 2), -- Fruit Salad x2
(18, 16, 1), -- Espresso x1
(19, 17, 1), -- Cappuccino x1
(19, 18, 2), -- Iced Lemon Tea x2
(20, 19, 2), -- Smoothie x2
(20, 20, 1), -- Orange Juice x1

-- Order 21-25
(21, 1, 1), -- Pizza x1
(21, 2, 2), -- Spaghetti Carbonara x2
(22, 3, 1), -- Grilled Chicken x1
(22, 4, 2), -- Beef Steak x2
(23, 5, 1), -- Salmon Teriyaki x1
(23, 6, 2), -- Caesar Salad x2
(24, 7, 1), -- Garlic Bread x1
(24, 8, 2), -- Spring Rolls x2
(25, 9, 1), -- Tomato Soup x1
(25, 10, 2), -- Stuffed Mushrooms x2

-- Order 26-30
(26, 11, 1), -- Ice Cream x1
(26, 12, 2), -- Cheesecake x2
(27, 13, 2), -- Brownies x2
(27, 14, 1), -- Tiramisu x1
(28, 15, 1), -- Fruit Salad x1
(28, 16, 2), -- Espresso x2
(29, 17, 1), -- Cappuccino x1
(29, 18, 1), -- Iced Lemon Tea x1
(30, 19, 2), -- Smoothie x2
(30, 20, 1); -- Orange Juice x1
