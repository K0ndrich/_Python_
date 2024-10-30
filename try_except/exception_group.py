# ExceptionGoup и BaseExceptionGroup
# Позволяют поднять сразу много исключений за один раз и дает им обобщающее свое название

# ExceptionGoup поднимаю стандарные исключения из средины иерархии
# BaseExceptionGroup позволяют поднимать исключения из более высокого уровня иерархии


# -----   ExceptionGoup   -------------------------------------------------------------------------------------------------------------------


try:
    # хранит набор исключений
    my_except = ExceptionGroup(
        "my exception group",
        [
            TypeError(1),
            ValueError(2),
        ],
    )
    raise my_except

except ExceptionGroup as my_item:
    print(my_item)  # -> my exception group (2 sub-exceptions)
    print(my_item.args)  # -> ('my exception group', [TypeError(1), ValueError(2)])


# -----   BaseExceptionGroup   -------------------------------------------------------------------------------------------------------------------
try:
    my_except = BaseExceptionGroup(
        "my base exception group",
        [
            TypeError(1),
            GeneratorExit(2),
        ],
    )
    raise my_except

except BaseExceptionGroup as my_item:
    print(my_item)  # -> my base exception group (2 sub-exceptions)
    print(
        my_item.args
    )  # -> ('my base exception group', [TypeError(1), GeneratorExit(2)])
