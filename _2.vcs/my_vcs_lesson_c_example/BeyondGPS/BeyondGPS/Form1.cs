
/* GPS Viewer & KML Logging Application                                      
 * Copyright (C) 2011 Craig Peacock                                           
 * Version 1.0 16th June 2011
 * 
 * This program is free software; you can redistribute it and/or modify it 
 * under the terms of the GNU General Public License as published by the Free 
 * Software Foundation; either version 2 of the License, or (at your option) 
 * any later version.

 * This program is distributed in the hope that it will be useful, but 
 * WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY 
 * or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License 
 * for more details.

 * You should have received a copy of the GNU General Public License along 
 * with this program; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA. */

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.IO.Ports;
using System.Collections;
using Microsoft.Win32;
using System.IO;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class MainForm : Form
    {
        private const uint MAX_SATELLITES = 16;

        bool kml_logging = false;   
        Int32 log_counts;
        TextWriter fs;
        
        Label[] label_SAT = new Label[MAX_SATELLITES];
        Label[] label_ELV = new Label[MAX_SATELLITES];
        Label[] label_AZI = new Label[MAX_SATELLITES];
        Label[] label_SNR = new Label[MAX_SATELLITES];

        public MainForm()
        {
            InitializeComponent();
                   
            Label label_SAT_Header = new Label();
            Label label_ELV_Header = new Label();
            Label label_AZI_Header = new Label();
            Label label_SNR_Header = new Label();

            label_SAT_Header.Text = "ID";
            label_SAT_Header.Height = 12;
            label_SAT_Header.AutoSize = true;
            label_SAT_Header.TextAlign = ContentAlignment.MiddleCenter;
            label_SAT_Header.Location = new Point(50, 20);
            gbSatellites.Controls.Add(label_SAT_Header);

            label_ELV_Header.Text = "Elevation";
            label_ELV_Header.Height = 12;
            label_ELV_Header.AutoSize = true;
            label_ELV_Header.TextAlign = ContentAlignment.MiddleCenter;
            label_ELV_Header.Location = new Point(83, 20);
            gbSatellites.Controls.Add(label_ELV_Header);

            label_AZI_Header.Text = "Azimuth";
            label_AZI_Header.Height = 12;
            label_AZI_Header.AutoSize = true;
            label_AZI_Header.TextAlign = ContentAlignment.MiddleCenter;
            label_AZI_Header.Location = new Point(140, 20);
            gbSatellites.Controls.Add(label_AZI_Header);

            label_SNR_Header.Text = "SN";
            label_SNR_Header.Height = 12;
            label_SNR_Header.AutoSize = true;
            label_SNR_Header.TextAlign = ContentAlignment.MiddleCenter;
            label_SNR_Header.Location = new Point(198, 20);
            gbSatellites.Controls.Add(label_SNR_Header);

            for (int i = 0; i < MAX_SATELLITES; i++)
            {
                label_SAT[i] = new Label();
                label_SAT[i].Text = "";
                label_SAT[i].Height = 12;
                label_SAT[i].AutoSize = true;
                label_SAT[i].TextAlign = ContentAlignment.MiddleCenter;
                label_SAT[i].Location = new Point(50, 43 + (i * 15));
                gbSatellites.Controls.Add(label_SAT[i]);

                label_ELV[i] = new Label();
                label_ELV[i].Text = "";
                label_ELV[i].Height = 12;
                label_ELV[i].AutoSize = true;
                label_ELV[i].TextAlign = ContentAlignment.MiddleCenter;
                label_ELV[i].Location = new Point(100, 43 + (i * 15));
                gbSatellites.Controls.Add(label_ELV[i]);

                label_AZI[i] = new Label();
                label_AZI[i].Text = "";
                label_AZI[i].Height = 12;
                label_AZI[i].AutoSize = true;
                label_AZI[i].TextAlign = ContentAlignment.MiddleCenter;
                label_AZI[i].Location = new Point(150, 43 + (i * 15));
                gbSatellites.Controls.Add(label_AZI[i]);

                label_SNR[i] = new Label();
                label_SNR[i].Text = "";
                label_SNR[i].Height = 12;
                label_SNR[i].AutoSize = true;
                label_SNR[i].TextAlign = ContentAlignment.MiddleCenter;
                label_SNR[i].Location = new Point(200, 43 + (i * 15));
                gbSatellites.Controls.Add(label_SNR[i]);
            }
        }

        private void SetControlText(Control control, string text)
        {
            if (control.InvokeRequired)
            {
                control.BeginInvoke(new Action<Control, string>(SetControlText), new object[] { control, text });
            }
            else
            {
                control.Text = text;
            }
        }

        private string GetControlText(Control control)
        {
            if (control.InvokeRequired)
            {
                // http://blogs.msdn.com/b/bclteam/archive/2006/10/10/top-5-serialport-tips-_5b00_kim-hamilton_5d00_.aspx
                // These functions may be called from the SerialPort DataReceived Event Handler 
                // Any sychronous calls can lead to a deadlock when the serial port is closed and the event 
                // handler is modifing a GUI control.
                // Therefore we use two asychronous calls with a timeout, to prevent deadlocks.
                IAsyncResult ar = control.BeginInvoke(new Func<string>(() => GetControlText(control)));
                for (int i = 0; i <= 20; i++)
                {
                    // If there are a lot of calls from the DataReceived handler when the serial port is 
                    // closing, the delays can add up, resulting in a lag when closing the UI. Therefore
                    // we check if the serial port is closing prior to calling a 1mS sleep.
                    if (SerialPort1.IsOpen) Thread.Sleep(1);
                    if (ar.IsCompleted)
                        return ((string)control.EndInvoke(ar));
                }
                return ("");
            }
            else
            {
                string Text = control.Text;
                return Text;
            }
        }

        private void SetControlFont(Control control, Font font)
        {
            
            if (control.InvokeRequired)
            {
                IAsyncResult ar = control.BeginInvoke(new EventHandler(delegate { control.Font = font; }));
                for (int i = 0; i <= 3; i++)
                {
                    if (SerialPort1.IsOpen) Thread.Sleep(1);
                    if (ar.IsCompleted) break;
                }
            }
            else
            {
                control.Font = font;
            }
        }

        private void Initialise_labels()
        {
            // Set labels to default values
            label_Altitude.Text = "0.000";
            label_Latitude.Text = "0.000000";
            label_Longitude.Text = "0.000000";
            label_Speedkmh.Text = "0.000";

            label_LocalTime.Text = "";
            label_LocalDate.Text = "";

            label_Satellites.Text = "0";

            label_FixStatus.Text = "No Fix";
            label_HDOP1.Text = "0.00";
            label_PDOP.Text = "0.00";
            label_VDOP.Text = "0.00";

            for (int i = 0; i < MAX_SATELLITES; i++)
            {
                label_SAT[i].Text = "-";
                label_ELV[i].Text = "-";
                label_AZI[i].Text = "-";
                label_SNR[i].Text = "-";
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            RegistryKey key;

            key = Registry.CurrentUser.OpenSubKey("Software\\BeyondLogic\\GPS Display");

            // Attempt to retrieve the value X; if null is returned, the value
            // doesn't exist in the registry.
            if (key.GetValue("KML Filename") != null)
                tbxFilename.Text = (string)key.GetValue("KML Filename");

            if (key.GetValue("KML Logging Interval") != null)
                tbxLogInterval.Text = (string)key.GetValue("KML Logging Interval");

            if (key.GetValue("COM Port") != null)
                cbCOMPort.Text = (string)key.GetValue("COM Port");

            if (key.GetValue("Baud Rate") != null)
                cbBaudRate.Text = (string)key.GetValue("Baud Rate");

            key.Close();

            Initialise_labels();

            // Populate list of avaliable COM Ports
            foreach (string s in SerialPort.GetPortNames())
            {
                cbCOMPort.Items.Add(s);
            }

            // Open the COM port
            try
            {
                SerialPort1.PortName = cbCOMPort.Text;
                SerialPort1.BaudRate = Convert.ToInt32(cbBaudRate.Text);
                SerialPort1.Open();
                SerialPort1.DiscardInBuffer();      
                SerialPort1.ReadTimeout = 100; //milliSeconds     
                btnOpenComPort.Text = "Close";
                StatusStrip.Items[0].Text = "Serial Port " + SerialPort1.PortName + " Opened at " + SerialPort1.BaudRate.ToString() + "bps";
            }

            catch (Exception ex)
            {
                StatusStrip.Items[0].Text = ex.Message.ToString();
            }

        }

        private void serialPort1_DataReceived(object sender, SerialDataReceivedEventArgs e)
        {

            try
            {
                String Response = SerialPort1.ReadLine();
                float Minutes;
                Int32 Degrees;

                /* If Latitude and longitude, with time of position fix and status */
                if (String.Compare(Response, 0, "$GPGGA", 0, 6) == 0)
                {
                    try
                    {
                        string[] Array = Response.Split(new char[] { ',' });

                        /* Get and Convert Latitude */
                        Degrees = Convert.ToInt32(Array[2].Substring(0, 2));
                        if (String.Compare(Array[3], "S") == 0) Degrees = -Degrees;
                        Minutes = Convert.ToSingle(Array[2].Substring(2));
                        SetControlText(label_Latitude, Degrees + (Minutes / 60).ToString(".000000"));

                        /* Get and Convert Longitude */
                        Degrees = Convert.ToInt32(Array[4].Substring(0, 3));
                        if (String.Compare(Array[5], "W") == 0) Degrees = -Degrees;
                        Minutes = (float)Convert.ToDouble(Array[4].Substring(3));
                        SetControlText(label_Longitude, Degrees + (Minutes / 60).ToString(".000000"));

                        /* Get number of Satellites used */
                        Int32 SatellitesUsed;
                        SatellitesUsed = Convert.ToInt32(Array[7]);
                        SetControlText(label_Satellites, SatellitesUsed.ToString());

                        /* Get Altitude */
                        SetControlText(label_Altitude, Array[9]);
                    }
                    catch
                    {
                    }
                }

                if (String.Compare(Response, 0, "$GPVTG", 0, 6) == 0)
                {
                    try
                    {
                        string[] Array = Response.Split(new char[] { ',' });
                        SetControlText(label_Speedkmh, Array[7]);
                    }
                    catch
                    {
                    }
                }

                if (String.Compare(Response, 0, "$GPRMC", 0, 6) == 0)
                {
                    try
                    {
                        string[] Array = Response.Split(new char[] { ',' });
                        // Concat the time and year together into one string
                        string DateText = Array[1] + " " + Array[9];

                        // Convert string to DateTime Format
                        DateTime time_UTC;
                        time_UTC = DateTime.SpecifyKind(DateTime.ParseExact(DateText, "HHmmss.ff ddMMyy", System.Globalization.CultureInfo.InvariantCulture), DateTimeKind.Utc);

                        // Convert DateTime to local time
                        DateTime time_local = time_UTC.ToLocalTime();

                        // And display 
                        SetControlText(label_LocalTime, time_local.ToString("hh:mm:ss tt"));
                        SetControlText(label_LocalDate, time_local.ToLongDateString());
                    }
                    catch
                    {
                    }
                }

                // Statistics of GPS satellites in view
                if (String.Compare(Response, 0, "$GPGSV", 0, 6) == 0)
                {
                    try
                        {
                        Int32 SatellitesInView;
                        string[] Array = Response.Split(new char[] { ',', '*' });

                        SatellitesInView = Convert.ToInt32(Array[3]);
                        SetControlText(gbSatellites, "Satellites (" + SatellitesInView + ") ");
                       
                        // Satellites in view come via strings containing the stats of four SVs.
                        // Array[2] holds the string number
                        int i = Convert.ToInt32(Array[2]);
                        i = (i -1) * 4;

                        SetControlText(label_SAT[i], Array[4]);
                        SetControlText(label_ELV[i], Array[5]);
                        SetControlText(label_AZI[i], Array[6]);
                        SetControlText(label_SNR[i], Array[7]);

                        if ((i + 1) < SatellitesInView)
                        {
                            SetControlText(label_SAT[i + 1], Array[8]);
                            SetControlText(label_ELV[i + 1], Array[9]);
                            SetControlText(label_AZI[i + 1], Array[10]);
                            SetControlText(label_SNR[i + 1], Array[11]);
                        }
                        if ((i + 2) < SatellitesInView)
                        {
                            SetControlText(label_SAT[i + 2], Array[12]);
                            SetControlText(label_ELV[i + 2], Array[13]);
                            SetControlText(label_AZI[i + 2], Array[14]);
                            SetControlText(label_SNR[i + 2], Array[15]);
                        }
                                               
                        if ((i + 3) < SatellitesInView)
                        {
                            SetControlText(label_SAT[i + 3], Array[16]);
                            SetControlText(label_ELV[i + 3], Array[17]);
                            SetControlText(label_AZI[i + 3], Array[18]);
                            SetControlText(label_SNR[i + 3], Array[19]);
                        }

                        // Blank out any remaining satellites no longer in view
                        for (i = (SatellitesInView); i <= MAX_SATELLITES; i++)
                        {
                            SetControlText(label_SAT[i], " ");
                            SetControlText(label_ELV[i], " ");
                            SetControlText(label_AZI[i], " ");
                            SetControlText(label_SNR[i], " ");                     
                        }
                    }
                    catch
                    {

                    }
                }

                // GPS DOP and active satellites
                if (String.Compare(Response, 0, "$GPGSA", 0, 6) == 0)
                {
                    try
                    {
                        string[] Array = Response.Split(new char[] { ',', '*' });

                        if (String.Compare(Array[2], "1") == 0)
                            SetControlText(label_FixStatus, "No Fix");

                        if (String.Compare(Array[2], "2") == 0)
                            SetControlText(label_FixStatus, "2D Fix");

                        if (String.Compare(Array[2], "3") == 0)
                            SetControlText(label_FixStatus, "3D Fix");

                        string SAT_ID;

                        // Loop thru each satellite entry to find a match
                        for (uint i = 0; i < (MAX_SATELLITES); i++)
                        {
                            bool match = false;

                            SAT_ID = GetControlText(label_SAT[i]);

                            // Loop thru all the SV ID's used in a position fix
                            for (uint sv_idx = 3; sv_idx < 15; sv_idx++)
                            {
                                if (String.Compare(Array[sv_idx], SAT_ID ) == 0)
                                       match = true;
                            }
                            
                            if (match == true)
                            {
                                // Highlight Satellites in use
                                SetControlFont(label_SAT[i], new Font(FontFamily.GenericSansSerif, (float)8.25, FontStyle.Bold));
                                SetControlFont(label_ELV[i], new Font(FontFamily.GenericSansSerif, (float)8.25, FontStyle.Bold));
                                SetControlFont(label_AZI[i], new Font(FontFamily.GenericSansSerif, (float)8.25, FontStyle.Bold));
                                SetControlFont(label_SNR[i], new Font(FontFamily.GenericSansSerif, (float)8.25, FontStyle.Bold));
                            }
                            else
                            {
                                SetControlFont(label_SAT[i], new Font(FontFamily.GenericSansSerif, (float)8.25, FontStyle.Regular));
                                SetControlFont(label_ELV[i], new Font(FontFamily.GenericSansSerif, (float)8.25, FontStyle.Regular));
                                SetControlFont(label_AZI[i], new Font(FontFamily.GenericSansSerif, (float)8.25, FontStyle.Regular));
                                SetControlFont(label_SNR[i], new Font(FontFamily.GenericSansSerif, (float)8.25, FontStyle.Regular));
                            }
                        }

                        SetControlText(label_PDOP, Array[15]);
                        SetControlText(label_HDOP1, Array[16]);
                        SetControlText(label_VDOP, Array[17]);

                    }
                    catch
                    {
                    }
                }
            }
            catch
            {
            }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            
            SerialPort1.Close();
        
            RegistryKey key;

            key = Registry.CurrentUser.CreateSubKey("Software\\BeyondLogic\\GPS Display");

            // If the return value is null, the key doesn't exist
            if (key == null)
            {
                // The key doesn't exist; create it / open it
                key = Registry.CurrentUser.CreateSubKey("Software\\BeyondLogic\\GPS Display");
            }

            key.SetValue("KML Filename", (string)tbxFilename.Text);
            key.SetValue("KML Logging Interval", (string)tbxLogInterval.Text);
            key.SetValue("COM Port", (string)cbCOMPort.Text);
            key.SetValue("Baud Rate", (string)cbBaudRate.Text);

            key.Close();
        }

        private void button1_Click_2(object sender, EventArgs e)
        {
            if (SerialPort1.IsOpen)
            {
                SerialPort1.Close();
                btnOpenComPort.Text = "Open";
                StatusStrip.Items[0].Text = "Serial Port Closed";
                Initialise_labels();
            }
            else
            {
                try
                {
                    SerialPort1.PortName = cbCOMPort.Text;
                    SerialPort1.BaudRate = Convert.ToInt32(cbBaudRate.Text);
                    SerialPort1.Open();
                    SerialPort1.DiscardInBuffer();  
                    SerialPort1.ReadTimeout = 1000;  
                    btnOpenComPort.Text = "Close";
                    StatusStrip.Items[0].Text = "Serial Port " + SerialPort1.PortName + " Opened at " + SerialPort1.BaudRate.ToString() + "bps";
                }
                catch (Exception ex)
                {
                    StatusStrip.Items[0].Text = ex.Message.ToString();
                }
            }
        }

        private void linkLabel_GoogleEarthPlacemark_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            Form2 CreateKLMForm = new Form2();
            CreateKLMForm.tbLatitude.Text = label_Latitude.Text;
            CreateKLMForm.tbLongitude.Text = label_Longitude.Text;
            CreateKLMForm.ShowDialog();
        }

        private void linkLabel_GoogleMaps_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start("iexplore.exe", "http://maps.google.com/maps/api/staticmap?center=" + label_Latitude.Text + "," + label_Longitude.Text + "&zoom=18&maptype=satellite&size=6000x600&markers=color:blue|label:S|" + label_Latitude.Text + "," + label_Longitude.Text + "&sensor=true");
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start("iexplore.exe", "http://www.beyondlogic.org");
        }

        private void button_logging_Click(object sender, EventArgs e)
        {
            if (!kml_logging) {
                try
                {
                    fs = new StreamWriter(tbxFilename.Text);
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message, "KML Filename");
                    return;
                }
              
                log_counts = 0;
                fs.WriteLine("<?xml version=\"1.0\" encoding=\"UTF-8\"?>");
                fs.WriteLine("<kml xmlns=\"http://www.opengis.net/kml/2.2\">");
                fs.WriteLine("<Document>");

                try
                {
                    Timer_LogInterval.Interval = Convert.ToInt32(tbxLogInterval.Text) * 1000;
                    Timer_LogInterval.Start();
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message, "Timer Value");
                    fs.Close();
                    return;
                }
                kml_logging = true;
                btnLogging.Text = "Stop";
            } else {
                Timer_LogInterval.Stop();
                fs.WriteLine("</Document>");
                fs.WriteLine("</kml>");
                fs.Close();
                kml_logging = false;
                btnLogging.Text = "Start";
            }
        }

        private void Timer_LogInterval_Tick(object sender, EventArgs e)
        {
            log_counts++;
            label_Positions_Recorded.Text = log_counts.ToString();
            fs.WriteLine("  <Placemark>");
            fs.WriteLine("    <name>(" + log_counts.ToString() + ")</name>");
            fs.WriteLine("    <description>Speed " + label_Speedkmh.Text +" km/h\n</description>");
            fs.WriteLine("    <Point>");
            fs.WriteLine("     <coordinates>" + label_Longitude.Text + "," + label_Latitude.Text + ",0</coordinates>");
            fs.WriteLine("    </Point>");
            fs.WriteLine("  </Placemark>");
        }

        private void bttFileName_Click(object sender, EventArgs e)
        {
            SaveFileDlg_Log.Filter = "kml files (*.kml)|*.kml";
            SaveFileDlg_Log.FileName = tbxFilename.Text;
            SaveFileDlg_Log.ShowDialog();
            tbxFilename.Text = SaveFileDlg_Log.FileName;
        }

    }
}
