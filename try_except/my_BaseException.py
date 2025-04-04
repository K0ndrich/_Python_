# Иерархия Наследования Исключений 

# BaseException
# ├── SystemExit
# ├── KeyboardInterrupt
# ├── GeneratorExit
# └── Exception
#     ├── ArithmeticError
#     │   ├── FloatingPointError
#     │   ├── OverflowError
#     │   └── ZeroDivisionError
#     ├── AssertionError
#     ├── AttributeError
#     ├── BufferError
#     ├── EOFError
#     ├── ImportError
#     │   └── ModuleNotFoundError
#     ├── LookupError
#     │   ├── IndexError
#     │   └── KeyError
#     ├── MemoryError
#     ├── NameError
#     │   └── UnboundLocalError
#     ├── OSError
#     │   ├── BlockingIOError
#     │   ├── ChildProcessError
#     │   ├── ConnectionError
#     │   │   ├── BrokenPipeError
#     │   │   ├── ConnectionAbortedError
#     │   │   ├── ConnectionRefusedError
#     │   │   └── ConnectionResetError
#     │   ├── FileExistsError
#     │   ├── FileNotFoundError
#     │   ├── InterruptedError
#     │   ├── IsADirectoryError
#     │   ├── NotADirectoryError
#     │   ├── PermissionError
#     │   ├── ProcessLookupError
#     │   └── TimeoutError
#     ├── ReferenceError
#     ├── RuntimeError
#     │   ├── NotImplementedError
#     │   └── RecursionError
#     ├── StopIteration
#     ├── StopAsyncIteration
#     ├── SyntaxError
#     │   └── IndentationError
#     │       └── TabError
#     ├── SystemError
#     ├── TypeError
#     ├── ValueError
#     │   └── UnicodeError
#     │       ├── UnicodeDecodeError
#     │       ├── UnicodeEncodeError
#     │       └── UnicodeTranslateError
#     └── Warning
#         ├── DeprecationWarning
#         ├── PendingDeprecationWarning
#         ├── RuntimeWarning
#         ├── SyntaxWarning
#         ├── UserWarning
#         ├── FutureWarning
#         ├── ImportWarning
#         ├── UnicodeWarning
#         └── BytesWarning
