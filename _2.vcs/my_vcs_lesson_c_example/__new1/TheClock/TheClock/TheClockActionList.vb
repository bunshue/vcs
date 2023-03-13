Public Class TheClockActionList
    Inherits DesignerActionList

    Private myClock As TheClock
    Private designerActionUISvc As DesignerActionUIService = Nothing

    Public Sub New(ByVal component As IComponent)

        MyBase.New(component)
        Me.myClock = component

        Me.designerActionUISvc = _
        CType(GetService(GetType(System.ComponentModel.Design.DesignerActionUIService)), _
        System.ComponentModel.Design.DesignerActionUIService)
    End Sub

    Private Function GetPropertyByName(ByVal propName As String) _
    As PropertyDescriptor
        Dim prop As PropertyDescriptor
        prop = TypeDescriptor.GetProperties(myClock)(propName)
        If prop Is Nothing Then
            Throw New ArgumentException( _
            "Matching TheClock property not found!", propName)
        Else
            Return prop
        End If
    End Function

#Region "Component Properties"
    Public Property [Text]() As String
        Get
            Return myClock.Text
        End Get
        Set(ByVal value As String)
            GetPropertyByName("Text").SetValue(myClock, value)
        End Set
    End Property

    Public Property Style() As TheClock.Styles
        Get
            Return myClock.Style
        End Get
        Set(ByVal value As TheClock.Styles)
            GetPropertyByName("Style").SetValue(myClock, value)
        End Set
    End Property

    Public Property SecondTick() As TheClock.SecondTicks
        Get
            Return myClock.SecondTick
        End Get
        Set(ByVal value As TheClock.SecondTicks)
            GetPropertyByName("SecondTick").SetValue(myClock, value)
        End Set
    End Property

    Public Property ShowSecond() As Boolean
        Get
            Return myClock.ShowSecond
        End Get
        Set(ByVal value As Boolean)
            GetPropertyByName("ShowSecond").SetValue(myClock, value)
        End Set
    End Property

    'Reserved for future use
    'Public Property AdvancedMode() As Boolean
    '    Get
    '        Return myClock.AdvancedMode
    '    End Get
    '    Set(ByVal value As Boolean)
    '        GetPropertyByName("AdvancedMode").SetValue(myClock, value)
    '    End Set
    'End Property

    Public Property EnableFadeFocus() As Boolean
        Get
            Return myClock.EnableFadeFocus
        End Get
        Set(ByVal value As Boolean)
            GetPropertyByName("EnableFadeFocus").SetValue(myClock, value)
        End Set
    End Property
#End Region

#Region "Procedures"
    Public Sub TimeZoneSettings()
        Dim frmSetting As New TimezoneForm
        If frmSetting.ShowDialog = DialogResult.OK Then
            GetPropertyByName("ClockSpan").SetValue(myClock, frmSetting.NewSpan)
        End If
    End Sub
#End Region

    Public Overrides Function GetSortedActionItems() _
    As DesignerActionItemCollection

        Dim items As New DesignerActionItemCollection()

        items.Add(New DesignerActionHeaderItem("Appearance"))
        items.Add(New DesignerActionHeaderItem("Features"))

        items.Add( _
        New DesignerActionPropertyItem( _
        "Text", _
        "Text", _
        "Appearance", _
        "Sets the display text."))

        items.Add( _
        New DesignerActionPropertyItem( _
        "SecondTick", _
        "Second Tick", _
        "Appearance", _
        "Sets second tick style."))

        items.Add( _
        New DesignerActionPropertyItem( _
        "Style", _
        "Style", _
        "Appearance", _
        "Sets analog style."))

        items.Add( _
        New DesignerActionPropertyItem( _
        "ShowSecond", _
        "Show Second", _
        "Features", _
        "Display second's hand."))

        'Reserved for future use
        'items.Add( _
        'New DesignerActionPropertyItem( _
        '"AdvancedMode", _
        '"Advanced Mode", _
        '"Features", _
        '"Enable Advanced mode."))

        items.Add( _
        New DesignerActionPropertyItem( _
        "EnableFadeFocus", _
        "Fade Focus", _
        "Features", _
        "Enable fade In and out on focus."))

        items.Add( _
        New System.ComponentModel.Design.DesignerActionMethodItem( _
        Me, _
        "TimeZoneSettings", _
        "Timezone Settings...", _
        "Features", _
        "Select a new timezone"))

        Return items
    End Function
End Class
