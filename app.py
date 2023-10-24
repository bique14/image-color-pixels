from flask import Flask, jsonify, request
from flask_cors import CORS
from image_to_pixels import ImagePixels
import base64

app = Flask(__name__)

# Allow CORS for all routes
CORS(app)


@app.route("/", methods=["GET"])
def check_health():
    response = {"message": "ok"}
    return jsonify(response)


@app.route("/upload", methods=["POST"])
def upload_image():
    response = {}
    data = request.get_json()

    if "image" in data:
        image_data_splited = data["image"].split(";")

        # image_extension = image_data_splited[0].split("/")[-1]
        image_base64_data = image_data_splited[1].split(",")[-1]

        # Decode the base64 image into binary datap
        try:
            # image_data = base64.b64decode(base64_image)
            # print(image_data)
            image_processor = ImagePixels(image_base64_data)
            image_processor.process_image()
            colors = image_processor.get_colors()

            numRows = 77
            numColumns = 52

            # Create an array of arrays
            array_of_arrays = [[] for _ in range(numRows)]

            # Add each item to the corresponding subarray
            for index, item in enumerate(colors):
                row_index = index // numColumns  # Calculate the row index
                array_of_arrays[row_index].append(item)

            response = array_of_arrays

        except Exception as e:
            response["message"] = "Error decoding base64 image: " + str(e)
    else:
        response["message"] = "No 'image' field in the request JSON."

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
