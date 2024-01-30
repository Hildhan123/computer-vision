import cv2

def apply_blur(image, blur_type):
    if blur_type == "Gaussian":
        return cv2.GaussianBlur(image, (5, 5), 0)
    elif blur_type == "Median":
        return cv2.medianBlur(image, 5)
    else:
        return image

def apply_filter(image, filter_type):
    if filter_type == "Sobel":
        return cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    elif filter_type == "Laplacian":
        return cv2.Laplacian(image, cv2.CV_64F)
    else:
        return image

def apply_noise_reduction(image, reduction_type):
    if reduction_type == "Gaussian":
        return cv2.GaussianBlur(image, (5, 5), 0)
    elif reduction_type == "Bilateral":
        return cv2.bilateralFilter(image, 9, 75, 75)
    else:
        return image

def main():
    cap = cv2.VideoCapture(0)  # Mengakses webcam (0 adalah indeks kamera default)

    while True:
        ret, frame = cap.read()  # Membaca frame dari webcam

        if not ret:
            break

        # Mengaplikasikan teknik pengaburan (blur)
        blurred_frame = apply_blur(frame, "Gaussian")

        # Mengaplikasikan teknik filtering
        filtered_frame = apply_filter(frame, "Sobel")

        # Mengaplikasikan teknik pengurangan noise
        denoised_frame = apply_noise_reduction(frame, "Bilateral")

        # Menampilkan gambar hasil
        cv2.imshow("Webcam (Original)", frame)
        cv2.imshow("Webcam (Blurred)", blurred_frame)
        cv2.imshow("Webcam (Filtered)", filtered_frame)
        cv2.imshow("Webcam (Denoised)", denoised_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
