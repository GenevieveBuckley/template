import mypackage.module1


def test_spam():
    expected = "spam"
    output = mypackage.module1.spam()
    assert output == expected
