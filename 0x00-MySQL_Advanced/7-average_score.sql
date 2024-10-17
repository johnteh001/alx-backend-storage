-- script creates a stored procedure for computing avarage score
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE average FLOAT;
	SET average = (SELECT AVG(score) FROM corrections AS cor WHERE cor.user_id=user_id);
	UPDATE users SET average_score = average WHERE id=user_id;
END$$
DELIMITER ;
