;获得当前时间，只处理一个小时以内的文件
;FormatTime, CurrentTime, %A_Now%, yyyyMMddHHmmss 
;CurrentTime -= 10100 ; 获得上一次处理的时间戳间隔，当前使用61min


FileList =
Loop, C:\Windows\Minidump\*.dmp, 1
    FileList = %FileList%%A_LoopFileTimeModified%`t%A_LoopFileName%`n
Sort, FileList, R  ; 根据日期排序.
num=0
Loop, parse, FileList, `n
{
    FormatTime, CurrentTime, %A_Now%, yyyyMMddHHmmss 
    if A_LoopField =  ; 忽略列表末尾的最后一个换行符 (空项).
        continue
    StringSplit, FileItem, A_LoopField, %A_Tab%  ; 用 tab 作为分隔符将其分为两部分.
  ;  MsgBox, 4,, %CurrentTime% (%FileItem1%) %FileItem2% `nContinue?
  ; IfMsgBox, No
  ;      break
    EnvSub, CurrentTime, %FileItem1%, seconds
    if CurrentTime < 3361 ; 
        ;MsgBox %CurrentTime% is now
        FileAppend ,`n%FileItem2%, send_mail.txt
        num+=1    
}

Loop, C:\Program Files\tbEdr\*.dmp, 1
    FileList = %FileList%%A_LoopFileTimeModified%`t%A_LoopFileName%`n
Sort, FileList, R  ; 根据日期排序.
Loop, parse, FileList, `n
{
    FormatTime, CurrentTime, %A_Now%, yyyyMMddHHmmss 
    if A_LoopField =  ; 忽略列表末尾的最后一个换行符 (空项).
        continue
    StringSplit, FileItem, A_LoopField, %A_Tab%  ; 用 tab 作为分隔符将其分为两部分.
  ;  MsgBox, 4,, %CurrentTime% (%FileItem1%) %FileItem2% `nContinue?
  ; IfMsgBox, No
  ;      break
    EnvSub, CurrentTime, %FileItem1%, seconds
    if CurrentTime < 3361 ; 
        ;MsgBox %CurrentTime% is now
        FileAppend ,`n%FileItem2%, send_mail.txt
        num+=1    
}
if num > 0 ;
   Run python C:\tool\sendMail.py

