@echo off
REM Move to the script directory
cd /d %~dp0

REM Check if virtual environment exists
if not exist "venv\Scripts\activate" (
    echo Creating virtual environment...
    python -m venv venv

    echo Activating virtual environment...
    call venv\Scripts\activate

    echo Installing dependencies...
    pip install -r requirements.txt
)

REM Activate the existing virtual environment and run the program
echo Activating virtual environment...
call venv\Scripts\activate

echo Running the program...
python src\main.py

REM Pause to keep the window open
echo.
echo Press any key to exit...
pause >nul
