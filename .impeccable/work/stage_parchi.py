"""Stage the flat slip render (slip-flat.png) as a phone-photo style JPEG.

Run from the project root after rendering .impeccable/work/slip.html to
.impeccable/work/slip-flat.png at 2x in headless Edge.
"""
from PIL import Image, ImageFilter, ImageChops
import math


def solve(A, B):
    n = len(B)
    M = [row[:] + [b] for row, b in zip(A, B)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[p] = M[p], M[i]
        for r in range(n):
            if r != i:
                f = M[r][i] / M[i][i]
                M[r] = [a - f * b for a, b in zip(M[r], M[i])]
    return [M[i][n] / M[i][i] for i in range(n)]


def coeffs(src, dst):
    A, B = [], []
    for (x, y), (u, v) in zip(dst, src):
        A.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); B.append(u)
        A.append([0, 0, 0, x, y, 1, -v * x, -v * y]); B.append(v)
    return solve(A, B)


flat = Image.open('.impeccable/work/slip-flat.png').convert('RGB')
bbox = ImageChops.difference(flat, Image.new('RGB', flat.size, (255, 255, 255))).getbbox()
slip = flat.crop(bbox)
sw, sh = slip.size
W, H = sw + 360, sh + 280
base = Image.new('RGB', (W, H), (176, 168, 156))
noise = Image.effect_noise((W, H), 20).convert('L')
counter = Image.composite(base, Image.new('RGB', (W, H), (163, 155, 144)), noise).filter(ImageFilter.GaussianBlur(1.2))
ox, oy = 180, 120
dst = [(ox + 30, oy + 8), (ox + sw - 14, oy + 40), (ox + sw + 18, oy + sh - 6), (ox - 12, oy + sh + 22)]
c = coeffs([(0, 0), (sw, 0), (sw, sh), (0, sh)], dst)
warped = slip.transform((W, H), Image.PERSPECTIVE, c, Image.BICUBIC)
wmask = Image.new('L', (sw, sh), 255).transform((W, H), Image.PERSPECTIVE, c, Image.BICUBIC)
off = Image.new('L', (W, H), 0)
off.paste(wmask.filter(ImageFilter.GaussianBlur(24)), (16, 28))
counter = Image.composite(Image.new('RGB', (W, H), (58, 48, 38)), counter, off.point(lambda v: int(v * .55)))
counter.paste(warped, (0, 0), wmask)
g = Image.new('L', (64, 48))
gd = g.load()
for y in range(48):
    for x in range(64):
        d = math.hypot(x - 14, y - 8) / 70
        gd[x, y] = int(255 * max(0, 1 - d * .95))
light = g.resize((W, H), Image.BICUBIC)
img = Image.composite(counter, Image.new('RGB', (W, H), (38, 32, 26)), light.point(lambda v: int(125 + v * .51)))
img = Image.blend(img, Image.effect_noise((W, H), 26).convert('RGB'), .045).filter(ImageFilter.GaussianBlur(.6))
tw = 820
img = img.resize((tw, int(H * tw / W)), Image.LANCZOS)
img.save('assets/parchi-sample.jpg', quality=82, optimize=True, progressive=True)
print(img.size)
