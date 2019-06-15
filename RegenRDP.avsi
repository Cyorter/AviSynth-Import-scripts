/* REMOVE DUPLICATED PIXELS FOR REGEN RECORDINGS
 * WARNING: Do NOT use functions that affects the size BEFORE using the remove duplicated pixels, but you can do it AFTER if you wish.
 * WARNING: Do NOT modify the file (unless I mistaken in RealSpeed function).
 * WARNING: Remember using Import("RegenRDP.avsi") if you don't have it in the AviSynth plugins folder.
 * WARNING: Not tested in AviSynthPlus (AviSynth+).
 * There are 18 duplicated pixels in Regen (10 horizontal + 8 vertical), and this script helps removing them.
 * And also removes the black bars if you have them, the int argument is "crop-pixels", you can set a value between 0-2.
 * 0 sets to 320x240/640x480/960x720
 * 1 sets to 320x224/640x448/960x672 (default as most games have this resolution)
 * 2 sets to 256x224/512x448/768x672
 * There's also a "Real Speed" function, it just set Regen's speed to sync with real MegaDrive (or at least very close). It's a good function for comparisons.
 * Usage example in your script: RegenRDP(video,0) or RegenRDP(v,1) or RegenRDP(last,2) depending of your choice with the black bars.
 */

function RegenRealSpeed(clip m)
{
	return m.HasAudio ? m.AssumeFPS(49.501,true) : m.AssumeFPS(49.501)
}
function RegenRDP(clip m, int cropix)
{
	err = (cropix < 3) && (cropix >= 0) ? 1 : 0
	siz = (m.width == 328) && (m.height == 248) ? 1 : (m.width == 648) && (m.height == 488) ? 2 : (m.width == 968) && (m.height == 728) ? 3 : 0
	cropix = default(cropix,1)
	
	Assert(IsInt(cropix), "Use a INTEGRER between 0-2")
	Assert(err != 0, "Use a number between 0-2!
0 for 320x240
1 for 320x224
2 for 256x224
Or same multiplied by 2 or 3 depending of your clip")
	Assert(siz != 0, "Invalid size! Use Regen's sizes:
328x248
648x488
968x728
Did you resized it BEFORE using this function?")
	
	m = siz == 1 ? RDP1(m) : siz == 2 ? RDP2(m) : siz == 3 ? RDP3(m) : NOP
	s = m.width + m.height
	
	return (cropix == 1) || (cropix == 2) ? CropBB(m,s,cropix) : cropix == 0 ? m : Subtitle(m,"ERROR")
}
function CropBB(m,s,c)
{
	v = s == 560 ? Crop(m,0,8,0,224) : s == 1120 ? Crop(m,0,16,0,448) : s == 1680 ? Crop(m,0,24,0,672) : NOP
	h = s == 560 ? Crop(m,32,8,256,224) : s == 1120 ? Crop(m,64,16,512,448) : s == 1680 ? Crop(m,96,24,768,672) : NOP
	return c == 1 ? v : c == 2 ? h : Subtitle(m,"ERROR")
}
function RDP1(m)
{
	s0 = Crop(m,0,0,17,0)
	s1 = Crop(m,18,0,32,0)
	s2 = Crop(m,51,0,32,0)
	s3 = Crop(m,84,0,32,0)
	s4 = Crop(m,117,0,32,0)
	s5 = Crop(m,150,0,32,0)
	s6 = Crop(m,183,0,32,0)
	s7 = Crop(m,216,0,32,0)
	s8 = Crop(m,249,0,32,0)
	s9 = Crop(m,282,0,32,0)
	sa = Crop(m,315,0,0,0)
	s = StackHorizontal(s0,s1,s2,s3,s4,s5,s6,s7,s8,s9,sa)
	
	s0 = Crop(s,0,0,0,15)
	s1 = Crop(s,0,16,0,30)
	s2 = Crop(s,0,47,0,30)
	s3 = Crop(s,0,78,0,30)
	s4 = Crop(s,0,109,0,30)
	s5 = Crop(s,0,140,0,30)
	s6 = Crop(s,0,171,0,30)
	s7 = Crop(s,0,202,0,30)
	s8 = Crop(s,0,233,0,0)
	
	return StackVertical(s0,s1,s2,s3,s4,s5,s6,s7,s8).AddBorders(0,0,2,0)
}
function RDP2(m)
{
	s0 = Crop(m,0,0,34,0)
	s1 = Crop(m,35,0,64,0)
	s2 = Crop(m,100,0,64,0)
	s3 = Crop(m,165,0,64,0)
	s4 = Crop(m,230,0,64,0)
	s5 = Crop(m,295,0,64,0)
	s6 = Crop(m,360,0,64,0)
	s7 = Crop(m,425,0,64,0)
	s8 = Crop(m,490,0,64,0)
	s9 = Crop(m,555,0,64,0)
	sa = Crop(m,620,0,0,0)
	s = StackHorizontal(s0,s1,s2,s3,s4,s5,s6,s7,s8,s9,sa)
	
	s0 = Crop(s,0,0,0,30)
	s1 = Crop(s,0,31,0,60)
	s2 = Crop(s,0,92,0,60)
	s3 = Crop(s,0,153,0,60)
	s4 = Crop(s,0,214,0,60)
	s5 = Crop(s,0,275,0,60)
	s6 = Crop(s,0,336,0,60)
	s7 = Crop(s,0,397,0,60)
	s8 = Crop(s,0,458,0,0)
	
	return StackVertical(s0,s1,s2,s3,s4,s5,s6,s7,s8).AddBorders(0,0,2,0)
}
function RDP3(m)
{
	s0 = Crop(m,0,0,51,0)
	s1 = Crop(m,52,0,96,0)
	s2 = Crop(m,149,0,96,0)
	s3 = Crop(m,246,0,96,0)
	s4 = Crop(m,343,0,96,0)
	s5 = Crop(m,440,0,96,0)
	s6 = Crop(m,537,0,96,0)
	s7 = Crop(m,634,0,96,0)
	s8 = Crop(m,731,0,96,0)
	s9 = Crop(m,828,0,96,0)
	sa = Crop(m,925,0,0,0)
	s = StackHorizontal(s0,s1,s2,s3,s4,s5,s6,s7,s8,s9,sa)
	
	s0 = Crop(s,0,0,0,45)
	s1 = Crop(s,0,46,0,90)
	s2 = Crop(s,0,137,0,90)
	s3 = Crop(s,0,228,0,90)
	s4 = Crop(s,0,319,0,90)
	s5 = Crop(s,0,410,0,90)
	s6 = Crop(s,0,501,0,90)
	s7 = Crop(s,0,592,0,90)
	s8 = Crop(s,0,683,0,0)
	
	return StackVertical(s0,s1,s2,s3,s4,s5,s6,s7,s8).AddBorders(0,0,2,0)
}
