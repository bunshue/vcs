/////////////////////////////////////////////////////////////////////////////
//
// (c) 2007 BinaryComponents Ltd.  All Rights Reserved.
//
// http://www.binarycomponents.com/
//
/////////////////////////////////////////////////////////////////////////////

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Media.Animation;

namespace BinaryComponents.PresentationUtility.Controls
{
	public class FadeInOutWindow : Window
	{
		public FadeInOutWindow()
		{
			Loaded += new RoutedEventHandler( FadeInOutWindow_Loaded );
		}

		protected override void OnClosing( System.ComponentModel.CancelEventArgs e )
		{
			base.OnClosing( e );

			if( !_forceClose )
			{
				e.Cancel = true;

				DoubleAnimation animation = new DoubleAnimation( 1, 0, new Duration( new TimeSpan( 0, 0, 0, 0, 300 ) ) );

				animation.Completed += new EventHandler( ClosingAnimation_Completed );

				BeginAnimation( Window.OpacityProperty, animation );
			}
		}

		private void ClosingAnimation_Completed( object sender, EventArgs e )
		{
			_forceClose = true;

			Close();
		}

		private void FadeInOutWindow_Loaded( object sender, RoutedEventArgs e )
		{
			BeginAnimation( Window.OpacityProperty, new DoubleAnimation( 0, 1, new Duration( new TimeSpan( 0, 0, 0, 0, 300 ) ) ) );
		}

		private bool _forceClose;
	}
}
