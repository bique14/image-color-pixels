from PIL import Image, ImageDraw, ImageFont
from images_repo import images_repo
from io import BytesIO
import base64


class ImagePixels:
    # def __init__(self, image_path, output_path):
    def __init__(self, base64_image_src):
        self.num_rows = 77
        self.num_columns = 52
        self.portrait_width = 540
        self.portrait_height = 800
        self.image_src = base64_image_src
        self.colors = []
        # self.image_path = image_path
        # self.output_path = output_path

    def process_image(self):
        # image = Image.open(self.image_path)
        image_data = base64.b64decode(self.image_src)
        image = Image.open(BytesIO(image_data))
        image = image.resize((self.portrait_width, self.portrait_height))

        draw = ImageDraw.Draw(image)

        # Calculate the size of each rectangle
        rectangle_width = image.width / self.num_columns
        rectangle_height = image.height / self.num_rows

        for row in range(self.num_rows):
            for col in range(self.num_columns):
                # Calculate the position of the rectangle
                x0 = col * rectangle_width
                y0 = row * rectangle_height
                x1 = x0 + rectangle_width
                y1 = y0 + rectangle_height

                rectangle = image.crop((x0, y0, x1, y1))

                average_color = tuple(
                    int(sum(c) / len(c)) for c in zip(*rectangle.getdata())
                )

                self.colors.append(
                    {
                        "r": average_color[0],
                        "g": average_color[1],
                        "b": average_color[2],
                    }
                )

                # Draw the rectangle with a border
                # if you don't want a border block, you can set width to 0
                draw.rectangle(
                    [x0, y0, x1, y1], fill=average_color, outline=(0, 0, 0), width=1
                )

        # Save the resulting image
        # image.save(self.output_path)

        # Close the local image
        image.close()

    def get_colors(self):
        return self.colors


# Usage example:
# if __name__ == "__main__":
#     image_selected = images_repo["aespa-01"]
#     image_path = image_selected["src"]
#     output_image_path = (
#         f"./outputs/{image_selected['name']}-output_image.{image_selected['extension']}"
#     )

#     image_processor = ImagePixels(image_path, output_image_path)
#     # image_processor = ImagePixels("")
#     image_processor.process_image()
#     print(image_processor.get_colors())
