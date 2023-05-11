import cv2

img = cv2.imread('solar-system.jpg')

cv2.putText(
    img,
    "Sun",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)
cv2.putText(
    img,
    "Moon",
    (330,200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.25,
    (0,0,225)
)
cv2.putText(
    img,
    "Mercury",
    (100,200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (0,0,225)
)
cv2.putText(
    img,
    "Venus",
    (200,200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (0,0,225)
)
cv2.putText(
    img,
    "Earth",
    (300,200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (0,0,225)
)
cv2.putText(
    img,
    "Mars",
    (400,200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (0,0,225)
)
cv2.putText(
    img,
    "Jupiter",
    (600,200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (0,0,225)
)
cv2.putText(
    img,
    "Saturn",
    (800,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (0,0,225)
)
cv2.putText(
    img,
    "Uranus",
    (950,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (0,0,225)
)
cv2.putText(
    img,
    "Neptune",
    (1100,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (0,0,225)
)

cv2.imshow('solar-system.jpg',img)

cv2.waitKey(0)