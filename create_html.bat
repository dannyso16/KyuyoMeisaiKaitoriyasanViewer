python .\create_html.py
git status
git add --a

for /f "tokens=2 delims==" %%i in ('wmic os get localdatetime /value ^| find "="') do set datetime=%%i
set commit_date=%datetime:~0,8%
git commit -m "add: %commit_date%"

start cmd /k echo push‚Æ‚©‚ÍŽ©•ª‚Å‚â‚Á‚Ä‚Ë
pause