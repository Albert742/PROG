@echo off
set origine=C:\Users\alber\Desktop\PROG
set destinazione=G:\Il mio Drive\Bak

echo Copai in corso...
xcopy "%origine%" "%destinazione%" /s /e /y

echo Copia conclusa.
pause