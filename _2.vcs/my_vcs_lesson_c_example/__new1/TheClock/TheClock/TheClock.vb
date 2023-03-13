#Region "The Clock - Copyright (C) 2007 Michael Rawi"

'The Clock
'Windows Forms Component - NET Framework 2.0
'Copyright (C) 2007 Michael Rawi

'This library is free software; you can redistribute it and/or
'modify it under the terms of the GNU Lesser General Public
'License as published by the Free Software Foundation; either
'version 2.1 of the License, or (at your option) any later version.

'This library is distributed in the hope that it will be useful,
'but WITHOUT ANY WARRANTY; without even the implied warranty of
'MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
'Lesser General Public License for more details.

'Michael Rawi
#End Region
Imports System.DateTime

''' <summary>
''' An analog clock.
''' </summary>
''' <remarks>Created by Michael Rawi</remarks>
<Designer(GetType(TheClockDesigner)), _
Description("A modern analog clock."), _
ToolboxBitmap(GetType(TheClock), "TheClock.png")> _
Public Class TheClock
    Inherits Control
    Implements System.ComponentModel.ISupportInitialize

#Region "Enumeration"
    Public Enum Styles
        Analog = 0
    End Enum

    Public Enum SecondTicks
        [Default] = 0
        Rapid = 1
        Original = 2
    End Enum

    Private Enum FadeStatus
        [In] = 0 'Slowly disappeared - 1.0F~0.5F in 0.5 second by 5 Frame
        Out = 1 'Slowly reappeared
    End Enum
#End Region

#Region "Component Variables"
#Region "Core Variables"
    Private WithEvents _tmrTime As Timer
    Private WithEvents _tmrTick As Timer
    Private WithEvents _tmrLoad As Timer

    Private _imgS As Image
    Private _imgM As Image
    Private _imgH As Image

    Private _angleS As Single
    Private _angleM As Single
    Private _angleH As Single

    Private _ComInfo As New Devices.ComputerInfo
#End Region
#Region "Private Properties"
    Private _secTick As SecondTicks = SecondTicks.Default
    Private _style As Styles
#End Region
#Region "Load Animation"
    Private _loadTimeframe As Single
    Private _loadHAngle As Single
    Private _loadMAngle As Single
    Private _loadSAngle As Single
    Private _loadMod As Integer
#End Region
#Region "Features"
    Private _ShowSecond As Boolean = True
    Private _AdvancedMode As Boolean = False

    Private _FadeFocus As Boolean = True
    Private _FadeStatus As FadeStatus = FadeStatus.Out
    Private _FadeAlpha As Single = 0.5F
    Private WithEvents _tmrFade As Timer

    Private _span As TimeSpan = New TimeSpan(0, 0, 0)
    Private _State As String
#End Region
#End Region

