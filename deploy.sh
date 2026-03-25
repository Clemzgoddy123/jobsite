#!/bin/bash
# Deploy script for free hosting platforms

echo "🚀 Deploying Django Jobsite..."

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput --clear

# Run migrations
echo "🗄️ Running database migrations..."
python manage.py migrate --noinput

echo "✅ Deployment complete!"
echo ""
echo "🔑 Environment variables needed:"
echo "  DJANGO_SECRET_KEY=your-secret-key"
echo "  DJANGO_DEBUG=False"
echo "  DJANGO_ALLOWED_HOSTS=yourdomain.com"
echo "  DATABASE_URL=postgres://user:pass@host:5432/dbname (optional, defaults to SQLite)"
