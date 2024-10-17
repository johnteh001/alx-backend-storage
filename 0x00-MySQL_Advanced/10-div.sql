-- script creates function safeDiv 
-- function deives the first by second number and returns else returns 0
-- if second numbr is equal to 0
DELIMITER $$
CREATE FUNCTION SafeDiv (num1 INT, num2 INT) RETURNS FLOAT
DETERMINISTIC NO SQL
BEGIN
	DECLARE res FLOAT;
	IF num2 = 0 THEN SET res = 0;
	ELSE SET res = num1 / num2;
	END IF;
	RETURN res;
END$$
DELIMITER ;
