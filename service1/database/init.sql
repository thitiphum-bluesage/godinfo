CREATE DATABASE IF NOT EXISTS godinfo;
USE godinfo;

CREATE TABLE IF NOT EXISTS gods (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    religion VARCHAR(100),
    power VARCHAR(200)
);

INSERT INTO gods (name, religion, power)
VALUES
    ('Zeus', 'Greek', 'God of the sky, lightning, and thunder'),
    ('Odin', 'Norse', 'God of wisdom, poetry, and war'),
    ('Brahma', 'Hindu', 'God of creation');
