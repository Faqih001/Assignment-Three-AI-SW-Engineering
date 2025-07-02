# 🍏 Fitness Nutrition AI Assistant

A personalized nutrition and fitness companion powered by Azure AI, built with Streamlit.

## Features

- **Personalized Calorie Calculator**: Uses Harris-Benedict formula with gender-specific calculations
- **AI-Powered Meal Planning**: Generates custom meal plans based on your preferences and goals
- **Smart Nutrition Q&A**: Ask questions and get expert nutrition advice from AI
- **Recipe Finder**: AI-powered recipe suggestions based on dietary preferences
- **Food Diary**: Track your daily food intake with calorie counting
- **Multiple Diet Types**: Support for Balanced, Keto, Vegan, Low-Carb, High-Protein, and Mediterranean diets
- **Goal-Based Planning**: Tailored recommendations for weight loss, maintenance, muscle gain, or health improvement

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd fitness-nutrition-ai-assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

1. Copy the example environment file:

   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file and add your Azure AI credentials:

   ```bash
   # Azure AI Configuration
   AZURE_INFERENCE_SDK_ENDPOINT=https://yourservice.services.ai.azure.com/models
   DEPLOYMENT_NAME=your-model-deployment-name
   AZURE_INFERENCE_SDK_KEY=your-azure-ai-key-here
   ```

### 4. Azure AI Setup

To use the AI features, you need an Azure AI service:

1. **Create an Azure Account**: Go to [Azure Portal](https://portal.azure.com)
2. **Create an AI Service**: Create an Azure OpenAI or Azure AI service
3. **Deploy a Model**: Deploy a chat completion model (like GPT-3.5 or GPT-4)
4. **Get Credentials**: Copy your endpoint URL, deployment name, and API key
5. **Update .env**: Add your credentials to the `.env` file

### 5. Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `AZURE_INFERENCE_SDK_ENDPOINT` | Your Azure AI service endpoint URL | Yes |
| `DEPLOYMENT_NAME` | Name of your deployed model | Yes |
| `AZURE_INFERENCE_SDK_KEY` | Your Azure AI service API key | Yes |
| `APP_NAME` | Application name (optional) | No |
| `DEBUG` | Enable debug mode (optional) | No |

## Security Notes

- **Never commit your `.env` file** to version control
- The `.env` file is already included in `.gitignore`
- Keep your API keys secure and rotate them regularly
- Consider using Azure Key Vault for production deployments

## Deployment Options

### Streamlit Community Cloud

1. Push your code to GitHub (without the `.env` file)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Add your environment variables in the Streamlit Cloud settings
5. Deploy with one click

### Local Development

The app runs locally with the command above. Perfect for development and testing.

## Features Overview

### 🧮 Calorie Calculator

- Gender-specific BMR calculations
- Activity level adjustments
- Goal-based calorie recommendations

### 🍽️ AI Meal Planning

- Personalized meal plans based on your profile
- Considers dietary restrictions and allergies
- Provides calorie estimates for each meal

### 💬 Nutrition Q&A

- Ask questions about nutrition and fitness
- Get evidence-based AI responses
- Context-aware answers based on your profile

### 🔍 Recipe Finder

- AI-powered recipe suggestions
- Filter by meal type and cuisine
- Dietary preference-aware recommendations

### 📝 Food Diary

- Log your daily food intake
- Track calories consumed vs. goal
- Persistent data storage
- Daily summary reports

## Tech Stack

- **Frontend**: Streamlit
- **AI**: Azure AI Services
- **Data Storage**: JSON files (local)
- **Python Libraries**: pandas, python-dotenv

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

This app provides general nutrition information and should not replace professional medical advice. Always consult with healthcare professionals for personalized medical guidance.
