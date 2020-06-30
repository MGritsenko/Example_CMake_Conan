cls
"C:\Program Files\CMake\bin\cmake" ^
C:\eSignal\example ^
-DVERSION="0.0.0" ^
-DPRODUCTION=1 ^
-Dcmake-toolkit_DIR=C:\.conan\9bfc8d\1\cmake ^
-DQt5_DIR=C:\deps\latest\qt\qt512_vc141_x64\lib\cmake\Qt5 ^
-DQt5Core_DIR=C:\deps\latest\qt\qt512_vc141_x64\lib\cmake\Qt5Core ^
-DBUILD_SHARED_LIBS=ON ^
-G "Visual Studio 15 2017" -A x64 ^
-T "v141"