Sub URL()
'
' URL Macro
' Transfer url texts to clickable urls
' could also use Range("A1").CurrentRegion.Cells or similar
'
Dim cell As Range: For Each cell In Selection.Cells
    If Left(cell.Value, 7) = "http://" Or Left(cell.Value, 8) = "https://" Or Left(cell.Value, 6) = "ftp://" Then
        Call cell.Hyperlinks.Add(cell, cell.Value)
    End If
Next cell

End Sub