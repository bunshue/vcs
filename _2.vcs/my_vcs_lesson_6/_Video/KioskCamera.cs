using AForge.Video.DirectShow;
using Apollo.Kiosk.Hardware.Camera.Interface;
using System;
using System.Drawing;
using System.Linq;

namespace Apollo.Kiosk.Hardware.Camera
{
    public class KioskCamera : IKioskCamera
    {
        FilterInfoCollection USBWebcams;
		VideoCaptureDevice Cam = null;
        VideoCaptureDevice Cam;
        Bitmap lastFrame;
        object locker = new object();
        bool running = false;

        public bool Running 
        {
            get { return running; }
        }

        /// <summary>
        /// Create kiosk camera instance
        /// </summary>
        public KioskCamera()
        {
			USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice); //枚舉所有視頻輸入設備

            int webcam_count = USBWebcams.Count;
            richTextBox1.Text += "找到 " + webcam_count.ToString() + " 台WebCam\n";

            for (int i = 0; i < USBWebcams.Count; i++)
            {
                if (USBWebcams[i].Name.Contains("Microsoft"))
                {
                    Cam = new VideoCaptureDevice(USBWebcams[i].MonikerString);
                    break;
                }
            }

            if (Cam == null)
            {
                throw new ApplicationException("Kiosk camera by Microsoft wasn't found.");
            }

            Cam.NewFrame += Cam_NewFrame;
        }

        /// <summary>
        /// Capture image from camera
        /// </summary>
        public Bitmap CaptureImage()
        {
            if (!running)
            {
                throw new ApplicationException("Camera not running.");
            }

            lock (locker)
            {
                if (lastFrame == null)
                {
                    throw new ApplicationException("No frame capture yet.");
                }
                return (Bitmap)lastFrame.Clone();
            }
        }

        /// <summary>
        /// Start camera
        /// </summary>
        public void Start()
        {
            if (running) return;

            Cam.Start();

            while (!Cam.IsRunning) System.Threading.Thread.Sleep(25);
            running = true;
        }

        /// <summary>
        /// Stop camera
        /// </summary>
        public void Stop()
        {
            if (!running) return;

            if (Cam.IsRunning)
            {
                Cam.SignalToStop();
                Cam.WaitForStop();
            }

            running = false;

            if (lastFrame != null)
            {
                lastFrame.Dispose();
                lastFrame = null;
            }
        }

        public void SetFocus(short value)
        {
            short v = 0;
            if (value >= 0 && value < short.MaxValue) v = value;
            Cam.SetCameraProperty(CameraControlProperty.Focus, v, CameraControlFlags.Manual);
        }

        public void SetExposure(short value)
        {
            short v = 0;
            if (value >= 0 && value < short.MaxValue) v = value;
            Cam.SetCameraProperty(CameraControlProperty.Exposure, v, CameraControlFlags.Manual);
        }

        public void SetIris(short value)
        {
            short v = 0;
            if (value >= 0 && value < short.MaxValue) v = value;
            Cam.SetCameraProperty(CameraControlProperty.Iris, v, CameraControlFlags.Manual);
        }

        public void SetPan(short value)
        {
            short v = 0;
            if (value >= 0 && value < short.MaxValue) v = value;
            Cam.SetCameraProperty(CameraControlProperty.Pan, v, CameraControlFlags.Manual);
        }

        public void SetRoll(short value)
        {
            short v = 0;
            if (value >= 0 && value < short.MaxValue) v = value;
            Cam.SetCameraProperty(CameraControlProperty.Roll, v, CameraControlFlags.Manual);
        }

        public void SetTilt(short value)
        {
            short v = 0;
            if (value >= 0 && value < short.MaxValue) v = value;
            Cam.SetCameraProperty(CameraControlProperty.Tilt, v, CameraControlFlags.Manual);
        }

        public void SetZoom(short value)
        {
            short v = 0;
            if (value >= 0 && value < short.MaxValue) v = value;
            Cam.SetCameraProperty(CameraControlProperty.Zoom, v, CameraControlFlags.Manual);
        }

        private void Cam_NewFrame(object sender, AForge.Video.NewFrameEventArgs eventArgs)
        {
            if (!running) return;

            lock (locker)
            {
                if (lastFrame != null)
                {
                    lastFrame.Dispose();
                    lastFrame = null;
                }

                lastFrame = (Bitmap)eventArgs.Frame.Clone();
            }
        }
    }
}
