SET "_pasta_bat=%~dp0"

ECHO "%_pasta_bat%"

CD /D "%_pasta_bat%"

SET "cmd_python=python -m venv .venv"
%cmd_python%

CALL ".venv\Scripts\activate.bat"

SET "cmd_python=python -m pip install pip --upgrade"
%cmd_python%

SET "cmd_python=pip install -r requirements.txt"
%cmd_python%


FOR /f "delims=" %%a in ('python -V ^| findstr ".6"') do set "$py=6"
FOR /f "delims=" %%a in ('python -V ^| findstr ".7"') do set "$py=7"
ECHO %$py%
GOTO:%$py%

:6
ECHO python versao 3.6
SET "cmd_python=pip install libs\PyAudio-0.2.11-cp36-cp36m-win_amd64.whl"
%cmd_python%

:7
ECHO python versao 3.7
SET "cmd_python=pip install libs\PyAudio-0.2.11-cp37-cp37m-win_amd64.whl"
%cmd_python%