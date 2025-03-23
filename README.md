# AI Debate Simulator

*Generate dynamic debates between an optimist and a skeptic using the Gemini API.*

## Overview

The AI Debate Simulator is a Flask-based web application that uses the Gemini API to generate debates on user-provided topics. Users can input a topic (e.g., "AI in Education"), and the app creates a multi-round debate between a confident optimist and a critical skeptic. The arguments are displayed in a clean, styled interface, making it easy to explore AI-driven argumentation.

### Features
- **Topic-Based Debates**: Enter any topic to generate a debate.
- **Two Personas**: Features a confident optimist and a critical skeptic.
- **Multi-Round Debates**: Generates 3 rounds of back-and-forth arguments by default.
- **User-Friendly Interface**: Built with HTML and CSS for a clean, responsive design.
- **Extensible**: Easily add more personas or adjust the number of rounds.

## Demo
A live demo is available at [https://ai-debate-simulator-demo.vercel.app](https://ai-debate-simulator-demo.vercel.app).  
*(Replace the above link with your actual deployment URL if available.)*

## Installation

### Prerequisites
- Python 3.8 or higher
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/)
- Git (optional, for cloning the repo)

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/username/ai-debate-simulator.git
   cd ai-debate-simulator
   ```
   *(Replace `username` with your GitHub username.)*

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. **Install Dependencies**
   Create a `requirements.txt` file with the following content:
   ```bash
   flask==2.3.3
   requests==2.32.3
   python-dotenv==1.0.1
   ```
   Then install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Gemini API Key**
   Create a `.env` file in the project root and add your Gemini API key:
   ```bash
   GEMINI_API_KEY=your-api-key-here
   ```
   Replace `your-api-key-here` with your actual Gemini API key.

5. **Run the Application**
   ```bash
   python app.py
   ```
   The app will run on `http://127.0.0.1:5000`. Open this URL in your browser.

## Usage
1. Navigate to `http://127.0.0.1:5000` in your browser.
2. Enter a debate topic (e.g., "AI in Education").
3. Click "Start Debate" to generate a 3-round debate between the optimist and skeptic.
4. View the arguments displayed in styled cards.

## Technologies Used
- **Python**: Core programming language.
- **Flask**: Web framework for the app.
- **Gemini API**: For generating debate arguments.
- **HTML/CSS**: For the frontend interface.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Open a pull request.

## Contact
For questions, suggestions, or issues, feel free to reach out:  
📧 Email: [regregd@outlook.com](mailto:regregd@outlook.com)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
