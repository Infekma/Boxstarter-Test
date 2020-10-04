@echo off

echo import option ; > base-config.jam
echo using msvc ; >> base-config.jam
echo option.set keep-going : false ; >> base-config.jam

REM 64 bit 2.7
copy base-config.jam project-config.jam
echo using python : 2.7 : C:/Python27-64/python.exe : C:/Python27-64/include : C:/Python27-64/libs ; >> project-config.jam
b2 --build-dir=C:\boost_build --prefix=C:\boost --libdir=C:\boost\lib64 --layout=tagged address-model=64 -j16 toolset=msvc-14.1 install
del c:\boost_build\boost\bin.v2\libs\python /Q

REM 64 bit 3.7
copy base-config.jam project-config.jam
echo using python : 3.7 : C:/Python37-64/python.exe : C:/Python37-64/include : C:/Python37-64/libs ; >> project-config.jam
b2 --build-dir=C:\boost_build --prefix=C:\boost --libdir=C:\boost\lib64 --layout=tagged address-model=64 -j16 toolset=msvc-14.1 install
del c:\boost_build\boost\bin.v2\libs\python /Q

REM 32 bit 2.7
copy base-config.jam project-config.jam
echo using python : 2.7 : C:/Python27-32/python.exe : C:/Python27-32/include : C:/Python27-32/libs ; >> project-config.jam
b2 --build-dir=C:\boost_build --prefix=C:\boost --libdir=C:\boost\lib32 --layout=tagged address-model=32 -j16 toolset=msvc-14.1 install
del c:\boost_build\boost\bin.v2\libs\python /Q

REM 32 bit 3.7
copy base-config.jam project-config.jam
echo using python : 3.7 : C:/Python37-32/python.exe : C:/Python37-32/include : C:/Python37-32/libs ; >> project-config.jam
b2 --build-dir=C:\boost_build --prefix=C:\boost --libdir=C:\boost\lib32 --layout=tagged address-model=32 -j16 toolset=msvc-14.1 install
del c:\boost_build\boost\bin.v2\libs\python /Q
