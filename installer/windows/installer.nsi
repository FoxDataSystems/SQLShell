
; SQLShell Windows Installer Script
; Requires NSIS 3.x

!include "MUI2.nsh"
!include "FileFunc.nsh"

; General
Name "R.A.L.P.H. – Read/Analyze/Load/Parse Hub"
OutFile "..\..\dist\R.A.L.P.H. – Read/Analyze/Load/Parse Hub-0.3.5-win64-setup.exe"
InstallDir "$PROGRAMFILES64\R.A.L.P.H. – Read/Analyze/Load/Parse Hub"
InstallDirRegKey HKLM "Software\R.A.L.P.H. – Read/Analyze/Load/Parse Hub" "InstallDir"
RequestExecutionLevel admin

; Interface Settings
!define MUI_ABORTWARNING
!define MUI_ICON "..\..\sqlshell\resources\icon.ico"
!define MUI_UNICON "..\..\sqlshell\resources\icon.ico"

; Pages
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE "..\..\sqlshell\LICENSE"
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

; Languages
!insertmacro MUI_LANGUAGE "English"

; Installer Section
Section "Install"
    SetOutPath "$INSTDIR"
    
    ; Copy all files from dist
    File /r "..\..\dist\R.A.L.P.H. – Read/Analyze/Load/Parse Hub\*.*"
    
    ; Create uninstaller
    WriteUninstaller "$INSTDIR\Uninstall.exe"
    
    ; Create Start Menu shortcuts
    CreateDirectory "$SMPROGRAMS\R.A.L.P.H. – Read/Analyze/Load/Parse Hub"
    CreateShortcut "$SMPROGRAMS\R.A.L.P.H. – Read/Analyze/Load/Parse Hub\R.A.L.P.H. – Read/Analyze/Load/Parse Hub.lnk" "$INSTDIR\R.A.L.P.H. – Read/Analyze/Load/Parse Hub.exe"
    CreateShortcut "$SMPROGRAMS\R.A.L.P.H. – Read/Analyze/Load/Parse Hub\Uninstall.lnk" "$INSTDIR\Uninstall.exe"
    
    ; Create Desktop shortcut
    CreateShortcut "$DESKTOP\R.A.L.P.H. – Read/Analyze/Load/Parse Hub.lnk" "$INSTDIR\R.A.L.P.H. – Read/Analyze/Load/Parse Hub.exe"
    
    ; Registry entries for Add/Remove Programs
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\R.A.L.P.H. – Read/Analyze/Load/Parse Hub" "DisplayName" "R.A.L.P.H. – Read/Analyze/Load/Parse Hub"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\R.A.L.P.H. – Read/Analyze/Load/Parse Hub" "UninstallString" "$INSTDIR\Uninstall.exe"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\R.A.L.P.H. – Read/Analyze/Load/Parse Hub" "DisplayIcon" "$INSTDIR\R.A.L.P.H. – Read/Analyze/Load/Parse Hub.exe"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\R.A.L.P.H. – Read/Analyze/Load/Parse Hub" "Publisher" "Wortell"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\R.A.L.P.H. – Read/Analyze/Load/Parse Hub" "DisplayVersion" "0.3.5"
    
    ; Get installed size
    ${GetSize} "$INSTDIR" "/S=0K" $0 $1 $2
    IntFmt $0 "0x%08X" $0
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\R.A.L.P.H. – Read/Analyze/Load/Parse Hub" "EstimatedSize" "$0"
SectionEnd

; Uninstaller Section
Section "Uninstall"
    ; Remove files
    RMDir /r "$INSTDIR"
    
    ; Remove Start Menu shortcuts
    RMDir /r "$SMPROGRAMS\R.A.L.P.H. – Read/Analyze/Load/Parse Hub"
    
    ; Remove Desktop shortcut
    Delete "$DESKTOP\R.A.L.P.H. – Read/Analyze/Load/Parse Hub.lnk"
    
    ; Remove registry entries
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\R.A.L.P.H. – Read/Analyze/Load/Parse Hub"
    DeleteRegKey HKLM "Software\R.A.L.P.H. – Read/Analyze/Load/Parse Hub"
SectionEnd
