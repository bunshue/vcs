/////////////////////////////////////////////////////////////////////////////
//
// (c) 2007 BinaryComponents Ltd.  All Rights Reserved.
//
// http://www.binarycomponents.com/
//
/////////////////////////////////////////////////////////////////////////////

using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Windows.Threading;

namespace BinaryComponents.WorldClocks.Controls
{
	public partial class Clock : System.Windows.Controls.UserControl
	{
		public Clock()
		{
			InitializeComponent();

			_canvas.DataContext = this;

			_timer = new DispatcherTimer();
			_timer.Interval = new TimeSpan( 0, 0, 0, 0, 100 );
			_timer.Tick += new EventHandler( _timer_Tick );
			_timer.Start();
		}

		static Clock()
		{
			TimeInfoProperty = DependencyProperty.Register
				( "TimeInfo", typeof( Data.TimeInfo ), typeof( Clock )
				, new FrameworkPropertyMetadata( null, FrameworkPropertyMetadataOptions.AffectsRender ) );

			HourAngleProperty = DependencyProperty.Register
				( "HourAngle", typeof( double ), typeof( Clock )
				, new FrameworkPropertyMetadata( 0.0, FrameworkPropertyMetadataOptions.AffectsRender ) );
			MinuteAngleProperty = DependencyProperty.Register
				( "MinuteAngle", typeof( double ), typeof( Clock )
				, new FrameworkPropertyMetadata( 0.0, FrameworkPropertyMetadataOptions.AffectsRender ) );
			SecondAngleProperty = DependencyProperty.Register
				( "SecondAngle", typeof( double ), typeof( Clock )
				, new FrameworkPropertyMetadata( 0.0, FrameworkPropertyMetadataOptions.AffectsRender ) );
		}

		public Data.TimeInfo TimeInfo
		{
			get
			{
				return (Data.TimeInfo) GetValue( TimeInfoProperty );
			}
			set
			{
				SetValue( TimeInfoProperty, value );
			}
		}

		public double HourAngle
		{
			get
			{
				return (double) GetValue( HourAngleProperty );
			}
			set
			{
				SetValue( HourAngleProperty, value );
			}
		}

		public double MinuteAngle
		{
			get
			{
				return (double) GetValue( MinuteAngleProperty );
			}
			set
			{
				SetValue( MinuteAngleProperty, value );
			}
		}

		public double SecondAngle
		{
			get
			{
				return (double) GetValue( SecondAngleProperty );
			}
			set
			{
				SetValue( SecondAngleProperty, value );
			}
		}

		protected override void OnInitialized( EventArgs e )
		{
			base.OnInitialized( e );

			for( int i = 0; i < 60; ++i )
			{
				Rectangle marker = new Rectangle();

				if( ( i % 5 ) == 0 )
				{
					marker.Width = 3;
					marker.Height = 8;
					marker.Fill = new SolidColorBrush( Color.FromArgb( 0xe0, 0xff, 0xff, 0xff ) );
					marker.Stroke = new SolidColorBrush( Color.FromArgb( 0x80, 0x33, 0x33, 0x33 ) );
					marker.StrokeThickness = 0.5;
				}
				else
				{
					marker.Width = 0.5;
					marker.Height = 3;
					marker.Fill = new SolidColorBrush( Color.FromArgb( 0x80, 0xff, 0xff, 0xff ) );
					marker.Stroke = null;
					marker.StrokeThickness = 0;
				}

				TransformGroup transforms = new TransformGroup();

				transforms.Children.Add( new TranslateTransform( -( marker.Width / 2 ), marker.Width / 2 - 40 - marker.Height ) );
				transforms.Children.Add( new RotateTransform( i * 6 ) );
				transforms.Children.Add( new TranslateTransform( 50, 50 ) );

				marker.RenderTransform = transforms;

				_markersCanvas.Children.Add( marker );
			}

			for( int i = 1; i <= 12; ++i )
			{
				TextBlock tb = new TextBlock();

				tb.Text = i.ToString();
				tb.TextAlignment = TextAlignment.Center;
				tb.RenderTransformOrigin = new Point( 1, 1 );
				tb.Foreground = Brushes.White;
				tb.FontSize = 4;

				tb.RenderTransform = new ScaleTransform( 2, 2 );

				double r = 34;
				double angle = Math.PI * i * 30.0 / 180.0;
				double x = Math.Sin( angle ) * r + 50, y = -Math.Cos( angle ) * r + 50;

				Canvas.SetLeft( tb, x );
				Canvas.SetTop( tb, y );

				_markersCanvas.Children.Add( tb );
			}
		}

		private void _timer_Tick( object sender, EventArgs e )
		{
			Data.TimeInfo ti = TimeInfo;

			if( ti == null )
			{
				HourAngle = MinuteAngle = SecondAngle = 0;
			}
			else
			{
				double hour = ti.GetAdjusted( DateTime.UtcNow ).Hour;
				double minute = ti.GetAdjusted( DateTime.UtcNow ).Minute;
				double second = ti.GetAdjusted( DateTime.UtcNow ).Second;

				double hourAngle = 30 * hour + minute / 2 + second / 120;
				double minuteAngle = 6 * minute + second / 10;
				double secondAngle = 6 * second;

				HourAngle = hourAngle;
				MinuteAngle = minuteAngle;
				SecondAngle = secondAngle;
			}
		}

		public static DependencyProperty TimeInfoProperty, HourAngleProperty, MinuteAngleProperty, SecondAngleProperty;

		private DispatcherTimer _timer = new DispatcherTimer();
	}
}
