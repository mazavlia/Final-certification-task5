DROP TABLE IF EXISTS default.users;

CREATE TABLE default.users
(id UInt32, user_name String, age UInt32, salary Float32)
ENGINE = MergeTree()
ORDER BY id;