#Region "Properties"
    ''' <summary>
    ''' Get or set the style of the clock.
    ''' </summary>
    ''' <value>Style</value>
    ''' <returns>Current Style</returns>
    ''' <remarks></remarks>
    <Description("Get or set the style of the Clock"), Category("Features"), _
    DefaultValue(GetType(Styles), "Analog")> _
    Public Property Style() As Styles
        Get
            Return _style
        End Get
        Set(ByVal value As Styles)
            _style = value
        End Set
    End Property

    ''' <summary>
    ''' Get or set the second tick's style.
    ''' </summary>
    ''' <value>SecondTick</value>
    ''' <returns>Current SecondTicks</returns>
    ''' <remarks></remarks>
    <Description("Get or set the second tick's style"), Category("Features"), _
    DefaultValue(GetType(SecondTicks), "Default")> _
    Public Property SecondTick() As SecondTicks
        Get
            Return _secTick
        End Get
        Set(ByVal value As SecondTicks)
            _secTick = value
            Select Case value
                Case SecondTicks.Rapid
                    _tmrTime.Interval = 100
                Case Else
                    _tmrTime.Interval = 1000
            End Select
        End Set
    End Property

    ''' <summary>
    ''' Get or set the second visibility.
    ''' </summary>
    ''' <value>Boolean</value>
    ''' <returns>Second visibility</returns>
    ''' <remarks></remarks>
    <Description("Get or set the second visibility"), Category("Features"), _
    DefaultValue(True)> _
    Public Property ShowSecond() As Boolean
        Get
            Return _ShowSecond
        End Get
        Set(ByVal value As Boolean)
            _ShowSecond = value
        End Set
    End Property

    ''' <summary>
    ''' Enable advanced mode. This feature has not ready yet
    ''' </summary>
    ''' <value>Boolean</value>
    ''' <returns>AdvancedMode</returns>
    ''' <remarks></remarks>
    <Browsable(False)> _
    Public Property AdvancedMode() As Boolean
        Get
            Return _AdvancedMode
        End Get
        Set(ByVal value As Boolean)
            _AdvancedMode = value
        End Set
    End Property

    ''' <summary>
    ''' Enable fade focus effect.
    ''' </summary>
    ''' <value>Boolean</value>
    ''' <returns>Curent fadefocus effect</returns>
    ''' <remarks></remarks>
    <Description("Enable fade focus effect"), Category("Features"), _
    DefaultValue(True)> _
    Public Property EnableFadeFocus() As Boolean
        Get
            Return _FadeFocus
        End Get
        Set(ByVal value As Boolean)
            _FadeFocus = value
            Me.Refresh()
        End Set
    End Property

    ''' <summary>
    ''' Set clock time span against current time.
    ''' </summary>
    ''' <value>Timespan</value>
    ''' <returns>Current timespan</returns>
    ''' <remarks></remarks>
    <Description("Set clock time span against current time"), Category("Features"), _
    DefaultValue(GetType(TimeSpan), "00:00:00")> _
    Public Property ClockSpan() As TimeSpan
        Get
            Return _span
        End Get
        Set(ByVal value As TimeSpan)
            _span = value
        End Set
    End Property
#End Region

#Region "Overrides Methods"
    Protected Overrides Sub OnSizeChanged(ByVal e As System.EventArgs)
        'MyBase.OnSizeChanged(e) 'Size is readonly
        MyBase.Size = New Size(130, 130)
    End Sub
#End Region

#Region "Draw Surface Area"
#Region "Second"
    Private Sub DrawSecondHand(ByVal g As Graphics, ByVal Angle As Single)
        Dim container As Rectangle
        If Angle <> 180 Then
            container = New Rectangle(-6, -64, 13, 129)
        Else
            If _ComInfo.OSVersion.StartsWith("5.1") Then
                container = New Rectangle(-7, -65, 13, 129) 'This works on XP
            Else
                container = New Rectangle(-6, -64, 13, 129) 'This works on Vista
            End If
        End If

        g.TranslateTransform(64.0F, 65.0F)
        g.RotateTransform(Angle)
        If _FadeFocus Then
            Using ia As New Imaging.ImageAttributes
                Dim cm As New Imaging.ColorMatrix

                cm.Matrix33 = _FadeAlpha
                ia.SetColorMatrix(cm)
                g.DrawImage(_imgS, container, 0, 0, 13, 129, _
                    GraphicsUnit.Pixel, ia)
            End Using
        Else
            g.DrawImage(_imgS, container)
        End If
        'g.DrawImage(_imgS, container)
        g.ResetTransform()
    End Sub
