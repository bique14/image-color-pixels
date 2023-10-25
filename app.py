from flask import Flask, jsonify, request
from image_to_pixels import ImagePixels

# from flask_cors import CORS


app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 3 * 1024 * 1024  # 3MB

# Allow CORS for all routes
# CORS(app)


@app.route("/", methods=["GET"])
def check_health():
    response = {"message": "ok"}
    return jsonify(response)


@app.route("/upload", methods=["POST"])
def upload_image():
    response = {}
    data = request.get_json()

    if "image" in data:
        # Decode the base64 image into binary datap
        try:
            image_processor = ImagePixels(data["image"])
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
