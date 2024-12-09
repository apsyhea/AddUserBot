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

    echo Running the program...
    python src\main.py

    echo Deactivating virtual environment...
    deactivate
) else (
    echo Activating virtual environment...
    call venv\Scripts\activate

    echo Running the program...
    python src\main.py

    echo Deactivating virtual environment...
    deactivate
)

REM Pause to keep the window open
echo.
echo Press any key to exit...
pause >nul
