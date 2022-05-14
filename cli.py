import argparse
from image_handler import get_embeddings, match_embeddings

def get_image_paths(folder):
    images = []
    for filename in os.listdir(folder):
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            continue
        images.append(os.path.join(folder,filename))
    return images

def main():
    parser = argparse.ArgumentParser(
        description='classify kindergarden images by child')
    parser.add_argument(
        '-kid', '--kid_file', required=True, type=str, help='path to the child image')
    parser.add_argument(
        '-d', '--input_dir', required=True, type=str, help='path to the batch of images')
    parser.add_argument(
        '-o', '--output_dir', required=False, type=str, help='path to output batch of images')
    args = parser.parse_args()

    for img_path in get_image_paths(args.input_dir):
        embeddings_array = [args.kid_file, second_file]
        embeddings = get_embeddings(embeddings_array)
        if match_embeddings(embeddings[0], embeddings[1]):
            print("%s has Person match!" % testing_img_file)
        else:
            print("%s has NOOOO match!" % testing_img_file)


if __name__ == "__main__":
    main()