#End Region
#Region "Minute"
    Private Sub DrawMinuteHand(ByVal g As Graphics, ByVal Angle As Single)
        Dim container As Rectangle
        If Angle <> 180 Then
            container = New Rectangle(-6, -64, 13, 129)
        Else
            If _ComInfo.OSVersion.StartsWith("5.1") Then
                container = New Rectangle(-7, -65, 13, 129) 'This works on XP
            Else
                container = New Rectangle(-6, -64, 13, 129) 'This works on Vista
            End If
        End If

        g.TranslateTransform(64.0F, 65.0F)
        g.RotateTransform(Angle)
        If _FadeFocus Then
            Using ia As New Imaging.ImageAttributes
                Dim cm As New Imaging.ColorMatrix

                cm.Matrix33 = _FadeAlpha
                ia.SetColorMatrix(cm)
                g.DrawImage(_imgM, container, 0, 0, 13, 129, _
                    GraphicsUnit.Pixel, ia)
            End Using
        Else
            g.DrawImage(_imgM, container)
        End If

        Using sPen As New Pen(Color.FromArgb(50 - CInt((1.0F - _FadeAlpha) * 50), Color.Black))
            g.SmoothingMode = Drawing2D.SmoothingMode.AntiAlias
            If Angle >= 45 And Angle < 90 Then
                g.DrawLine(sPen, 4, 14, 4, -47)
                g.DrawLine(sPen, 5, 14, 5, -47)
            ElseIf Angle >= 90 And Angle < 135 Then
                g.DrawLine(sPen, 4, 14, 4, -47)
                g.DrawLine(sPen, 5, 14, 5, -47)
                g.DrawLine(sPen, 4, -47, -3, -47)
            ElseIf Angle >= 135 And Angle < 180 Then
                g.DrawLine(sPen, -4, 14, -4, -47)
                g.DrawLine(sPen, 4, -47, -3, -47)
            ElseIf Angle >= 180 And Angle < 225 Then
                g.DrawLine(sPen, -4, 14, -4, -47)
                g.DrawLine(sPen, -5, 14, -5, -47)
                g.DrawLine(sPen, 2, -47, -4, -47)
            ElseIf Angle >= 225 And Angle < 270 Then
                g.DrawLine(sPen, -4, 14, -4, -45)
                g.DrawLine(sPen, -5, 14, -5, -45)
            ElseIf Angle >= 270 And Angle < 315 Then
                g.DrawLine(sPen, -4, 15, -4, -44)
                g.DrawLine(sPen, -5, 15, -5, -44)
                g.DrawLine(sPen, 3, 15, -4, 15)
            ElseIf Angle >= 315 And Angle < 360 Then
                g.DrawLine(sPen, 4, 15, 4, -44)
                g.DrawLine(sPen, 5, 15, 5, -44)
                g.DrawLine(sPen, -3, 15, 4, 15)
            ElseIf Angle >= 0 And Angle < 45 Then
                g.DrawLine(sPen, 4, 15, 4, -47)
                g.DrawLine(sPen, 5, 15, 5, -47)
                g.DrawLine(sPen, -3, 15, 4, 15)
            End If
        End Using
        'g.DrawImage(_imgM, container)
        g.ResetTransform()
    End Sub
