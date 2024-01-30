import cv2
import numpy as np

def scale_image(image, scale_factor):
    scaled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor)
    return scaled_image

def rotate_image(image, angle):
    center = (image.shape[1] // 2, image.shape[0] // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))
    return rotated_image

def translate_image(image, tx, ty):
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))
    return translated_image

def skew_image(image, skew_matrix):
    skewed_image = cv2.warpAffine(image, skew_matrix, (image.shape[1], image.shape[0]))
    return skewed_image

def mirror_image(image, axis):
    mirrored_image = cv2.flip(image, axis)
    return mirrored_image

def affine_transform(image, affine_matrix):
    affine_transformed_image = cv2.warpAffine(image, affine_matrix, (image.shape[1], image.shape[0]))
    return affine_transformed_image

def main():
    # Inisialisasi webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        # Transformasi Skala
        scaled_frame = scale_image(frame, 1.5)

        # Transformasi Rotasi
        rotated_frame = rotate_image(frame, 45)

        # Transformasi Translasi
        translated_frame = translate_image(frame, 50, 30)

        # Transformasi Skew
        skew_matrix = np.float32([[1, 0.5, 0], [0.5, 1, 0]])
        skewed_frame = skew_image(frame, skew_matrix)

        # Transformasi Mirror
        mirrored_frame = mirror_image(frame, 1)  # 1 untuk mencerminkan sumbu horizontal

        # Transformasi Affine
        affine_matrix = np.float32([[1.5, 0.5, 50], [0.5, 1.5, 30]])
        affine_transformed_frame = affine_transform(frame, affine_matrix)

        # Menampilkan frame asli dan hasil transformasi
        cv2.imshow("Original Frame", frame)
        cv2.imshow("Scaled Frame", scaled_frame)
        cv2.imshow("Rotated Frame", rotated_frame)
        cv2.imshow("Translated Frame", translated_frame)
        cv2.imshow("Skewed Frame", skewed_frame)
        cv2.imshow("Mirrored Frame", mirrored_frame)
        cv2.imshow("Affine Transformed Frame", affine_transformed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
