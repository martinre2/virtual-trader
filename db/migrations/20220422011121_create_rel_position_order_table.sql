-- migrate:up
CREATE TABLE order_position (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(), 
  position_id uuid NOT NULL,
  order_id uuid NOT NULL,
  created_at   timestamp not null DEFAULT CURRENT_TIMESTAMP,
  updated_at   timestamp not null DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY(position_id) REFERENCES public.position(id),
  FOREIGN KEY(order_id) REFERENCES public.order(id)
);

-- migrate:down

DROP TABLE order_position
