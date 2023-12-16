"""
테스트 기록 보기에서 원하는 날의 테스트기록을 opencv로 결합함
출력은 하지않고 저장만하게 둠
"""
import cv2
import os


def merge_images(current_date):

    image1_path = f'graph_pictures/test_graph/{current_date}_Pull-Up_test.png'
    image2_path = f'graph_pictures/test_graph/{current_date}_Push-Up_test.png'
    image3_path = f'graph_pictures/test_graph/{current_date}_Squat_test.png'

    output_path = f'graph_pictures/test_graph/{current_date}_Merged_Image.png'

    images = []  # 이미지를 저장할 리스트

    # 이미지 파일이 존재하는지 확인하고 리스트에 추가
    if os.path.exists(image1_path):
        images.append(cv2.imread(image1_path))
    if os.path.exists(image2_path):
        images.append(cv2.imread(image2_path))
    if os.path.exists(image3_path):
        images.append(cv2.imread(image3_path))


    if not images:
        print("이미지 파일이 존재하지 않습니다.")
        return


    scale_factor = 0.8
    resized_images = [cv2.resize(image, None, fx=scale_factor, fy=scale_factor) for image in images]

    merged_image = cv2.hconcat(resized_images)

    cv2.imwrite(output_path, merged_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
