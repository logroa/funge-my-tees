CREATE TABLE users (
    id serial PRIMARY KEY,
    email varchar ( 255 ) UNIQUE NOT NULL,
    password varchar ( 50 ) NOT NULL
    created_on TIMESTAMP NOT NULL,
    last_order TIMESTAMP
);

CREATE TABLE roles (
    id serial PRIMARY KEY,
    name VARCHAR ( 255 ) UNIQUE NOT NULL
);

CREATE TABLE user_roles (
    user_id INT NOT NULL,
    role_id INT NOT NULL,
    grant_date TIMESTAMP,
    PRIMARY KEY (user_id, role_id),
    FOREIGN KEY (user_id)
        REFERENCES users (id),
    FOREIGN KEY (role_id)
        REFERENCES roles (id)
);

CREATE table shirts (
    id serial PRIMARY KEY,
    name varchar ( 100 ) UNIQUE NOT NULL,
    front_img_url varchar ( 100 ) NOT NULL,
    back_img_url varchar ( 100 ),
    price FLOAT,
    available BOOLEAN
);

CREATE TABLE orders (
    id serial PRIMARY KEY,
    user_id INT NOT NULL,
    shirt_id INT NOT NULL,
    shirt_size varchar ( 5 ) NOT NULL,
    order_num INT,
    order_date TIMESTAMP,
    FOREIGN KEY (user_id)
        REFERENCES users (id),
    FOREIGN KEY (shirt_id)
        REFERENCES shirts (id)
);

CREATE TABLE suggestions (
    id serial PRIMARY KEY,
    more varchar ( 100 ),
    less varchar ( 100 )
);

CREATE TABLE user_suggestions (
    user_id INT NOT NULL,
    suggestions_id INT NOT NULL,
    PRIMARY KEY (user_id, suggestions_id),
    FOREIGN KEY (user_id)
        REFERENCES users (id),
    FOREIGN KEY (suggestions_id)
        REFERENCES suggestions (id)    
);