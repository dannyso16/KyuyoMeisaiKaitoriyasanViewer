python .\create_html.py
git status

set /p yn_check="Git commit? (y/n):  "
IF %yn_check:Y=Y%==Y (
  for /f "tokens=2 delims==" %%i in ('wmic os get localdatetime /value ^| find "="') do set datetime=%%i
  set commit_date=%datetime:~0,8%
  git add --a
  git commit -m "add: %commit_date%"
  
  set /p yn_check="Git pushH (y/n):  "
  IF %yn_check:Y=Y%==Y (
    --git push
    pause
  )
  ELSE (
    GOTO DOIT
  )
) ELSE (
  GOTO DOIT
) 

:DOIT
start cmd /k echo push‚Æ‚©‚Í©•ª‚Å‚â‚Á‚Ä‚Ë