import cv2

if __name__ == '__main__':
    raw_bg = cv2.imread('65de4b399f571296e440603e656f2dfc.jpg')
    raw_slide = cv2.imread('65de4b399f571296e440603e656f2dfc.frag.png')
    canny_bg = cv2.Canny(raw_bg, 155, 280)
    canny_slide = cv2.Canny(raw_slide, 155, 280)
    res = cv2.matchTemplate(canny_bg, canny_slide, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    x1, y1 = max_loc[0], max_loc[1]
    x2, y2 = x1 + raw_slide.shape[1], y1 + raw_slide.shape[0]
    cv2.rectangle(raw_bg, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.imshow('raw_bg', raw_bg)
    cv2.imshow('raw_slide', raw_slide)
    cv2.waitKey(0)