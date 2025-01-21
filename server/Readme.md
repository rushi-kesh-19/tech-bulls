# Flask Backend Project

## Overview
This Flask application is designed to handle backend requests for a web-based platform. It integrates MongoDB for database management, Cloudinary for file uploads, and JWT for user authentication.

## Features
- **File Upload**: Uploads and manages PDFs and images via Cloudinary.
- **User Authentication**: Secure login functionality using JWT.
- **MongoDB Integration**: Efficient data storage and retrieval.
- **Error Handling**: Comprehensive error management for user requests and server operations.

## Prerequisites
Ensure you have the following installed:
- Python 3.8+
- MongoDB (local or cloud-based)
- Cloudinary account for file uploads

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

2. Navigate to the server directory:
   ```bash
   cd Hack2Hire/server
   ```

3. Set up a virtual environment:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # For Windows: myenv\Scripts\activate
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Configure environment variables:
   - Create a `.env` file in the root directory.
   - Add the following keys:
     ```env
     SECRET_KEY=your_secret_key
     MONGO_URI=your_mongodb_connection_string
     CLOUDINARY_API_KEY=your_cloudinary_api_key
     CLOUDINARY_API_SECRET=your_cloudinary_api_secret
     ```

## Usage
1. Run the application:
   ```bash
   python run.py
   ```

2. Access the app at:
   ```
   http://127.0.0.1:5000
   ```

## API Endpoints
### Home (`/`)
**Method**: `GET`
- Renders the main page.

### Upload (`/upload`)
**Method**: `POST`
**Form Data**:
- `pdf`: PDF file to upload.
- `image`: Image file to upload.
- `name`: Name associated with the files.

**Response**:
- **Success**:
  ```json
  {
      "message": "Files uploaded successfully",
      "name": "John Doe",
      "pdf_url": "https://cloudinary.com/secure-pdf-url",
      "image_url": "https://cloudinary.com/secure-image-url"
  }
  ```
- **Error**:
  ```json
  {
      "error": "No PDF part in the request"
  }
  ```

### Authentication (`/login`)
**Method**: `POST`
- Handles user login.

## Project Structure
```
Hack2Hire/
├── server/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── models.py
│   │   ├── utils.py
│   │   ├── templates/
│   │   └── static/
│   ├── config.py
│   ├── run.py
│   ├── requirements.txt
│   ├── .env
│   └── .gitignore
├── frontend/
└── README.md
```

## Error Handling
- Handles missing fields in requests.
- Manages unexpected server errors.
- Validates file types before uploading.

## Future Enhancements
- Add user registration and profile management.
- Implement role-based access control.
- Enhance file validation and metadata storage.

## Contributing
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with detailed changes.

## License
This project is licensed under the MIT License.

