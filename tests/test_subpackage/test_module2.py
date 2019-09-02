import mypackage.subpackage.module2


def test_eggs():
    output = mypackage.subpackage.module2.eggs(2)
    expected = "2 eggs, please!"
    assert output == expected
