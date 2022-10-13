# High Definition Resizer
# Made specially for retro-games encodings but can be used for general purpose.

# ResizeHD (clip, resolution_standarding_name)
# ResizeHD (clip, custom_width, custom_height)

function ResizeHD(clip c, string "std")
{
	std = default(std,"FHD")
	std = UCase(std)

	std = std == "HD" ? "WHD" : std
	std = std == "2K" ? "2HD" : std
	std = std == "4K" ? "UHD" : std
	std = std == "4:3" ? "SHD" : std
	std = std == "1080" ? "FHD" : std
	std = std == "720" ? "WHD" : std

	# width & height (before)
	bw = c.width
	bh = c.height

	# width & height (after)
	aw = std == "SHD" ? 960 : std == "WHD" ? 1280 : std == "2HD" ? 2048 : std == "UHD" ? 4096 : 1920
	ah = std == "SHD" ? 720 : std == "WHD" ? 720  : std == "2HD" ? 1080 : std == "UHD" ? 2160 : 1080

	# multiplier
	m = min(int(aw/bw),int(ah/bh))

	PointResize(c,bw*m,bh*m)
	return BilinearResize(aw,ah)
}

function ResizeHD(clip c, int aw, int ah)
{
	bw = c.width
	bh = c.height

	m = min(int(aw/bw),int(ah/bh))

	PointResize(c,bw*m,bh*m)
	return BilinearResize(aw,ah)
}
