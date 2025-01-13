import pytest
from lib.project_a.md_project_a import main
from lib.project_a.md_project_a import fn_proc_00
from lib.project_a.md_project_a import fn_proc_99

def test_fn_proc_00(capsys):
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
    assert captured.out.strip() == "task holder start completed"

def test_fn_proc_99(capsys):
    fn_proc_99(
        'snf_account',
        'snf_user',
        'snf_pass',
        'snf_keypath',
        'snf_role',
        'snf_warehouse',
        'snf_business_case',
        'snf_environment'
    )
    assert captured.out.strip() == "task holder end completed"

def test_main(capsys):
    # Test main to ensure it works as expected
    main()
    captured = capsys.readouterr()
    assert "task holder start completed" in captured.out
