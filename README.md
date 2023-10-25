# Image Processing API

This is a simple Flask API for processing images and extracting pixel data. and working together with `4000 weeks` project. it means the pixel colors will contains 77 rows and each row contains 52 array items.

## Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Getting Started

To get started with this API, you'll need to have Python and Flask installed on your system. You can install the required packages using the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the API by running app.py:

```bash
python3 app.py
```

2. The API will be available at http://localhost:5000.

3. You can test the health check route by visiting http://localhost:5000/ in your browser or using a tool like curl.

## API Endpoints

- `GET /:` A health check endpoint to ensure the API is running.

- `POST /upload:` Upload an image in JSON format, process it, and return the pixel data.

Payload:

```json
{
  "image": "base64_encoded_image_data"
}
```

Response:

```json
[
  [{ r: 255, g: 255, b: 255 }, { r: 200, g: 200, b: 255 }, ...],
  [{ r: 100, g: 255, b: 200 }, { r: 100, g: 255, b: 215 }, ...],
  ...
]
```

Happy coding!
