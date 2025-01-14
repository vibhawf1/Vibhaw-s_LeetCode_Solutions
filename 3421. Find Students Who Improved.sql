# Write your MySQL query statement below
WITH t1 AS
(
    SELECT student_id,subject,MIN(exam_date) AS m1,MAX(exam_date) AS m2
    FROM Scores
    GROUP BY student_id,subject
),
t2 AS
(
    SELECT a.student_id,a.subject,b.score AS first_score,c.score AS latest_score
    FROM t1 a
    JOIN Scores b
    ON a.student_id=b.student_id AND a.subject=b.subject AND a.m1=b.exam_date
    JOIN Scores c
    ON a.student_id=c.student_id AND a.subject=c.subject AND a.m2=c.exam_date AND b.exam_date!=c.exam_date
)
SELECT student_id,subject,first_score,latest_score FROM t2
WHERE latest_score>first_score
ORDER BY student_id,subject;
