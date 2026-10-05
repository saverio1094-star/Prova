#!/usr/bin/env python3
"""Sostituisce la «MA» disegnata da ChatGPT col logo MA vero (M tagliata + A incastrata).
Uso: uv run --with numpy --with opencv-python-headless python fix_logo.py src.png out.png TLx TLy TRx TRy BRx BRy BLx BLy [--pad 6] [--dark] [--erase 8 numeri] [--white 150] [--tint 0.5]
- il quad = dove va il rettangolo del logo (angoli nell'ordine TL TR BR BL), in prospettiva sulla superficie
- la vecchia scritta (pixel bianchi/arancioni dentro il quad allargato) viene cancellata con inpaint
- --dark: M scura (per superfici chiare), altrimenti M bianca"""
import sys, numpy as np, cv2
LOGO = "/Users/admin/Claude/Mr Automation Academy/04_Riferimenti_Visivi/brand/logo.png"
args = sys.argv[1:]
pad = 6; dark = "--dark" in args
if "--pad" in args: pad = int(args[args.index("--pad") + 1])
nums = [float(a) for a in args[2:10]]
src, out = args[0], args[1]
img = cv2.imread(src, cv2.IMREAD_COLOR)
H, W = img.shape[:2]
quad = np.float32(nums).reshape(4, 2)

# --- logo vero: alpha dalla luminosità, colori puliti
lg = cv2.imread(LOGO)[:, :, ::-1].astype(np.float32)
lum = lg.max(axis=2)
alpha = np.clip((lum - 30) / 200, 0, 1)
orange = (lg[..., 0] - lg[..., 1]) > 60
ys, xs = np.where(alpha > 0.1)
y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
alpha, orange = alpha[y0:y1, x0:x1], orange[y0:y1, x0:x1]
up = 4  # supersampling per bordi puliti
alpha = cv2.resize(alpha, None, fx=up, fy=up, interpolation=cv2.INTER_CUBIC).clip(0, 1)
orange = cv2.resize(orange.astype(np.float32), None, fx=up, fy=up, interpolation=cv2.INTER_LINEAR) > 0.5
lh, lw = alpha.shape
col = np.zeros((lh, lw, 3), np.float32)
col[:] = (38, 36, 34) if dark else (242, 242, 240)     # M
col[orange] = (255, 75, 28)                            # A arancione MA (#FF4B1C)

M = cv2.getPerspectiveTransform(np.float32([[0, 0], [lw, 0], [lw, lh], [0, lh]]), quad)
a_w = cv2.warpPerspective(alpha, M, (W, H), flags=cv2.INTER_AREA)
c_w = cv2.warpPerspective(col, M, (W, H), flags=cv2.INTER_AREA)

# --- cancella la vecchia scritta: pixel chiari o arancioni dentro il quad allargato
reg = np.zeros((H, W), np.uint8)
cv2.fillConvexPoly(reg, quad.astype(np.int32), 255)
if "--erase" in args:  # zona della vecchia scritta, se diversa dal nuovo quad (TL TR BR BL)
    i = args.index("--erase"); eq = np.float32([float(a) for a in args[i + 1:i + 9]]).reshape(4, 2)
    cv2.fillConvexPoly(reg, eq.astype(np.int32), 255)
reg = cv2.dilate(reg, np.ones((2 * pad + 1, 2 * pad + 1), np.uint8))
rgb = img[:, :, ::-1].astype(int)
r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
wt = int(args[args.index("--white") + 1]) if "--white" in args else 150
old = ((rgb.min(axis=2) > wt) | ((r - g > 50) & (r > 150) & (b < 120)) | ((r - b > 70) & (r > 170))) & (reg > 0)
old = cv2.dilate(old.astype(np.uint8) * 255, np.ones((5, 5), np.uint8))
clean = cv2.inpaint(img, old, 7, cv2.INPAINT_TELEA)
# ammorbidisce la zona ricostruita perché non si vedano strisce
blur = cv2.GaussianBlur(clean, (0, 0), 2.2)
m3 = (cv2.GaussianBlur(old, (0, 0), 2) / 255.0)[..., None]
clean = (clean * (1 - m3) + blur * m3).astype(np.uint8)

# --- luce della superficie: il logo segue le variazioni di luminosità del materiale
g_bg = cv2.cvtColor(clean, cv2.COLOR_BGR2GRAY).astype(np.float32)
g_s = cv2.GaussianBlur(g_bg, (0, 0), 9)
inside = a_w > 0.05
ref = np.median(g_s[inside]) if inside.any() else 128
shade = np.clip(0.82 + 0.18 * (g_s / max(ref, 1)), 0.7, 1.08)[..., None]
logo_bgr = c_w[:, :, ::-1] * shade
if "--tint" in args:  # colora il logo con la luce della scena (0 = niente, 1 = pieno)
    k = float(args[args.index("--tint") + 1])
    ring = cv2.dilate(inside.astype(np.uint8), np.ones((25, 25), np.uint8)) > 0
    mc = clean[ring].reshape(-1, 3).astype(np.float32).mean(axis=0)
    tint = mc / mc.max()
    logo_bgr = logo_bgr * ((1 - k) + k * tint)
a3 = cv2.GaussianBlur(a_w, (0, 0), 0.6)[..., None] * 0.97   # serigrafia: bordo morbido, lascia trasparire un filo di materiale
res = clean.astype(np.float32) * (1 - a3) + logo_bgr * a3
cv2.imwrite(out, np.clip(res, 0, 255).astype(np.uint8))
print(out)
