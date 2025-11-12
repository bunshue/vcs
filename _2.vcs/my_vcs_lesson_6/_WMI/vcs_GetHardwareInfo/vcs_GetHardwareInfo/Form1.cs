using System;
using System.Collections;
using System.Management;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace vcs_GetHardwareInfo
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            cmbxOption.SelectedItem = "Win32_Processor";
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;
            int w = 320;
            int h = 64;
        }

        private void InsertInfo(string Key, ref ListView lst, bool DontInsertNull)
        {
            lst.Items.Clear();

            ManagementObjectSearcher searcher = new ManagementObjectSearcher("select * from " + Key);

            try
            {
                foreach (ManagementObject share in searcher.Get())
                {

                    ListViewGroup grp;
                    try
                    {
                        grp = lst.Groups.Add(share["Name"].ToString(), share["Name"].ToString());
                    }
                    catch
                    {
                        grp = lst.Groups.Add(share.ToString(), share.ToString());
                    }

                    if (share.Properties.Count <= 0)
                    {
                        MessageBox.Show("No Information Available", "No Info", MessageBoxButtons.OK, MessageBoxIcon.Information);
                        return;
                    }

                    foreach (PropertyData PC in share.Properties)
                    {

                        ListViewItem item = new ListViewItem(grp);
                        if (lst.Items.Count % 2 != 0)
                            item.BackColor = Color.White;
                        else
                            item.BackColor = Color.WhiteSmoke;

                        item.Text = PC.Name;

                        if (PC.Value != null && PC.Value.ToString() != "")
                        {
                            switch (PC.Value.GetType().ToString())
                            {
                                case "System.String[]":
                                    string[] str = (string[])PC.Value;

                                    string str2 = "";
                                    foreach (string st in str)
                                        str2 += st + " ";

                                    item.SubItems.Add(str2);

                                    break;
                                case "System.UInt16[]":
                                    ushort[] shortData = (ushort[])PC.Value;


                                    string tstr2 = "";
                                    foreach (ushort st in shortData)
                                        tstr2 += st.ToString() + " ";

                                    item.SubItems.Add(tstr2);

                                    break;

                                default:
                                    item.SubItems.Add(PC.Value.ToString());
                                    break;
                            }
                        }
                        else
                        {
                            if (!DontInsertNull)
                                item.SubItems.Add("No Information available");
                            else
                                continue;
                        }
                        lst.Items.Add(item);
                    }
                }
            }


            catch (Exception exp)
            {
                MessageBox.Show("can't get data because of the followeing error \n" + exp.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }


        }

        private void RemoveNullValue(ref ListView lst)
        {
            foreach (ListViewItem item in lst.Items)
                if (item.SubItems[1].Text == "No Information available")
                    item.Remove();
        }

        private void cmbxNetwork_SelectedIndexChanged(object sender, EventArgs e)
        {
            InsertInfo(cmbxNetwork.SelectedItem.ToString(), ref lstNetwork, chkNetwork.Checked);
        }

        private void cmbxSystemInfo_SelectedIndexChanged(object sender, EventArgs e)
        {
            InsertInfo(cmbxSystemInfo.SelectedItem.ToString(), ref lstSystemInfo, chkSystemInfo.Checked);
        }

        private void cmbxUtility_SelectedIndexChanged(object sender, EventArgs e)
        {
            InsertInfo(cmbxUtility.SelectedItem.ToString(), ref lstUtility, chkUtility.Checked);
        }

        private void cmbxUserAccount_SelectedIndexChanged(object sender, EventArgs e)
        {
            InsertInfo(cmbxUserAccount.SelectedItem.ToString(), ref lstUserAccount, chkUserAccount.Checked);
        }

        private void cmbxStorage_SelectedIndexChanged(object sender, EventArgs e)
        {
            InsertInfo(cmbxStorage.SelectedItem.ToString(), ref lstStorage, chkDataStorage.Checked);
        }

        private void cmbxDeveloper_SelectedIndexChanged(object sender, EventArgs e)
        {
            InsertInfo(cmbxDeveloper.SelectedItem.ToString(), ref lstDeveloper, chkDeveloper.Checked);
        }

        private void cmbxMemory_SelectedIndexChanged(object sender, EventArgs e)
        {
            InsertInfo(cmbxMemory.SelectedItem.ToString(), ref lstMemory, chkMemory.Checked);
        }

        private void chkHardware_CheckedChanged(object sender, EventArgs e)
        {
            if (chkHardware.Checked)
                RemoveNullValue(ref lstDisplayHardware);
            else
                InsertInfo(cmbxOption.SelectedItem.ToString(), ref lstDisplayHardware, chkHardware.Checked);
        }

        private void cmbxOption_SelectedIndexChanged(object sender, EventArgs e)
        {
            InsertInfo(cmbxOption.SelectedItem.ToString(), ref lstDisplayHardware, chkHardware.Checked);
        }

        private void chkDataStorage_CheckedChanged(object sender, EventArgs e)
        {
            if (chkDataStorage.Checked)
                RemoveNullValue(ref lstStorage);
            else
                InsertInfo(cmbxStorage.SelectedItem.ToString(), ref lstStorage, chkDataStorage.Checked);
        }

        private void chkMemory_CheckedChanged(object sender, EventArgs e)
        {
            if (chkMemory.Checked)
                RemoveNullValue(ref lstMemory);
            else
                InsertInfo(cmbxMemory.SelectedItem.ToString(), ref lstStorage, false);
        }

        private void chkSystemInfo_CheckedChanged(object sender, EventArgs e)
        {
            if (chkSystemInfo.Checked)
                RemoveNullValue(ref lstSystemInfo);
            else
                InsertInfo(cmbxSystemInfo.SelectedItem.ToString(), ref lstSystemInfo, false);
        }

        private void chkNetwork_CheckedChanged(object sender, EventArgs e)
        {
            if (chkNetwork.Checked)
                RemoveNullValue(ref lstNetwork);
            else
                InsertInfo(cmbxNetwork.SelectedItem.ToString(), ref lstNetwork, false);
        }

        private void chkUserAccount_CheckedChanged(object sender, EventArgs e)
        {
            if (chkUserAccount.Checked)
                RemoveNullValue(ref lstUserAccount);
            else
                InsertInfo(cmbxUserAccount.SelectedItem.ToString(), ref lstUserAccount, false);
        }

        private void chkDeveloper_CheckedChanged(object sender, EventArgs e)
        {
            if (chkDeveloper.Checked)
                RemoveNullValue(ref lstDeveloper);
            else
                InsertInfo(cmbxDeveloper.SelectedItem.ToString(), ref lstDeveloper, false);
        }

        private void chkUtility_CheckedChanged(object sender, EventArgs e)
        {
            if (chkUtility.Checked)
                RemoveNullValue(ref lstUtility);
            else
                InsertInfo(cmbxUtility.SelectedItem.ToString(), ref lstUtility, false);
        }
    }
}
