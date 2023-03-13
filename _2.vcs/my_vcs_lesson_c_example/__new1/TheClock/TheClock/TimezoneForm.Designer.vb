<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class TimezoneForm
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.Label1 = New System.Windows.Forms.Label
        Me.cmbTimezone = New System.Windows.Forms.ComboBox
        Me.Label2 = New System.Windows.Forms.Label
        Me.Label3 = New System.Windows.Forms.Label
        Me.lblCurrent = New System.Windows.Forms.Label
        Me.lblNext = New System.Windows.Forms.Label
        Me.chkOwn = New System.Windows.Forms.CheckBox
        Me.rAscend = New System.Windows.Forms.RadioButton
        Me.rDecend = New System.Windows.Forms.RadioButton
        Me.mtbValue = New System.Windows.Forms.MaskedTextBox
        Me.Label6 = New System.Windows.Forms.Label
        Me.pnlCommand = New System.Windows.Forms.Panel
        Me.btnCancel = New System.Windows.Forms.Button
        Me.btnOk = New System.Windows.Forms.Button
        Me.GroupBox1 = New System.Windows.Forms.GroupBox
        Me.pnlCommand.SuspendLayout()
        Me.GroupBox1.SuspendLayout()
        Me.SuspendLayout()
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(12, 9)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(59, 13)
        Me.Label1.TabIndex = 0
        Me.Label1.Text = "Time zone:"
        '
        'cmbTimezone
        '
        Me.cmbTimezone.Anchor = CType(((System.Windows.Forms.AnchorStyles.Top Or System.Windows.Forms.AnchorStyles.Left) _
                    Or System.Windows.Forms.AnchorStyles.Right), System.Windows.Forms.AnchorStyles)
        Me.cmbTimezone.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
        Me.cmbTimezone.FormattingEnabled = True
        Me.cmbTimezone.Location = New System.Drawing.Point(15, 25)
        Me.cmbTimezone.Name = "cmbTimezone"
        Me.cmbTimezone.Size = New System.Drawing.Size(408, 21)
        Me.cmbTimezone.TabIndex = 1
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Location = New System.Drawing.Point(12, 175)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(92, 13)
        Me.Label2.TabIndex = 2
        Me.Label2.Text = "Current time zone:"
        '
        'Label3
        '
        Me.Label3.AutoSize = True
        Me.Label3.Location = New System.Drawing.Point(24, 197)
        Me.Label3.Name = "Label3"
        Me.Label3.Size = New System.Drawing.Size(80, 13)
        Me.Label3.TabIndex = 3
        Me.Label3.Text = "Netx time zone:"
        '
        'lblCurrent
        '
        Me.lblCurrent.AutoSize = True
        Me.lblCurrent.Location = New System.Drawing.Point(110, 175)
        Me.lblCurrent.Name = "lblCurrent"
        Me.lblCurrent.Size = New System.Drawing.Size(39, 13)
        Me.lblCurrent.TabIndex = 4
        Me.lblCurrent.Text = "Label4"
        '
        'lblNext
        '
        Me.lblNext.AutoSize = True
        Me.lblNext.Location = New System.Drawing.Point(110, 197)
        Me.lblNext.Name = "lblNext"
        Me.lblNext.Size = New System.Drawing.Size(39, 13)
        Me.lblNext.TabIndex = 5
        Me.lblNext.Text = "Label5"
        '
        'chkOwn
        '
        Me.chkOwn.AutoSize = True
        Me.chkOwn.Location = New System.Drawing.Point(6, 0)
        Me.chkOwn.Name = "chkOwn"
        Me.chkOwn.Size = New System.Drawing.Size(118, 17)
        Me.chkOwn.TabIndex = 6
        Me.chkOwn.Text = "Use my own setting"
        Me.chkOwn.UseVisualStyleBackColor = True
        '
        'rAscend
        '
        Me.rAscend.AutoSize = True
        Me.rAscend.Checked = True
        Me.rAscend.Enabled = False
        Me.rAscend.Location = New System.Drawing.Point(24, 19)
        Me.rAscend.Name = "rAscend"
        Me.rAscend.Size = New System.Drawing.Size(61, 17)
        Me.rAscend.TabIndex = 7
        Me.rAscend.TabStop = True
        Me.rAscend.Text = "Ascend"
        Me.rAscend.UseVisualStyleBackColor = True
        '
        'rDecend
        '
        Me.rDecend.AutoSize = True
        Me.rDecend.Enabled = False
        Me.rDecend.Location = New System.Drawing.Point(24, 42)
        Me.rDecend.Name = "rDecend"
        Me.rDecend.Size = New System.Drawing.Size(63, 17)
        Me.rDecend.TabIndex = 8
        Me.rDecend.Text = "Decend"
        Me.rDecend.UseVisualStyleBackColor = True
        '
        'mtbValue
        '
        Me.mtbValue.Enabled = False
        Me.mtbValue.Location = New System.Drawing.Point(64, 71)
        Me.mtbValue.Mask = "90:00"
        Me.mtbValue.Name = "mtbValue"
        Me.mtbValue.Size = New System.Drawing.Size(34, 20)
        Me.mtbValue.TabIndex = 9
        Me.mtbValue.ValidatingType = GetType(Date)
        '
        'Label6
        '
        Me.Label6.AutoSize = True
        Me.Label6.Location = New System.Drawing.Point(21, 74)
        Me.Label6.Name = "Label6"
        Me.Label6.Size = New System.Drawing.Size(37, 13)
        Me.Label6.TabIndex = 10
        Me.Label6.Text = "Value:"
        '
        'pnlCommand
        '
        Me.pnlCommand.BackColor = System.Drawing.SystemColors.Control
        Me.pnlCommand.Controls.Add(Me.btnCancel)
        Me.pnlCommand.Controls.Add(Me.btnOk)
        Me.pnlCommand.Dock = System.Windows.Forms.DockStyle.Bottom
        Me.pnlCommand.Location = New System.Drawing.Point(0, 224)
        Me.pnlCommand.Name = "pnlCommand"
        Me.pnlCommand.Size = New System.Drawing.Size(435, 53)
        Me.pnlCommand.TabIndex = 11
        '
        'btnCancel
        '
        Me.btnCancel.Anchor = CType((System.Windows.Forms.AnchorStyles.Top Or System.Windows.Forms.AnchorStyles.Right), System.Windows.Forms.AnchorStyles)
        Me.btnCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel
        Me.btnCancel.Location = New System.Drawing.Point(348, 15)
        Me.btnCancel.Name = "btnCancel"
        Me.btnCancel.Size = New System.Drawing.Size(75, 23)
        Me.btnCancel.TabIndex = 1
        Me.btnCancel.Text = "Cancel"
        Me.btnCancel.UseVisualStyleBackColor = True
        '
        'btnOk
        '
        Me.btnOk.Anchor = CType((System.Windows.Forms.AnchorStyles.Top Or System.Windows.Forms.AnchorStyles.Right), System.Windows.Forms.AnchorStyles)
        Me.btnOk.Location = New System.Drawing.Point(267, 15)
        Me.btnOk.Name = "btnOk"
        Me.btnOk.Size = New System.Drawing.Size(75, 23)
        Me.btnOk.TabIndex = 0
        Me.btnOk.Text = "Ok"
        Me.btnOk.UseVisualStyleBackColor = True
        '
        'GroupBox1
        '
        Me.GroupBox1.Controls.Add(Me.chkOwn)
        Me.GroupBox1.Controls.Add(Me.rAscend)
        Me.GroupBox1.Controls.Add(Me.rDecend)
        Me.GroupBox1.Controls.Add(Me.mtbValue)
        Me.GroupBox1.Controls.Add(Me.Label6)
        Me.GroupBox1.Location = New System.Drawing.Point(15, 63)
        Me.GroupBox1.Name = "GroupBox1"
        Me.GroupBox1.Size = New System.Drawing.Size(200, 100)
        Me.GroupBox1.TabIndex = 12
        Me.GroupBox1.TabStop = False
        '
        'TimezoneForm
        '
        Me.AcceptButton = Me.btnOk
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.BackColor = System.Drawing.Color.White
        Me.CancelButton = Me.btnCancel
        Me.ClientSize = New System.Drawing.Size(435, 277)
        Me.Controls.Add(Me.GroupBox1)
        Me.Controls.Add(Me.pnlCommand)
        Me.Controls.Add(Me.lblNext)
        Me.Controls.Add(Me.lblCurrent)
        Me.Controls.Add(Me.Label3)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.cmbTimezone)
        Me.Controls.Add(Me.Label1)
        Me.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog
        Me.MaximizeBox = False
        Me.MinimizeBox = False
        Me.Name = "TimezoneForm"
        Me.Text = "Timezone Settings"
        Me.pnlCommand.ResumeLayout(False)
        Me.GroupBox1.ResumeLayout(False)
        Me.GroupBox1.PerformLayout()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents cmbTimezone As System.Windows.Forms.ComboBox
    Friend WithEvents Label2 As System.Windows.Forms.Label
    Friend WithEvents Label3 As System.Windows.Forms.Label
    Friend WithEvents lblCurrent As System.Windows.Forms.Label
    Friend WithEvents lblNext As System.Windows.Forms.Label
    Friend WithEvents chkOwn As System.Windows.Forms.CheckBox
    Friend WithEvents rAscend As System.Windows.Forms.RadioButton
    Friend WithEvents rDecend As System.Windows.Forms.RadioButton
    Friend WithEvents mtbValue As System.Windows.Forms.MaskedTextBox
    Friend WithEvents Label6 As System.Windows.Forms.Label
    Friend WithEvents pnlCommand As System.Windows.Forms.Panel
    Friend WithEvents btnCancel As System.Windows.Forms.Button
    Friend WithEvents btnOk As System.Windows.Forms.Button
    Friend WithEvents GroupBox1 As System.Windows.Forms.GroupBox
End Class
