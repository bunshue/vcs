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
using System.Collections.ObjectModel;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Shapes;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Controls.Primitives;
using System.Windows.Media.Animation;

namespace BinaryComponents.WorldClocks.Windows
{
	public partial class MainWindow : BinaryComponents.PresentationUtility.Controls.FadeInOutWindow
	{
		public MainWindow()
		{
			InitializeComponent();

			_stack.Margin = new Thickness( _expandSide, _expandTop, _expandSide - _spacing, 4 );

			UpdateForTimeInfos();

			Left = SystemParameters.WorkArea.Right - Width;
			Top = SystemParameters.WorkArea.Bottom - Height - 10;
		}

		private Data.TimeInfo[] TimeInfos
		{
			get
			{
				App app = (App) App.Current;

				return app.Settings.TimeInfos.ToArray();
			}
		}

		private void UpdateForTimeInfos()
		{
			Size thumbnailSize = GetThumbnailSize();

			Data.TimeInfo[] timeInfos = TimeInfos;

			Width = thumbnailSize.Width * timeInfos.Length + _expandSide * 2;
			Height = thumbnailSize.Height + _expandTop;

			_stack.Children.Clear();

			for( int i = 0; i < timeInfos.Length; ++i )
			{
				Data.TimeInfo ti = timeInfos[i];
				Controls.ClockDisplay display = new Controls.ClockDisplay();

				display.TimeInfo = ti;
				display.Margin = new Thickness( 0, 0, _spacing, 0 );

				_stack.Children.Add( display );
			}
		}

		private Size GetThumbnailSize()
		{
			double screen = SystemParameters.PrimaryScreenWidth * 0.75;
			double size = 180;

			if( size * TimeInfos.Length > screen )
			{
				size = screen / TimeInfos.Length;
			}

			return new Size( size * 0.87, size );
		}

		private const double _spacing = 10;
		private const double _expandSide = 20;
		private const double _expandTop = 100;
	}
}
