using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace howto_skyline_problem
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private Rectangle[] Buildings = null;
        private Point[] Skyline = null;

        private void btnGo_Click(object sender, EventArgs e)
        {
            // Create random buildings.
            const int margin = 10;
            int wid = picCanvas.ClientSize.Width;
            int hgt = picCanvas.ClientSize.Height;
            int xmin = margin;
            int xmax = wid - margin;
            int basey = hgt - margin;
            int min_hgt = margin;
            int max_hgt = hgt - 2 * margin;
            int min_wid = margin;
            int max_wid = (wid - 2 * margin) / 4;

            int num_buildings = int.Parse(txtNumBuildings.Text);
            Buildings = new Rectangle[num_buildings];
            Random rand = new Random();
            for (int i = 0; i < num_buildings; i++)
            {
                const int block_size = 10;
                int width = rand.Next(min_wid, max_wid + 1);
                width = block_size * (int)(width / block_size);
                if (width < block_size) width = block_size;

                int height = rand.Next(min_hgt, max_hgt + 1);
                height = block_size * (int)(height / block_size);
                if (height < block_size) height = block_size;

                int x = rand.Next(xmin, xmax - width + 1);
                int y = basey - height;

                Buildings[i] = new Rectangle(x, y, width, height);
            }

            // Find the skyline.
            Skyline = FindSkyline(Buildings).ToArray();

            // Redraw.
            picCanvas.Refresh();
        }

        // Draw the buildings and skyline.
        private void picCanvas_Paint(object sender, PaintEventArgs e)
        {
            if (Buildings == null) return;
            e.Graphics.Clear(picCanvas.BackColor);

            // Draw the skyline.
            using (Pen pen = new Pen(Color.Black, 5))
            {
                e.Graphics.DrawLines(pen, Skyline);
            }

            // Draw the buildings.
            using (Brush brush = new SolidBrush(Color.FromArgb(128, Color.LightBlue)))
            {
                foreach (Rectangle building in Buildings)
                {
                    e.Graphics.FillRectangle(brush, building);
                    e.Graphics.DrawRectangle(Pens.Blue, building);
                }
            }
        }

        // Return a skyline point list for the rectangles.
        private List<Point> FindSkyline(Rectangle[] buildings)
        {
            // Create building start and end events.
            int num_buildings = buildings.Length;
            List<BuildingEvent> building_events = new List<BuildingEvent>();
            for (int i = 0; i < num_buildings; i++)
            {
                building_events.Add(new BuildingEvent(
                    buildings[i].X,
                    BuildingEvent.EventTypes.Start, i));
                building_events.Add(new BuildingEvent(
                    buildings[i].Right,
                    BuildingEvent.EventTypes.End, i));
            }

            // Sort the events.
            building_events.Sort();

            // Make a list for the currently active buildings.
            List<Rectangle> active_buildings = new List<Rectangle>();

            // Initially ymin is the building baseline.
            int ground = buildings[0].Bottom;
            int ymin = ground;

            // Make the result list.
            List<Point> results = new List<Point>();
            results.Add(new Point(0, ymin));

            // Process the events.
            int num_events = 2 * num_buildings;
            foreach (BuildingEvent building_event in building_events)
            {
                // Get the building index;
                int building_index = building_event.BuildingIndex;

                // Get the event's X coordinate.
                int event_x = building_event.X;

                // See if it's a start or stop.
                if (building_event.EventType == BuildingEvent.EventTypes.Start)
                {
                    // It's a start.
                    // See if this building is taller
                    // than the currently active one.
                    if (buildings[building_index].Top < ymin)
                    {
                        results.Add(new Point(event_x, ymin));
                        ymin = buildings[building_index].Y;
                        results.Add(new Point(event_x, ymin));
                    }

                    // Add the building to the active list.
                    active_buildings.Add(buildings[building_index]);
                }
                else
                {
                    // It's a stop.
                    // Remove the building from the active list.
                    active_buildings.Remove(buildings[building_index]);

                    // See if this building was the tallest.
                    if (buildings[building_index].Top <= ymin)
                    {
                        // This building was tallest.
                        // Mark this point.
                        results.Add(new Point(event_x, ymin));

                        // Find the new tallest active building.
                        if (active_buildings.Count == 0) ymin = ground;
                        else
                        {
                            ymin = active_buildings[0].Top;
                            for (int j = 1; j < active_buildings.Count; j++)
                            {
                                if (ymin > active_buildings[j].Top)
                                    ymin = active_buildings[j].Top;
                            }
                        }

                        // Mark this point.
                        results.Add(new Point(event_x, ymin));
                    }
                }
            }

            // Add a final point off to the right.
            results.Add(new Point(10000, ground));

            return results;
        }
    }
}
