def test_wav(h, f):
    import wave
    # 'RIFF' <len> 'WAVE' 'fmt ' <len>
    if not h.startswith(b'RIFF') or h[8:12] != b'WAVE' or h[12:16] != b'fmt ':
        return None
    f.seek(0)
    try:
        w = wave.openfp(f, 'r')
    except (EOFError, wave.Error):
        return None
    return ('wav', w.getframerate(), w.getnchannels(),
                   w.getnframes(), 8*w.getsampwidth())

