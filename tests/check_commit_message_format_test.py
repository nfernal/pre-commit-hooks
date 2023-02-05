# from __future__ import annotations
# import pytest
# from pre_commit_hooks.check_commit_message_format import main
# from testing.util import get_resource_path
# @pytest.mark.parametrize(
#     ('filename', 'expected_retval'), (
#         ('bad_commit_message_format', 1),
#         ('ok_commit_message_format', 0),
#     ),
# )
# def test_main(capsys, filename, expected_retval) -> None:
#     ret = main([get_resource_path(filename)])
#     assert ret == expected_retval
#     if expected_retval == 1:
#         stdout, _ = capsys.readouterr()
#         assert filename in stdout
# def test_non_utf8_file(tmpdir)  -> None:
#     f = tmpdir.join('t.json')
#     f.write_binary(b'\xa9\xfe\x12')
#     assert main((str(f),))
from __future__ import annotations
