INSERT INTO IngredientPrice (IngredientName, PricePerUnit, Unit)
VALUES
-- วัตถุดิบที่เป็นผง/ของแข็ง (กรัม -> กิโลกรัม)
('Flour', 75.00, 'kilograms'),          -- แป้งสาลี
('Tomato Sauce', 120.00, 'kilograms'),  -- ซอสมะเขือเทศ
('Cheese', 350.00, 'kilograms'),        -- ชีส
('Cocoa Powder', 350.00, 'kilograms'),  -- ผงโกโก้

-- วัตถุดิบที่เป็นเนื้อสัตว์/อาหารทะเล (กรัม -> กิโลกรัม)
('Chicken Breast', 120.00, 'kilograms'),-- อกไก่
('Beef', 250.00, 'kilograms'),          -- เนื้อวัว
('Salmon', 700.00, 'kilograms'),        -- ปลาแซลมอน

-- ซอสและน้ำสลัด (มิลลิลิตร -> ลิตร)
('Teriyaki Sauce', 95.00, 'liters'),    -- ซอสเทอริยากิ
('Caesar Dressing', 150.00, 'liters'),  -- น้ำสลัดซีซาร์
('Chocolate Sauce', 120.00, 'liters'),  -- ซอสช็อกโกแลต
('Yogurt', 110.00, 'liters'),           -- โยเกิร์ต

-- วัตถุดิบที่เป็นผักและผลไม้ (กรัม -> กิโลกรัม)
('Lettuce', 50.00, 'kilograms'),        -- ผักกาดหอม
('Tomatoes', 35.00, 'kilograms'),       -- มะเขือเทศ
('Mushrooms', 120.00, 'kilograms'),     -- เห็ด
('Fruits', 70.00, 'kilograms'),         -- ผลไม้รวม

-- วัตถุดิบที่เป็นผลไม้แบบชิ้น
('Lemon', 8.00, 'pieces'),              -- มะนาว (บาทต่อชิ้น)
('Orange', 9.00, 'pieces'),             -- ส้ม (บาทต่อชิ้น)

-- วัตถุดิบสำหรับเครื่องดื่ม (มิลลิลิตร -> ลิตร)
('Espresso', 350.00, 'liters'),         -- เอสเปรสโซ
('Milk Foam', 200.00, 'liters'),
('Mushroom Sauce', 250.00, 'liters'),      -- ซอสมะเขือเทศเห็ด
('Garlic Butter', 120.00, 'kilograms'),   -- เนยกระเทียม
('Vegetable', 50.00, 'kilograms'),        -- ผักรวม
('Breadsticks', 100.00, 'kilograms'),     -- ขนมปังกรอบ
('Herbs', 300.00, 'kilograms'),           -- สมุนไพร
('Vanilla', 400.00, 'kilograms'),         -- วานิลลา
('Graham Crust', 150.00, 'kilograms'),    -- แป้งเกรแฮมสำหรับฐาน
('Nuts', 500.00, 'kilograms'),            -- ถั่วรวม
('Honey Drizzle', 800.00, 'liters'),      -- น้ำผึ้งสำหรับราดหน้า
('Tea', 100.00, 'kilograms'),
('Spaghetti', 100.00, 'kilograms');   