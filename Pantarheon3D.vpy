################################################################################
##                                                                             #
## Pantarheon 3D AviSynth Toolbox, version 1.1.                                #
## http://www.pantarheon.org/AviSynth3DToolbox/                                #
## VapourSynth port version 1.0.                                               #
##                                                                             #
## Copyright (c) 2010 G. Adam Stanislav                                        #
## Copyright (c) 2019 César (Cyorter)                                          #
## All rights reserved                                                         #
##                                                                             #
################################################################################
##                                                                             #
## Contacting Adam Stanislav:                                                  #
## If you have any questions, I log in to                                      #
## http://www.dvinfo.net/forum/3d-stereoscopic-production-delivery/            #
## every day. It is a great forum!!!                                           #
##                                                                             #
################################################################################
##                                                                             #
## Contacting Cyorter:                                                         #
## Discord: Cyorter#2655                                                       #
## Twitter: Cyorter1                                                           #
## TASVideos: Cyorter                                                          #
## Github: Cyorter                                                             #
##                                                                             #
################################################################################

import vapoursynth as vs
core = vs.get_core()

################################################################################
###      BASIC 3D FUNCTIONS to combine a left and a right video into 3D      ###
################################################################################

# Both left and right must have the same properties (size and pixel type).
# I wrote a AviSynth's ReduceBy2 equivalent for creating reduced 3D videos.

# Create a 3D video for side-by-side viewing (left/right).

def LeftRight3D(l: vs.VideoNode, r: vs.VideoNode):
    assert l.width == r.width and l.height == r.height, 'Not same size!'
    assert l.format.name == r.format.name, 'Not same pixel type'
    return core.std.StackHorizontal([l,r])

# Create a 3D video for cross-eyed viewing (right/left).

def CrossEyed3D(l: vs.VideoNode, r: vs.VideoNode):
    assert l.width == r.width and l.height == r.height, 'Not same size!'
    assert l.format.name == r.format.name, 'Not same pixel type'
    return core.std.StackHorizontal([r,l])

# Create a top/down 3D video (left on top).

def TopDown3D(l: vs.VideoNode, r: vs.VideoNode):
    assert l.width == r.width and l.height == r.height, 'Not same size!'
    assert l.format.name == r.format.name, 'Not same pixel type'
    return core.std.StackVertical([l,r])

# Create a down/top 3D video (right on top).

def DownTop3D(l: vs.VideoNode, r: vs.VideoNode):
    assert l.width == r.width and l.height == r.height, 'Not same size!'
    assert l.format.name == r.format.name, 'Not same pixel type'
    return core.std.StackVertical([r,l])

# Create an HDMI v.1.4a 3D video.
# This will place the left video above the right video with 45 blank lines
# between them. A very strange standard considering many YUV formats do not
# allow an odd number of lines...

def HDMI3D(l: vs.VideoNode, r: vs.VideoNode):
    assert l.width == r.width and l.height == r.height, 'Not same size!'
    assert l.format.name == r.format.name, 'Not same pixel type'
    assert l.format.color_family != 'YUV', 'Not acceptable pixel type'
    return core.std.StackVertical([l, core.std.BlankClip(l, height=45), r])

# Create a reduced left/right 3D video.

