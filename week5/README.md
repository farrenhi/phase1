# Task 3 SQL CRUD


## Action 0 Create Database and Table
```SQL
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
![task3_SQL_CRUD_1](https://github.com/farrenhi/phase1/assets/114633763/72565ce3-dc58-48f1-8954-2326f3aad9ee)

## Action 1
```SQL
INSERT INTO member(name, username, password, follower_count) VALUES('Allen', 'test', 'test', 1);
INSERT INTO member(name, username, password, follower_count) VALUES('Bob', 'little', 'big', 2);
INSERT INTO member(name, username, password, follower_count) VALUES('Cindy', 'high', 'low', 3);
INSERT INTO member(name, username, password, follower_count) VALUES('David', 'tall', 'short', 10);
```
![task3_SQL_CRUD_1](https://github.com/farrenhi/phase1/assets/114633763/72565ce3-dc58-48f1-8954-2326f3aad9ee)

## Action 2
```SQL
SELECT * FROM member;
```
![task3_SQL_CRUD_2](https://github.com/farrenhi/phase1/assets/114633763/4f8dcd51-2b66-462f-b190-0ae74ec394ae)

## Action 3
```SQL
SELECT * FROM member ORDER BY time DESC;
```
![task3_SQL_CRUD_3](https://github.com/farrenhi/phase1/assets/114633763/b93bdb19-629f-4d78-9caa-74e11ef861f6)

## Action 4
```SQL
SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
```
![task3_SQL_CRUD_4](https://github.com/farrenhi/phase1/assets/114633763/ac180644-7684-4abb-a24b-153b332dcb27)

## Action 5
```SQL
SELECT * FROM member WHERE username = 'test';
```
![task3_SQL_CRUD_5](https://github.com/farrenhi/phase1/assets/114633763/07681798-2332-4201-a529-efc9991e0b08)

## Action 6
```SQL
SELECT * FROM member WHERE username = 'test' AND password = 'test';
```
![task3_SQL_CRUD_6](https://github.com/farrenhi/phase1/assets/114633763/2343d102-b2eb-412a-8702-e886a12d74d3)

## Action 7
```SQL
UPDATE member
SET name = 'test2'
WHERE username = 'test';
select * from member;
```
![task3_SQL_CRUD_7](https://github.com/farrenhi/phase1/assets/114633763/f276f691-0109-4bbb-897c-34fbcd7af77f)

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
