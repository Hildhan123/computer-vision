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

if __name__ == "__main__":
    image = cv2.imread("./L.jpg")
    original = image

    # Mengaplikasikan teknik pengaburan (blur)
    blurred_image = apply_blur(image, "Gaussian")

    # Mengaplikasikan teknik filtering
    filtered_image = apply_filter(image, "Sobel")

    # Mengaplikasikan teknik pengurangan noise
    denoised_image = apply_noise_reduction(image, "Bilateral")

    # Menampilkan gambar hasil
    cv2.imshow("Original Image", original)
    cv2.imshow("Blurred Image", blurred_image)
    cv2.imshow("Filtered Image", filtered_image)
    cv2.imshow("Denoised Image", denoised_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
