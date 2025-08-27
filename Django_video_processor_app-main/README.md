# Django Video Processor App

## Overview

The Django Video Processor App is a web application that allows users to upload videos, automatically extract subtitles using FFmpeg, and view the uploaded videos along with their subtitles. The application is built using Django, PostgreSQL, and Docker for containerization.

## Features

- **Video Upload**: Users can upload videos through a simple form.
- **Subtitle Extraction**: Automatically extract subtitles from uploaded videos using FFmpeg.
- **Video List**: View a list of uploaded videos with links to access them.
- **Subtitle Display**: Display extracted subtitles along with the videos.

## Technologies Used

- **Django**: A high-level Python web framework used for building the web application.
- **PostgreSQL**: The database used to store video metadata and other information.
- **FFmpeg**: A powerful multimedia framework used to extract subtitles from videos.
- **Docker**: Used for containerization to ensure consistent deployment.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/devmishra1708/Django_video_processor_app.git
2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
3. Apply migrations:
    ```bash
    python manage.py migrate
4. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
5. Run the development server:
   ```bash
       python manage.py runserver

### Using Docker
6. Build and Run the Docker Containers

      ```bash
         docker-compose up --build
7. FFmpeg Integration
      ```bash
      ffmpeg -i <input_video> -map 0:s:0 <output_subtitle_file>

# Screenshots
## Home page
![Screenshot 2024-09-15 011723](https://github.com/user-attachments/assets/304c9a92-5dd8-4697-9ced-5cb9c875702f)
## Page to upload video
![to upload a video ](https://github.com/user-attachments/assets/c5ef8f94-5628-4cc1-b332-b8f4a7658bf9)
## Video list page and uploaded video
![uploaded videos](https://github.com/user-attachments/assets/92727b37-39c4-4fde-8e42-daf7b21ad179)
## View video page
![view video page](https://github.com/user-attachments/assets/4f7f4cba-d45e-4b64-bb81-26bc28816066)
## Subtitles
![subtitles](https://github.com/user-attachments/assets/1d21d3d1-30a1-4091-8a50-71aac1e899df)
## Subtitle option through threedots
![subtitles options](https://github.com/user-attachments/assets/723a2fc3-e247-4f58-9317-9634c2197fa8)
![Screenshot 2024-09-15 171136](https://github.com/user-attachments/assets/57b0726f-c2b1-48fe-a82c-86af39dda8fe)
## Transcript
![transcript](https://github.com/user-attachments/assets/28be411b-6b6a-4e16-9089-4ca8c4bd3423)
## Search and result 
![search and search result](https://github.com/user-attachments/assets/58fc566e-318f-4bca-a94f-0f8f9df8b359)
## Download subtitles .vtt format
![Screenshot 2024-09-15 171257](https://github.com/user-attachments/assets/304a9fb6-260d-466d-b0c7-c6ab90d86553)







