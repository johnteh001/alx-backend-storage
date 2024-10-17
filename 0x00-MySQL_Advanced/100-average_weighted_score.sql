DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weight INT DEFAULT 0;
    DECLARE weighted_score_sum FLOAT DEFAULT 0;
    DECLARE avg_weighted_score FLOAT DEFAULT 0;

    SELECT SUM(p.weight), SUM(c.score * p.weight)
    INTO total_weight, weighted_score_sum
    FROM corrections AS c
    JOIN projects AS p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    IF total_weight > 0 THEN
        SET avg_weighted_score = weighted_score_sum / total_weight;
    ELSE
        SET avg_weighted_score = 0;
    END IF;

    UPDATE users
    SET average_score = avg_weighted_score
    WHERE id = user_id;
END //

DELIMITER ;
