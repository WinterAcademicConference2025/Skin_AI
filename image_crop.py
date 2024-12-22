import cv2


cv2_img = cv2.imread("/Users/jjummi/Desktop/WinterAcademicConfernece2025/skindisease_imgsample.jpg", cv2.IMREAD_COLOR) # 원본 이미지
print(cv2_img.shape)

resized_img = cv2.resize(cv2_img, (1000,1000),interpolation=cv2.INTER_LINEAR) # 픽셀 지정으로 이미지 크기 설정
print(resized_img.shape)

cv2.imshow('image',resized_img) # 이미지창 띄우기
cv2.waitKey() # 사용자가 키보드 키를 누르기 전까지 무한 대기