#End Region
#Region "Hour"
    Private Sub DrawHourHand(ByVal g As Graphics, ByVal Angle As Single)
        Dim container As Rectangle
        If Angle <> 180 Then
            container = New Rectangle(-6, -64, 13, 129)
        Else
            If _ComInfo.OSVersion.StartsWith("5.1") Then
                container = New Rectangle(-7, -65, 13, 129) 'This works on XP
            Else
                container = New Rectangle(-6, -64, 13, 129) 'This works on Vista
            End If
        End If

        g.TranslateTransform(64.0F, 65.0F)
        g.RotateTransform(Angle)
        If _FadeFocus Then
            Using ia As New Imaging.ImageAttributes
                Dim cm As New Imaging.ColorMatrix

                cm.Matrix33 = _FadeAlpha
                ia.SetColorMatrix(cm)
                g.DrawImage(_imgH, container, 0, 0, 13, 129, _
                    GraphicsUnit.Pixel, ia)
            End Using
        Else
            g.DrawImage(_imgH, container)
        End If
        'g.DrawImage(_imgH, container)

        Using sPen As New Pen(Color.FromArgb(50 - CInt((1.0F - _FadeAlpha) * 50), Color.Black))
            g.SmoothingMode = Drawing2D.SmoothingMode.AntiAlias
            If Angle >= 45 And Angle < 90 Then
                g.DrawLine(sPen, 4, 14, 4, -37)
                g.DrawLine(sPen, 5, 14, 5, -37)
            ElseIf Angle >= 90 And Angle < 135 Then
                g.DrawLine(sPen, 4, 14, 4, -37)
                g.DrawLine(sPen, 5, 14, 5, -37)
                g.DrawLine(sPen, 4, -37, -3, -37)
            ElseIf Angle >= 135 And Angle < 180 Then
                g.DrawLine(sPen, -4, 14, -4, -37)
                g.DrawLine(sPen, 4, -37, -3, -37)
            ElseIf Angle >= 180 And Angle < 225 Then
                g.DrawLine(sPen, -4, 14, -4, -37)
                g.DrawLine(sPen, -5, 14, -5, -37)
                g.DrawLine(sPen, 2, -37, -4, -37)
            ElseIf Angle >= 225 And Angle < 270 Then
                g.DrawLine(sPen, -4, 14, -4, -35)
                g.DrawLine(sPen, -5, 14, -5, -35)
            ElseIf Angle >= 270 And Angle < 315 Then
                g.DrawLine(sPen, -4, 15, -4, -34)
                g.DrawLine(sPen, -5, 15, -5, -34)
                g.DrawLine(sPen, 3, 15, -4, 15)
            ElseIf Angle >= 315 And Angle < 360 Then
                g.DrawLine(sPen, 4, 15, 4, -34)
                g.DrawLine(sPen, 5, 15, 5, -34)
                g.DrawLine(sPen, -3, 15, 4, 15)
            ElseIf Angle >= 0 And Angle < 45 Then
                g.DrawLine(sPen, 4, 15, 4, -37)
                g.DrawLine(sPen, 5, 15, 5, -37)
                g.DrawLine(sPen, -3, 15, 4, 15)
            End If
        End Using

        g.ResetTransform()
    End Sub
#End Region
#Region "Background"
    Private Sub DrawBackground(ByVal g As Graphics)
        If _FadeFocus Then
            Using ia As New Imaging.ImageAttributes
                Dim cm As New Imaging.ColorMatrix

                cm.Matrix33 = _FadeAlpha
                ia.SetColorMatrix(cm)
                g.DrawImage(My.Resources.modern, Me.ClientRectangle, 0, 0, 130, 130, _
                    GraphicsUnit.Pixel, ia)
            End Using
        Else
            g.DrawImage(My.Resources.modern, 0, 0)
        End If
    End Sub
#End Region
#End Region

#Region "Constructor"
    Public Sub New()
        Me.SetStyle(ControlStyles.AllPaintingInWmPaint Or ControlStyles.ResizeRedraw Or _
            ControlStyles.SupportsTransparentBackColor Or ControlStyles.OptimizedDoubleBuffer Or _
            ControlStyles.UserPaint, True)

        MyBase.Size = New Size(130, 130)
        MyBase.BackColor = Color.Transparent
        'MyBase.BackgroundImage = My.Resources.modern
        MyBase.Text = ""

        MyClass._style = Styles.Analog
        MyClass._imgS = My.Resources.modern_s
        MyClass._imgM = My.Resources.modern_m
        MyClass._imgH = My.Resources.modern_h

        _tmrTime = New Timer
        _tmrTime.Interval = 1000

        _tmrTick = New Timer
        _tmrTick.Interval = 50

        _tmrFade = New Timer
        _tmrFade.Interval = 100

        _angleH = 0
        _angleM = 0
        Me.Refresh()
    End Sub
#End Region

