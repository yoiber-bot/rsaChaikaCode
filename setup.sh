#!/bin/bash

echo "======================================================"
echo "🚀 RSA System - Setup Script"
echo "======================================================"
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python --version 2>&1)
echo "✓ Found: $python_version"
echo ""

# Install dependencies
echo "Installing dependencies..."
pip install -q -r requirements.txt
if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed successfully"
else
    echo "✗ Failed to install dependencies"
    exit 1
fi
echo ""

# Check for .env file
if [ ! -f .env ]; then
    echo "Setting up .env file..."
    cp .env.example .env
    echo "✓ .env file created"
    echo ""
    echo "⚠️  IMPORTANTE: Debes configurar tu GEMINI_API_KEY en .env"
    echo ""
    echo "1. Obtén tu API key en: https://makersuite.google.com/app/apikey"
    echo "2. Edita .env y reemplaza 'your_api_key_here' con tu clave"
    echo ""
else
    echo "✓ .env file already exists"
    echo ""
fi

# Run tests
echo "Running logic tests..."
python test_logic.py
if [ $? -eq 0 ]; then
    echo ""
    echo "======================================================"
    echo "✅ Setup completed successfully!"
    echo "======================================================"
    echo ""
    echo "Next steps:"
    echo ""
    echo "1. Configure your GEMINI_API_KEY in .env file"
    echo "2. Run demo: python demo.py"
    echo "3. Run with API: python main.py \"your prompt here\""
    echo ""
    echo "For more info, see:"
    echo "  - README.md"
    echo "  - USAGE_GUIDE.md"
    echo ""
else
    echo ""
    echo "✗ Tests failed"
    exit 1
fi
