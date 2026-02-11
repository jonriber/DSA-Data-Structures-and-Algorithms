# Backend + SQL - Scenario 1

Simple task-tracking service.

## Requirements

- Users can create tasks with title, status (todo/in_progress/done), and created_at.
- You need an endpoint: GET /users/:id/tasks?status=...&limit=...&offset=...
- Return tasks for a user, filtered by status if provided, ordered by newest first.
- We also want a query for “active users” in the last 7 days (users who created at least 3 tasks in the last 7 days).

## Tasks

1. Propose a minimal PostgreSQL schema (tables + important indexes).
2. Write the SQL for the endpoint query.
3. Write the SQL for “active users.”

## Resolution

### Minimal PostgreSQL schema (table + important indexes)

First entry: Minimal PostgreSQL schema would be: one important table for tasks, this is the center of the application. Another table for users, in which I can create a relantionship between tasks and users, another table for audit, where all transactions are stored

Polished Entry: Keep it minimal: users and tasks are enough. If you want audit, explain why it’s needed for the requirements.

Table tasks would have a column to identify a single column with a unique id, a column for the title, a column for the status and another column with the time stamp, column with the id of the owner of the task (primary key for the user table)
Table users would have a column for a unique id, to identify each specific user, one column for the name, one column for the family name.
For an audit table, I would have one column to identify each entry on this table, one column to identify the task, one colum to identify the transaction, what was done.

The minimal SQL would be:

```sql
-- users
id           BIGSERIAL PRIMARY KEY
first_name   TEXT NOT NULL
last_name    TEXT NOT NULL

-- tasks
id           BIGSERIAL PRIMARY KEY
user_id      BIGINT NOT NULL REFERENCES users(id)
title        TEXT NOT NULL
status       TEXT NOT NULL CHECK (status IN ('todo','in_progress','done'))
created_at   TIMESTAMPTZ NOT NULL DEFAULT now()

```

#### Indexes
An index speeds up lookups and ordering by letting the DB find rows *without scanning* the whole table.

Example index for the endpoint: We filter by user_id, sometimes status, and order by created_at DESC.

A good index is:
```sql
CREATE INDEX tasks_user_status_created_at_idx
ON tasks (user_id, status, created_at DESC);

```
That lets Postgres quickly find a user’s tasks, optionally filtered by status, and already ordered by newest.

### SQL query for the endpoint

The endpoint is: *GET /users/:id/tasks?status=...&limit=...&offset=...*

Parameters:
- $1 = user_id
- $2 = status (nullable)
- $3 = limit
- $4 = offset

```sql
SELECT id, user_id, title, status, created_at
FROM tasks
WHERE user_id = $1
  AND ($2 IS NULL OR status = $2)
ORDER BY created_at DESC
LIMIT $3 OFFSET $4;

```

My translation for this SQL query: 
- this will select the columns (id, user_id, title, status, created_at) from the table tasks.
- wheen user id is the one from the $1 parameter, which means, filtering all users from the table
- and for that specific status provided, and if not provided, bring all tasks
- order is new first
- pagination with limit and offset

#### now the second endpoint