; -----------------------------------------------------------
; 仅在 Outlook 处于当前窗口时生效
; -----------------------------------------------------------
#IfWinActive ahk_exe outlook.exe
 
; Shift + W = 向上选中邮件
+w::Send {Up}
; Shift + S = 向下选中邮件
+s::Send {Down}
 
; ===========================================================
; Alt + N : 新建 Booking/Arrival 通知 (Word 内核强制 12号字)
; ===========================================================
!n::
    try {
        olApp := ComObjActive("Outlook.Application")
    } catch {
        MsgBox, 请确保 Outlook 已经打开。
        return
    }
 
    olItem := olApp.CreateItem(0) 
    olItem.Display
 
    ; 1. 插入 HTML 内容 (暂时不管字体)
    NewContent := "
    (
    <p>Dear ,</p>
    <p>Please kindly see attached for your reference:</p>
    <p>Attached documents:</p>
    <ul>
        <li>Arrival Notice & Invoice (AN)</li>
        <li>Cargo Manifest (MNF)</li>
        <li>Return Guarantee (DN COC)</li>
    </ul>
    <p>Outstanding:</p>
    <ul>
        <li>Please surrender your original bill of lading with BL release OR get telex release.</li>
        <li>Kindly arrange payment. (WE DON’T ACCEPT WIRE TRANSFER)</li>
        <li>Please sign the empty return guarantee letter and email it back to us for shipment release.</li>
    </ul>
    <p>If you need more information, please feel free to contact us.</p>
    <p>If you need your shipment urgently, please consider applying for ERS(Expedite Rail Service). Check with us for the rate if you are interested.</p>
    <p>Please also advise if you need help with custom clearance and delivery.</p>
    <p>Thank you.</p>
    <p>Have a good day/ Bonne journée</p>
    )"
 
    olItem.HTMLBody := NewContent . olItem.HTMLBody
    
    ; 2. 强制调用 Word 内核刷字体
    doc := olItem.GetInspector.WordEditor
    doc.Content.Font.Name := "Calibri"
    doc.Content.Font.Size := 12
return
 
; ===========================================================
; Alt + E : ETA 更新 (Reply All + 强制 12号字)
; ===========================================================
!e::
    try {
        olApp := ComObjActive("Outlook.Application")
        try {
            SelItem := olApp.ActiveExplorer.Selection.Item(1)
            olItem := SelItem.ReplyAll() 
        } catch {
            olItem := olApp.CreateItem(0)
        }
    } catch {
        MsgBox, 请确保 Outlook 已经打开。
        return
    }
 
    olItem.Display
 
    EtaContent := "
    (
    <p>Good day,</p>
    <p>Please see the ETA below:</p>
    <p>&nbsp;</p> 
    <p>Have a good day/ Bonne journée</p>
    )"
 
    olItem.HTMLBody := EtaContent . olItem.HTMLBody
 
    ; 强制调用 Word 内核刷字体
    doc := olItem.GetInspector.WordEditor
    doc.Content.Font.Name := "Calibri"
    doc.Content.Font.Size := 12
return
 
; ===========================================================
; Alt + W : Well Received (Reply All + 强制 12号字)
; ===========================================================
!w::
    try {
        olApp := ComObjActive("Outlook.Application")
        try {
            SelItem := olApp.ActiveExplorer.Selection.Item(1)
            olItem := SelItem.ReplyAll() 
        } catch {
            olItem := olApp.CreateItem(0)
        }
    } catch {
        MsgBox, 请确保 Outlook 已经打开。
        return
    }
 
    olItem.Display
 
    WContent := "
    (
    <p>Good day,</p>
    <p>Well received with thx.</p>
    <p>Have a good day/ Bonne journée</p>
    )"
 
    olItem.HTMLBody := WContent . olItem.HTMLBody
 
    ; 强制调用 Word 内核刷字体
    doc := olItem.GetInspector.WordEditor
    doc.Content.Font.Name := "Calibri"
    doc.Content.Font.Size := 12
return
 
#IfWinActive
