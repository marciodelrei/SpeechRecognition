SET "_pasta_bat=%~dp0"

ECHO "%_pasta_bat%"

CD /D "%_pasta_bat%"

CALL ".venv\Scripts\activate.bat"

SET "cmd_python=python main.py"
%cmd_python%

SET "msg=Saindo em 5s..."

ECHO %msg%
timeout 5 > NUL