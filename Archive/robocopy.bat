REM -----------------------------------------------------------------------------
REM Script Name: robocopy.bat
REM Description: Synchronizes the contents of E:\Photos_Videos to F:\Photos_Videos
REM              using robocopy with mirror mode. Retries twice on failure, waits
REM              5 seconds between retries, and logs output to E:\Logs\Photos_Videos.log.
REM -----------------------------------------------------------------------------
robocopy E:\Photos_Videos F:\Photos_Videos /MIR
robocopy E:\Photos_Videos F:\Photos_Videos /MIR /R:2 /W:5 /LOG:E:\Logs\Photos_Videos.log