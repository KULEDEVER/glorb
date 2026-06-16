@echo off
echo ====================================
echo  Building all Python files with PyInstaller
echo ====================================

REM Create output folder
if not exist dist mkdir dist
if not exist build mkdir build

REM Loop through all python files in current directory
for %%f in (*.py) do (
    echo ------------------------------------
    echo Building %%f
    echo ------------------------------------

    python -m PyInstaller --onefile --clean --distpath dist --workpath build "%%f"
)

echo ====================================
echo Done building all Python files.
echo ====================================
pause