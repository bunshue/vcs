<System.Security.Permissions.PermissionSetAttribute(System.Security.Permissions.SecurityAction.Demand, Name:="FullTrust")> _
Public Class TheClockDesigner
    Inherits System.Windows.Forms.Design.ControlDesigner

    Private lists As DesignerActionListCollection

    Public Overrides ReadOnly Property ActionLists() _
            As DesignerActionListCollection
        Get
            If lists Is Nothing Then
                lists = New DesignerActionListCollection()
                lists.Add( _
                New TheClockActionList(Me.Component))
            End If
            Return lists
        End Get
    End Property
End Class
