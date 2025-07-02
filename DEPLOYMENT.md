# 🚀 Streamlit Cloud Deployment Guide

This guide will help you deploy your Fitness Nutrition AI Assistant to Streamlit Community Cloud.

## 📋 Prerequisites

1. GitHub account
2. Azure AI service credentials
3. Your app code ready in a GitHub repository

## 🛠️ Step-by-Step Deployment

### 1. Prepare Your Repository

Make sure your repository has these files:

- `app.py` (main application)
- `requirements.txt` (dependencies)
- `secrets.toml.example` (template for secrets)
- `README.md` (documentation)
- `.gitignore` (excludes sensitive files)

**Important**: Never commit `secrets.toml` or `.env` files to your repository!

### 2. Push to GitHub

```bash
git add .
git commit -m "Prepare for Streamlit Cloud deployment"
git push origin main
```

### 3. Deploy to Streamlit Cloud

1. **Go to Streamlit Cloud**: Visit [share.streamlit.io](https://share.streamlit.io)

2. **Sign in**: Use your GitHub account to sign in

3. **Create New App**: Click "New app" button

4. **Connect Repository**:
   - Select your GitHub repository
   - Choose the branch (usually `main`)
   - Set main file path: `app.py`

5. **Configure Secrets**:
   - Click on "Advanced settings"
   - Go to the "Secrets" section
   - Copy the content from your local `secrets.toml` file
   - Paste it into the secrets text area

### 4. Secrets Configuration

Copy this template to your Streamlit Cloud secrets section:

```toml
[azure_ai]
AZURE_INFERENCE_SDK_ENDPOINT = "https://mybots254.services.ai.azure.com/models"
DEPLOYMENT_NAME = "grok-3"
AZURE_INFERENCE_SDK_KEY = "3uTQWVskUTQFsIJbZVt2PfQFlha9afMlLhTmzgXbYY6BNq79PU69JQQJ99BEACYeBjFXJ3w3AAAAACOGMM1w"

[app_config]
APP_NAME = "Fitness Nutrition AI Assistant"
DEBUG = false
```

### 5. Deploy

1. Click "Deploy!" button
2. Wait for the app to build and deploy
3. Your app will be available at: `https://your-app-name.streamlit.app`

## 🔧 Configuration Details

### Azure AI Configuration

Your app automatically detects the deployment environment:

- **Local Development**: Uses `.env` file
- **Streamlit Cloud**: Uses `st.secrets` from the TOML configuration
- **Fallback**: Graceful error handling if configuration is missing

### Environment Detection

The app uses this logic:

```python
# Try Streamlit secrets first (cloud deployment)
if hasattr(st, 'secrets') and 'azure_ai' in st.secrets:
    endpoint = st.secrets["azure_ai"]["AZURE_INFERENCE_SDK_ENDPOINT"]
    model_name = st.secrets["azure_ai"]["DEPLOYMENT_NAME"]
    key = st.secrets["azure_ai"]["AZURE_INFERENCE_SDK_KEY"]
else:
    # Fallback to environment variables (local development)
    endpoint = os.getenv("AZURE_INFERENCE_SDK_ENDPOINT")
    model_name = os.getenv("DEPLOYMENT_NAME")
    key = os.getenv("AZURE_INFERENCE_SDK_KEY")
```

## 🔒 Security Best Practices

### ✅ Do's

- Use Streamlit Cloud's built-in secrets management
- Keep your API keys secure and rotate them regularly
- Test your app locally before deploying
- Use meaningful names for your secrets
- Set appropriate permissions on your GitHub repository

### ❌ Don'ts

- Never commit `secrets.toml` or `.env` files to your repository
- Don't hardcode API keys in your source code
- Don't share your secrets in plain text
- Don't use production credentials for testing

## 🚨 Troubleshooting

### Common Issues

1. **App won't start**: Check your `requirements.txt` file
2. **Azure AI not working**: Verify your secrets configuration
3. **Import errors**: Make sure all dependencies are listed
4. **Authentication errors**: Check your Azure AI credentials

### Debug Steps

1. **Check Logs**: View deployment logs in Streamlit Cloud
2. **Test Locally**: Ensure the app works on your local machine
3. **Verify Secrets**: Double-check the secrets format and values
4. **Dependencies**: Confirm all packages are in `requirements.txt`

## 📱 App Features in Cloud

Once deployed, your app will have:

- **AI-Powered Meal Planning**: Personalized meal plans using Azure AI
- **Smart Recipe Finder**: AI-generated recipes based on preferences
- **Nutrition Q&A**: Interactive AI nutrition coach
- **Food Diary**: Persistent food logging with AI analysis
- **Responsive Design**: Works on desktop and mobile devices

## 🔄 Updating Your App

To update your deployed app:

1. Make changes to your code locally
2. Test thoroughly
3. Commit and push to GitHub
4. Streamlit Cloud will automatically redeploy

## 📊 Monitoring

After deployment, you can:

- View app analytics in Streamlit Cloud dashboard
- Monitor usage and performance
- Check error logs and debugging information
- Manage app settings and secrets

## 🆘 Getting Help

If you encounter issues:

1. **Streamlit Documentation**: [docs.streamlit.io](https://docs.streamlit.io)
2. **Community Forum**: [discuss.streamlit.io](https://discuss.streamlit.io)
3. **GitHub Issues**: Create an issue in your repository
4. **Azure AI Support**: [Azure Support Portal](https://portal.azure.com)

## 🎉 Success

Once deployed successfully, your Fitness Nutrition AI Assistant will be:

- ✅ Accessible via public URL
- ✅ Using secure cloud-based secrets
- ✅ Automatically updating when you push changes
- ✅ Scalable and reliable on Streamlit's infrastructure

Your app URL will be: `https://[your-app-name].streamlit.app`

---

**Need help?** Check the [Streamlit Cloud documentation](https://docs.streamlit.io/streamlit-community-cloud) for more details.
