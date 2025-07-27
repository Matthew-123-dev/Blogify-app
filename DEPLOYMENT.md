# 🚀 Deploying Blogify to Render

## Quick Deployment Steps

### 1. Push your code to GitHub
```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

### 2. Create Render Service
1. Go to [render.com](https://render.com) and sign up/login
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Select your Blogify repository

### 3. Configure Service Settings
- **Name**: `blogify-app`
- **Runtime**: `Python 3`
- **Build Command**: `./build.sh`
- **Start Command**: `cd src && gunicorn blogify.wsgi:application`

### 4. Set Environment Variables
In Render dashboard, add these environment variables:

| Variable | Value |
|----------|-------|
| `SECRET_KEY` | Generate a new Django secret key |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `your-app-name.onrender.com` |

### 5. Add Database (Optional)
1. Create PostgreSQL database in Render
2. It will automatically set `DATABASE_URL` environment variable

### 6. Deploy
Click "Create Web Service" and wait for deployment!

## Generate Secret Key
Run this Python command to generate a secure secret key:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

## Your app will be live at:
`https://your-app-name.onrender.com`

## After First Deployment
Run these commands in Render Shell:
```bash
python src/manage.py createsuperuser
```
