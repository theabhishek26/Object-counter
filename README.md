# Object Counter

A Python-based object counting system utilizing the YOLO object detection framework. This project enables real-time object detection and counting through  video files. There are two projects , one is to count the incoming cars on the highway and other is to count how many people go through the Elevator up and down.
## Features

- Real-time object detection using YOLO.
- Supports both webcam and video file inputs.
- Customizable object classes for detection.
- Modular code structure for easy integration and scalability.
- Requirements file shows how much tech stack is used in this project.
## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/theabhishek26/Object-counter.git
   cd Object-counter
   ```


2. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```


## Usage

### Running with Webcam


```bash
python main.py
```


### Running with Video File


```bash
python test.py --video_path path_to_video.mp4
```


*Note: Replace `path_to_video.mp4` with the actual path to your video file.*

## Directory Structure


```plaintext
Object-counter/
├── .idea/                 # IDE configuration files
├── Projects/              # Project-related files
├── Vedios/                # Sample videos for testing
├── Yolo/                  # YOLO configuration files
├── Yolo_Weights/          # Pre-trained YOLO weights
├── Yolo_webcam/           # Scripts for webcam detection
├── main.py                # Main script for webcam detection
├── requirements.txt       # Python dependencies
└── test.py                # Script for video file detection
```


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

Feel free to customize this `README.md` further to align with your project's specific details and requirements. 
