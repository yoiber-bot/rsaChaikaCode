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

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
    if [ $? -eq 0 ]; then
        echo "✓ Virtual environment created successfully"
    else
        echo "✗ Failed to create virtual environment"
        exit 1
    fi
    echo ""
else
    echo "✓ Virtual environment already exists"
    echo ""
fi

# Activate virtual environment
echo "Activating virtual environment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi
echo "✓ Virtual environment activated"
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
    echo "1. Activate the virtual environment:"
    echo "   - Linux/Mac: source venv/bin/activate"
    echo "   - Windows: venv\\Scripts\\activate"
    echo ""
    echo "2. Configure your GEMINI_API_KEY in .env file"
    echo "3. Run demo: python demo.py"
    echo "4. Run with API: python main.py \"your prompt here\""
    echo ""
    echo "⚠️  Remember to activate the virtual environment each time"
    echo "   you work on this project!"
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
