from ora_doc import parse_tables,render_markdown

def test_ddl_documentation():
    sql="""CREATE TABLE dwh.customer_dim (
      customer_id NUMBER NOT NULL,
      customer_name VARCHAR2(200),
      CONSTRAINT pk_customer_dim PRIMARY KEY (customer_id)
    );"""
    tables=parse_tables(sql)
    assert tables[0].name=="DWH.CUSTOMER_DIM"
    assert tables[0].columns[0].nullable is False
    assert "CUSTOMER_NAME" in render_markdown(tables)
