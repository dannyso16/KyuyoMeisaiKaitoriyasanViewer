  for /f "tokens=2 delims==" %%i in ('wmic os get localdatetime /value ^| find "="') do set datetime=%%i
  set commit_date=%datetime:~0,8%
  git add --a
  echo "add: %commit_date%"
pause