Week5

Task 3 SQL CRUD
Action 1
INSERT INTO member(name, username, password, follower_count) VALUES('Allen', 'test', 'test', 1);
INSERT INTO member(name, username, password, follower_count) VALUES('Bob', 'little', 'big', 2);
INSERT INTO member(name, username, password, follower_count) VALUES('Cindy', 'high', 'low', 3);
INSERT INTO member(name, username, password, follower_count) VALUES('David', 'tall', 'short', 10);

Action 2
SELECT * FROM member;

Action 3
SELECT * FROM member ORDER BY time DESC;

Action 4
SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;

Action 5
SELECT * FROM member WHERE username = 'test';

Action 6
SELECT * FROM member WHERE username = 'test' AND password = 'test';

Action 7
UPDATE member
SET name = 'test2'
WHERE username = 'test';
select * from member;

Task 4 SQL Aggregate Functions
Action 1
SELECT COUNT(*) AS row_count FROM member;

Action 2
SELECT SUM(follower_count) AS total_followers FROM member;

Action 3
SELECT AVG(follower_count) AS average_followers FROM member;

Task 5 SQL Join
Action 1
SELECT message.*, member.name
FROM message
INNER JOIN member ON message.member_id = member.id;

Action 2
SELECT message.content, member.name, member.username
FROM message
JOIN member ON message.member_id = member.id
WHERE member.username = 'test';

Action 3
SELECT member.username, AVG(message.like_count) AS average_like_count
FROM message
JOIN member ON message.member_id = member.id
WHERE member.username = 'test'
GROUP BY member.username;