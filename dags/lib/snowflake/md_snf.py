def fn_cursor_python_create(
    snf_account,
    snf_user,
    snf_pass,
    snf_keypath,
    snf_role,
    snf_warehouse,
    snf_business_case,
    snf_environment
):
    import snowflake.connector
    import os
    import datetime

    conn = snowflake.connector.connect(
        user=snf_user,
        account=snf_account,
        private_key_file=snf_keypath,
        private_key_file_pwd=snf_pass,
        warehouse=snf_warehouse,
        database=snf_database,
        session_parameters={
        "CLIENT_TELEMETRY_ENABLED": False,
        "QUERY_TAG": f'{"app-name":snf_business_case,"business-area":"USE_CASE_DEVELOPMENT","business-owner":"ANALYTIC","business-unit":"ANALYTIC","technical-owner":"ANALYTIC","criticality":"C1","environment":snf_environment,"info-class":"Internal​","data-sensitivity":"PII"}'
        }
    )
    # Create a cursor to execute queries
    cur = conn.cursor()

    return cur

def fn_session_snowpark_create(
    snf_account,
    snf_user,
    snf_pass,
    snf_keypath,
    snf_role,
    snf_warehouse,
    snf_business_case,
    snf_environment
):
    import os, json
    import snowflake.snowpark as snowpark
    from snowflake.snowpark import *
    from snowflake.snowpark.functions import *
    from snowflake.snowpark.types import *
    from snowflake.snowpark.functions import col
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives.asymmetric import dsa
    from cryptography.hazmat.primitives import serialization

    with open(snf_keypath, "rb") as key:
        p_key= serialization.load_pem_private_key(
            key.read(),
            #password=os.environ['PRIVATE_KEY_PASSPHRASE'].encode(),
                password=str.encode(snf_pass),
            backend=default_backend()

        )
        pkb = p_key.private_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

    session = snowpark.Session.builder.configs({
        "account": snf_account,
        "user": snf_user,
        "role": snf_role,
        "private_key":pkb,
        "warehouse": snf_warehouse
    }).create()

    set_output_list = []

    set_output_list.append(
        session.sql(f"""
                ALTER SESSION SET QUERY_TAG = '{"app-name":snf_business_case,"business-area":"USE_CASE_DEVELOPMENT","business-owner":"ANALYTIC","business-unit":"ANALYTIC","technical-owner":"ANALYTIC","criticality":"NC","environment":snf_environment,"info-class":"Internal​","data-sensitivity":"PII"}';
                """).collect()
    )
    return session

def fn_qry(
    qry_text,
    snf_account,
    snf_user,
    snf_pass,
    snf_keypath,
    snf_role,
    snf_warehouse,
    snf_business_case,
    snf_environment
):
    curr = fn_cursor_python_create(
        snf_account,
        snf_user,
        snf_pass,
        snf_keypath,
        snf_role,
        snf_warehouse,
        snf_business_case,
        snf_environment
    )

    cur.execute(f"""{qry_text}""")
    results = cur.fetchall()
    try:
        columns = [desc[0] for desc in cur.description]
        output = pd.DataFrame(results, columns=columns)
    except Exception as e:
        output = results

    curr.close()

    return output