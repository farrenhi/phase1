# Task 3 SQL CRUD

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
![task4_1](https://github.com/farrenhi/phase1/assets/114633763/683bce01-6ff5-4d92-869a-9e6ff54a4ad7)


## Action 2
```SQL
SELECT SUM(follower_count) AS total_followers FROM member;
```
![task4_2](https://github.com/farrenhi/phase1/assets/114633763/96d1acdc-0178-4188-9b65-78c3f8f02355)


## Action 3
```SQL
SELECT AVG(follower_count) AS average_followers FROM member;
```
![task4_3](https://github.com/farrenhi/phase1/assets/114633763/0a2c1a3e-e8cd-485f-9122-ac11982ca267)

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
![task5_0](https://github.com/farrenhi/phase1/assets/114633763/ccf718c3-ab0e-452a-afab-6735f4631e6f)

## Action 1
```SQL
SELECT message.*, member.name
FROM message
INNER JOIN member ON message.member_id = member.id;
```
![task5_1](https://github.com/farrenhi/phase1/assets/114633763/7e0c043d-1571-4a1c-a21f-da4d67b9674e)

## Action 2
```SQL
SELECT message.content, member.name, member.username
FROM message
JOIN member ON message.member_id = member.id
WHERE member.username = 'test';
```
![task5_2](https://github.com/farrenhi/phase1/assets/114633763/77f22eed-e8a9-4c1b-abb7-5119861ab859)


## Action 3
```SQL
SELECT member.username, AVG(message.like_count) AS average_like_count
FROM message
JOIN member ON message.member_id = member.id
WHERE member.username = 'test'
GROUP BY member.username;
```
![task5_3](https://github.com/farrenhi/phase1/assets/114633763/c93eb5e0-e279-4c2b-a6e0-9191c1d7ad77)
