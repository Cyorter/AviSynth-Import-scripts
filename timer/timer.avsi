/* Timer for AviSynth videos
It's just another obvious timer and can be used as another alternative to other timers.

Easy usage: timer(seconds,cropmethod,miliseconds)
-Seconds: can be float for miliseconds or int for just seconds (up to 86399 (default value), which is 24 hours).
-Cropmethod: (0-5) crop a number of digits from left to right, if 0, it won't crop (00:00:00), if 2, it will crop hours (00:00).
-Miliseconds: (0-3) number of miliseconds digits, if 0, it won't display miliseconds, if 3, output will be (~.000).

Example: t = time(30,3,2).ChangeFPS(framerate,false)
         Layer(t, x = width - width(t), y = height - height(t))

Output will be 0:00.00, if there's video, you must change timer framerate to video framerate.
Layer is to overlay the video with transparency (if you don't want transparency use Overlay instead of Layer).
The set for x and y is used to display time at the bottom-right, if want to display at top-left use x = 0 and y = 0.

If you just want the timer (no base video), use "timer(59.765,0,3).ChangeFPS(60,false)" (in this case you can use any framerate).
*/

function timer(float sec, int cropm, int ms)
{
    sec = default(sec, 86399)

    cropm = default(cropm, 1)
    cropm = cropm == 0 ? 0 : cropm == 1 ? 40 : cropm == 2 ? 96 : cropm == 3 ? 136 : cropm == 4 ? 192 : cropm == 5 ? 232 : 1

    ms = default(ms, 3)
    ms = ms == 3 ? 0 : ms == 2 ? -40 : ms == 1 ? -80 : ms == 0 ? -136 : 1

    assert(sec > 0 && sec < 86400, "Invalid value (maximum is 86399.99)")
    assert(cropm != 1, "Invalid crop method (range is 0-5)")
    assert(ms != 1, "Invalid number of ms digits (range is 0-3)")

    t0 = ImageSource("0.png",0,23,pixel_type="RGB32")
    t1 = ImageSource("1.png",0,23,pixel_type="RGB32")
    t2 = ImageSource("2.png",0,23,pixel_type="RGB32")
    t3 = ImageSource("3.png",0,23,pixel_type="RGB32")
    t4 = ImageSource("4.png",0,23,pixel_type="RGB32")
    t5 = ImageSource("5.png",0,23,pixel_type="RGB32")
    t6 = ImageSource("6.png",0,23,pixel_type="RGB32")
    t7 = ImageSource("7.png",0,23,pixel_type="RGB32")
    t8 = ImageSource("8.png",0,23,pixel_type="RGB32")
    t9 = ImageSource("9.png",0,23,pixel_type="RGB32")
    ts = ImageSource("s.png",0,23,pixel_type="RGB32") # Separator

    su = t0++t1++t2++t3++t4++t5++t6++t7++t8++t9
    sd = su.AssumeFPS(2.4).ChangeFPS(24).Trim(0,1439)

    su = su++su++su++su++su++su
    sd = sd++sd++sd++sd++sd++sd++sd++sd++sd++sd

    s = BlankClip(100000,72,40,"RGB32",24).Layer(sd,x=0).Layer(su,x=40).Trim(0,1439)
    s = s++s++s++s++s++s++s++s++s++s
    s = s++s++s++s++s++s

    m = s.AssumeFPS(0.4).ChangeFPS(24)
    h = m.AssumeFPS(0.4).ChangeFPS(24)

    s = s++s++s++s++s++s++s++s++s++s
    s = s++s++s++s++s++s

    t = StackHorizontal(h,ts,m,ts,s).Trim(0,2073599)
    t = Crop(t,cropm,0,0,0).ChangeFPS(1000)
    t = StackHorizontal(t,mili).Crop(0,0,ms,0)

    sec = int(sec * 1000)

    return t.Trim(0,sec)
}

function mili()
{
    t0 = ImageSource("0.png",0,0,1000,pixel_type="RGB32")
    t1 = ImageSource("1.png",0,0,1000,pixel_type="RGB32")
    t2 = ImageSource("2.png",0,0,1000,pixel_type="RGB32")
    t3 = ImageSource("3.png",0,0,1000,pixel_type="RGB32")
    t4 = ImageSource("4.png",0,0,1000,pixel_type="RGB32")
    t5 = ImageSource("5.png",0,0,1000,pixel_type="RGB32")
    t6 = ImageSource("6.png",0,0,1000,pixel_type="RGB32")
    t7 = ImageSource("7.png",0,0,1000,pixel_type="RGB32")
    t8 = ImageSource("8.png",0,0,1000,pixel_type="RGB32")
    t9 = ImageSource("9.png",0,0,1000,pixel_type="RGB32")
    td = ImageSource("d.png",0,0,1000,pixel_type="RGB32")

    m2 = t0++t1++t2++t3++t4++t5++t6++t7++t8++t9
    m1 = m2.AssumeFPS(100).ChangeFPS(1000)
    m0 = m1.AssumeFPS(100).ChangeFPS(1000)

    m2 = m2++m2++m2++m2++m2++m2++m2++m2++m2++m2
    m2 = m2++m2++m2++m2++m2++m2++m2++m2++m2++m2
    m1 = m1++m1++m1++m1++m1++m1++m1++m1++m1++m1

    t = BlankClip(1000,136,40,"RGB32",1000).Layer(td,x=0).Layer(m0,x=24).Layer(m1,x=64).Layer(m2,x=104)
    t = t++t++t++t++t++t++t++t++t++t
    t = t++t++t++t++t++t++t++t++t++t
    t = t++t++t++t++t++t++t++t++t++t
    t = t++t++t++t++t++t++t++t++t++t
    t = t++t++t++t++t++t++t++t++t++t

    return t.Trim(0,86399999)
}
