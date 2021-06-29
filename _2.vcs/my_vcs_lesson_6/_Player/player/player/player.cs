using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Un4seen.Bass;

namespace player
{
    class player
    {
        int stream;
        public player()
        {
            Bass.BASS_Init(-1, 44100, BASSInit.BASS_DEVICE_DEFAULT, System.IntPtr.Zero);    
        }
        public void LoadSong(string location)
        {
            stream = Bass.BASS_StreamCreateFile(location, 0, 0, BASSFlag.BASS_SAMPLE_FLOAT);
        }

        public void PlaySong()
        {
            Bass.BASS_ChannelPlay(stream,false);
        }

        public void StopSong()
        {
            Bass.BASS_ChannelStop(stream);
        }

        public void PauseSong()
        {
            Bass.BASS_ChannelPause(stream);
        }

        ~player()
        {
            Bass.BASS_Free();
        }
    }
}
