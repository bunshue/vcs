using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using InTheHand.Net.Sockets;
using System.IO;
using InTheHand.Net.Bluetooth;

namespace vcs_Bluetooth
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void menuItem3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void ConnectService()
        {
            BluetoothClient client = new BluetoothClient();
            BluetoothDeviceInfo[] devices = client.DiscoverDevices();
            BluetoothDeviceInfo device = null;
            foreach (BluetoothDeviceInfo d in devices)
            {
                if (d.DeviceName == "BLUETOOTH_DEVICE")
                {
                    device = d;
                    break;
                }
            }
            if (device != null)
            {
                WriteMessage(String.Format("Name:{0} Address:{1:C}", device.DeviceName, device.DeviceAddress));
                client.Connect(device.DeviceAddress, BluetoothService.SerialPort);
                Stream peerStream = client.GetStream();

                // Create storage for receiving data
                byte[] buffer = new byte[2000];

                // Read Data
                peerStream.Read(buffer, 0, 50);

                // Convert Data to String
                string data = System.Text.ASCIIEncoding.ASCII.GetString(buffer, 0, 50);
                WriteMessage("Receiving data: " + data);

                int i = 0;
                while (true)
                {
                    WriteMessage("Writing: " + i.ToString());
                    byte[] dataBuffer = System.Text.ASCIIEncoding.ASCII.GetBytes(i.ToString());

                    peerStream.Write(dataBuffer, 0, dataBuffer.Length);
                    ++i;
                    if (i >= int.MaxValue)
                    {
                        i = 0;
                    }
                    System.Threading.Thread.Sleep(500);
                }
                // Close network stream
                peerStream.Close();
            }
        }

        public delegate void SafeWinFormsThreadDelegate(string msg);
        private void WriteMessage(string msg)
        {
            SafeWinFormsThreadDelegate d = new SafeWinFormsThreadDelegate(UpdateUi);
            Invoke(d, new object[] { msg });
        }

        private void UpdateUi(string msg)
        {
            if (listBoxMsg.Items.Count > 100)
            {
                listBoxMsg.Items.RemoveAt(0);
            }
            listBoxMsg.SelectedIndex = listBoxMsg.Items.Add(msg);
        }

        private void menuItem5_Click(object sender, EventArgs e)
        {
            DisplayBluetoothRadio();
            ConnectService();
        }


        private void menuItem4_Click(object sender, EventArgs e)
        {
            DisplayBluetoothRadio();
            StartService();
        }

        public void DisplayBluetoothRadio()
        {
            BluetoothRadio myRadio = BluetoothRadio.PrimaryRadio;
            if (myRadio == null)
            {
                WriteMessage("No radio hardware or unsupported software stack");
                return;
            }
            // Warning: LocalAddress is null if the radio is powered-off.
            WriteMessage(String.Format("* Radio, address: {0:C}", myRadio.LocalAddress));
            WriteMessage("Mode: " + myRadio.Mode.ToString());
            WriteMessage("Name: " + myRadio.Name + ", LmpSubversion: " + myRadio.LmpSubversion);
            WriteMessage("ClassOfDevice: " + myRadio.ClassOfDevice.ToString() + ", device: " + myRadio.ClassOfDevice.Device.ToString() + " / service: " + myRadio.ClassOfDevice.Service.ToString());

            // Enable discoverable mode
            myRadio.Mode = RadioMode.Discoverable;
            WriteMessage("Radio Mode now: " + myRadio.Mode.ToString());
        }

        private void StartService()
        {
            BluetoothListener listener = new BluetoothListener(BluetoothService.SerialPort);
            listener.Start();
            WriteMessage("Service started!");
            BluetoothClient client = listener.AcceptBluetoothClient();
            WriteMessage("Got a request!");

            Stream peerStream = client.GetStream();

            string dataToSend = "Hello from service!";

            // Convert dataToSend into a byte array
            byte[] dataBuffer = System.Text.ASCIIEncoding.ASCII.GetBytes(dataToSend);

            // Output data to stream
            peerStream.Write(dataBuffer, 0, dataBuffer.Length);

            byte[] buffer = new byte[2000];
            while (true)
            {
                if (peerStream.CanRead)
                {
                    peerStream.Read(buffer, 0, 50);
                    string data = System.Text.ASCIIEncoding.ASCII.GetString(buffer, 0, 50);
                    WriteMessage("Receiving data: " + data);
                }
            }
        }
    }
}
