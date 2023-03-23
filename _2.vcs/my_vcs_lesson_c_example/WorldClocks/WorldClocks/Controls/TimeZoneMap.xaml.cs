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
using System.Linq;
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

namespace BinaryComponents.WorldClocks.Controls
{
	/// <summary>
	/// Interaction logic for TimeZoneMap.xaml
	/// </summary>
	public partial class TimeZoneMap : System.Windows.Controls.UserControl
	{
		public TimeZoneMap()
		{
			InitializeComponent();
		}

		static TimeZoneMap()
		{
			TimeZoneInfoProperty = DependencyProperty.Register
				( "TimeZoneInfo", typeof( TimeZoneInfo ), typeof( TimeZoneMap )
				, new FrameworkPropertyMetadata( null, FrameworkPropertyMetadataOptions.AffectsRender, TimeZoneInfo_Changed ) );

			RegisterOverlay( new TimeSpan(), "Z0" );

			for( int i = 1; i <= 10; ++i )
			{
				RegisterOverlay( new TimeSpan( -i, 0, 0 ), string.Format( "L{0}", i ) );
			}
			foreach( int i in new int[] { 3, 9 } )
			{
				RegisterOverlay( new TimeSpan( -i, -30, 0 ), string.Format( "L{0}.5", i ) );
			}
			for( int i = 1; i <= 12; ++i )
			{
				RegisterOverlay( new TimeSpan( i, 0, 0 ), string.Format( "R{0}", i ) );
			}
			foreach( int i in new int[] { 3, 4, 5, 6, 9 } )
			{
				RegisterOverlay( new TimeSpan( i, 30, 0 ), string.Format( "R{0}.5", i ) );
			}
		}

		public TimeZoneInfo TimeZoneInfo
		{
			get
			{
				return (TimeZoneInfo) GetValue( TimeZoneInfoProperty );
			}
			set
			{
				SetValue( TimeZoneInfoProperty, value );
			}
		}

		private static void RegisterOverlay( TimeSpan ts, string name )
		{
			name = string.Format( "pack://application:,,,/Resources/Images/{0}.png", name );

			BitmapSource source = PngBitmapDecoder.Create( new Uri( name ), BitmapCreateOptions.DelayCreation, BitmapCacheOption.OnDemand ).Frames[0]; 

			_images.Add( ts, source );
		}

		private static void TimeZoneInfo_Changed( DependencyObject d, DependencyPropertyChangedEventArgs e )
		{
			TimeZoneMap timeZoneMap = (TimeZoneMap) d;
			TimeZoneInfo tzi = (TimeZoneInfo) e.NewValue;

			if( tzi == null )
			{
				timeZoneMap._overlayImage.Source = null;
			}
			else
			{
				BitmapSource source = null;

				_images.TryGetValue( tzi.BaseUtcOffset, out source );

				timeZoneMap._overlayImage.Source = source;
			}
		}

		public static DependencyProperty TimeZoneInfoProperty;

		private static Dictionary<TimeSpan, BitmapSource> _images = new Dictionary<TimeSpan, BitmapSource>();
	}
}
