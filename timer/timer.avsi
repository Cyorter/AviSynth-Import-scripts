/* Timer for AviSynth videos
It's just another obvious timer and can be used as another alternative to other timers.
TODO: DEFAULT VALUES NOT WORKING!

Easy usage: timer(seconds, cropmethod, miliseconds, pixelsize)
-Seconds: can be float for miliseconds or int for just seconds (up to 86499 (default value), which is 24 hours).
-CropMethod: (0-5) crop a number of digits from left to right, if 0, it won't crop (00:00:00), if 2, it will crop hours (00:00).
-Miliseconds: (0-3) number of miliseconds digits, if 0, it won't display miliseconds, if 3, output will be (~.000).
-PixelSize: size in pixels * 4, by default is 4 (4x4 = 16) but you can use lower or higher resolutions.

Example: t = timer(30, 3, 2, 8).ChangeFPS(framerate, false) #Linear = false
		 Layer(t, x = width - width(t), y = height - height(t))

Output will be 0:00.00, you must change timer framerate to video framerate.
Layer is to overlay the video on top of the video (if you don't want a transparent background use Overlay instead of Layer).
The substraction for x and y is used to display time at the bottom-right, if want to display at top-left use x = 0 and y = 0.

If you just want the timer (no base video), use "timer(59.765, 0, 3, 16).ChangeFPS(60, false)" (in this case you can use any framerate).
*/

function timer(float sec, int cropm, int ms, int pixs)
{
    sec   = default(sec, 86499)
    cropm = default(cropm, 1)
    ms    = default(ms, 3)
    pixs  = default(pixs, 4)

    cropm = cropm == 0 ? 0 : cropm == 1 ? 20 : cropm == 2 ? 48 : cropm == 3 ? 68 : cropm == 4 ? 96 : cropm == 5 ? 116 : 1
    ms = ms == 3 ? 0 : ms == 2 ? -20 : ms == 1 ? -40 : ms == 0 ? -68 : 1

    assert(sec > 0 && sec < 86500, "Invalid length (maximum is 86499).")
    assert(cropm != 1, "Invalid crop method (range is 0-5).")
    assert(ms != 1, "Invalid number of ms digits (range is 0-3).")
    assert(pixs > 0, "Pixel size must be positive.")

    t0 = ImageSource("0.png",0,23,24, pixel_type="RGB32")
    t1 = ImageSource("1.png",0,23,24, pixel_type="RGB32")
    t2 = ImageSource("2.png",0,23,24, pixel_type="RGB32")
    t3 = ImageSource("3.png",0,23,24, pixel_type="RGB32")
    t4 = ImageSource("4.png",0,23,24, pixel_type="RGB32")
    t5 = ImageSource("5.png",0,23,24, pixel_type="RGB32")
    t6 = ImageSource("6.png",0,23,24, pixel_type="RGB32")
    t7 = ImageSource("7.png",0,23,24, pixel_type="RGB32")
    t8 = ImageSource("8.png",0,23,24, pixel_type="RGB32")
    t9 = ImageSource("9.png",0,23,24, pixel_type="RGB32")
    ts = ImageSource("s.png",0,23,24, pixel_type="RGB32") # Separator

    su = Loop(t0++t1++t2++t3++t4++t5++t6++t7++t8++t9,6)
    sd = Loop(Trim(su,0,240),10).AssumeFPS(2.4).ChangeFPS(24)

    s = BlankClip(2000,48,22,"RGB32",24).Layer(sd, x = 0).Layer(su, x = 20).Layer(ts, x = 36).Trim(0,1439)
    s = Loop(s,60)

    m = s.AssumeFPS(0.4).ChangeFPS(24)
    h = m.AssumeFPS(0.4).ChangeFPS(24)

    s = Loop(s,60)

    t = StackHorizontal(h,m,s).Trim(0,2073599).Crop(cropm,0,134 - cropm,0).ChangeFPS(1000)
    t = StackHorizontal(t,mili).Crop(0,0,ms,0)

    sec = int(sec * 1000)

    return t.Trim(0,sec).PointResize(width(t) * pixs, height(t) * pixs)
}

function mili()
{
    t0 = ImageSource("0.png",0,0,1000, pixel_type="RGB32")
    t1 = ImageSource("1.png",0,0,1000, pixel_type="RGB32")
    t2 = ImageSource("2.png",0,0,1000, pixel_type="RGB32")
    t3 = ImageSource("3.png",0,0,1000, pixel_type="RGB32")
    t4 = ImageSource("4.png",0,0,1000, pixel_type="RGB32")
    t5 = ImageSource("5.png",0,0,1000, pixel_type="RGB32")
    t6 = ImageSource("6.png",0,0,1000, pixel_type="RGB32")
    t7 = ImageSource("7.png",0,0,1000, pixel_type="RGB32")
    t8 = ImageSource("8.png",0,0,1000, pixel_type="RGB32")
    t9 = ImageSource("9.png",0,0,1000, pixel_type="RGB32")
    td = ImageSource("d.png",0,0,1000, pixel_type="RGB32")

    m2 = t0++t1++t2++t3++t4++t5++t6++t7++t8++t9
    m1 = m2.AssumeFPS(100).ChangeFPS(1000)
    m0 = m1.AssumeFPS(100).ChangeFPS(1000)

    m2 = Loop(m2,100)
    m1 = Loop(m1,10)

    t = BlankClip(1000,68,22,"RGB32",1000).Layer(td, x = -2).Layer(m0, x = 10).Layer(m1, x = 30).Layer(m2, x = 50)
    t = Loop(t,100000)

    return t.Trim(0,86399999)
}
