
def test_funtion():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_funtion()
# inner_function() - отсюда эту функию не видно
