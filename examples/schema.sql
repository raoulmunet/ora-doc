CREATE TABLE dwh.customer_dim (
    customer_id NUMBER NOT NULL,
    customer_name VARCHAR2(200),
    status VARCHAR2(20),
    CONSTRAINT pk_customer_dim PRIMARY KEY (customer_id)
);
