# My Django Jobsite

A responsive job board platform with a beautiful landing page, mobile-friendly navigation, and user authentication.

## Features

✅ Responsive landing page with mobile toggling navbar  
✅ Login & Register system  
✅ Job listings and job detail views  
✅ User-friendly interface with smooth animations  
✅ Production-ready deployment configuration  

---

## Local Setup

### 1. Clone & Install

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd my_django_project
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run Migrations

```bash
python manage.py migrate
```

### 3. Create Superuser (optional)

```bash
python manage.py createsuperuser
```

### 4. Run Locally

```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000**

---

## Free Hosting Deployment

### Option 1: Railway (Recommended - Easiest)

1. Go to [railway.app](https://railway.app) and sign up
2. Connect your GitHub account
3. Create new project → GitHub repo
4. Select `my_django_jobsite` repository
5. Add environment variables:
   ```
   DJANGO_SECRET_KEY=your-unique-secret-key-here
   DJANGO_DEBUG=False
   DJANGO_ALLOWED_HOSTS=*.railway.app
   ```
6. Deploy automatically! 🚀

**Free tier**: 500 hours/month (enough for continuous hosting)

---

### Option 2: Render (Free & Easy)

1. Go to [render.com](https://render.com) and sign up
2. New → Web Service → Connect GitHub
3. Select your repository
4. Configure:
   - **Environment**: Python 3.11
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput --clear`
   - **Start Command**: `gunicorn jobsite.wsgi:application`
5. Add environment variables (same as Railway)
6. Deploy! 🚀

**Free tier**: Auto-sleep after 15 min inactivity, limited resources

---

### Option 3: Heroku (Classic)

1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   heroku config:set DJANGO_SECRET_KEY=your-secret-key
   heroku config:set DJANGO_DEBUG=False
   heroku run python manage.py migrate
   ```

**Note**: Heroku free tier is now paid-only (as of Nov 2022)

---

### Option 4: PythonAnywhere (Simple & Free)

1. Go to [pythonanywhere.com](https://pythonanywhere.com)
2. Create free account
3. Upload project files via Web interface or Git
4. Configure virtual env + WSGI file
5. Reload web app

---

## Environment Variables

Create a `.env` file locally (copy from `.env.example`):

```
DJANGO_SECRET_KEY=your-unique-secret-key-here
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=yourdomain.com www.yourdomain.com
DATABASE_URL=postgres://user:pass@host:5432/dbname  # Optional (defaults to SQLite)
```

**Important**: Never commit `.env` to GitHub. It's in `.gitignore`.

---

## Production Checklist

- ✅ `DJANGO_DEBUG=False` in production
- ✅ `DJANGO_SECRET_KEY` is unique and secret
- ✅ Database migrations applied (`python manage.py migrate`)
- ✅ Static files collected (`python manage.py collectstatic`)
- ✅ Whitenoise middleware configured for static files
- ✅ HTTPS/SSL enabled (free via Certbot on most platforms)
- ✅ Allowed hosts configured
- ✅ GitHub Actions CI running and passing

---

## Troubleshooting

### Static files not loading

```bash
python manage.py collectstatic --noinput --clear
```

### Database migration errors

```bash
python manage.py migrate --noinput
```

### "ALLOWED_HOSTS" error

Set environment variable:
```
DJANGO_ALLOWED_HOSTS=yourdomain.com www.yourdomain.com
```

### Port/Binding errors

Most PaaS platforms auto-assign ports. The app listens via `$PORT` env var (handled in `Procfile`).

---

## Project Structure

```
my_django_project/
├── jobs/                  # Main app
│   ├── migrations/
│   ├── templates/
│   ├── views.py
│   ├── models.py
│   └── urls.py
├── jobsite/               # Project settings
│   ├── settings.py        # ⚙️ Production-ready
│   ├── urls.py
│   └── wsgi.py
├── templates/             # Global templates
│   └── landing.html       # 📱 Responsive landing
├── manage.py
├── requirements.txt       # 📦 All dependencies
├── Procfile               # 🚀 PaaS deployment
├── runtime.txt            # Python version
└── README.md
```

---

## Links

- **GitHub**: [Clemzgoddy123/my-django-jobsite](https://github.com/Clemzgoddy123/my-django-jobsite)
- **Job App**: See `/jobs/` for models and views
- **Responsive Design**: Check `/templates/landing.html`

---

## License

Open source. Feel free to use and modify!

---

## Support

Questions? Check Django docs: [docs.djangoproject.com](https://docs.djangoproject.com)