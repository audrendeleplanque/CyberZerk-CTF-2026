Attribute VB_Name = "Module1"
' Macro héritée du classeur de suivi des congés (Tricatel)
Private Sub Workbook_Open()
    Dim s As String
    s = Chr(102) & Chr(84) & Chr(78) & Chr(122) & Chr(99) & Chr(106) & Chr(78) & Chr(50) & Chr(77) & Chr(51) & Chr(74) & Chr(102) & Chr(78) & Chr(68) & Chr(90) & Chr(105) & Chr(88) & Chr(51) & Chr(74) & Chr(111) & Chr(89) & Chr(49) & Chr(56) & Chr(122) & Chr(98) & Chr(109) & Chr(107) & Chr(48) & Chr(97) & Chr(71) & Chr(78) & Chr(102) & Chr(98) & Chr(106) & Chr(65) & Chr(120) & Chr(100) & Chr(68) & Chr(82) & Chr(106) & Chr(99) & Chr(51) & Chr(86) & Chr(109) & Chr(89) & Chr(106) & Chr(66) & Chr(122) & Chr(77) & Chr(50) & Chr(82) & Chr(102) & Chr(89) & Chr(87) & Chr(74) & Chr(50) & Chr(101) & Chr(50) & Chr(116) & Chr(121) & Chr(90) & Chr(86) & Chr(112) & Chr(121) & Chr(90) & Chr(87) & Chr(74) & Chr(53) & Chr(81) & Chr(119) & Chr(61) & Chr(61)
    ' s contient une chaîne encodée ; decodee puis inversee a l'execution
    Dim raw As String
    raw = DecodeBase64(s)
    MsgBox StrReverse(raw)
End Sub

Private Function DecodeBase64(ByVal b64 As String) As String
    Dim xml As Object, node As Object
    Set xml = CreateObject("MSXML2.DOMDocument.3.0")
    Set node = xml.createElement("b64")
    node.DataType = "bin.base64"
    node.Text = b64
    DecodeBase64 = StrConv(node.nodeTypedValue, vbUnicode)
End Function
