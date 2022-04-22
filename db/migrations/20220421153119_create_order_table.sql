-- migrate:up
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TYPE order_side AS ENUM ('BUY', 'SELL');
CREATE TYPE order_status AS ENUM ('PENDING', 'FILLED');

CREATE TABLE public.order (
	id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  instrument VARCHAR(12) NOT NULL,
  side order_side DEFAULT 'BUY',
  quantity INT NOT NULL,
  quantity_buy INT NOT NULL DEFAULT 0,
  quantity_sell INT NOT NULL DEFAULT 0,
  type VARCHAR(12) NOT NULL,
  user_id uuid NOT NULL,
  status order_status DEFAULT 'PENDING',
  filled_price VARCHAR(12) DEFAULT '0.00',
  created_at   timestamp not null DEFAULT CURRENT_TIMESTAMP,
	updated_at   timestamp not null DEFAULT CURRENT_TIMESTAMP
);


-- migrate:down
DROP TABLE order;
