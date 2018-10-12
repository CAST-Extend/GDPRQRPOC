@echo off
MODE CON: COLS=132 LINES=40

::Parameters to adapt to each analysis env :
Set SourceFolder=C:\Oxygenworkspacegdprjava\com.castsoftware.labs.javagdpr\DevTools
Set TargetFolder=C:\Oxygenworkspacegdprjava\com.castsoftware.labs.javagdpr\MasterFiles
Set adgMetrics=AdgMetrics_GDPR.xml

::Parameters to adapt in some cases :
Set MetricsCompiler_BAT_path=.\MetricsCompiler.bat


Title Generating %adgMetrics% from MASTER FILES at %TargetFolder%

:: call Compiler - full syntax (with specific AdgConfigData file name)
call %MetricsCompiler_BAT_path% -encodeUA -inputdir %TargetFolder% -outputdir %SourceFolder% -filename %adgMetrics%

::TOBE : Manage ERRORLEVEL ?
pause