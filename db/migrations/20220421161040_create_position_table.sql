-- migrate:up

CREATE TYPE position_status AS ENUM ('OPEN', 'CLOSED');

CREATE TABLE position (
	id uuid PRIMARY KEY DEFAULT uuid_generate_v4(), 
  user_id uuid NOT NULL,
  instrument VARCHAR(12) NOT NULL,
  shares INT NOT NULL,
  status position_status DEFAULT 'OPEN',
  open_at   timestamp not null DEFAULT CURRENT_TIMESTAMP,
  close_at   timestamp,
  created_at   timestamp not null DEFAULT CURRENT_TIMESTAMP,
	updated_at   timestamp not null DEFAULT CURRENT_TIMESTAMP
);


-- migrate:down

DROP TABLE position
