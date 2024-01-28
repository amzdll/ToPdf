-- sql/users.py

-- name: get-user-by-id^
SELECT *
FROM users
WHERE id = :user_id
LIMIT 1;

-- name: create-new-user<!
INSERT INTO users (id)
VALUES (:id)
RETURNING *;
