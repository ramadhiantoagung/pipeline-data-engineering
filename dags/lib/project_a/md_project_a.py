def fn_proc_00(
    snf_account,
    snf_user,
    snf_pass,
    snf_keypath,
    snf_role,
    snf_warehouse,
    snf_business_case,
    snf_environment
):
    from snowflake.md_snf import fn_qry

    output = 'task holder start completed'
    print(output)

    return output

def fn_proc_01(
    snf_account,
    snf_user,
    snf_pass,
    snf_keypath,
    snf_role,
    snf_warehouse,
    snf_business_case,
    snf_environment
):
    from snowflake.md_snf import fn_qry

    output = fn_qry(f"""SHOW WAREHOUSES""")

    return output

def fn_proc_02(
    snf_account,
    snf_user,
    snf_pass,
    snf_keypath,
    snf_role,
    snf_warehouse,
    snf_business_case,
    snf_environment
):
    from snowflake.md_snf import fn_qry

    output = fn_qry(f"""SHOW WAREHOUSES""")

    return output

def fn_proc_03(
    snf_account,
    snf_user,
    snf_pass,
    snf_keypath,
    snf_role,
    snf_warehouse,
    snf_business_case,
    snf_environment
):
    from snowflake.md_snf import fn_qry

    output = fn_qry(f"""SHOW WAREHOUSES""")

    return output

def fn_proc_99(
    snf_account,
    snf_user,
    snf_pass,
    snf_keypath,
    snf_role,
    snf_warehouse,
    snf_business_case,
    snf_environment
):
    output = 'task holder end completed'
    print(output)

    return output

def main():
    fn_proc_00(
        'snf_account',
        'snf_user',
        'snf_pass',
        'snf_keypath',
        'snf_role',
        'snf_warehouse',
        'snf_business_case',
        'snf_environment'
    )

if __name__ == "__main__":
    main()