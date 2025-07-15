# Options Market Making Bot (OMMB)

# Setup

Create environment with Python 3.11
conda create -n options_trading python=3.11 -y

Activate environment
conda activate options_trading

Verify you're in the right environment
which python  # Should show path with options_trading

# Create main project directory
mkdir ~/projects/options_market_maker
cd ~/projects/options_market_maker

# Create subdirectories
mkdir -p {config,data,models,strategies,backtesting,execution,monitoring,logs,notebooks,tests}

# Create initial files
touch {config/__init__.py,data/__init__.py,models/__init__.py,strategies/__init__.py}
touch {backtesting/__init__.py,execution/__init__.py,monitoring/__init__.py}
touch main.py requirements.txt README.md .gitignore
