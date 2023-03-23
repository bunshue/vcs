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
	/// <summary>
	/// Interaction logic for ClockDisplay.xaml
	/// </summary>
	public partial class ClockDisplay : System.Windows.Controls.UserControl
	{
		public ClockDisplay()
		{
			InitializeComponent();

			_panel.DataContext = this;

			_timer = new DispatcherTimer();
			_timer.Interval = new TimeSpan( 0, 0, 1 );
			_timer.Tick += new EventHandler( _timer_Tick );
			_timer.Start();
		}

		static ClockDisplay()
		{
			TimeInfoProperty = DependencyProperty.Register
				( "TimeInfo", typeof( Data.TimeInfo ), typeof( ClockDisplay )
				, new FrameworkPropertyMetadata( null, FrameworkPropertyMetadataOptions.AffectsRender, TimeInfo_Changed ) );

			NowProperty = DependencyProperty.Register
				( "Now", typeof( DateTime ), typeof( ClockDisplay ) );

			ClockZoomProperty = DependencyProperty.Register
				( "ClockZoom", typeof( double ), typeof( ClockDisplay )
				, new FrameworkPropertyMetadata( 1.0, FrameworkPropertyMetadataOptions.AffectsRender ) );

			TextZoomProperty = DependencyProperty.Register
				( "TextZoom", typeof( double ), typeof( ClockDisplay )
				, new FrameworkPropertyMetadata( 1.0, FrameworkPropertyMetadataOptions.AffectsRender ) );
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

		public DateTime Now
		{
			get
			{
				return (DateTime) GetValue( NowProperty );
			}
			set
			{
				SetValue( NowProperty, value );
			}
		}

		public double ClockZoom
		{
			get
			{
				return (double) GetValue( ClockZoomProperty );
			}
			set
			{
				SetValue( ClockZoomProperty, value );
			}
		}

		public double TextZoom
		{
			get
			{
				return (double) GetValue( TextZoomProperty );
			}
			set
			{
				SetValue( TextZoomProperty, value );
			}
		}

		private void _timer_Tick( object sender, EventArgs e )
		{
			Data.TimeInfo ti = TimeInfo;

			if( ti != null )
			{
				Now = TimeInfo.GetAdjusted( DateTime.UtcNow );
			}
		}

		private static void TimeInfo_Changed( DependencyObject d, DependencyPropertyChangedEventArgs e )
		{
			Data.TimeInfo ti = (Data.TimeInfo) d.GetValue( TimeInfoProperty );

			if( ti != null )
			{
				d.SetValue( NowProperty, ti.GetAdjusted( DateTime.UtcNow ) );
			}
		}

		public static DependencyProperty TimeInfoProperty, NowProperty, ClockZoomProperty, TextZoomProperty;

		private DispatcherTimer _timer;
	}
}
