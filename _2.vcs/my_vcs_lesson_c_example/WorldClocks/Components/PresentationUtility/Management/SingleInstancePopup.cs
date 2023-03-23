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

namespace BinaryComponents.PresentationUtility.Management
{
	public static class SingleInstancePopup<T> where T : Window, new()
	{
		public static void Show()
		{
			if( _window != null )
			{
				_window.Focus();
				_window.Activate();
				return;
			}

			_window = new T();
			_window.Closing += new System.ComponentModel.CancelEventHandler( _window_Closing );
			_window.Deactivated += new EventHandler( _window_Deactivated );
			_window.LostFocus += new RoutedEventHandler( _window_LostFocus );

			_window.Show();
			_window.Activate();
		}

		private static void _window_LostFocus( object sender, RoutedEventArgs e )
		{
			DestroyWindow( true );
		}

		private static void _window_Deactivated( object sender, EventArgs e )
		{
			DestroyWindow( true );
		}

		private static void _window_Closing( object sender, System.ComponentModel.CancelEventArgs e )
		{
			DestroyWindow( false );
		}

		private static void DestroyWindow( bool close )
		{
			if( _window != null )
			{
				_window.LostFocus -= new RoutedEventHandler( _window_LostFocus );
				_window.Deactivated -= new EventHandler( _window_Deactivated );
				_window.Closing -= new System.ComponentModel.CancelEventHandler( _window_Closing );

				if( close )
				{
					_window.Close();
				}

				_window = null;
			}
		}

		private static T _window;
	}
}
