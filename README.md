# Face Recognition App

This repository contains the frontend code for a real-time face detection and recognition system. The application provides a live video preview, displays detection information, and highlights key features of the system.

## Table of Contents

*   [Features](#features)
*   [Technologies Used](#technologies-used)
*   [Setup and Installation](#setup-and-installation)
*   [Usage](#usage)
*   [Project Structure](#project-structure)
*   [Contributing](#contributing)


## Features

The Face Recognition App offers a range of functionalities designed for efficient and accurate face detection:

*   **Live Preview**: Real-time video feed with an overlay canvas for drawing detection results.
*   **Frame Enhancement**: Advanced processing for improved brightness, contrast, and sharpening of video frames.
*   **Known Face Detection**: Identifies and recognizes faces that have been trained and stored in the system's database.
*   **Unknown Face Detection**: Detects and flags faces that are not present in the system's database.
*   **Optimized Performance**: Utilizes frame skipping to ensure efficient processing and maintain responsiveness.
*   **Auto-Close**: Configurable option to automatically close the application after a specified duration (e.g., 5 seconds) of continuous known face detection.
*   **Configurable Settings**: Easy modification of various parameters, such as the frame skip rate, to customize performance.
*   **Detection Statistics**: Displays real-time counts of known and unknown faces detected.
*   **Match Status Indicator**: Provides visual feedback (checkmark for known, cross for unknown) for detected faces.

## Technologies Used

*   **HTML5**: For the basic structure of the web page.
*   **Tailwind CSS**: A utility-first CSS framework for rapid UI development and styling.
*   **Font Awesome**: For scalable vector icons.
*   **JavaScript**: For interactive functionalities, camera access, and simulated face detection logic.

## Setup and Installation

To get this project up and running locally, follow these steps:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/face-recognition-app.git
    cd face-recognition-app
    ```

2.  **Open the `MultipleFiles/Face_recog.html` file**:
    Since this is a frontend-only application, you can simply open the `MultipleFiles/Face_recog.html` file in your web browser.

    ```bash
    # Example for Linux/macOS
    open MultipleFiles/Face_recog.html
    # Example for Windows
    start MultipleFiles/Face_recog.html
    ```

    Alternatively, you can use a live server extension in your code editor (like Live Server for VS Code) for better development experience.

## Usage

1.  **Start Detection**: Click the "Start" button in the "Live Preview" section to initiate the camera feed and begin the simulated face detection process.
2.  **Stop Detection**: Click the "Stop" button to halt the camera feed and clear any detection results.
3.  **Monitor Status**: The "Detection Info" section will update with the current status, including the number of known and unknown faces detected.
4.  **Download Application**: The "Download Application" button is a placeholder and will trigger an alert in this demo. In a full implementation, it would download the complete application files.

**Note**: The face detection and recognition logic in this frontend is simulated using JavaScript's `setTimeout` and `Math.random()` for demonstration purposes. A real-world application would require a backend (e.g., Python with OpenCV or Face Recognition libraries) to perform actual face detection and recognition.

## Project Structure

.
└── MultipleFiles/
    
        └───── Face_recog.html  # Main HTML file containing the application's frontend code

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add new feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