def LeftRight3DReduced(l: vs.VideoNode, r: vs.VideoNode):
    assert l.width == r.width and l.height == r.height, 'Not same size!'
    assert l.format.name == r.format.name, 'Not same pixel type'
    L = core.resize.Bilinear(l, l.width//2, l.height, src_left=0.5)
    R = core.resize.Bilinear(r, r.width//2, r.height, src_left=0.5)
    return core.std.StackHorizontal([L,R])

# Create a reduced right/left 3D video.

def CrossEyed3DReduced(l: vs.VideoNode, r: vs.VideoNode):
    assert l.width == r.width and l.height == r.height, 'Not same size!'
    assert l.format.name == r.format.name, 'Not same pixel type'
    L = core.resize.Bilinear(l, l.width//2, l.height, src_left=0.5)
    R = core.resize.Bilinear(r, r.width//2, r.height, src_left=0.5)
    return core.std.StackHorizontal([R,L])

# Create a 3D video for YouTube's "yt3d" method. This requires the clips
# to be reduced horizontally by 2 and the left view be in the right half
# of the video and the right view in the left half.
# This, by the way, is the same as CrossEyed3DReduced.

def Yt3D(l: vs.VideoNode, r: vs.VideoNode):
    assert l.width == r.width and l.height == r.height, 'Not same size!'
    assert l.format.name == r.format.name, 'Not same pixel type'
    L = core.resize.Bilinear(l, l.width//2, l.height, src_left=0.5)
    R = core.resize.Bilinear(r, r.width//2, r.height, src_left=0.5)
    return core.std.StackHorizontal([R,L])

# Create a reduced top/down 3D video.

def TopDown3DReduced(l: vs.VideoNode, r: vs.VideoNode):
    assert l.width == r.width and l.height == r.height, 'Not same size!'
    assert l.format.name == r.format.name, 'Not same pixel type'
    L = core.resize.Bilinear(l, l.width, l.height//2, src_top=-0.5)
    R = core.resize.Bilinear(r, r.width, r.height//2, src_top=-0.5)
    return core.std.StackVertical([L,R])

# Create a reduced down/top 3D video.

def DownTop3DReduced(l: vs.VideoNode, r: vs.VideoNode):
    assert l.width == r.width and l.height == r.height, 'Not same size!'
    assert l.format.name == r.format.name, 'Not same pixel type'
    L = core.resize.Bilinear(l, l.width, l.height//2, src_top=-0.5)
    R = core.resize.Bilinear(r, r.width, r.height//2, src_top=-0.5)
    return core.std.StackVertical([R,L])

# Create a left/right 3D video alternating frames.

def AlternatingLeftRight3D(l: vs.VideoNode, r: vs.VideoNode):
    assert l.width == r.width and l.height == r.height, 'Not same size!'
    assert l.format.name == r.format.name, 'Not same pixel type'
    return core.std.Interleave([l,r])

# Create a right/left 3D video alternating frames.

def AlternatingCrossEyed3D(l: vs.VideoNode, r: vs.VideoNode):
    assert l.width == r.width and l.height == r.height, 'Not same size!'
    assert l.format.name == r.format.name, 'Not same pixel type'
    return core.std.Interleave([r,l])

# Create an interleaved rows 3D video (left/right).

def InterleaveRowsLeftRight3D(l: vs.VideoNode, r: vs.VideoNode):
    assert l.width == r.width and l.height == r.height, 'Not same size!'
    assert l.format.name == r.format.name, 'Not same pixel type'
    video = core.std.Interleave([l,r])
    video = core.std.DoubleWeave(video,2)
    return core.std.SelectEvery(video,2,0)

# Create an interleaved rows 3D video (right/left).

def InterleaveRowsCrossEyed3D(l: vs.VideoNode, r: vs.VideoNode):
    assert l.width == r.width and l.height == r.height, 'Not same size!'
    assert l.format.name == r.format.name, 'Not same pixel type'
    video = core.std.Interleave([r,l])
    video = core.std.DoubleWeave(video,2)
    return core.std.SelectEvery(video,2,0)

# Create an interleaved columns 3D video (left/right).

def InterleaveColsLeftRight3D(l: vs.VideoNode, r: vs.VideoNode):
    assert l.width == r.width and l.height == r.height, 'Not same size!'
    assert l.format.name == r.format.name, 'Not same pixel type'
    video = core.std.Interleave([l,r])
    video = core.std.Transpose(video)
    video = core.std.DoubleWeave(video,2)
    video = core.std.Transpose(video)
    return core.std.SelectEvery(video,2,0)

# Create an interleaved columns 3D video (right/left).

def InterleaveColsCrossEyed3D(l: vs.VideoNode, r: vs.VideoNode):
    assert l.width == r.width and l.height == r.height, 'Not same size!'
    assert l.format.name == r.format.name, 'Not same pixel type'
    video = core.std.Interleave([r,l])
    video = core.std.Transpose(video)
    video = core.std.DoubleWeave(video,2)
    video = core.std.Transpose(video)
    return core.std.SelectEvery(video,2,0)

################################################################################
###                                ANAGLYPHS                                 ###
################################################################################

# These are just the very basic anaglyphs. More sophisticated anaglyphs
# require more than scripting. Adam Stanislav's Bororo 3D plug-in for Sony Vegas
# can make them. See <http://www.pantarheon.org/Bororo3D/>.

# You may want to convert your video(s) to RGB or GRAY if it is YUV.
# YUV works but does not give the anaglyph you may want.
# I didn't write a RGB convert in case you REALLY want anaglyph from YUV.

# Green/Blue anaglyph.

def GBAnaglyph(l: vs.VideoNode, r: vs.VideoNode):
    assert l.width == r.width and l.height == r.height, 'Not same size!'
    assert l.format.name == r.format.name, 'Not same pixel type'
    return core.std.ShufflePlanes([core.std.BlankClip(l),l,r],0,vs.YUV if l.format.color_family == 'YUV' else vs.RGB)

# Red/Blue anaglyph.

def RBAnaglyph(l: vs.VideoNode, r: vs.VideoNode):
    assert l.width == r.width and l.height == r.height, 'Not same size!'
    assert l.format.name == r.format.name, 'Not same pixel type'
    return core.std.ShufflePlanes([l,core.std.BlankClip(l),r],0,vs.YUV if l.format.color_family == 'YUV' else vs.RGB)

# Red/Green anaglyph.

def RGAnaglyph(l: vs.VideoNode, r: vs.VideoNode):
    assert l.width == r.width and l.height == r.height, 'Not same size!'
    assert l.format.name == r.format.name, 'Not same pixel type'
    return core.std.ShufflePlanes([l,r,core.std.BlankClip(l)],0,vs.YUV if l.format.color_family == 'YUV' else vs.RGB)

# Red/Cyan anaglyph.

def RCAnaglyph(l: vs.VideoNode, r: vs.VideoNode):
    assert l.width == r.width and l.height == r.height, 'Not same size!'
    assert l.format.name == r.format.name, 'Not same pixel type'
    return core.std.ShufflePlanes([l,r,r],0,vs.YUV if l.format.color_family == 'YUV' else vs.RGB)

# Green/Magneto anaglyph.

def GMAnaglyph(l: vs.VideoNode, r: vs.VideoNode):
    assert l.width == r.width and l.height == r.height, 'Not same size!'
    assert l.format.name == r.format.name, 'Not same pixel type'
    return core.std.ShufflePlanes([l,r,l],0,vs.YUV if l.format.color_family == 'YUV' else vs.RGB)

# Yellow/Blue anaglyph.

def YBAnaglyph(l: vs.VideoNode, r: vs.VideoNode):
    assert l.width == r.width and l.height == r.height, 'Not same size!'
    assert l.format.name == r.format.name, 'Not same pixel type'
    return core.std.ShufflePlanes([l,l,r],0,vs.YUV if l.format.color_family == 'YUV' else vs.RGB)

################################################################################
###                              SWAP ANAGLYPHS                              ###
################################################################################

# Swap/Alternate anaglyph colors.
# Equivalent to __AnaglyphToLeftRight + CrossEyedTo__Anaglyph.

def SwapGBAnaglyph(c: vs.VideoNode): return GBAnaglyph(GBAnaglyphToRight(c),GBAnaglyphToLeft(c))
def SwapRBAnaglyph(c: vs.VideoNode): return RBAnaglyph(RBAnaglyphToRight(c),RBAnaglyphToLeft(c))
def SwapRGAnaglyph(c: vs.VideoNode): return RGAnaglyph(RGAnaglyphToRight(c),RGAnaglyphToLeft(c))
def SwapRCAnaglyph(c: vs.VideoNode): return RCAnaglyph(RCAnaglyphToRight(c),RCAnaglyphToLeft(c))
def SwapGMAnaglyph(c: vs.VideoNode): return GMAnaglyph(GMAnaglyphToRight(c),GMAnaglyphToLeft(c))
def SwapYBAnaglyph(c: vs.VideoNode): return YBAnaglyph(YBAnaglyphToRight(c),YBAnaglyphToLeft(c))

################################################################################
###                            EXTRACT LEFT VIEW                             ###
################################################################################

def LeftRight3DToLeft(c: vs.VideoNode):
    return core.std.CropAbs(c, c.width//2, c.height)
def CrossEyed3DToLeft(c: vs.VideoNode):
    return core.std.CropAbs(c, c.width//2, c.height, c.width//2, 0)
def TopDown3DToLeft(c: vs.VideoNode):
    return core.std.CropAbs(c, c.width, c.height//2)
def DownTop3DToLeft(c: vs.VideoNode):
    return core.std.CropAbs(c, c.width, c.height//2, 0, c.height//2)
def HDMI3DToLeft(c: vs.VideoNode):
    return core.std.CropAbs(c, c.width, (c.height - 45) // 2)
def LeftRight3DReducedToLeft(c: vs.VideoNode):
    cropd = core.std.CropAbs(c, c.width//2, c.height)
    return core.resize.Lanczos(cropd, c.width, c.height)
def CrossEyed3DReducedToLeft(c: vs.VideoNode):
    cropd = core.std.CropAbs(c, c.width//2, c.height, c.width//2, 0)
    return core.resize.Lanczos(cropd, c.width, c.height)
def Yt3DToLeft(c: vs.VideoNode):
    cropd = core.std.CropAbs(c, c.width//2, c.height, c.width//2, 0)
    return core.resize.Lanczos(cropd, c.width, c.height)
def TopDown3DReducedToLeft(c: vs.VideoNode):
    cropd = core.std.CropAbs(c, c.width, c.height//2)
    return core.resize.Lanczos(cropd, c.width, c.height)
def DownTop3DReducedToLeft(c: vs.VideoNode):
    cropd = core.std.CropAbs(c, c.width, c.height//2, 0, c.height//2)
    return core.resize.Lanczos(cropd, c.width, c.height)
def AlternatingLeftRight3DToLeft(c: vs.VideoNode):
    return core.std.SelectEvery(c, 2, 0)
def AlternatingCrossEyed3DToLeft(c: vs.VideoNode):
    return core.std.SelectEvery(c, 2, 1)
def InterleaveRowsLeftRight3DToLeft(c: vs.VideoNode):
    sepfd = core.std.SeparateFields(c, 0)
    return core.std.SelectEvery(sepfd, 2, 0)
def InterleaveRowsCrossEyed3DToLeft(c: vs.VideoNode):
    sepfd = core.std.SeparateFields(c, 0)
    return core.std.SelectEvery(sepfd, 2, 1)
def InterleaveColsLeftRight3DToLeft(c: vs.VideoNode):
    trand = core.std.Transpose(c)
    sepfd = core.std.SeparateFields(trand, 0)
    trand = core.std.Transpose(sepfd)
    return core.std.SelectEvery(trand, 2, 0)
def InterleaveColsCrossEyed3DToLeft(c: vs.VideoNode):
    trand = core.std.Transpose(c)
    sepfd = core.std.SeparateFields(trand, 0)
    trand = core.std.Transpose(sepfd)
    return core.std.SelectEvery(trand, 2, 1)
def GBAnaglyphToLeft(c: vs.VideoNode):
    return core.std.ShufflePlanes(c, 1, vs.GRAY)
def RBAnaglyphToLeft(c: vs.VideoNode):
    return core.std.ShufflePlanes(c, 0, vs.GRAY)
def RGAnaglyphToLeft(c: vs.VideoNode):
    return core.std.ShufflePlanes(c, 0, vs.GRAY)
def RCAnaglyphToLeft(c: vs.VideoNode):
    return core.std.ShufflePlanes(c, 0, vs.GRAY)
def GMAnaglyphToLeft(c: vs.VideoNode):
    return core.std.ShufflePlanes(c, 0, vs.GRAY)
def YBAnaglyphToLeft(c: vs.VideoNode):
    return core.std.ShufflePlanes(c, 0, vs.GRAY)

################################################################################
###                            EXTRACT RIGHT VIEW                            ###
################################################################################

def LeftRight3DToRight(c: vs.VideoNode):
    return core.std.CropAbs(c, c.width//2, c.height, c.width//2, 0)
def CrossEyed3DToRight(c: vs.VideoNode):
    return core.std.CropAbs(c, c.width//2, c.height)
def TopDown3DToRight(c: vs.VideoNode):
    return core.std.CropAbs(c, c.width, c.height//2, 0, c.height//2)
def DownTop3DToRight(c: vs.VideoNode):
    return core.std.CropAbs(c, c.width, c.height//2)
def HDMI3DToRight(c: vs.VideoNode):
    return core.std.CropAbs(c, c.width, (c.height - 45) // 2, 0, (c.height - 45) // 2 + 45)
def LeftRight3DReducedToRight(c: vs.VideoNode):
    cropd = core.std.CropAbs(c, c.width//2, c.height, c.width//2, 0)
    return core.resize.Lanczos(cropd, c.width, c.height)
def CrossEyed3DReducedToRight(c: vs.VideoNode):
    cropd = core.std.CropAbs(c, c.width//2, c.height)
    return core.resize.Lanczos(cropd, c.width, c.height)
def Yt3DToRight(c: vs.VideoNode):
    cropd = core.std.CropAbs(c, c.width//2, c.height)
    return core.resize.Lanczos(cropd, c.width, c.height)
def TopDown3DReducedToRight(c: vs.VideoNode):
    cropd = core.std.CropAbs(c, c.width, c.height//2, 0, c.height//2)
    return core.resize.Lanczos(cropd, c.width, c.height)
def DownTop3DReducedToRight(c: vs.VideoNode):
    cropd = core.std.CropAbs(c, c.width, c.height//2)
    return core.resize.Lanczos(cropd, c.width, c.height)
def AlternatingLeftRight3DToRight(c: vs.VideoNode):
    return core.std.SelectEvery(c, 2, 1)
def AlternatingCrossEyed3DToRight(c: vs.VideoNode):
    return core.std.SelectEvery(c, 2, 0)
def InterleaveRowsLeftRight3DToRight(c: vs.VideoNode):
    sepfd = core.std.SeparateFields(c, 0)
    return core.std.SelectEvery(sepfd, 2, 1)
def InterleaveRowsCrossEyed3DToRight(c: vs.VideoNode):
    sepfd = core.std.SeparateFields(c, 0)
    return core.std.SelectEvery(sepfd, 2, 0)
def InterleaveColsLeftRight3DToRight(c: vs.VideoNode):
    trand = core.std.Transpose(c)
    sepfd = core.std.SeparateFields(trand, 0)
    trand = core.std.Transpose(sepfd)
    return core.std.SelectEvery(trand, 2, 1)
def InterleaveColsCrossEyed3DToRight(c: vs.VideoNode):
    trand = core.std.Transpose(c)
    sepfd = core.std.SeparateFields(trand, 0)
    trand = core.std.Transpose(sepfd)
    return core.std.SelectEvery(trand, 2, 0)
def GBAnaglyphToRight(c: vs.VideoNode):
    return core.std.ShufflePlanes(c, 2, vs.GRAY)
def RBAnaglyphToRight(c: vs.VideoNode):
    return core.std.ShufflePlanes(c, 2, vs.GRAY)
def RGAnaglyphToRight(c: vs.VideoNode):
    return core.std.ShufflePlanes(c, 1, vs.GRAY)
def RCAnaglyphToRight(c: vs.VideoNode):
    return core.std.ShufflePlanes(c, 2, vs.GRAY)
def GMAnaglyphToRight(c: vs.VideoNode):
    return core.std.ShufflePlanes(c, 1, vs.GRAY)
def YBAnaglyphToRight(c: vs.VideoNode):
    return core.std.ShufflePlanes(c, 2, vs.GRAY)

################################################################################
###                CONVERSIONS FROM ONE 3D FORMAT TO ANOTHER                 ###
################################################################################

# Convert a left/right video to other formats.

def LeftRight3DToCrossEyed(c: vs.VideoNode): return CrossEyed3D(LeftRight3DToLeft(c),LeftRight3DToRight(c))
def LeftRight3DToTopDown(c: vs.VideoNode): return TopDown3D(LeftRight3DToLeft(c),LeftRight3DToRight(c))
def LeftRight3DToDownTop(c: vs.VideoNode): return DownTop3D(LeftRight3DToLeft(c),LeftRight3DToRight(c))
def LeftRight3DToLeftRightReduced(c: vs.VideoNode): return LeftRight3DReduced(LeftRight3DToLeft(c),LeftRight3DToRight(c))
def LeftRight3DToCrossEyedReduced(c: vs.VideoNode): return CrossEyed3DReduced(LeftRight3DToLeft(c),LeftRight3DToRight(c))
def LeftRight3DToYt3D(c: vs.VideoNode): return Yt3D(LeftRight3DToLeft(c),LeftRight3DToRight(c))
def LeftRight3DToTopDownReduced(c: vs.VideoNode): return TopDown3DReduced(LeftRight3DToLeft(c),LeftRight3DToRight(c))
def LeftRight3DToDownTopReduced(c: vs.VideoNode): return DownTop3DReduced(LeftRight3DToLeft(c),LeftRight3DToRight(c))
def LeftRight3DToHDMI(c: vs.VideoNode): return HDMI3D(LeftRight3DToLeft(c),LeftRight3DToRight(c))
def LeftRight3DToAlternatingLeftRight(c: vs.VideoNode): return AlternatingLeftRight3D(LeftRight3DToLeft(c),LeftRight3DToRight(c))
def LeftRight3DToAlternatingCrossEyed(c: vs.VideoNode): return AlternatingCrossEyed3D(LeftRight3DToLeft(c),LeftRight3DToRight(c))
def LeftRight3DToInterleaveRowsLeftRight(c: vs.VideoNode): return InterleaveRowsLeftRight3D(LeftRight3DToLeft(c),LeftRight3DToRight(c))
def LeftRight3DToInterleaveRowsCrossEyed(c: vs.VideoNode): return InterleaveRowsCrossEyed3D(LeftRight3DToLeft(c),LeftRight3DToRight(c))
def LeftRight3DToInterleaveColsLeftRight(c: vs.VideoNode): return InterleaveColsLeftRight3D(LeftRight3DToLeft(c),LeftRight3DToRight(c))
def LeftRight3DToInterleaveColsCrossEyed(c: vs.VideoNode): return InterleaveColsCrossEyed3D(LeftRight3DToLeft(c),LeftRight3DToRight(c))
def LeftRight3DToGBAnaglyph(c: vs.VideoNode): return GBAnaglyph(LeftRight3DToLeft(c),LeftRight3DToRight(c))
def LeftRight3DToRBAnaglyph(c: vs.VideoNode): return RBAnaglyph(LeftRight3DToLeft(c),LeftRight3DToRight(c))
def LeftRight3DToRGAnaglyph(c: vs.VideoNode): return RGAnaglyph(LeftRight3DToLeft(c),LeftRight3DToRight(c))
def LeftRight3DToRCAnaglyph(c: vs.VideoNode): return RCAnaglyph(LeftRight3DToLeft(c),LeftRight3DToRight(c))
def LeftRight3DToGMAnaglyph(c: vs.VideoNode): return GMAnaglyph(LeftRight3DToLeft(c),LeftRight3DToRight(c))
def LeftRight3DToYBAnaglyph(c: vs.VideoNode): return YBAnaglyph(LeftRight3DToLeft(c),LeftRight3DToRight(c))

# Convert a cross-eyed video to other formats.

def CrossEyed3DToLeftRight(c: vs.VideoNode): return LeftRight3D(CrossEyed3DToLeft(c),CrossEyed3DToRight(c))
def CrossEyed3DToTopDown(c: vs.VideoNode): return TopDown3D(CrossEyed3DToLeft(c),CrossEyed3DToRight(c))
def CrossEyed3DToDownTop(c: vs.VideoNode): return DownTop3D(CrossEyed3DToLeft(c),CrossEyed3DToRight(c))
def CrossEyed3DToLeftRightReduced(c: vs.VideoNode): return LeftRight3DReduced(CrossEyed3DToLeft(c),CrossEyed3DToRight(c))
def CrossEyed3DToCrossEyedReduced(c: vs.VideoNode): return CrossEyed3DReduced(CrossEyed3DToLeft(c),CrossEyed3DToRight(c))
def CrossEyed3DToYt3D(c: vs.VideoNode): return Yt3D(CrossEyed3DToLeft(c),CrossEyed3DToRight(c))
def CrossEyed3DToTopDownReduced(c: vs.VideoNode): return TopDown3DReduced(CrossEyed3DToLeft(c),CrossEyed3DToRight(c))
def CrossEyed3DToDownTopReduced(c: vs.VideoNode): return DownTop3DReduced(CrossEyed3DToLeft(c),CrossEyed3DToRight(c))
def CrossEyed3DToHDMI(c: vs.VideoNode): return HDMI3D(CrossEyed3DToLeft(c),CrossEyed3DToRight(c))
def CrossEyed3DToAlternatingLeftRight(c: vs.VideoNode): return AlternatingLeftRight3D(CrossEyed3DToLeft(c),CrossEyed3DToRight(c))
def CrossEyed3DToAlternatingCrossEyed(c: vs.VideoNode): return AlternatingCrossEyed3D(CrossEyed3DToLeft(c),CrossEyed3DToRight(c))
def CrossEyed3DToInterleaveRowsLeftRight(c: vs.VideoNode): return InterleaveRowsLeftRight3D(CrossEyed3DToLeft(c),CrossEyed3DToRight(c))
def CrossEyed3DToInterleaveRowsCrossEyed(c: vs.VideoNode): return InterleaveRowsCrossEyed3D(CrossEyed3DToLeft(c),CrossEyed3DToRight(c))
def CrossEyed3DToInterleaveColsLeftRight(c: vs.VideoNode): return InterleaveColsLeftRight3D(CrossEyed3DToLeft(c),CrossEyed3DToRight(c))
def CrossEyed3DToInterleaveColsCrossEyed(c: vs.VideoNode): return InterleaveColsCrossEyed3D(CrossEyed3DToLeft(c),CrossEyed3DToRight(c))
def CrossEyed3DToGBAnaglyph(c: vs.VideoNode): return GBAnaglyph(CrossEyed3DToLeft(c),CrossEyed3DToRight(c))
def CrossEyed3DToRBAnaglyph(c: vs.VideoNode): return RBAnaglyph(CrossEyed3DToLeft(c),CrossEyed3DToRight(c))
def CrossEyed3DToRGAnaglyph(c: vs.VideoNode): return RGAnaglyph(CrossEyed3DToLeft(c),CrossEyed3DToRight(c))
def CrossEyed3DToRCAnaglyph(c: vs.VideoNode): return RCAnaglyph(CrossEyed3DToLeft(c),CrossEyed3DToRight(c))
def CrossEyed3DToGMAnaglyph(c: vs.VideoNode): return GMAnaglyph(CrossEyed3DToLeft(c),CrossEyed3DToRight(c))
def CrossEyed3DToYBAnaglyph(c: vs.VideoNode): return YBAnaglyph(CrossEyed3DToLeft(c),CrossEyed3DToRight(c))

# Convert a top/down video to other formats.

def TopDown3DToLeftRight(c: vs.VideoNode): return LeftRight3D(TopDown3DToLeft(c),TopDown3DToRight(c))
def TopDown3DToCrossEyed(c: vs.VideoNode): return CrossEyed3D(TopDown3DToLeft(c),TopDown3DToRight(c))
def TopDown3DToDownTop(c: vs.VideoNode): return DownTop3D(TopDown3DToLeft(c),TopDown3DToRight(c))
def TopDown3DToLeftRightReduced(c: vs.VideoNode): return LeftRight3DReduced(TopDown3DToLeft(c),TopDown3DToRight(c))
def TopDown3DToCrossEyedReduced(c: vs.VideoNode): return CrossEyed3DReduced(TopDown3DToLeft(c),TopDown3DToRight(c))
def TopDown3DToYt3D(c: vs.VideoNode): return Yt3D(TopDown3DToLeft(c),TopDown3DToRight(c))
def TopDown3DToTopDownReduced(c: vs.VideoNode): return TopDown3DReduced(TopDown3DToLeft(c),TopDown3DToRight(c))
def TopDown3DToDownTopReduced(c: vs.VideoNode): return DownTop3DReduced(TopDown3DToLeft(c),TopDown3DToRight(c))
def TopDown3DToHDMI(c: vs.VideoNode): return HDMI3D(TopDown3DToLeft(c),TopDown3DToRight(c))
def TopDown3DToAlternatingLeftRight(c: vs.VideoNode): return AlternatingLeftRight3D(TopDown3DToLeft(c),TopDown3DToRight(c))
def TopDown3DToAlternatingCrossEyed(c: vs.VideoNode): return AlternatingCrossEyed3D(TopDown3DToLeft(c),TopDown3DToRight(c))
def TopDown3DToInterleaveRowsLeftRight(c: vs.VideoNode): return InterleaveRowsLeftRight3D(TopDown3DToLeft(c),TopDown3DToRight(c))
def TopDown3DToInterleaveRowsCrossEyed(c: vs.VideoNode): return InterleaveRowsCrossEyed3D(TopDown3DToLeft(c),TopDown3DToRight(c))
def TopDown3DToInterleaveColsLeftRight(c: vs.VideoNode): return InterleaveColsLeftRight3D(TopDown3DToLeft(c),TopDown3DToRight(c))
def TopDown3DToInterleaveColsCrossEyed(c: vs.VideoNode): return InterleaveColsCrossEyed3D(TopDown3DToLeft(c),TopDown3DToRight(c))
def TopDown3DToGBAnaglyph(c: vs.VideoNode): return GBAnaglyph(TopDown3DToLeft(c),TopDown3DToRight(c))
def TopDown3DToRBAnaglyph(c: vs.VideoNode): return RBAnaglyph(TopDown3DToLeft(c),TopDown3DToRight(c))
def TopDown3DToRGAnaglyph(c: vs.VideoNode): return RGAnaglyph(TopDown3DToLeft(c),TopDown3DToRight(c))
def TopDown3DToRCAnaglyph(c: vs.VideoNode): return RCAnaglyph(TopDown3DToLeft(c),TopDown3DToRight(c))
def TopDown3DToGMAnaglyph(c: vs.VideoNode): return GMAnaglyph(TopDown3DToLeft(c),TopDown3DToRight(c))
def TopDown3DToYBAnaglyph(c: vs.VideoNode): return YBAnaglyph(TopDown3DToLeft(c),TopDown3DToRight(c))

# Convert a down/top video to other formats.

def DownTop3DToLeftRight(c: vs.VideoNode): return LeftRight3D(DownTop3DToLeft(c),DownTop3DToRight(c))
def DownTop3DToCrossEyed(c: vs.VideoNode): return CrossEyed3D(DownTop3DToLeft(c),DownTop3DToRight(c))
def DownTop3DToTopDown(c: vs.VideoNode): return TopDown3D(DownTop3DToLeft(c),DownTop3DToRight(c))
def DownTop3DToLeftRightReduced(c: vs.VideoNode): return LeftRight3DReduced(DownTop3DToLeft(c),DownTop3DToRight(c))
def DownTop3DToCrossEyedReduced(c: vs.VideoNode): return CrossEyed3DReduced(DownTop3DToLeft(c),DownTop3DToRight(c))
def DownTop3DToYt3D(c: vs.VideoNode): return Yt3D(DownTop3DToLeft(c),DownTop3DToRight(c))
def DownTop3DToTopDownReduced(c: vs.VideoNode): return TopDown3DReduced(DownTop3DToLeft(c),DownTop3DToRight(c))
def DownTop3DToDownTopReduced(c: vs.VideoNode): return DownTop3DReduced(DownTop3DToLeft(c),DownTop3DToRight(c))
def DownTop3DToHDMI(c: vs.VideoNode): return HDMI3D(DownTop3DToLeft(c),DownTop3DToRight(c))
def DownTop3DToAlternatingLeftRight(c: vs.VideoNode): return AlternatingLeftRight3D(DownTop3DToLeft(c),DownTop3DToRight(c))
def DownTop3DToAlternatingCrossEyed(c: vs.VideoNode): return AlternatingCrossEyed3D(DownTop3DToLeft(c),DownTop3DToRight(c))
def DownTop3DToInterleaveRowsLeftRight(c: vs.VideoNode): return InterleaveRowsLeftRight3D(DownTop3DToLeft(c),DownTop3DToRight(c))
def DownTop3DToInterleaveRowsCrossEyed(c: vs.VideoNode): return InterleaveRowsCrossEyed3D(DownTop3DToLeft(c),DownTop3DToRight(c))
def DownTop3DToInterleaveColsLeftRight(c: vs.VideoNode): return InterleaveColsLeftRight3D(DownTop3DToLeft(c),DownTop3DToRight(c))
def DownTop3DToInterleaveColsCrossEyed(c: vs.VideoNode): return InterleaveColsCrossEyed3D(DownTop3DToLeft(c),DownTop3DToRight(c))
def DownTop3DToGBAnaglyph(c: vs.VideoNode): return GBAnaglyph(DownTop3DToLeft(c),DownTop3DToRight(c))
def DownTop3DToRBAnaglyph(c: vs.VideoNode): return RBAnaglyph(DownTop3DToLeft(c),DownTop3DToRight(c))
def DownTop3DToRGAnaglyph(c: vs.VideoNode): return RGAnaglyph(DownTop3DToLeft(c),DownTop3DToRight(c))
def DownTop3DToRCAnaglyph(c: vs.VideoNode): return RCAnaglyph(DownTop3DToLeft(c),DownTop3DToRight(c))
def DownTop3DToGMAnaglyph(c: vs.VideoNode): return GMAnaglyph(DownTop3DToLeft(c),DownTop3DToRight(c))
def DownTop3DToYBAnaglyph(c: vs.VideoNode): return YBAnaglyph(DownTop3DToLeft(c),DownTop3DToRight(c))

# Convert an HDMI video to other formats.

def HDMI3DToLeftRight(c: vs.VideoNode): return LeftRight3D(HDMI3DToLeft(c),HDMI3DToRight(c))
def HDMI3DToCrossEyed(c: vs.VideoNode): return CrossEyed3D(HDMI3DToLeft(c),HDMI3DToRight(c))
def HDMI3DToTopDown(c: vs.VideoNode): return TopDown3D(HDMI3DToLeft(c),HDMI3DToRight(c))
def HDMI3DToDownTop(c: vs.VideoNode): return DownTop3D(HDMI3DToLeft(c),HDMI3DToRight(c))
def HDMI3DToLeftRightReduced(c: vs.VideoNode): return LeftRight3DReduced(HDMI3DToLeft(c),HDMI3DToRight(c))
def HDMI3DToCrossEyedReduced(c: vs.VideoNode): return CrossEyed3DReduced(HDMI3DToLeft(c),HDMI3DToRight(c))
def HDMI3DToYt3D(c: vs.VideoNode): return Yt3D(HDMI3DToLeft(c),HDMI3DToRight(c))
def HDMI3DToTopDownReduced(c: vs.VideoNode): return TopDown3DReduced(HDMI3DToLeft(c),HDMI3DToRight(c))
def HDMI3DToDownTopReduced(c: vs.VideoNode): return DownTop3DReduced(HDMI3DToLeft(c),HDMI3DToRight(c))
def HDMI3DToAlternatingLeftRight(c: vs.VideoNode): return AlternatingLeftRight3D(HDMI3DToLeft(c),HDMI3DToRight(c))
def HDMI3DToAlternatingCrossEyed(c: vs.VideoNode): return AlternatingCrossEyed3D(HDMI3DToLeft(c),HDMI3DToRight(c))
def HDMI3DToInterleaveRowsLeftRight(c: vs.VideoNode): return InterleaveRowsLeftRight3D(HDMI3DToLeft(c),HDMI3DToRight(c))
def HDMI3DToInterleaveRowsCrossEyed(c: vs.VideoNode): return InterleaveRowsCrossEyed3D(HDMI3DToLeft(c),HDMI3DToRight(c))
def HDMI3DToInterleaveColsLeftRight(c: vs.VideoNode): return InterleaveColsLeftRight3D(HDMI3DToLeft(c),HDMI3DToRight(c))
def HDMI3DToInterleaveColsCrossEyed(c: vs.VideoNode): return InterleaveColsCrossEyed3D(HDMI3DToLeft(c),HDMI3DToRight(c))
def HDMI3DToGBAnaglyph(c: vs.VideoNode): return GBAnaglyph(HDMI3DToLeft(c),HDMI3DToRight(c))
def HDMI3DToRBAnaglyph(c: vs.VideoNode): return RBAnaglyph(HDMI3DToLeft(c),HDMI3DToRight(c))
def HDMI3DToRGAnaglyph(c: vs.VideoNode): return RGAnaglyph(HDMI3DToLeft(c),HDMI3DToRight(c))
def HDMI3DToRCAnaglyph(c: vs.VideoNode): return RCAnaglyph(HDMI3DToLeft(c),HDMI3DToRight(c))
def HDMI3DToGMAnaglyph(c: vs.VideoNode): return GMAnaglyph(HDMI3DToLeft(c),HDMI3DToRight(c))
def HDMI3DToYBAnaglyph(c: vs.VideoNode): return YBAnaglyph(HDMI3DToLeft(c),HDMI3DToRight(c))

# Convert a reduced left/right video to other formats.

def LeftRight3DReducedToLeftRight(c: vs.VideoNode): return LeftRight3D(LeftRight3DReducedToLeft(c),LeftRight3DReducedToRight(c))
def LeftRight3DReducedToCrossEyed(c: vs.VideoNode): return CrossEyed3D(LeftRight3DReducedToLeft(c),LeftRight3DReducedToRight(c))
def LeftRight3DReducedToTopDown(c: vs.VideoNode): return TopDown3D(LeftRight3DReducedToLeft(c),LeftRight3DReducedToRight(c))
def LeftRight3DReducedToDownTop(c: vs.VideoNode): return DownTop3D(LeftRight3DReducedToLeft(c),LeftRight3DReducedToRight(c))
def LeftRight3DReducedToCrossEyedReduced(c: vs.VideoNode): return CrossEyed3D(LeftRight3DToLeft(c),LeftRight3DToRight(c))
def LeftRight3DReducedToYt3D(c: vs.VideoNode): return CrossEyed3D(LeftRight3DToLeft(c),LeftRight3DToRight(c))
def LeftRight3DReducedToTopDownReduced(c: vs.VideoNode): return TopDown3DReduced(LeftRight3DReducedToLeft(c),LeftRight3DReducedToRight(c))
def LeftRight3DReducedToDownTopReduced(c: vs.VideoNode): return DownTop3DReduced(LeftRight3DReducedToLeft(c),LeftRight3DReducedToRight(c))
def LeftRight3DReducedToHDMI(c: vs.VideoNode): return HDMI3D(LeftRight3DReducedToLeft(c),LeftRight3DReducedToRight(c))
def LeftRight3DReducedToAlternatingLeftRight(c: vs.VideoNode): return AlternatingLeftRight3D(LeftRight3DReducedToLeft(c),LeftRight3DReducedToRight(c))
def LeftRight3DReducedToAlternatingCrossEyed(c: vs.VideoNode): return AlternatingCrossEyed3D(LeftRight3DReducedToLeft(c),LeftRight3DReducedToRight(c))
def LeftRight3DReducedToInterleaveRowsLeftRight(c: vs.VideoNode): return InterleaveRowsLeftRight3D(LeftRight3DReducedToLeft(c),LeftRight3DReducedToRight(c))
def LeftRight3DReducedToInterleaveRowsCrossEyed(c: vs.VideoNode): return InterleaveRowsCrossEyed3D(LeftRight3DReducedToLeft(c),LeftRight3DReducedToRight(c))
def LeftRight3DReducedToInterleaveColsLeftRight(c: vs.VideoNode): return InterleaveColsLeftRight3D(LeftRight3DReducedToLeft(c),LeftRight3DReducedToRight(c))
def LeftRight3DReducedToInterleaveColsCrossEyed(c: vs.VideoNode): return InterleaveColsCrossEyed3D(LeftRight3DReducedToLeft(c),LeftRight3DReducedToRight(c))
def LeftRight3DReducedToGBAnaglyph(c: vs.VideoNode): return GBAnaglyph(LeftRight3DReducedToLeft(c),LeftRight3DReducedToRight(c))
def LeftRight3DReducedToRBAnaglyph(c: vs.VideoNode): return RBAnaglyph(LeftRight3DReducedToLeft(c),LeftRight3DReducedToRight(c))
def LeftRight3DReducedToRGAnaglyph(c: vs.VideoNode): return RGAnaglyph(LeftRight3DReducedToLeft(c),LeftRight3DReducedToRight(c))
def LeftRight3DReducedToRCAnaglyph(c: vs.VideoNode): return RCAnaglyph(LeftRight3DReducedToLeft(c),LeftRight3DReducedToRight(c))
def LeftRight3DReducedToGMAnaglyph(c: vs.VideoNode): return GMAnaglyph(LeftRight3DReducedToLeft(c),LeftRight3DReducedToRight(c))
def LeftRight3DReducedToYBAnaglyph(c: vs.VideoNode): return YBAnaglyph(LeftRight3DReducedToLeft(c),LeftRight3DReducedToRight(c))

# Convert a reduced cross-eyed video to other formats.

def CrossEyed3DReducedToLeftRight(c: vs.VideoNode): return LeftRight3D(CrossEyed3DReducedToLeft(c),CrossEyed3DReducedToRight(c))
def CrossEyed3DReducedToCrossEyed(c: vs.VideoNode): return CrossEyed3D(CrossEyed3DReducedToLeft(c),CrossEyed3DReducedToRight(c))
def CrossEyed3DReducedToTopDown(c: vs.VideoNode): return TopDown3D(CrossEyed3DReducedToLeft(c),CrossEyed3DReducedToRight(c))
def CrossEyed3DReducedToDownTop(c: vs.VideoNode): return DownTop3D(CrossEyed3DReducedToLeft(c),CrossEyed3DReducedToRight(c))
def CrossEyed3DReducedToLeftRightReduced(c: vs.VideoNode): return LeftRight3D(CrossEyed3DToLeft(c),CrossEyed3DToRight(c))
def CrossEyed3DReducedToYt3D(c: vs.VideoNode): return c
def CrossEyed3DReducedToTopDownReduced(c: vs.VideoNode): return TopDown3DReduced(CrossEyed3DReducedToLeft(c),CrossEyed3DReducedToRight(c))
def CrossEyed3DReducedToDownTopReduced(c: vs.VideoNode): return DownTop3DReduced(CrossEyed3DReducedToLeft(c),CrossEyed3DReducedToRight(c))
def CrossEyed3DReducedToHDMI(c: vs.VideoNode): return HDMI3D(CrossEyed3DReducedToLeft(c),CrossEyed3DReducedToRight(c))
def CrossEyed3DReducedToAlternatingLeftRight(c: vs.VideoNode): return AlternatingLeftRight3D(CrossEyed3DReducedToLeft(c),CrossEyed3DReducedToRight(c))
def CrossEyed3DReducedToAlternatingCrossEyed(c: vs.VideoNode): return AlternatingCrossEyed3D(CrossEyed3DReducedToLeft(c),CrossEyed3DReducedToRight(c))
def CrossEyed3DReducedToInterleaveRowsLeftRight(c: vs.VideoNode): return InterleaveRowsLeftRight3D(CrossEyed3DReducedToLeft(c),CrossEyed3DReducedToRight(c))
def CrossEyed3DReducedToInterleaveRowsCrossEyed(c: vs.VideoNode): return InterleaveRowsCrossEyed3D(CrossEyed3DReducedToLeft(c),CrossEyed3DReducedToRight(c))
def CrossEyed3DReducedToInterleaveColsLeftRight(c: vs.VideoNode): return InterleaveColsLeftRight3D(CrossEyed3DReducedToLeft(c),CrossEyed3DReducedToRight(c))
def CrossEyed3DReducedToInterleaveColsCrossEyed(c: vs.VideoNode): return InterleaveColsCrossEyed3D(CrossEyed3DReducedToLeft(c),CrossEyed3DReducedToRight(c))
def CrossEyed3DReducedToGBAnaglyph(c: vs.VideoNode): return GBAnaglyph(CrossEyed3DReducedToLeft(c),CrossEyed3DReducedToRight(c))
def CrossEyed3DReducedToRBAnaglyph(c: vs.VideoNode): return RBAnaglyph(CrossEyed3DReducedToLeft(c),CrossEyed3DReducedToRight(c))
def CrossEyed3DReducedToRGAnaglyph(c: vs.VideoNode): return RGAnaglyph(CrossEyed3DReducedToLeft(c),CrossEyed3DReducedToRight(c))
def CrossEyed3DReducedToRCAnaglyph(c: vs.VideoNode): return RCAnaglyph(CrossEyed3DReducedToLeft(c),CrossEyed3DReducedToRight(c))
def CrossEyed3DReducedToGMAnaglyph(c: vs.VideoNode): return GMAnaglyph(CrossEyed3DReducedToLeft(c),CrossEyed3DReducedToRight(c))
def CrossEyed3DReducedToYBAnaglyph(c: vs.VideoNode): return YBAnaglyph(CrossEyed3DReducedToLeft(c),CrossEyed3DReducedToRight(c))

# Convert a Yt3D video to other formats.

def Yt3DToLeftRight(c: vs.VideoNode): return LeftRight3D(Yt3DToLeft(c),Yt3DToRight(c))
def Yt3DToCrossEyed(c: vs.VideoNode): return CrossEyed3D(Yt3DToLeft(c),Yt3DToRight(c))
def Yt3DToTopDown(c: vs.VideoNode): return TopDown3D(Yt3DToLeft(c),Yt3DToRight(c))
def Yt3DToDownTop(c: vs.VideoNode): return DownTop3D(Yt3DToLeft(c),Yt3DToRight(c))
def Yt3DToLeftRightReduced(c: vs.VideoNode): return LeftRight3D(CrossEyed3DToLeft(c),CrossEyed3DToRight(c))
def Yt3DToCrossEyedReduced(c: vs.VideoNode): return c
def Yt3DToTopDownReduced(c: vs.VideoNode): return TopDown3DReduced(Yt3DToLeft(c),Yt3DToRight(c))
def Yt3DToDownTopReduced(c: vs.VideoNode): return DownTop3DReduced(Yt3DToLeft(c),Yt3DToRight(c))
def Yt3DToHDMI(c: vs.VideoNode): return HDMI3D(Yt3DToLeft(c),Yt3DToRight(c))
def Yt3DToAlternatingLeftRight(c: vs.VideoNode): return AlternatingLeftRight3D(Yt3DToLeft(c),Yt3DToRight(c))
def Yt3DToAlternatingCrossEyed(c: vs.VideoNode): return AlternatingCrossEyed3D(Yt3DToLeft(c),Yt3DToRight(c))
def Yt3DToInterleaveRowsLeftRight(c: vs.VideoNode): return InterleaveRowsLeftRight3D(Yt3DToLeft(c),Yt3DToRight(c))
def Yt3DToInterleaveRowsCrossEyed(c: vs.VideoNode): return InterleaveRowsCrossEyed3D(Yt3DToLeft(c),Yt3DToRight(c))
def Yt3DToInterleaveColsLeftRight(c: vs.VideoNode): return InterleaveColsLeftRight3D(Yt3DToLeft(c),Yt3DToRight(c))
def Yt3DToInterleaveColsCrossEyed(c: vs.VideoNode): return InterleaveColsCrossEyed3D(Yt3DToLeft(c),Yt3DToRight(c))
def Yt3DToGBAnaglyph(c: vs.VideoNode): return GBAnaglyph(Yt3DToLeft(c),Yt3DToRight(c))
def Yt3DToRBAnaglyph(c: vs.VideoNode): return RBAnaglyph(Yt3DToLeft(c),Yt3DToRight(c))
def Yt3DToRGAnaglyph(c: vs.VideoNode): return RGAnaglyph(Yt3DToLeft(c),Yt3DToRight(c))
def Yt3DToRCAnaglyph(c: vs.VideoNode): return RCAnaglyph(Yt3DToLeft(c),Yt3DToRight(c))
def Yt3DToGMAnaglyph(c: vs.VideoNode): return GMAnaglyph(Yt3DToLeft(c),Yt3DToRight(c))
def Yt3DToYBAnaglyph(c: vs.VideoNode): return YBAnaglyph(Yt3DToLeft(c),Yt3DToRight(c))

# Convert a reduced top/down video to other formats.

def TopDown3DReducedToLeftRight(c: vs.VideoNode): return LeftRight3D(TopDown3DReducedToLeft(c),TopDown3DReducedToRight(c))
def TopDown3DReducedToCrossEyed(c: vs.VideoNode): return CrossEyed3D(TopDown3DReducedToLeft(c),TopDown3DReducedToRight(c))
def TopDown3DReducedToTopDown(c: vs.VideoNode): return TopDown3D(TopDown3DReducedToLeft(c),TopDown3DReducedToRight(c))
def TopDown3DReducedToDownTop(c: vs.VideoNode): return DownTop3D(TopDown3DReducedToLeft(c),TopDown3DReducedToRight(c))
def TopDown3DReducedToLeftRightReduced(c: vs.VideoNode): return LeftRight3DReduced(TopDown3DReducedToLeft(c),TopDown3DReducedToRight(c))
def TopDown3DReducedToCrossEyedReduced(c: vs.VideoNode): return CrossEyed3DReduced(TopDown3DReducedToLeft(c),TopDown3DReducedToRight(c))
def TopDown3DReducedToYt3D(c: vs.VideoNode): return Yt3D(TopDown3DReducedToLeft(c),TopDown3DReducedToRight(c))
def TopDown3DReducedToDownTopReduced(c: vs.VideoNode): return DownTop3D(TopDown3DToLeft(c),TopDown3DToRight(c))
def TopDown3DReducedToHDMI(c: vs.VideoNode): return HDMI3D(TopDown3DReducedToLeft(c),TopDown3DReducedToRight(c))
def TopDown3DReducedToAlternatingLeftRight(c: vs.VideoNode): return AlternatingLeftRight3D(TopDown3DReducedToLeft(c),TopDown3DReducedToRight(c))
def TopDown3DReducedToAlternatingCrossEyed(c: vs.VideoNode): return AlternatingCrossEyed3D(TopDown3DReducedToLeft(c),TopDown3DReducedToRight(c))
def TopDown3DReducedToInterleaveRowsLeftRight(c: vs.VideoNode): return InterleaveRowsLeftRight3D(TopDown3DReducedToLeft(c),TopDown3DReducedToRight(c))
def TopDown3DReducedToInterleaveRowsCrossEyed(c: vs.VideoNode): return InterleaveRowsCrossEyed3D(TopDown3DReducedToLeft(c),TopDown3DReducedToRight(c))
def TopDown3DReducedToInterleaveColsLeftRight(c: vs.VideoNode): return InterleaveColsLeftRight3D(TopDown3DReducedToLeft(c),TopDown3DReducedToRight(c))
def TopDown3DReducedToInterleaveColsCrossEyed(c: vs.VideoNode): return InterleaveColsCrossEyed3D(TopDown3DReducedToLeft(c),TopDown3DReducedToRight(c))
def TopDown3DReducedToGBAnaglyph(c: vs.VideoNode): return GBAnaglyph(TopDown3DReducedToLeft(c),TopDown3DReducedToRight(c))
def TopDown3DReducedToRBAnaglyph(c: vs.VideoNode): return RBAnaglyph(TopDown3DReducedToLeft(c),TopDown3DReducedToRight(c))
def TopDown3DReducedToRGAnaglyph(c: vs.VideoNode): return RGAnaglyph(TopDown3DReducedToLeft(c),TopDown3DReducedToRight(c))
def TopDown3DReducedToRCAnaglyph(c: vs.VideoNode): return RCAnaglyph(TopDown3DReducedToLeft(c),TopDown3DReducedToRight(c))
def TopDown3DReducedToGMAnaglyph(c: vs.VideoNode): return GMAnaglyph(TopDown3DReducedToLeft(c),TopDown3DReducedToRight(c))
def TopDown3DReducedToYBAnaglyph(c: vs.VideoNode): return YBAnaglyph(TopDown3DReducedToLeft(c),TopDown3DReducedToRight(c))

# Convert a reduced down/top video to other formats.

def DownTop3DReducedToLeftRight(c: vs.VideoNode): return LeftRight3D(DownTop3DReducedToLeft(c),DownTop3DReducedToRight(c))
def DownTop3DReducedToCrossEyed(c: vs.VideoNode): return CrossEyed3D(DownTop3DReducedToLeft(c),DownTop3DReducedToRight(c))
def DownTop3DReducedToTopDown(c: vs.VideoNode): return TopDown3D(DownTop3DReducedToLeft(c),DownTop3DReducedToRight(c))
def DownTop3DReducedToDownTop(c: vs.VideoNode): return DownTop3D(DownTop3DReducedToLeft(c),DownTop3DReducedToRight(c))
def DownTop3DReducedToLeftRightReduced(c: vs.VideoNode): return LeftRight3DReduced(DownTop3DReducedToLeft(c),DownTop3DReducedToRight(c))
def DownTop3DReducedToCrossEyedReduced(c: vs.VideoNode): return CrossEyed3DReduced(DownTop3DReducedToLeft(c),DownTop3DReducedToRight(c))
def DownTop3DReducedToYt3D(c: vs.VideoNode): return Yt3D(DownTop3DReducedToLeft(c),DownTop3DReducedToRight(c))
def DownTop3DReducedToTopDownReduced(c: vs.VideoNode): return TopDown3D(DownTop3DToLeft(c),DownTop3DToRight(c))
def DownTop3DReducedToHDMI(c: vs.VideoNode): return HDMI3D(DownTop3DReducedToLeft(c),DownTop3DReducedToRight(c))
def DownTop3DReducedToAlternatingLeftRight(c: vs.VideoNode): return AlternatingLeftRight3D(DownTop3DReducedToLeft(c),DownTop3DReducedToRight(c))
def DownTop3DReducedToAlternatingCrossEyed(c: vs.VideoNode): return AlternatingCrossEyed3D(DownTop3DReducedToLeft(c),DownTop3DReducedToRight(c))
def DownTop3DReducedToInterleaveRowsLeftRight(c: vs.VideoNode): return InterleaveRowsLeftRight3D(DownTop3DReducedToLeft(c),DownTop3DReducedToRight(c))
def DownTop3DReducedToInterleaveRowsCrossEyed(c: vs.VideoNode): return InterleaveRowsCrossEyed3D(DownTop3DReducedToLeft(c),DownTop3DReducedToRight(c))
def DownTop3DReducedToInterleaveColsLeftRight(c: vs.VideoNode): return InterleaveColsLeftRight3D(DownTop3DReducedToLeft(c),DownTop3DReducedToRight(c))
def DownTop3DReducedToInterleaveColsCrossEyed(c: vs.VideoNode): return InterleaveColsCrossEyed3D(DownTop3DReducedToLeft(c),DownTop3DReducedToRight(c))
def DownTop3DReducedToGBAnaglyph(c: vs.VideoNode): return GBAnaglyph(DownTop3DReducedToLeft(c),DownTop3DReducedToRight(c))
def DownTop3DReducedToRBAnaglyph(c: vs.VideoNode): return RBAnaglyph(DownTop3DReducedToLeft(c),DownTop3DReducedToRight(c))
def DownTop3DReducedToRGAnaglyph(c: vs.VideoNode): return RGAnaglyph(DownTop3DReducedToLeft(c),DownTop3DReducedToRight(c))
def DownTop3DReducedToRCAnaglyph(c: vs.VideoNode): return RCAnaglyph(DownTop3DReducedToLeft(c),DownTop3DReducedToRight(c))
def DownTop3DReducedToGMAnaglyph(c: vs.VideoNode): return GMAnaglyph(DownTop3DReducedToLeft(c),DownTop3DReducedToRight(c))
def DownTop3DReducedToYBAnaglyph(c: vs.VideoNode): return YBAnaglyph(DownTop3DReducedToLeft(c),DownTop3DReducedToRight(c))

# Convert a left/right alternating frames video to other formats.

def AlternatingLeftRight3DToLeftRight(c: vs.VideoNode): return LeftRight3D(AlternatingLeftRight3DToLeft(c),AlternatingLeftRight3DToRight(c))
def AlternatingLeftRight3DToCrossEyed(c: vs.VideoNode): return CrossEyed3D(AlternatingLeftRight3DToLeft(c),AlternatingLeftRight3DToRight(c))
def AlternatingLeftRight3DToTopDown(c: vs.VideoNode): return TopDown3D(AlternatingLeftRight3DToLeft(c),AlternatingLeftRight3DToRight(c))
def AlternatingLeftRight3DToDownTop(c: vs.VideoNode): return DownTop3D(AlternatingLeftRight3DToLeft(c),AlternatingLeftRight3DToRight(c))
def AlternatingLeftRight3DToLeftRightReduced(c: vs.VideoNode): return LeftRight3DReduced(AlternatingLeftRight3DToLeft(c),AlternatingLeftRight3DToRight(c))
def AlternatingLeftRight3DToCrossEyedReduced(c: vs.VideoNode): return CrossEyed3DReduced(AlternatingLeftRight3DToLeft(c),AlternatingLeftRight3DToRight(c))
def AlternatingLeftRight3DToYt3D(c: vs.VideoNode): return Yt3D(AlternatingLeftRight3DToLeft(c),AlternatingLeftRight3DToRight(c))
def AlternatingLeftRight3DToTopDownReduced(c: vs.VideoNode): return TopDown3DReduced(AlternatingLeftRight3DToLeft(c),AlternatingLeftRight3DToRight(c))
def AlternatingLeftRight3DToDownTopReduced(c: vs.VideoNode): return DownTop3DReduced(AlternatingLeftRight3DToLeft(c),AlternatingLeftRight3DToRight(c))
def AlternatingLeftRight3DToHDMI(c: vs.VideoNode): return HDMI3D(AlternatingLeftRight3DToLeft(c),AlternatingLeftRight3DToRight(c))
def AlternatingLeftRight3DToAlternatingCrossEyed(c: vs.VideoNode): return AlternatingCrossEyed3D(AlternatingLeftRight3DToLeft(c),AlternatingLeftRight3DToRight(c))
def AlternatingLeftRight3DToInterleaveRowsLeftRight(c: vs.VideoNode): return InterleaveRowsLeftRight3D(AlternatingLeftRight3DToLeft(c),AlternatingLeftRight3DToRight(c))
def AlternatingLeftRight3DToInterleaveRowsCrossEyed(c: vs.VideoNode): return InterleaveRowsCrossEyed3D(AlternatingLeftRight3DToLeft(c),AlternatingLeftRight3DToRight(c))
def AlternatingLeftRight3DToInterleaveColsLeftRight(c: vs.VideoNode): return InterleaveColsLeftRight3D(AlternatingLeftRight3DToLeft(c),AlternatingLeftRight3DToRight(c))
def AlternatingLeftRight3DToInterleaveColsCrossEyed(c: vs.VideoNode): return InterleaveColsCrossEyed3D(AlternatingLeftRight3DToLeft(c),AlternatingLeftRight3DToRight(c))
def AlternatingLeftRight3DToGBAnaglyph(c: vs.VideoNode): return GBAnaglyph(AlternatingLeftRight3DToLeft(c),AlternatingLeftRight3DToRight(c))
def AlternatingLeftRight3DToRBAnaglyph(c: vs.VideoNode): return RBAnaglyph(AlternatingLeftRight3DToLeft(c),AlternatingLeftRight3DToRight(c))
def AlternatingLeftRight3DToRGAnaglyph(c: vs.VideoNode): return RGAnaglyph(AlternatingLeftRight3DToLeft(c),AlternatingLeftRight3DToRight(c))
def AlternatingLeftRight3DToRCAnaglyph(c: vs.VideoNode): return RCAnaglyph(AlternatingLeftRight3DToLeft(c),AlternatingLeftRight3DToRight(c))
def AlternatingLeftRight3DToGMAnaglyph(c: vs.VideoNode): return GMAnaglyph(AlternatingLeftRight3DToLeft(c),AlternatingLeftRight3DToRight(c))
def AlternatingLeftRight3DToYBAnaglyph(c: vs.VideoNode): return YBAnaglyph(AlternatingLeftRight3DToLeft(c),AlternatingLeftRight3DToRight(c))

# Convert a right/left alternating frames video to other formats.

def AlternatingCrossEyed3DToLeftRight(c: vs.VideoNode): return LeftRight3D(AlternatingCrossEyed3DToLeft(c),AlternatingCrossEyed3DToRight(c))
def AlternatingCrossEyed3DToCrossEyed(c: vs.VideoNode): return CrossEyed3D(AlternatingCrossEyed3DToLeft(c),AlternatingCrossEyed3DToRight(c))
def AlternatingCrossEyed3DToTopDown(c: vs.VideoNode): return TopDown3D(AlternatingCrossEyed3DToLeft(c),AlternatingCrossEyed3DToRight(c))
def AlternatingCrossEyed3DToDownTop(c: vs.VideoNode): return DownTop3D(AlternatingCrossEyed3DToLeft(c),AlternatingCrossEyed3DToRight(c))
def AlternatingCrossEyed3DToLeftRightReduced(c: vs.VideoNode): return LeftRight3DReduced(AlternatingCrossEyed3DToLeft(c),AlternatingCrossEyed3DToRight(c))
def AlternatingCrossEyed3DToCrossEyedReduced(c: vs.VideoNode): return CrossEyed3DReduced(AlternatingCrossEyed3DToLeft(c),AlternatingCrossEyed3DToRight(c))
def AlternatingCrossEyed3DToYt3D(c: vs.VideoNode): return Yt3D(AlternatingCrossEyed3DToLeft(c),AlternatingCrossEyed3DToRight(c))
def AlternatingCrossEyed3DToTopDownReduced(c: vs.VideoNode): return TopDown3DReduced(AlternatingCrossEyed3DToLeft(c),AlternatingCrossEyed3DToRight(c))
def AlternatingCrossEyed3DToDownTopReduced(c: vs.VideoNode): return DownTop3DReduced(AlternatingCrossEyed3DToLeft(c),AlternatingCrossEyed3DToRight(c))
def AlternatingCrossEyed3DToHDMI(c: vs.VideoNode): return HDMI3D(AlternatingCrossEyed3DToLeft(c),AlternatingCrossEyed3DToRight(c))
def AlternatingCrossEyed3DToAlternatingLeftRight(c: vs.VideoNode): return AlternatingLeftRight3D(AlternatingCrossEyed3DToLeft(c),AlternatingCrossEyed3DToRight(c))
def AlternatingCrossEyed3DToInterleaveRowsLeftRight(c: vs.VideoNode): return InterleaveRowsLeftRight3D(AlternatingCrossEyed3DToLeft(c),AlternatingCrossEyed3DToRight(c))
def AlternatingCrossEyed3DToInterleaveRowsCrossEyed(c: vs.VideoNode): return InterleaveRowsCrossEyed3D(AlternatingCrossEyed3DToLeft(c),AlternatingCrossEyed3DToRight(c))
def AlternatingCrossEyed3DToInterleaveColsLeftRight(c: vs.VideoNode): return InterleaveColsLeftRight3D(AlternatingCrossEyed3DToLeft(c),AlternatingCrossEyed3DToRight(c))
def AlternatingCrossEyed3DToInterleaveColsCrossEyed(c: vs.VideoNode): return InterleaveColsCrossEyed3D(AlternatingCrossEyed3DToLeft(c),AlternatingCrossEyed3DToRight(c))
def AlternatingCrossEyed3DToGBAnaglyph(c: vs.VideoNode): return GBAnaglyph(AlternatingCrossEyed3DToLeft(c),AlternatingCrossEyed3DToRight(c))
def AlternatingCrossEyed3DToRBAnaglyph(c: vs.VideoNode): return RBAnaglyph(AlternatingCrossEyed3DToLeft(c),AlternatingCrossEyed3DToRight(c))
def AlternatingCrossEyed3DToRGAnaglyph(c: vs.VideoNode): return RGAnaglyph(AlternatingCrossEyed3DToLeft(c),AlternatingCrossEyed3DToRight(c))
def AlternatingCrossEyed3DToRCAnaglyph(c: vs.VideoNode): return RCAnaglyph(AlternatingCrossEyed3DToLeft(c),AlternatingCrossEyed3DToRight(c))
def AlternatingCrossEyed3DToGMAnaglyph(c: vs.VideoNode): return GMAnaglyph(AlternatingCrossEyed3DToLeft(c),AlternatingCrossEyed3DToRight(c))
def AlternatingCrossEyed3DToYBAnaglyph(c: vs.VideoNode): return YBAnaglyph(AlternatingCrossEyed3DToLeft(c),AlternatingCrossEyed3DToRight(c))

# Convert a left/right interleave rows video to other formats.

def InterleaveRowsLeftRight3DToLeftRight(c: vs.VideoNode): return LeftRight3D(InterleaveRowsLeftRight3DToLeft(c),InterleaveRowsLeftRight3DToRight(c))
def InterleaveRowsLeftRight3DToCrossEyed(c: vs.VideoNode): return CrossEyed3D(InterleaveRowsLeftRight3DToLeft(c),InterleaveRowsLeftRight3DToRight(c))
def InterleaveRowsLeftRight3DToTopDown(c: vs.VideoNode): return TopDown3D(InterleaveRowsLeftRight3DToLeft(c),InterleaveRowsLeftRight3DToRight(c))
def InterleaveRowsLeftRight3DToDownTop(c: vs.VideoNode): return DownTop3D(InterleaveRowsLeftRight3DToLeft(c),InterleaveRowsLeftRight3DToRight(c))
def InterleaveRowsLeftRight3DToLeftRightReduced(c: vs.VideoNode): return LeftRight3DReduced(InterleaveRowsLeftRight3DToLeft(c),InterleaveRowsLeftRight3DToRight(c))
def InterleaveRowsLeftRight3DToCrossEyedReduced(c: vs.VideoNode): return CrossEyed3DReduced(InterleaveRowsLeftRight3DToLeft(c),InterleaveRowsLeftRight3DToRight(c))
def InterleaveRowsLeftRight3DToYt3D(c: vs.VideoNode): return Yt3D(InterleaveRowsLeftRight3DToLeft(c),InterleaveRowsLeftRight3DToRight(c))
def InterleaveRowsLeftRight3DToTopDownReduced(c: vs.VideoNode): return TopDown3DReduced(InterleaveRowsLeftRight3DToLeft(c),InterleaveRowsLeftRight3DToRight(c))
def InterleaveRowsLeftRight3DToDownTopReduced(c: vs.VideoNode): return DownTop3DReduced(InterleaveRowsLeftRight3DToLeft(c),InterleaveRowsLeftRight3DToRight(c))
def InterleaveRowsLeftRight3DToHDMI(c: vs.VideoNode): return HDMI3D(InterleaveRowsLeftRight3DToLeft(c),InterleaveRowsLeftRight3DToRight(c))
def InterleaveRowsLeftRight3DToAlternatingLeftRight(c: vs.VideoNode): return AlternatingLeftRight3D(InterleaveRowsLeftRight3DToLeft(c),InterleaveRowsLeftRight3DToRight(c))
def InterleaveRowsLeftRight3DToAlternatingCrossEyed(c: vs.VideoNode): return AlternatingCrossEyed3D(InterleaveRowsLeftRight3DToLeft(c),InterleaveRowsLeftRight3DToRight(c))
def InterleaveRowsLeftRight3DToInterleaveRowsCrossEyed(c: vs.VideoNode): return InterleaveRowsCrossEyed3D(InterleaveRowsLeftRight3DToLeft(c),InterleaveRowsLeftRight3DToRight(c))
def InterleaveRowsLeftRight3DToInterleaveColsLeftRight(c: vs.VideoNode): return InterleaveColsLeftRight3D(InterleaveRowsLeftRight3DToLeft(c),InterleaveRowsLeftRight3DToRight(c))
def InterleaveRowsLeftRight3DToInterleaveColsCrossEyed(c: vs.VideoNode): return InterleaveColsCrossEyed3D(InterleaveRowsLeftRight3DToLeft(c),InterleaveRowsLeftRight3DToRight(c))
def InterleaveRowsLeftRight3DToGBAnaglyph(c: vs.VideoNode): return GBAnaglyph(InterleaveRowsLeftRight3DToLeft(c),InterleaveRowsLeftRight3DToRight(c))
def InterleaveRowsLeftRight3DToRBAnaglyph(c: vs.VideoNode): return RBAnaglyph(InterleaveRowsLeftRight3DToLeft(c),InterleaveRowsLeftRight3DToRight(c))
def InterleaveRowsLeftRight3DToRGAnaglyph(c: vs.VideoNode): return RGAnaglyph(InterleaveRowsLeftRight3DToLeft(c),InterleaveRowsLeftRight3DToRight(c))
def InterleaveRowsLeftRight3DToRCAnaglyph(c: vs.VideoNode): return RCAnaglyph(InterleaveRowsLeftRight3DToLeft(c),InterleaveRowsLeftRight3DToRight(c))
def InterleaveRowsLeftRight3DToGMAnaglyph(c: vs.VideoNode): return GMAnaglyph(InterleaveRowsLeftRight3DToLeft(c),InterleaveRowsLeftRight3DToRight(c))
def InterleaveRowsLeftRight3DToYBAnaglyph(c: vs.VideoNode): return YBAnaglyph(InterleaveRowsLeftRight3DToLeft(c),InterleaveRowsLeftRight3DToRight(c))

# Convert a right/left interleave rows video to other formats.

def InterleaveRowsCrossEyed3DToLeftRight(c: vs.VideoNode): return LeftRight3D(InterleaveRowsCrossEyed3DToLeft(c),InterleaveRowsCrossEyed3DToRight(c))
def InterleaveRowsCrossEyed3DToCrossEyed(c: vs.VideoNode): return CrossEyed3D(InterleaveRowsCrossEyed3DToLeft(c),InterleaveRowsCrossEyed3DToRight(c))
def InterleaveRowsCrossEyed3DToTopDown(c: vs.VideoNode): return TopDown3D(InterleaveRowsCrossEyed3DToLeft(c),InterleaveRowsCrossEyed3DToRight(c))
def InterleaveRowsCrossEyed3DToDownTop(c: vs.VideoNode): return DownTop3D(InterleaveRowsCrossEyed3DToLeft(c),InterleaveRowsCrossEyed3DToRight(c))
def InterleaveRowsCrossEyed3DToLeftRightReduced(c: vs.VideoNode): return LeftRight3DReduced(InterleaveRowsCrossEyed3DToLeft(c),InterleaveRowsCrossEyed3DToRight(c))
def InterleaveRowsCrossEyed3DToCrossEyedReduced(c: vs.VideoNode): return CrossEyed3DReduced(InterleaveRowsCrossEyed3DToLeft(c),InterleaveRowsCrossEyed3DToRight(c))
def InterleaveRowsCrossEyed3DToYt3D(c: vs.VideoNode): return Yt3D(InterleaveRowsCrossEyed3DToLeft(c),InterleaveRowsCrossEyed3DToRight(c))
def InterleaveRowsCrossEyed3DToTopDownReduced(c: vs.VideoNode): return TopDown3DReduced(InterleaveRowsCrossEyed3DToLeft(c),InterleaveRowsCrossEyed3DToRight(c))
def InterleaveRowsCrossEyed3DToDownTopReduced(c: vs.VideoNode): return DownTop3DReduced(InterleaveRowsCrossEyed3DToLeft(c),InterleaveRowsCrossEyed3DToRight(c))
def InterleaveRowsCrossEyed3DToHDMI(c: vs.VideoNode): return HDMI3D(InterleaveRowsCrossEyed3DToLeft(c),InterleaveRowsCrossEyed3DToRight(c))
def InterleaveRowsCrossEyed3DToAlternatingLeftRight(c: vs.VideoNode): return AlternatingLeftRight3D(InterleaveRowsCrossEyed3DToLeft(c),InterleaveRowsCrossEyed3DToRight(c))
def InterleaveRowsCrossEyed3DToAlternatingCrossEyed(c: vs.VideoNode): return AlternatingCrossEyed3D(InterleaveRowsCrossEyed3DToLeft(c),InterleaveRowsCrossEyed3DToRight(c))
def InterleaveRowsCrossEyed3DToInterleaveRowsLeftRight(c: vs.VideoNode): return InterleaveRowsLeftRight3D(InterleaveRowsCrossEyed3DToLeft(c),InterleaveRowsCrossEyed3DToRight(c))
def InterleaveRowsCrossEyed3DToInterleaveColsLeftRight(c: vs.VideoNode): return InterleaveColsLeftRight3D(InterleaveRowsCrossEyed3DToLeft(c),InterleaveRowsCrossEyed3DToRight(c))
def InterleaveRowsCrossEyed3DToInterleaveColsCrossEyed(c: vs.VideoNode): return InterleaveColsCrossEyed3D(InterleaveRowsCrossEyed3DToLeft(c),InterleaveRowsCrossEyed3DToRight(c))
def InterleaveRowsCrossEyed3DToGBAnaglyph(c: vs.VideoNode): return GBAnaglyph(InterleaveRowsCrossEyed3DToLeft(c),InterleaveRowsCrossEyed3DToRight(c))
def InterleaveRowsCrossEyed3DToRBAnaglyph(c: vs.VideoNode): return RBAnaglyph(InterleaveRowsCrossEyed3DToLeft(c),InterleaveRowsCrossEyed3DToRight(c))
def InterleaveRowsCrossEyed3DToRGAnaglyph(c: vs.VideoNode): return RGAnaglyph(InterleaveRowsCrossEyed3DToLeft(c),InterleaveRowsCrossEyed3DToRight(c))
def InterleaveRowsCrossEyed3DToRCAnaglyph(c: vs.VideoNode): return RCAnaglyph(InterleaveRowsCrossEyed3DToLeft(c),InterleaveRowsCrossEyed3DToRight(c))
def InterleaveRowsCrossEyed3DToGMAnaglyph(c: vs.VideoNode): return GMAnaglyph(InterleaveRowsCrossEyed3DToLeft(c),InterleaveRowsCrossEyed3DToRight(c))
def InterleaveRowsCrossEyed3DToYBAnaglyph(c: vs.VideoNode): return YBAnaglyph(InterleaveRowsCrossEyed3DToLeft(c),InterleaveRowsCrossEyed3DToRight(c))

# Convert a left/right interleave columns video to other formats.

def InterleaveColsLeftRight3DToLeftRight(c: vs.VideoNode): return LeftRight3D(InterleaveColsLeftRight3DToLeft(c),InterleaveColsLeftRight3DToRight(c))
def InterleaveColsLeftRight3DToCrossEyed(c: vs.VideoNode): return CrossEyed3D(InterleaveColsLeftRight3DToLeft(c),InterleaveColsLeftRight3DToRight(c))
def InterleaveColsLeftRight3DToTopDown(c: vs.VideoNode): return TopDown3D(InterleaveColsLeftRight3DToLeft(c),InterleaveColsLeftRight3DToRight(c))
def InterleaveColsLeftRight3DToDownTop(c: vs.VideoNode): return DownTop3D(InterleaveColsLeftRight3DToLeft(c),InterleaveColsLeftRight3DToRight(c))
def InterleaveColsLeftRight3DToLeftRightReduced(c: vs.VideoNode): return LeftRight3DReduced(InterleaveColsLeftRight3DToLeft(c),InterleaveColsLeftRight3DToRight(c))
def InterleaveColsLeftRight3DToCrossEyedReduced(c: vs.VideoNode): return CrossEyed3DReduced(InterleaveColsLeftRight3DToLeft(c),InterleaveColsLeftRight3DToRight(c))
def InterleaveColsLeftRight3DToYt3D(c: vs.VideoNode): return Yt3D(InterleaveColsLeftRight3DToLeft(c),InterleaveColsLeftRight3DToRight(c))
def InterleaveColsLeftRight3DToTopDownReduced(c: vs.VideoNode): return TopDown3DReduced(InterleaveColsLeftRight3DToLeft(c),InterleaveColsLeftRight3DToRight(c))
def InterleaveColsLeftRight3DToDownTopReduced(c: vs.VideoNode): return DownTop3DReduced(InterleaveColsLeftRight3DToLeft(c),InterleaveColsLeftRight3DToRight(c))
def InterleaveColsLeftRight3DToHDMI(c: vs.VideoNode): return HDMI3D(InterleaveColsLeftRight3DToLeft(c),InterleaveColsLeftRight3DToRight(c))
def InterleaveColsLeftRight3DToAlternatingLeftRight(c: vs.VideoNode): return AlternatingLeftRight3D(InterleaveColsLeftRight3DToLeft(c),InterleaveColsLeftRight3DToRight(c))
def InterleaveColsLeftRight3DToAlternatingCrossEyed(c: vs.VideoNode): return AlternatingCrossEyed3D(InterleaveColsLeftRight3DToLeft(c),InterleaveColsLeftRight3DToRight(c))
def InterleaveColsLeftRight3DToInterleaveRowsLeftRight(c: vs.VideoNode): return InterleaveRowsLeftRight3D(InterleaveColsLeftRight3DToLeft(c),InterleaveColsLeftRight3DToRight(c))
def InterleaveColsLeftRight3DToInterleaveRowsCrossEyed(c: vs.VideoNode): return InterleaveRowsCrossEyed3D(InterleaveColsLeftRight3DToLeft(c),InterleaveColsLeftRight3DToRight(c))
def InterleaveColsLeftRight3DToInterleaveColsCrossEyed(c: vs.VideoNode): return InterleaveColsCrossEyed3D(InterleaveColsLeftRight3DToLeft(c),InterleaveColsLeftRight3DToRight(c))
def InterleaveColsLeftRight3DToGBAnaglyph(c: vs.VideoNode): return GBAnaglyph(InterleaveColsLeftRight3DToLeft(c),InterleaveColsLeftRight3DToRight(c))
def InterleaveColsLeftRight3DToRBAnaglyph(c: vs.VideoNode): return RBAnaglyph(InterleaveColsLeftRight3DToLeft(c),InterleaveColsLeftRight3DToRight(c))
def InterleaveColsLeftRight3DToRGAnaglyph(c: vs.VideoNode): return RGAnaglyph(InterleaveColsLeftRight3DToLeft(c),InterleaveColsLeftRight3DToRight(c))
def InterleaveColsLeftRight3DToRCAnaglyph(c: vs.VideoNode): return RCAnaglyph(InterleaveColsLeftRight3DToLeft(c),InterleaveColsLeftRight3DToRight(c))
def InterleaveColsLeftRight3DToGMAnaglyph(c: vs.VideoNode): return GMAnaglyph(InterleaveColsLeftRight3DToLeft(c),InterleaveColsLeftRight3DToRight(c))
def InterleaveColsLeftRight3DToYBAnaglyph(c: vs.VideoNode): return YBAnaglyph(InterleaveColsLeftRight3DToLeft(c),InterleaveColsLeftRight3DToRight(c))

# Convert a right/left interleave columns video to other formats.

def InterleaveColsCrossEyed3DToLeftRight(c: vs.VideoNode): return LeftRight3D(InterleaveColsCrossEyed3DToLeft(c),InterleaveColsCrossEyed3DToRight(c))
def InterleaveColsCrossEyed3DToCrossEyed(c: vs.VideoNode): return CrossEyed3D(InterleaveColsCrossEyed3DToLeft(c),InterleaveColsCrossEyed3DToRight(c))
def InterleaveColsCrossEyed3DToTopDown(c: vs.VideoNode): return TopDown3D(InterleaveColsCrossEyed3DToLeft(c),InterleaveColsCrossEyed3DToRight(c))
def InterleaveColsCrossEyed3DToDownTop(c: vs.VideoNode): return DownTop3D(InterleaveColsCrossEyed3DToLeft(c),InterleaveColsCrossEyed3DToRight(c))
def InterleaveColsCrossEyed3DToLeftRightReduced(c: vs.VideoNode): return LeftRight3DReduced(InterleaveColsCrossEyed3DToLeft(c),InterleaveColsCrossEyed3DToRight(c))
def InterleaveColsCrossEyed3DToCrossEyedReduced(c: vs.VideoNode): return CrossEyed3DReduced(InterleaveColsCrossEyed3DToLeft(c),InterleaveColsCrossEyed3DToRight(c))
def InterleaveColsCrossEyed3DToYt3D(c: vs.VideoNode): return Yt3D(InterleaveColsCrossEyed3DToLeft(c),InterleaveColsCrossEyed3DToRight(c))
def InterleaveColsCrossEyed3DToTopDownReduced(c: vs.VideoNode): return TopDown3DReduced(InterleaveColsCrossEyed3DToLeft(c),InterleaveColsCrossEyed3DToRight(c))
def InterleaveColsCrossEyed3DToDownTopReduced(c: vs.VideoNode): return DownTop3DReduced(InterleaveColsCrossEyed3DToLeft(c),InterleaveColsCrossEyed3DToRight(c))
def InterleaveColsCrossEyed3DToHDMI(c: vs.VideoNode): return HDMI3D(InterleaveColsCrossEyed3DToLeft(c),InterleaveColsCrossEyed3DToRight(c))
def InterleaveColsCrossEyed3DToAlternatingLeftRight(c: vs.VideoNode): return AlternatingLeftRight3D(InterleaveColsCrossEyed3DToLeft(c),InterleaveColsCrossEyed3DToRight(c))
def InterleaveColsCrossEyed3DToAlternatingCrossEyed(c: vs.VideoNode): return AlternatingCrossEyed3D(InterleaveColsCrossEyed3DToLeft(c),InterleaveColsCrossEyed3DToRight(c))
def InterleaveColsCrossEyed3DToInterleaveRowsLeftRight(c: vs.VideoNode): return InterleaveRowsLeftRight3D(InterleaveColsCrossEyed3DToLeft(c),InterleaveColsCrossEyed3DToRight(c))
def InterleaveColsCrossEyed3DToInterleaveRowsCrossEyed(c: vs.VideoNode): return InterleaveRowsCrossEyed3D(InterleaveColsCrossEyed3DToLeft(c),InterleaveColsCrossEyed3DToRight(c))
def InterleaveColsCrossEyed3DToInterleaveColsLeftRight(c: vs.VideoNode): return InterleaveColsLeftRight3D(InterleaveColsCrossEyed3DToLeft(c),InterleaveColsCrossEyed3DToRight(c))
def InterleaveColsCrossEyed3DToGBAnaglyph(c: vs.VideoNode): return GBAnaglyph(InterleaveColsCrossEyed3DToLeft(c),InterleaveColsCrossEyed3DToRight(c))
def InterleaveColsCrossEyed3DToRBAnaglyph(c: vs.VideoNode): return RBAnaglyph(InterleaveColsCrossEyed3DToLeft(c),InterleaveColsCrossEyed3DToRight(c))
def InterleaveColsCrossEyed3DToRGAnaglyph(c: vs.VideoNode): return RGAnaglyph(InterleaveColsCrossEyed3DToLeft(c),InterleaveColsCrossEyed3DToRight(c))
def InterleaveColsCrossEyed3DToRCAnaglyph(c: vs.VideoNode): return RCAnaglyph(InterleaveColsCrossEyed3DToLeft(c),InterleaveColsCrossEyed3DToRight(c))
def InterleaveColsCrossEyed3DToGMAnaglyph(c: vs.VideoNode): return GMAnaglyph(InterleaveColsCrossEyed3DToLeft(c),InterleaveColsCrossEyed3DToRight(c))
def InterleaveColsCrossEyed3DToYBAnaglyph(c: vs.VideoNode): return YBAnaglyph(InterleaveColsCrossEyed3DToLeft(c),InterleaveColsCrossEyed3DToRight(c))

# Convert a green/blue anaglyph video to other formats.

def GBAnaglyphToLeftRight(c: vs.VideoNode): return LeftRight3D(GBAnaglyphToLeft(c),GBAnaglyphToRight(c))
def GBAnaglyphToCrossEyed(c: vs.VideoNode): return CrossEyed3D(GBAnaglyphToLeft(c),GBAnaglyphToRight(c))
def GBAnaglyphToTopDown(c: vs.VideoNode): return TopDown3D(GBAnaglyphToLeft(c),GBAnaglyphToRight(c))
def GBAnaglyphToDownTop(c: vs.VideoNode): return DownTop3D(GBAnaglyphToLeft(c),GBAnaglyphToRight(c))
def GBAnaglyphToLeftRightReduced(c: vs.VideoNode): return LeftRight3DReduced(GBAnaglyphToLeft(c),GBAnaglyphToRight(c))
def GBAnaglyphToCrossEyedReduced(c: vs.VideoNode): return CrossEyed3DReduced(GBAnaglyphToLeft(c),GBAnaglyphToRight(c))
def GBAnaglyphToYt3D(c: vs.VideoNode): return Yt3D(GBAnaglyphToLeft(c),GBAnaglyphToRight(c))
def GBAnaglyphToTopDownReduced(c: vs.VideoNode): return TopDown3DReduced(GBAnaglyphToLeft(c),GBAnaglyphToRight(c))
def GBAnaglyphToDownTopReduced(c: vs.VideoNode): return DownTop3DReduced(GBAnaglyphToLeft(c),GBAnaglyphToRight(c))
def GBAnaglyphToHDMI(c: vs.VideoNode): return HDMI3D(GBAnaglyphToLeft(c),GBAnaglyphToRight(c))
def GBAnaglyphToAlternatingLeftRight(c: vs.VideoNode): return AlternatingLeftRight3D(GBAnaglyphToLeft(c),GBAnaglyphToRight(c))
def GBAnaglyphToAlternatingCrossEyed(c: vs.VideoNode): return AlternatingCrossEyed3D(GBAnaglyphToLeft(c),GBAnaglyphToRight(c))
def GBAnaglyphToInterleaveRowsLeftRight(c: vs.VideoNode): return InterleaveRowsLeftRight3D(GBAnaglyphToLeft(c),GBAnaglyphToRight(c))
def GBAnaglyphToInterleaveRowsCrossEyed(c: vs.VideoNode): return InterleaveRowsCrossEyed3D(GBAnaglyphToLeft(c),GBAnaglyphToRight(c))
def GBAnaglyphToInterleaveColsLeftRight(c: vs.VideoNode): return InterleaveColsLeftRight3D(GBAnaglyphToLeft(c),GBAnaglyphToRight(c))
def GBAnaglyphToInterleaveColsCrossEyed(c: vs.VideoNode): return InterleaveColsCrossEyed3D(GBAnaglyphToLeft(c),GBAnaglyphToRight(c))
def GBAnaglyphToRBAnaglyph(c: vs.VideoNode): return RBAnaglyph(GBAnaglyphToLeft(c),GBAnaglyphToRight(c))
def GBAnaglyphToRGAnaglyph(c: vs.VideoNode): return RGAnaglyph(GBAnaglyphToLeft(c),GBAnaglyphToRight(c))
def GBAnaglyphToRCAnaglyph(c: vs.VideoNode): return RCAnaglyph(GBAnaglyphToLeft(c),GBAnaglyphToRight(c))
def GBAnaglyphToGMAnaglyph(c: vs.VideoNode): return GMAnaglyph(GBAnaglyphToLeft(c),GBAnaglyphToRight(c))
def GBAnaglyphToYBAnaglyph(c: vs.VideoNode): return YBAnaglyph(GBAnaglyphToLeft(c),GBAnaglyphToRight(c))

# Convert a red/blue anaglyph video to other formats.

def RBAnaglyphToLeftRight(c: vs.VideoNode): return LeftRight3D(RBAnaglyphToLeft(c),RBAnaglyphToRight(c))
def RBAnaglyphToCrossEyed(c: vs.VideoNode): return CrossEyed3D(RBAnaglyphToLeft(c),RBAnaglyphToRight(c))
def RBAnaglyphToTopDown(c: vs.VideoNode): return TopDown3D(RBAnaglyphToLeft(c),RBAnaglyphToRight(c))
def RBAnaglyphToDownTop(c: vs.VideoNode): return DownTop3D(RBAnaglyphToLeft(c),RBAnaglyphToRight(c))
def RBAnaglyphToLeftRightReduced(c: vs.VideoNode): return LeftRight3DReduced(RBAnaglyphToLeft(c),RBAnaglyphToRight(c))
def RBAnaglyphToCrossEyedReduced(c: vs.VideoNode): return CrossEyed3DReduced(RBAnaglyphToLeft(c),RBAnaglyphToRight(c))
def RBAnaglyphToYt3D(c: vs.VideoNode): return Yt3D(RBAnaglyphToLeft(c),RBAnaglyphToRight(c))
def RBAnaglyphToTopDownReduced(c: vs.VideoNode): return TopDown3DReduced(RBAnaglyphToLeft(c),RBAnaglyphToRight(c))
def RBAnaglyphToDownTopReduced(c: vs.VideoNode): return DownTop3DReduced(RBAnaglyphToLeft(c),RBAnaglyphToRight(c))
def RBAnaglyphToHDMI(c: vs.VideoNode): return HDMI3D(RBAnaglyphToLeft(c),RBAnaglyphToRight(c))
def RBAnaglyphToAlternatingLeftRight(c: vs.VideoNode): return AlternatingLeftRight3D(RBAnaglyphToLeft(c),RBAnaglyphToRight(c))
def RBAnaglyphToAlternatingCrossEyed(c: vs.VideoNode): return AlternatingCrossEyed3D(RBAnaglyphToLeft(c),RBAnaglyphToRight(c))
def RBAnaglyphToInterleaveRowsLeftRight(c: vs.VideoNode): return InterleaveRowsLeftRight3D(RBAnaglyphToLeft(c),RBAnaglyphToRight(c))
def RBAnaglyphToInterleaveRowsCrossEyed(c: vs.VideoNode): return InterleaveRowsCrossEyed3D(RBAnaglyphToLeft(c),RBAnaglyphToRight(c))
def RBAnaglyphToInterleaveColsLeftRight(c: vs.VideoNode): return InterleaveColsLeftRight3D(RBAnaglyphToLeft(c),RBAnaglyphToRight(c))
def RBAnaglyphToInterleaveColsCrossEyed(c: vs.VideoNode): return InterleaveColsCrossEyed3D(RBAnaglyphToLeft(c),RBAnaglyphToRight(c))
def RBAnaglyphToGBAnaglyph(c: vs.VideoNode): return GBAnaglyph(RBAnaglyphToLeft(c),RBAnaglyphToRight(c))
def RBAnaglyphToRGAnaglyph(c: vs.VideoNode): return RGAnaglyph(RBAnaglyphToLeft(c),RBAnaglyphToRight(c))
def RBAnaglyphToRCAnaglyph(c: vs.VideoNode): return RCAnaglyph(RBAnaglyphToLeft(c),RBAnaglyphToRight(c))
def RBAnaglyphToGMAnaglyph(c: vs.VideoNode): return GMAnaglyph(RBAnaglyphToLeft(c),RBAnaglyphToRight(c))
def RBAnaglyphToYBAnaglyph(c: vs.VideoNode): return YBAnaglyph(RBAnaglyphToLeft(c),RBAnaglyphToRight(c))

# Convert a red/green anaglyph video to other formats.

def RGAnaglyphToLeftRight(c: vs.VideoNode): return LeftRight3D(RGAnaglyphToLeft(c),RGAnaglyphToRight(c))
def RGAnaglyphToCrossEyed(c: vs.VideoNode): return CrossEyed3D(RGAnaglyphToLeft(c),RGAnaglyphToRight(c))
def RGAnaglyphToTopDown(c: vs.VideoNode): return TopDown3D(RGAnaglyphToLeft(c),RGAnaglyphToRight(c))
def RGAnaglyphToDownTop(c: vs.VideoNode): return DownTop3D(RGAnaglyphToLeft(c),RGAnaglyphToRight(c))
def RGAnaglyphToLeftRightReduced(c: vs.VideoNode): return LeftRight3DReduced(RGAnaglyphToLeft(c),RGAnaglyphToRight(c))
def RGAnaglyphToCrossEyedReduced(c: vs.VideoNode): return CrossEyed3DReduced(RGAnaglyphToLeft(c),RGAnaglyphToRight(c))
def RGAnaglyphToYt3D(c: vs.VideoNode): return Yt3D(RGAnaglyphToLeft(c),RGAnaglyphToRight(c))
def RGAnaglyphToTopDownReduced(c: vs.VideoNode): return TopDown3DReduced(RGAnaglyphToLeft(c),RGAnaglyphToRight(c))
def RGAnaglyphToDownTopReduced(c: vs.VideoNode): return DownTop3DReduced(RGAnaglyphToLeft(c),RGAnaglyphToRight(c))
def RGAnaglyphToHDMI(c: vs.VideoNode): return HDMI3D(RGAnaglyphToLeft(c),RGAnaglyphToRight(c))
def RGAnaglyphToAlternatingLeftRight(c: vs.VideoNode): return AlternatingLeftRight3D(RGAnaglyphToLeft(c),RGAnaglyphToRight(c))
def RGAnaglyphToAlternatingCrossEyed(c: vs.VideoNode): return AlternatingCrossEyed3D(RGAnaglyphToLeft(c),RGAnaglyphToRight(c))
def RGAnaglyphToInterleaveRowsLeftRight(c: vs.VideoNode): return InterleaveRowsLeftRight3D(RGAnaglyphToLeft(c),RGAnaglyphToRight(c))
def RGAnaglyphToInterleaveRowsCrossEyed(c: vs.VideoNode): return InterleaveRowsCrossEyed3D(RGAnaglyphToLeft(c),RGAnaglyphToRight(c))
def RGAnaglyphToInterleaveColsLeftRight(c: vs.VideoNode): return InterleaveColsLeftRight3D(RGAnaglyphToLeft(c),RGAnaglyphToRight(c))
def RGAnaglyphToInterleaveColsCrossEyed(c: vs.VideoNode): return InterleaveColsCrossEyed3D(RGAnaglyphToLeft(c),RGAnaglyphToRight(c))
def RGAnaglyphToGBAnaglyph(c: vs.VideoNode): return GBAnaglyph(RGAnaglyphToLeft(c),RGAnaglyphToRight(c))
def RGAnaglyphToRBAnaglyph(c: vs.VideoNode): return RBAnaglyph(RGAnaglyphToLeft(c),RGAnaglyphToRight(c))
def RGAnaglyphToRCAnaglyph(c: vs.VideoNode): return RCAnaglyph(RGAnaglyphToLeft(c),RGAnaglyphToRight(c))
def RGAnaglyphToGMAnaglyph(c: vs.VideoNode): return GMAnaglyph(RGAnaglyphToLeft(c),RGAnaglyphToRight(c))
def RGAnaglyphToYBAnaglyph(c: vs.VideoNode): return YBAnaglyph(RGAnaglyphToLeft(c),RGAnaglyphToRight(c))

# Convert a red/cyan anaglyph video to other formats.

def RCAnaglyphToLeftRight(c: vs.VideoNode): return LeftRight3D(RCAnaglyphToLeft(c),RCAnaglyphToRight(c))
def RCAnaglyphToCrossEyed(c: vs.VideoNode): return CrossEyed3D(RCAnaglyphToLeft(c),RCAnaglyphToRight(c))
def RCAnaglyphToTopDown(c: vs.VideoNode): return TopDown3D(RCAnaglyphToLeft(c),RCAnaglyphToRight(c))
def RCAnaglyphToDownTop(c: vs.VideoNode): return DownTop3D(RCAnaglyphToLeft(c),RCAnaglyphToRight(c))
def RCAnaglyphToLeftRightReduced(c: vs.VideoNode): return LeftRight3DReduced(RCAnaglyphToLeft(c),RCAnaglyphToRight(c))
def RCAnaglyphToCrossEyedReduced(c: vs.VideoNode): return CrossEyed3DReduced(RCAnaglyphToLeft(c),RCAnaglyphToRight(c))
def RCAnaglyphToYt3D(c: vs.VideoNode): return Yt3D(RCAnaglyphToLeft(c),RCAnaglyphToRight(c))
def RCAnaglyphToTopDownReduced(c: vs.VideoNode): return TopDown3DReduced(RCAnaglyphToLeft(c),RCAnaglyphToRight(c))
def RCAnaglyphToDownTopReduced(c: vs.VideoNode): return DownTop3DReduced(RCAnaglyphToLeft(c),RCAnaglyphToRight(c))
def RCAnaglyphToHDMI(c: vs.VideoNode): return HDMI3D(RCAnaglyphToLeft(c),RCAnaglyphToRight(c))
def RCAnaglyphToAlternatingLeftRight(c: vs.VideoNode): return AlternatingLeftRight3D(RCAnaglyphToLeft(c),RCAnaglyphToRight(c))
def RCAnaglyphToAlternatingCrossEyed(c: vs.VideoNode): return AlternatingCrossEyed3D(RCAnaglyphToLeft(c),RCAnaglyphToRight(c))
def RCAnaglyphToInterleaveRowsLeftRight(c: vs.VideoNode): return InterleaveRowsLeftRight3D(RCAnaglyphToLeft(c),RCAnaglyphToRight(c))
def RCAnaglyphToInterleaveRowsCrossEyed(c: vs.VideoNode): return InterleaveRowsCrossEyed3D(RCAnaglyphToLeft(c),RCAnaglyphToRight(c))
def RCAnaglyphToInterleaveColsLeftRight(c: vs.VideoNode): return InterleaveColsLeftRight3D(RCAnaglyphToLeft(c),RCAnaglyphToRight(c))
def RCAnaglyphToInterleaveColsCrossEyed(c: vs.VideoNode): return InterleaveColsCrossEyed3D(RCAnaglyphToLeft(c),RCAnaglyphToRight(c))
def RCAnaglyphToGBAnaglyph(c: vs.VideoNode): return GBAnaglyph(RCAnaglyphToLeft(c),RCAnaglyphToRight(c))
def RCAnaglyphToRBAnaglyph(c: vs.VideoNode): return RBAnaglyph(RCAnaglyphToLeft(c),RCAnaglyphToRight(c))
def RCAnaglyphToRGAnaglyph(c: vs.VideoNode): return RGAnaglyph(RCAnaglyphToLeft(c),RCAnaglyphToRight(c))
def RCAnaglyphToGMAnaglyph(c: vs.VideoNode): return GMAnaglyph(RCAnaglyphToLeft(c),RCAnaglyphToRight(c))
def RCAnaglyphToYBAnaglyph(c: vs.VideoNode): return YBAnaglyph(RCAnaglyphToLeft(c),RCAnaglyphToRight(c))

# Convert a green/magneto anaglyph video to other formats.

def GMAnaglyphToLeftRight(c: vs.VideoNode): return LeftRight3D(GMAnaglyphToLeft(c),GMAnaglyphToRight(c))
def GMAnaglyphToCrossEyed(c: vs.VideoNode): return CrossEyed3D(GMAnaglyphToLeft(c),GMAnaglyphToRight(c))
def GMAnaglyphToTopDown(c: vs.VideoNode): return TopDown3D(GMAnaglyphToLeft(c),GMAnaglyphToRight(c))
def GMAnaglyphToDownTop(c: vs.VideoNode): return DownTop3D(GMAnaglyphToLeft(c),GMAnaglyphToRight(c))
def GMAnaglyphToLeftRightReduced(c: vs.VideoNode): return LeftRight3DReduced(GMAnaglyphToLeft(c),GMAnaglyphToRight(c))
def GMAnaglyphToCrossEyedReduced(c: vs.VideoNode): return CrossEyed3DReduced(GMAnaglyphToLeft(c),GMAnaglyphToRight(c))
def GMAnaglyphToYt3D(c: vs.VideoNode): return Yt3D(GMAnaglyphToLeft(c),GMAnaglyphToRight(c))
def GMAnaglyphToTopDownReduced(c: vs.VideoNode): return TopDown3DReduced(GMAnaglyphToLeft(c),GMAnaglyphToRight(c))
def GMAnaglyphToDownTopReduced(c: vs.VideoNode): return DownTop3DReduced(GMAnaglyphToLeft(c),GMAnaglyphToRight(c))
def GMAnaglyphToHDMI(c: vs.VideoNode): return HDMI3D(GMAnaglyphToLeft(c),GMAnaglyphToRight(c))
def GMAnaglyphToAlternatingLeftRight(c: vs.VideoNode): return AlternatingLeftRight3D(GMAnaglyphToLeft(c),GMAnaglyphToRight(c))
def GMAnaglyphToAlternatingCrossEyed(c: vs.VideoNode): return AlternatingCrossEyed3D(GMAnaglyphToLeft(c),GMAnaglyphToRight(c))
def GMAnaglyphToInterleaveRowsLeftRight(c: vs.VideoNode): return InterleaveRowsLeftRight3D(GMAnaglyphToLeft(c),GMAnaglyphToRight(c))
def GMAnaglyphToInterleaveRowsCrossEyed(c: vs.VideoNode): return InterleaveRowsCrossEyed3D(GMAnaglyphToLeft(c),GMAnaglyphToRight(c))
def GMAnaglyphToInterleaveColsLeftRight(c: vs.VideoNode): return InterleaveColsLeftRight3D(GMAnaglyphToLeft(c),GMAnaglyphToRight(c))
def GMAnaglyphToInterleaveColsCrossEyed(c: vs.VideoNode): return InterleaveColsCrossEyed3D(GMAnaglyphToLeft(c),GMAnaglyphToRight(c))
def GMAnaglyphToGBAnaglyph(c: vs.VideoNode): return GBAnaglyph(GMAnaglyphToLeft(c),GMAnaglyphToRight(c))
def GMAnaglyphToRBAnaglyph(c: vs.VideoNode): return RBAnaglyph(GMAnaglyphToLeft(c),GMAnaglyphToRight(c))
def GMAnaglyphToRGAnaglyph(c: vs.VideoNode): return RGAnaglyph(GMAnaglyphToLeft(c),GMAnaglyphToRight(c))
def GMAnaglyphToRCAnaglyph(c: vs.VideoNode): return RCAnaglyph(GMAnaglyphToLeft(c),GMAnaglyphToRight(c))
def GMAnaglyphToYBAnaglyph(c: vs.VideoNode): return YBAnaglyph(GMAnaglyphToLeft(c),GMAnaglyphToRight(c))

# Convert a yellow/blue anaglyph video to other formats.

def YBAnaglyphToLeftRight(c: vs.VideoNode): return LeftRight3D(YBAnaglyphToLeft(c),YBAnaglyphToRight(c))
def YBAnaglyphToCrossEyed(c: vs.VideoNode): return CrossEyed3D(YBAnaglyphToLeft(c),YBAnaglyphToRight(c))
def YBAnaglyphToTopDown(c: vs.VideoNode): return TopDown3D(YBAnaglyphToLeft(c),YBAnaglyphToRight(c))
def YBAnaglyphToDownTop(c: vs.VideoNode): return DownTop3D(YBAnaglyphToLeft(c),YBAnaglyphToRight(c))
def YBAnaglyphToLeftRightReduced(c: vs.VideoNode): return LeftRight3DReduced(YBAnaglyphToLeft(c),YBAnaglyphToRight(c))
def YBAnaglyphToCrossEyedReduced(c: vs.VideoNode): return CrossEyed3DReduced(YBAnaglyphToLeft(c),YBAnaglyphToRight(c))
def YBAnaglyphToYt3D(c: vs.VideoNode): return Yt3D(YBAnaglyphToLeft(c),YBAnaglyphToRight(c))
def YBAnaglyphToTopDownReduced(c: vs.VideoNode): return TopDown3DReduced(YBAnaglyphToLeft(c),YBAnaglyphToRight(c))
def YBAnaglyphToDownTopReduced(c: vs.VideoNode): return DownTop3DReduced(YBAnaglyphToLeft(c),YBAnaglyphToRight(c))
def YBAnaglyphToHDMI(c: vs.VideoNode): return HDMI3D(YBAnaglyphToLeft(c),YBAnaglyphToRight(c))
def YBAnaglyphToAlternatingLeftRight(c: vs.VideoNode): return AlternatingLeftRight3D(YBAnaglyphToLeft(c),YBAnaglyphToRight(c))
def YBAnaglyphToAlternatingCrossEyed(c: vs.VideoNode): return AlternatingCrossEyed3D(YBAnaglyphToLeft(c),YBAnaglyphToRight(c))
def YBAnaglyphToInterleaveRowsLeftRight(c: vs.VideoNode): return InterleaveRowsLeftRight3D(YBAnaglyphToLeft(c),YBAnaglyphToRight(c))
def YBAnaglyphToInterleaveRowsCrossEyed(c: vs.VideoNode): return InterleaveRowsCrossEyed3D(YBAnaglyphToLeft(c),YBAnaglyphToRight(c))
def YBAnaglyphToInterleaveColsLeftRight(c: vs.VideoNode): return InterleaveColsLeftRight3D(YBAnaglyphToLeft(c),YBAnaglyphToRight(c))
def YBAnaglyphToInterleaveColsCrossEyed(c: vs.VideoNode): return InterleaveColsCrossEyed3D(YBAnaglyphToLeft(c),YBAnaglyphToRight(c))
def YBAnaglyphToGBAnaglyph(c: vs.VideoNode): return GBAnaglyph(YBAnaglyphToLeft(c),YBAnaglyphToRight(c))
def YBAnaglyphToRBAnaglyph(c: vs.VideoNode): return RBAnaglyph(YBAnaglyphToLeft(c),YBAnaglyphToRight(c))
def YBAnaglyphToRGAnaglyph(c: vs.VideoNode): return RGAnaglyph(YBAnaglyphToLeft(c),YBAnaglyphToRight(c))
def YBAnaglyphToRCAnaglyph(c: vs.VideoNode): return RCAnaglyph(YBAnaglyphToLeft(c),YBAnaglyphToRight(c))
def YBAnaglyphToGMAnaglyph(c: vs.VideoNode): return GMAnaglyph(YBAnaglyphToLeft(c),YBAnaglyphToRight(c))
