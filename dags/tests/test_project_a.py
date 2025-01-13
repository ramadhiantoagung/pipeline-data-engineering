import pytest
from lib.project_a import fn_proc_00
from lib.project_a import fn_proc_99

def test_fn_proc_00(capsys):
    fn_proc_00()
    assert captured.out.strip() == "task holder start completed"

def test_fn_proc_99(capsys):
    fn_proc_99()
    assert captured.out.strip() == "task holder end completed"

def test_main(capsys):
    # Test main to ensure it works as expected
    main()
    captured = capsys.readouterr()
    assert "task holder start completed" in captured.out
