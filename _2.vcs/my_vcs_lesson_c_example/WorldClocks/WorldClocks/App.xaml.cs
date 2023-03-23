/////////////////////////////////////////////////////////////////////////////
//
// (c) 2007 BinaryComponents Ltd.  All Rights Reserved.
//
// http://www.binarycomponents.com/
//
/////////////////////////////////////////////////////////////////////////////

using System;
using System.Configuration;
using System.Data;
using System.Windows;
using System.Xml;
using System.IO;
using System.Reflection;
using System.Windows.Media.Imaging;

namespace BinaryComponents.WorldClocks
{
	public partial class App : Application
	{
		public App()
		{
			Assembly assembly = Assembly.GetExecutingAssembly();
			Stream iconStream = assembly.GetManifestResourceStream( "BinaryComponents.WorldClocks.Resources.Icons.WorldClocksTray.ico" );
			System.Drawing.Icon icon = new System.Drawing.Icon( iconStream, new System.Drawing.Size( 16, 16 ) );

			_notifyIcon.Icon = icon;
			_notifyIcon.Visible = true;
			_notifyIcon.ContextMenuStrip = CreateContextMenuStrip();

			_notifyIcon.MouseClick += new System.Windows.Forms.MouseEventHandler( _notifyIcon_MouseClick );
		}

		public Data.Settings Settings
		{
			get
			{
				return _settings;
			}
		}

		protected override void OnExit( ExitEventArgs e )
		{
			base.OnExit( e );

			_notifyIcon.MouseClick -= new System.Windows.Forms.MouseEventHandler( _notifyIcon_MouseClick );
			_notifyIcon.Visible = false;
			_notifyIcon.Dispose();

			_settings.Dispose();
		}

		private void _notifyIcon_MouseClick( object sender, System.Windows.Forms.MouseEventArgs e )
		{
			if( e.Button == System.Windows.Forms.MouseButtons.Left )
			{
				DisplayMainWindow();
			}
		}

		private void DisplayMainWindow()
		{
			PresentationUtility.Management.SingleInstancePopup<WorldClocks.Windows.MainWindow>.Show();
		}

		private System.Windows.Forms.ContextMenuStrip CreateContextMenuStrip()
		{
			System.Windows.Forms.ContextMenuStrip contextMenuStrip = new System.Windows.Forms.ContextMenuStrip();

			System.Windows.Forms.ToolStripItem openItem = contextMenuStrip.Items.Add( "Open" );

			openItem.Font = new System.Drawing.Font( openItem.Font, System.Drawing.FontStyle.Bold );
			openItem.Click += new EventHandler( ContextMenuStrip_OpenItem_Click );

			System.Windows.Forms.ToolStripItem settingsItem = contextMenuStrip.Items.Add( "Settings" );

			settingsItem.Click += new EventHandler( ContextMenuStrip_SettingsItem_Click );

			System.Windows.Forms.ToolStripItem exitItem = contextMenuStrip.Items.Add( "Exit" );

			exitItem.Click += new EventHandler( ContextMenuStrip_ExitItem_Click );

			return contextMenuStrip;
		}

		private void ContextMenuStrip_OpenItem_Click( object sender, EventArgs e )
		{
			DisplayMainWindow();
		}

		private void ContextMenuStrip_SettingsItem_Click( object sender, EventArgs e )
		{
			PresentationUtility.Management.SingleInstanceWindow<WorldClocks.Windows.SettingsWindow>.ShowDialog();
		}

		private void ContextMenuStrip_ExitItem_Click( object sender, EventArgs e )
		{
			Shutdown();
		}

		private Data.Settings _settings = new WorldClocks.Data.Settings();
		private System.Windows.Forms.NotifyIcon _notifyIcon = new System.Windows.Forms.NotifyIcon();
	}
}