#Region "Timers"
    Private Sub _tmrTick_Tick(ByVal sender As Object, ByVal e As System.EventArgs) Handles _tmrTick.Tick
        _angleS = Now.Second * 6
        _tmrTick.Stop()
        Me.Refresh()
    End Sub

    Private Sub _tmrTime_Tick(ByVal sender As Object, ByVal e As System.EventArgs) Handles _tmrTime.Tick
        _angleH = ((Now.Hour + _span.Hours) Mod 12) * 30 + (Now.Minute + _span.Minutes) * 6 \ 12
        _angleM = (Now.Minute + _span.Minutes) * 6 + (Now.Second \ 10)

        Select Case _secTick
            Case SecondTicks.Default
                _angleS = Now.Second * 6 + 3
                _tmrTick.Start()
            Case SecondTicks.Original
                _angleS = Now.Second * 6
            Case SecondTicks.Rapid
                _angleS = Now.Second * 6 + Now.Millisecond * 6 \ 1000
        End Select
        Me.Refresh()
    End Sub

    Private Sub _tmrLoad_Tick(ByVal sender As Object, ByVal e As System.EventArgs) Handles _tmrLoad.Tick
        _angleS = Now.Second * 6
        _angleH += _loadHAngle
        _angleM += _loadMAngle
        If _angleM < (Now.Minute + _span.Minutes) * 6 + (Now.Second \ 10) Then
            'Keep it go
            Me.Refresh()
        Else
            _angleH = ((Now.Hour + _span.Hours) Mod 12) * 30 + (Now.Minute + _span.Minutes) * 6 \ 12
            _angleM = (Now.Minute + _span.Minutes) * 6 + (Now.Second \ 10)
            Me.Refresh()

            _tmrLoad.Stop()
            _tmrTime.Start()
        End If
    End Sub

    Private Sub _tmrFade_Tick(ByVal sender As Object, ByVal e As System.EventArgs) Handles _tmrFade.Tick
        Dim modifier As Single
        Select Case _FadeStatus
            Case FadeStatus.In
                modifier = 0.1F
            Case FadeStatus.Out
                modifier = -0.1F
        End Select

        _FadeAlpha += modifier
        Me.Refresh()
        If _FadeAlpha >= 1.0F AndAlso _FadeStatus = FadeStatus.In Then
            _FadeAlpha = 1.0F
            _tmrFade.Stop()
        ElseIf _FadeAlpha <= 0.5F AndAlso _FadeStatus = FadeStatus.Out Then
            _FadeAlpha = 0.5F
            _tmrFade.Stop()
        End If
    End Sub
#End Region

#Region "ISupportInitialize"
    Public Sub BeginInit() Implements System.ComponentModel.ISupportInitialize.BeginInit
        'Not use anything here
    End Sub

    Public Sub EndInit() Implements System.ComponentModel.ISupportInitialize.EndInit
        'Activate the clock
        If Not Me.DesignMode Then
            If ((Now.Hour + _span.Hours) Mod 12) * 30 > (Now.Minute + _span.Minutes) * 6 Then
                _loadMod = 1
            Else
                _loadMod = 3
            End If
            _loadTimeframe = (Now.Minute + _span.Minutes) * 6 + (Now.Second \ 10)
            _loadHAngle = (((Now.Hour + _span.Hours) Mod 12) * 30 + ((Now.Minute + _span.Minutes) * 6 \ 12)) / (_loadTimeframe / 6)
            _loadMAngle = 6

            _tmrLoad = New Timer
            _tmrLoad.Interval = 50
            _angleH = 0
            _angleM = 0
            _angleS = 0
            Me.Refresh()
            _tmrLoad.Start()
        End If
    End Sub
#End Region

#Region "Componet Events"
    Private Sub TheClock_MouseEnter(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.MouseEnter
        _FadeStatus = FadeStatus.In
        _tmrFade.Start()
    End Sub

    Private Sub TheClock_MouseLeave(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.MouseLeave
        _FadeStatus = FadeStatus.Out
        _tmrFade.Start()
    End Sub

    Private Sub AnalogClock_Paint(ByVal sender As Object, ByVal e As System.Windows.Forms.PaintEventArgs) Handles Me.Paint
        'Drawing Main
        Me.DrawBackground(e.Graphics)
        Me.DrawMinuteHand(e.Graphics, _angleM)
        Me.DrawHourHand(e.Graphics, _angleH)

        If _ShowSecond Then
            Me.DrawSecondHand(e.Graphics, _angleS)
        End If
    End Sub
#End Region
End Class
