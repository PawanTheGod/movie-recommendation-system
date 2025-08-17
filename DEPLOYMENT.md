# 🚀 Deployment Guide

This guide will help you deploy your Movie Recommender System to various platforms.

## 🌐 Streamlit Cloud (Recommended)

Streamlit Cloud is the easiest way to deploy your app for free.

### Step 1: Prepare Your Repository
1. Make sure your code is on GitHub
2. Ensure `requirements.txt` is up to date
3. Your main file should be named `app.py`

### Step 2: Deploy to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository and branch
5. Set the main file path to `app.py`
6. Click "Deploy!"

### Step 3: Customize Your App
- **App URL**: Your app will be available at `https://your-app-name.streamlit.app`
- **Settings**: Configure in the Streamlit Cloud dashboard
- **Updates**: Automatically deploys when you push to GitHub

## 🐳 Docker Deployment

### Create Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Build and Run
```bash
docker build -t movie-recommender .
docker run -p 8501:8501 movie-recommender
```

## ☁️ Heroku Deployment

### Step 1: Install Heroku CLI
```bash
# Windows
# Download from https://devcenter.heroku.com/articles/heroku-cli

# macOS
brew tap heroku/brew && brew install heroku
```

### Step 2: Create Heroku App
```bash
heroku login
heroku create your-app-name
```

### Step 3: Deploy
```bash
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

### Step 4: Open App
```bash
heroku open
```

## 🐍 Local Deployment

### Run Locally
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

### Access Locally
- **Local URL**: http://localhost:8501
- **Network URL**: http://your-ip:8501

## 🔧 Configuration

### Environment Variables
Create a `.streamlit/config.toml` file:
```toml
[server]
port = 8501
address = "0.0.0.0"

[browser]
gatherUsageStats = false
```

### Custom Domain (Streamlit Cloud Pro)
1. Go to your app settings
2. Add custom domain
3. Update DNS records
4. Wait for propagation

## 📱 Mobile Optimization

Your app is already mobile-responsive! Test on:
- **Mobile browsers**: Chrome, Safari, Firefox
- **Tablets**: iPad, Android tablets
- **Different screen sizes**: 320px to 1920px+

## 🚨 Troubleshooting

### Common Issues

**App won't start:**
- Check `requirements.txt` is complete
- Ensure `app.py` is the main file
- Verify all imports are correct

**Data not loading:**
- Check file paths in your code
- Ensure data files are in the repository
- Verify pickle files are not corrupted

**Styling issues:**
- Check CSS syntax
- Ensure HTML is properly escaped
- Test on different browsers

### Performance Tips

1. **Optimize data loading**: Use caching for expensive operations
2. **Reduce file sizes**: Compress images and data files
3. **Use efficient algorithms**: Optimize your ML pipeline
4. **Monitor usage**: Check Streamlit Cloud analytics

## 🔒 Security Considerations

- **API Keys**: Never commit sensitive keys to GitHub
- **Data Privacy**: Ensure your dataset doesn't contain personal information
- **Rate Limiting**: Consider implementing request limits
- **HTTPS**: Always use secure connections in production

## 📊 Monitoring

### Streamlit Cloud
- **Analytics**: View usage statistics
- **Logs**: Check for errors and warnings
- **Performance**: Monitor app response times

### Custom Monitoring
```python
import time
import streamlit as st

# Add performance monitoring
start_time = time.time()
# Your code here
end_time = time.time()
st.write(f"Execution time: {end_time - start_time:.2f} seconds")
```

## 🎯 Next Steps

1. **Deploy to Streamlit Cloud** (easiest)
2. **Set up custom domain** (optional)
3. **Monitor performance** and usage
4. **Gather user feedback** and improve
5. **Scale up** as needed

---

**Need help?** Check the [Streamlit documentation](https://docs.streamlit.io/) or create an issue in your repository.
