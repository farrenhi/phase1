![t403](https://github.com/farrenhi/phase1/assets/114633763/a5234a62-faa8-46a2-b83d-17fda6c06ad3)# Task 3 SQL CRUD

## Action 0 Create Database and Table
```SQL
CREATE DATABASE website;
USE website;
CREATE TABLE member(
	id bigint auto_increment,
    primary key (id),
    name varchar(255) NOT NULL,
    username varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    follower_count int unsigned NOT NULL DEFAULT 0,
    time datetime NOT NULL default current_timestamp
);
```

## Action 1
```SQL
INSERT INTO member(name, username, password, follower_count) VALUES('Allen', 'test', 'test', 1);
INSERT INTO member(name, username, password, follower_count) VALUES('Bob', 'little', 'big', 2);
INSERT INTO member(name, username, password, follower_count) VALUES('Cindy', 'high', 'low', 3);
INSERT INTO member(name, username, password, follower_count) VALUES('David', 'tall', 'short', 10);
```
![t301](https://github.com/farrenhi/phase1/assets/114633763/9bb14a96-e3a4-473d-b6fb-5f34823ee244)

## Action 2
```SQL
SELECT * FROM member;
```
![t302](https://github.com/farrenhi/phase1/assets/114633763/49089656-07c0-402b-8405-b5e630979cfb)

## Action 3
```SQL
SELECT * FROM member ORDER BY time DESC;
```
![t303](https://github.com/farrenhi/phase1/assets/114633763/865c4f82-e4b2-436e-ada2-70a45c2027eb)

## Action 4
```SQL
SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
```
![t304](https://github.com/farrenhi/phase1/assets/114633763/cc3a6d6f-bccc-47b0-bfaf-213702f6118f)

## Action 5
```SQL
SELECT * FROM member WHERE username = 'test';
```
![t305](https://github.com/farrenhi/phase1/assets/114633763/475e4b6c-3eeb-497a-9a40-8726ff3dd4a3)

## Action 6
```SQL
SELECT * FROM member WHERE username = 'test' AND password = 'test';
```
![t306](https://github.com/farrenhi/phase1/assets/114633763/0460142b-acdd-48c0-8474-d23b1004ffc4)

## Action 7
```SQL
UPDATE member
SET name = 'test2'
WHERE username = 'test';
select * from member;
```
![t307](https://github.com/farrenhi/phase1/assets/114633763/660cf48f-b0ff-43d7-8dee-f3f74d459fb9)

# Task 4 SQL Aggregate Functions
## Action 1
```SQL
SELECT COUNT(*) AS row_count FROM member;
```
![t401](https://github.com/farrenhi/phase1/assets/114633763/e654f409-c881-4946-9b51-4cf59b9ea6d9)

## Action 2
```SQL
SELECT SUM(follower_count) AS total_followers FROM member;
```
![t402](https://github.com/farrenhi/phase1/assets/114633763/84940ee1-142f-40e3-9f85-2d0a3512f35e)

## Action 3
```SQL
SELECT AVG(follower_count) AS average_followers FROM member;
```
![t403](https://github.com/farrenhi/phase1/assets/114633763/dcee13e0-a1dd-41f1-8b9d-db221a8291fb)

# Task 5 SQL Join
## Action 0 Create Table
```SQL
USE website;
CREATE TABLE message(
	id bigint auto_increment,
    primary key (id),
    member_id bigint NOT NULL,
    FOREIGN KEY (member_id) REFERENCES member(id),
    content varchar(255) NOT NULL,
    like_count int unsigned NOT NULL DEFAULT 0,
    time datetime NOT NULL default current_timestamp
);
```
![t500](https://github.com/farrenhi/phase1/assets/114633763/420090d8-a0e8-43fd-8a5b-f9e740c8061b)

## Action 1
```SQL
SELECT message.*, member.name
FROM message
INNER JOIN member ON message.member_id = member.id;
```
![t501](https://github.com/farrenhi/phase1/assets/114633763/87c02db6-badc-4bc8-bd0b-64a195cda07a)

## Action 2
```SQL
SELECT message.content, member.name, member.username
FROM message
JOIN member ON message.member_id = member.id
WHERE member.username = 'test';
```
![t502](https://github.com/farrenhi/phase1/assets/114633763/7cb7e5f7-e2ea-4351-8ada-d4432b81a932)

## Action 3
```SQL
SELECT member.username, AVG(message.like_count) AS average_like_count
FROM message
JOIN member ON message.member_id = member.id
WHERE member.username = 'test'
GROUP BY member.username;
```
![t503](https://github.com/farrenhi/phase1/assets/114633763/b41855bb-f9cc-4fd8-b850-c0a8ee57e8f5)
