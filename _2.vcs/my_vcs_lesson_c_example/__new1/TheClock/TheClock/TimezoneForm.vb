Imports Microsoft.Win32

Public Class TimezoneForm
    Private Structure TimeZones
        Private _Display As String
        Private _Name As String
        Private _TimeSpan As TimeSpan

        Public Property DisplayName() As String
            Get
                Return _Display
            End Get
            Set(ByVal value As String)
                _Display = value
                Me.ValidateTimeSpan()
            End Set
        End Property

        Public Property Name() As String
            Get
                Return _Name
            End Get
            Set(ByVal value As String)
                _Name = value
            End Set
        End Property

        Public ReadOnly Property Span() As TimeSpan
            Get
                Return _TimeSpan
            End Get
        End Property

        Private Sub ValidateTimeSpan()
            '(GMT+07:00)
            Try
                Select Case Mid(_Display, 5, 1)
                    Case ")" 'GMT
                        _TimeSpan = New TimeSpan(0, 0, 0)
                    Case "+"
                        _TimeSpan = New TimeSpan(CInt(Mid(_Display, 6, 2)), CInt(Mid(_Display, 9, 2)), 0)
                    Case "-"
                        _TimeSpan = New TimeSpan(CInt(Mid(_Display, 6, 2)) * -1, CInt(Mid(_Display, 9, 2)) * -1, 0)
                End Select
            Catch ex As Exception
                'Error. Assumed it GMT
                _TimeSpan = New TimeSpan(0, 0, 0)
            End Try
        End Sub
    End Structure

    Private c As New System.Collections.Generic.List(Of TimeZones)

    Public ReadOnly Property NewSpan() As TimeSpan
        Get
            If chkOwn.Checked = False Then
                Return -TimeZone.CurrentTimeZone.GetUtcOffset(Now) + c.Item(cmbTimezone.SelectedIndex).Span
            Else
                Dim ts As TimeSpan
                If rAscend.Checked = True Then
                    ts = New TimeSpan(CInt(Mid(mtbValue.Text, 1, 2)), CInt(Mid(mtbValue.Text, 4, 2)), 0)
                ElseIf rDecend.Checked = True Then
                    ts = New TimeSpan(CInt(Mid(mtbValue.Text, 1, 2)) * -1, CInt(Mid(mtbValue.Text, 4, 2)) * -1, 0)
                End If
                Return ts
            End If
        End Get
    End Property

    Private Sub GenerateTimezone()
        Dim rk As RegistryKey = Registry.LocalMachine.OpenSubKey("SOFTWARE\" & _
            "Microsoft\Windows NT\CurrentVersion\Time Zones\", True)

        For Each sName As String In rk.GetSubKeyNames
            Dim tempKey As RegistryKey = rk.OpenSubKey(sName, True)

            Dim _tz As New TimeZones
            _tz.DisplayName = CType(tempKey.GetValue("Display"), String)
            _tz.Name = CType(tempKey.GetValue("Std"), String)

            c.Add(_tz)
        Next
    End Sub

    Private Function TimeZoneConvert(ByVal str As String) As String
        If Mid(str, 5, 1) = ")" Then
            Return "0"
        Else
            Return Mid(str, 5, 3) & Mid(str, 9, 2)
        End If
    End Function

    Private Function CompareTimezones(ByVal tz1 As TimeZones, ByVal tz2 As TimeZones) As Integer
        If IsNothing(tz1) Then
            If IsNothing(tz2) Then
                Return 0
            Else
                Return -1
            End If
        Else
            If IsNothing(tz2) Then
                Return 1
            Else
                Dim int1 As Integer = CInt(TimeZoneConvert(tz1.DisplayName))
                Dim int2 As Integer = CInt(TimeZoneConvert(tz2.DisplayName))

                If int1 > int2 Then
                    Return 1
                ElseIf int1 < int2 Then
                    Return -1
                Else
                    Return 0
                End If
            End If
        End If
    End Function

    Private Sub DisplayTimeZones()
        cmbTimezone.Items.Clear()

        c.Sort(AddressOf CompareTimezones)

        For Each tz As TimeZones In c
            cmbTimezone.Items.Add(tz.DisplayName)
            If TimeZone.CurrentTimeZone.StandardName = tz.Name Then
                cmbTimezone.Text = tz.DisplayName
            End If
        Next
    End Sub

    Private Sub chkOwn_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles chkOwn.CheckedChanged
        rAscend.Enabled = chkOwn.Checked
        rDecend.Enabled = chkOwn.Checked
        mtbValue.Enabled = chkOwn.Checked
        cmbTimezone.Enabled = Not chkOwn.Checked
    End Sub

    Private Sub pnlCommand_Paint(ByVal sender As Object, ByVal e As System.Windows.Forms.PaintEventArgs) Handles pnlCommand.Paint
        e.Graphics.DrawLine(New Drawing.Pen(Drawing.Color.FromArgb(224, 224, 224)), 2, 0, Me.ClientSize.Width - 3, 0)
        e.Graphics.DrawLine(Drawing.Pens.White, 2, 1, Me.ClientSize.Width - 3, 1)
    End Sub

    Public Sub New()
        ' This call is required by the Windows Form Designer.
        InitializeComponent()

        ' Add any initialization after the InitializeComponent() call.
        Me.GenerateTimezone()
        Me.DisplayTimeZones()

        lblCurrent.Text = Format(Now, "dddd, MMM d yyyy hh:mm tt")
        lblNext.Text = ""
    End Sub

    Private Sub cmbTimezone_SelectedIndexChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles cmbTimezone.SelectedIndexChanged
        lblNext.Text = Format(DateTime.UtcNow + c.Item(cmbTimezone.SelectedIndex).Span, "dddd, MMM d yyyy hh:mm tt")
    End Sub

    Private Sub btnOk_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles btnOk.Click
        Me.DialogResult = Windows.Forms.DialogResult.OK
    End Sub

    Private Sub btnCancel_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles btnCancel.Click
        Me.DialogResult = Windows.Forms.DialogResult.Cancel
    End Sub
End Class