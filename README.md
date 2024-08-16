
# 🍽️ Nutrition Analyzer

## Overview

Nutrition Analyzer is a Streamlit-based web application that uses Google's Gemini AI to provide detailed nutritional analysis of meals from uploaded images. This tool is designed to help users gain insights into the nutritional content of their food, promoting better dietary awareness and healthier eating habits.

## Features

- **Image Upload**: Users can upload images of their meals in JPG, JPEG, or PNG formats.
- **AI-Powered Analysis**: Utilizes Google's Gemini AI model for advanced image recognition and nutritional analysis.
- **Comprehensive Nutritional Breakdown**: Provides detailed information including:
  - Identified food items with estimated calorie content
  - Total calorie estimate for the entire meal
  - Macronutrient breakdown (carbohydrates, proteins, fats)
  - Estimated fiber and sugar content
  - Key vitamins and minerals present
  - Overall meal balance assessment
  - Potential allergens or dietary restrictions
- **User-Friendly Interface**: Clean and intuitive Streamlit-based UI for easy interaction.
- **Responsive Design**: Works well on both desktop and mobile devices.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/nutrition-analyzer.git
   cd nutrition-analyzer
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Google API key:
   - Create a `.env` file in the project root
   - Add your Google API key: `GOOGLE_API_KEY=your_api_key_here`

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and navigate to the provided local URL (typically `http://localhost:8501`).

3. Upload an image of your meal using the file uploader.

4. Click the "Analyze Nutrition" button to get the nutritional breakdown.

5. View the detailed analysis in the right column of the application.

## Dependencies

- streamlit
- python-dotenv
- google-generativeai
- Pillow

## Contributing

Contributions to improve Nutrition Analyzer are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements

- [Google Gemini AI](https://deepmind.google/technologies/gemini/)
- [Streamlit](https://streamlit.io/)

## Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter) - email@example.com

Project Link: [https://github.com/yourusername/nutrition-analyzer](https://github.com/yourusername/nutrition-analyzer)
