-- Creating trigger that decreases the quantity of an item after an order
DELIMITER $$
CREATE TRIGGER decrease_quantity
BEFORE INSERT
ON orders FOR EACH ROW
BEGIN
	UPDATE `items` SET `quantity` = quantity - NEW.number
	WHERE `name` = NEW.item_name;
END$$
DELIMITER ;

