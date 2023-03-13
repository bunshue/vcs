<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form1
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
        Me.PropertyGrid1 = New System.Windows.Forms.PropertyGrid
        Me.TheClock1 = New TheClock.TheClock
        CType(Me.TheClock1, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Font = New System.Drawing.Font("Microsoft Sans Serif", 9.75!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label1.Location = New System.Drawing.Point(6, 9)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(123, 16)
        Me.Label1.TabIndex = 5
        Me.Label1.Text = "TheClock Property:"
        '
        'PropertyGrid1
        '
        Me.PropertyGrid1.Location = New System.Drawing.Point(12, 32)
        Me.PropertyGrid1.Name = "PropertyGrid1"
        Me.PropertyGrid1.SelectedObject = Me.TheClock1
        Me.PropertyGrid1.Size = New System.Drawing.Size(319, 329)
        Me.PropertyGrid1.TabIndex = 3
        '
        'TheClock1
        '
        Me.TheClock1.AdvancedMode = False
        Me.TheClock1.BackColor = System.Drawing.Color.Transparent
        Me.TheClock1.Location = New System.Drawing.Point(357, 32)
        Me.TheClock1.Name = "TheClock1"
        Me.TheClock1.Size = New System.Drawing.Size(130, 130)
        Me.TheClock1.TabIndex = 6
        Me.TheClock1.Text = "TheClock1"
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(521, 373)
        Me.Controls.Add(Me.TheClock1)
        Me.Controls.Add(Me.Label1)
        Me.Controls.Add(Me.PropertyGrid1)
        Me.Name = "Form1"
        Me.Text = "TheClock Demo"
        CType(Me.TheClock1, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents PropertyGrid1 As System.Windows.Forms.PropertyGrid
    Friend WithEvents TheClock1 As TheClock.TheClock

End Class
