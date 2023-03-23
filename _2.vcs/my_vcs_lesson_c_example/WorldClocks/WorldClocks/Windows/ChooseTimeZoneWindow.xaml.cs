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
using System.Windows.Shapes;

namespace BinaryComponents.WorldClocks.Windows
{
	/// <summary>
	/// Interaction logic for ChooseTimeZoneWindow.xaml
	/// </summary>

	public partial class ChooseTimeZoneWindow : Window
	{
		public ChooseTimeZoneWindow()
		{
			InitializeComponent();
		}

		public Data.TimeInfo Add( Window owner )
		{
			Owner = owner;
			ShowDialog();

			if( DialogResult.Value )
			{
				TimeZoneInfo tzi = (TimeZoneInfo) _tzCombo.SelectedItem;

				Data.TimeInfo ti = new Data.TimeInfo( tzi );

				if( _descriptionControl.Text.Trim() != string.Empty )
				{
					ti.DisplayName = _descriptionControl.Text.Trim();
				}

				return ti;
			}
			else
			{
				return null;
			}
		}

		public bool Edit( Window owner, Data.TimeInfo ti )
		{
			_tzCombo.SelectedItem = ti.TimeZoneInfo;
			_tzCombo.IsEnabled = false;

			if( ti.IsDisplayNameOverridden )
			{
				_descriptionControl.Text = ti.DisplayName;
			}
			
			Owner = owner;
			ShowDialog();

			if( DialogResult.Value )
			{
				if( _descriptionControl.Text.Trim() != string.Empty )
				{
					ti.DisplayName = _descriptionControl.Text.Trim();
				}

				return true;
			}
			else
			{
				return false;
			}
		}

		protected override void OnInitialized( EventArgs e )
		{
			base.OnInitialized( e );

			var timezones = TimeZoneInfo.GetSystemTimeZones();

			_tzCombo.ItemsSource = timezones;
		}

		private void _okButton_CanExecute( object sender, CanExecuteRoutedEventArgs e )
		{
			e.CanExecute = _tzCombo != null && _tzCombo.SelectedItem != null;
		}

		private void _okButton_OnExecuted( object sender, ExecutedRoutedEventArgs e )
		{
			DialogResult = true;
		}

		private void _tzCombo_SelectionChanged( object sender, SelectionChangedEventArgs e )
		{
			_timeZoneMap.TimeZoneInfo = (TimeZoneInfo) _tzCombo.SelectedItem;
		}

		public readonly static RoutedUICommand Ok = new RoutedUICommand();
	}
}
