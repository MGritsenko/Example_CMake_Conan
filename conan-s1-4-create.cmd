cls

set CONAN_VERBOSE_TRACEBACK=1

conan create . lexer/1.0.0@mikhail/testing ^
-o lexer:shared=True ^
--profile x86_64-Windows-v141-Debug