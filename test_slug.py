from slug import slugify


def test_basic():
    assert slugify("Hello World") == "hello-world"


def test_multi():
    assert slugify("  Foo   Bar Baz ") == "foo-bar-baz"
