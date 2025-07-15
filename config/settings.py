import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # IBKR Settings
    IBKR_HOST = os.getenv('IBKR_HOST', '127.0.0.1')
    IBKR_PORT = int(os.getenv('IBKR_PORT', 7497))
    IBKR_CLIENT_ID = int(os.getenv('IBKR_CLIENT_ID', 1))

    '''
    # Database
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///data/trading_data.db')
    
    # Trading Parameters
    MAX_POSITION_SIZE = int(os.getenv('MAX_POSITION_SIZE', 10))
    MAX_PORTFOLIO_DELTA = float(os.getenv('MAX_PORTFOLIO_DELTA', 100))
    RISK_FREE_RATE = float(os.getenv('RISK_FREE_RATE', 0.05))
    
    # Environment
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
    DEBUG = ENVIRONMENT == 'development'
    '''
