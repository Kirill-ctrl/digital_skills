CREATE TABLE account (
    _id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL CONSTRAINT unique_account_email UNIQUE,
    hash_password NOT NULL
);

-- ----------------------------------------------------------------

CREATE TABLE category (
    _id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
);

-- ----------------------------------------------------------------

CREATE TABLE product (
    _id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    price TEXT NOT NULL,
    photo_link TEXT,
    category_id INTEGER NOT NULL REFERENCES category(id) ON DELETE CASCADE
);

-- ----------------------------------------------------------------

CREATE TABLE ec_order (
    _id INTEGER PRIMARY KEY AUTOINCREMENT,
    number INTEGER NOT NULL CONSTRAINT unique_order_number UNIQUE,
    account_id INTEGER NOT NULL REFERENCES account(id) ON DELETE CASCADE,
    status TEXT
);

-- ----------------------------------------------------------------

CREATE TABLE ordered_product (
    _id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL REFERENCES product(id) ON DELETE CASCADE,
    ec_order_id INTEGER NOT NULL REFERENCES ec_order(id) ON DELETE CASCADE,
    quantity INTEGER NOT NULL
);

-- ----------------------------------------------------------------

CREATE TABLE shopping_cart (
    account_id INTEGER NOT NULL REFERENCES account(id) ON DELETE CASCADE,
    status_cart TEXT
);

-- ----------------------------------------------------------------

CREATE TABLE cart_product (
    shopping_cart_id INTEGER NOT NULL REFERENCES shopping_cart(id) ON DELETE CASCADE,
    product_id INTEGER NOT NULL REFERENCES product(id) ON DELETE CASCADE,
    quantity_product INTEGER
)
