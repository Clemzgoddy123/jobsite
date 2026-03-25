# Deployment Guide - Step by Step

## ✅ What's Ready

Your Django jobsite is now debugged and **100% free for hosting**:

- ✅ Environment-based configurations
- ✅ Support for SQLite (local) + PostgreSQL (production)
- ✅ Whitenoise for static files
- ✅ Gunicorn production server
- ✅ Responsive landing page with mobile navbar
- ✅ Security headers configured
- ✅ Logging for production debugging
- ✅ GitHub Actions CI/CD
- ✅ `.gitignore` to prevent accidental secret leaks

---

## 🚀 Quick Deploy to Railway (Recommended)

### Step 1: Prepare GitHub
```bash
cd c:\Users\chromeworld\OneDrive\Desktop\idoko\ assignment\my_django_project
git init
git add .
git commit -m "Production-ready, responsive navbar, free hosting"
git remote add origin https://github.com/Clemzgoddy123/my-django-jobsite.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy to Railway
1. Visit [railway.app](https://railway.app)
2. Sign in with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select `my-django-jobsite`
5. Add environment variables:
   - `DJANGO_SECRET_KEY` = Generate: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
   - `DJANGO_DEBUG` = `False`
   - `DJANGO_ALLOWED_HOSTS` = `*.railway.app`
6. Click "Deploy" 🎉

**Your app will be live in ~2-3 minutes!**

---

## 🆓 Free Tier Limits

### Railway
- **500 hours/month** (runs 24/7 continuously)
- **100 GB bandwidth free**
- **Free PostgreSQL** (great for scaling)
- Auto-scales on demand

### Render
- **Always active**, but sleeps after 15 min inactivity
- **750 compute hours/month**
- Free SSL included
- Good for low-traffic sites

### Heroku
- Free tier **discontinued** (pay-only now)

---

## 🔑 Environment Variables Explained

```
DJANGO_SECRET_KEY
  → Unique encryption key. Generate with:
    python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
  → Never share or commit this!

DJANGO_DEBUG
  → Set to "False" in production (NEVER "True")
  → "False" enables production security settings

DJANGO_ALLOWED_HOSTS
  → List of domains allowed to access your app
  → For Railway: *.railway.app
  → For custom domain: yourdomain.com www.yourdomain.com

DATABASE_URL (optional)
  → Most free platforms provide this automatically
  → Format: postgres://user:password@host:port/dbname
  → If not set, defaults to SQLite
```

---

## 🐛 Debugging Issues

### App won't start?
Check logs:
```bash
# Railway/Render: View in dashboard
# Heroku: heroku logs --tail
```

### 500 error on landing page?
1. Check `ALLOWED_HOSTS` includes your domain
2. Run: `python manage.py check --deploy`
3. View logs for detailed error

### Static files (CSS/JS) not loading?
1. Run locally: `python manage.py collectstatic --noinput`
2. In production, this runs automatically during deploy

### Database errors?
Some platforms need manual migration:
```bash
# In platform's web terminal/console:
python manage.py migrate --noinput
```

---

## 📱 Testing Locally Before Deploy

```bash
# 1. Set test production env vars
set DJANGO_DEBUG=False
set DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1
set DJANGO_SECRET_KEY=test-secret-key

# 2. Run locally
python manage.py runserver

# 3. Test landing page
# Visit http://127.0.0.1:8000
# Toggle mobile navbar (should work)
# Check login/register buttons visible
```

---

## 🔄 Deployment Checklist

Before pushing:
- [ ] All database migrations applied
- [ ] `DEBUG=False` in settings (via env var)
- [ ] `ALLOWED_HOSTS` configured
- [ ] `SECRET_KEY` is secret (in env var, not in code)
- [ ] Static files collected
- [ ] No `.env` file committed (should be in `.gitignore`)
- [ ] Landing page responsive on mobile
- [ ] Links work (login, register, job links)

---

## 📊 Monitoring & Scaling

### Free monitoring resources:
- **Sentry.io**: Error tracking (free tier)
- **UptimeRobot**: Ping service to keep app awake (free)
- **LogRocket**: Session replay (free tier)

### When ready to scale:
- Upgrade Railway/Render plan
- Add cloud database (PostgreSQL)
- Use CDN for static files (Cloudflare free)
- Add redis caching (if needed)

---

## 🎓 Next Steps (Optional)

1. **Custom domain**: Most platforms offer $x/month (Railway: from $5)
2. **Email service**: SendGrid, Mailgun (free tier)
3. **File storage**: AWS S3, Cloudinary (free tier)
4. **Analytics**: Google Analytics, Mixpanel (free)

---

## 💬 Support

- Django Docs: https://docs.djangoproject.com
- Railway Docs: https://docs.railway.app
- Render Docs: https://render.com/docs
- Stack Overflow: Tag `django`

---

**Your app is production-ready! 🚀**