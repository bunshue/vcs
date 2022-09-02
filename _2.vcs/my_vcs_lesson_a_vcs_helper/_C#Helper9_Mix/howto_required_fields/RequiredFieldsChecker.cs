using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics;
using System.Linq;
using System.Text;

using System.Windows.Forms;
using System.Drawing;

namespace howto_required_fields
{
    [System.Drawing.ToolboxBitmap("RequiredTextBox_Tool.bmp")]
    [ProvideProperty("MissingBackColor", "System.Windows.Forms.TextBox")]
    public partial class RequiredFieldsChecker : Component, IExtenderProvider
    {
        public RequiredFieldsChecker()
        {
            InitializeComponent();
        }

        public RequiredFieldsChecker(IContainer container)
        {
            container.Add(this);

            InitializeComponent();
        }

        #region IExtenderProvider Members

        // We can only extend TextBoxes.
        public bool CanExtend(object extendee)
        {
            return (extendee is TextBox);
        }

        // The list of our clients and their colors.
        private List<TextBox> Clients =
            new List<TextBox>();
        private Dictionary<TextBox, Color> MissingColors =
            new Dictionary<TextBox, Color>();
        private Dictionary<TextBox, Color> PresentColors =
            new Dictionary<TextBox, Color>();

        // Implement the MissingBackColor extension property.
        // Return this client's MissingBackColor value.
        [Category("Appearance")]
        [DefaultValue(null)]
        public Color? GetMissingBackColor(TextBox client)
        {
            // Return the control's MissingBackColor if it exists.
            if (MissingColors.ContainsKey(client))
                return MissingColors[client];
            return null;
        }

        // Set this control's MissingBackColor.
        [Category("Appearance")]
        [DefaultValue(null)]
        public void SetMissingBackColor(TextBox client,
            Color? missing_back_color)
        {
            if (missing_back_color.HasValue)
            {
                // Save the client's colors.
                MissingColors[client] = missing_back_color.Value;
                PresentColors[client] = client.BackColor;

                // If the control isn't already
                // in our client list, add it.
                if (!Clients.Contains(client))
                {
                    Clients.Add(client);
                    client.Validating += Client_Validating;
                }
            }
            else
            {
                // If the client is in our client list, remove it.
                if (Clients.Contains(client))
                {
                    Clients.Remove(client);
                    MissingColors.Remove(client);
                    PresentColors.Remove(client);
                    client.Validating -= Client_Validating;
                }
            }
        }

        // Display the appropriate BackColor.
        private void Client_Validating(object sender, CancelEventArgs e)
        {
            ValidateClient(sender as TextBox);
        }
        private void ValidateClient(TextBox client)
        {
            client.BackColor = CorrectColor(client);
        }

        // Return the correct color for a TextBox.
        private Color CorrectColor(TextBox client)
        {
            if (client.Text.Length < 1)
                return MissingColors[client];
            else
                return PresentColors[client];
        }

        #endregion

        // Return the first required field that is blank.
        public TextBox FirstMissingField()
        {
            // Check all of the fields.
            CheckAllFields();

            // See if any clients are blank.
            foreach (TextBox client in Clients)
                if (client.Text.Length == 0) return client;
            return null;
        }

        // Check all clients now. This is useful
        // for initializing background colors.
        public void CheckAllFields()
        {
            foreach (TextBox client in Clients)
                ValidateClient(client);
        }
    }
}
