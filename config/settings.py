# Quickstart version
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # IBKR Settings
    IBKR_HOST = os.getenv('IBKR_HOST', '127.0.0.1')
    IBKR_PORT = int(os.getenv('IBKR_PORT', 7497))
    IBKR_CLIENT_ID = int(os.getenv('IBKR_CLIENT_ID', 1))

    # Database
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///data/trading_data.db')
    
    # Trading Parameters
    MAX_POSITION_SIZE = int(os.getenv('MAX_POSITION_SIZE', 10))
    MAX_PORTFOLIO_DELTA = float(os.getenv('MAX_PORTFOLIO_DELTA', 100))
    RISK_FREE_RATE = float(os.getenv('RISK_FREE_RATE', 0.05))
    
    # Environment
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
    DEBUG = ENVIRONMENT == 'development'


# Complex version
'''
import os
from typing import Dict, List, Optional
from dataclasses import dataclass
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@dataclass
class IBKRConfig:
    """IBKR connection configuration"""
    host: str = os.getenv('IBKR_HOST', '127.0.0.1')
    paper_port: int = int(os.getenv('IBKR_PAPER_PORT', 7497))
    live_port: int = int(os.getenv('IBKR_LIVE_PORT', 7496))
    client_id: int = int(os.getenv('IBKR_CLIENT_ID', 1))
    timeout: int = int(os.getenv('IBKR_TIMEOUT', 10))
    
    @property
    def port(self) -> int:
        """Return appropriate port based on environment"""
        return self.paper_port if Config.is_paper_trading else self.live_port

@dataclass
class DatabaseConfig:
    """Database configuration"""
    url: str = os.getenv('DATABASE_URL', 'sqlite:///data/trading_data.db')
    echo: bool = os.getenv('DB_ECHO', 'false').lower() == 'true'
    pool_size: int = int(os.getenv('DB_POOL_SIZE', 5))
    max_overflow: int = int(os.getenv('DB_MAX_OVERFLOW', 10))

@dataclass
class TradingConfig:
    """Trading strategy configuration"""
    # Position Limits
    max_position_per_option: int = int(os.getenv('MAX_POSITION_PER_OPTION', 10))
    max_portfolio_delta: float = float(os.getenv('MAX_PORTFOLIO_DELTA', 100))
    max_portfolio_gamma: float = float(os.getenv('MAX_PORTFOLIO_GAMMA', 5.0))
    max_portfolio_vega: float = float(os.getenv('MAX_PORTFOLIO_VEGA', 500))
    
    # Risk Management
    max_daily_loss_pct: float = float(os.getenv('MAX_DAILY_LOSS_PCT', 0.02))
    max_single_symbol_pct: float = float(os.getenv('MAX_SINGLE_SYMBOL_PCT', 0.30))
    stop_loss_pct: float = float(os.getenv('STOP_LOSS_PCT', 0.05))
    
    # Market Making Parameters
    min_spread: float = float(os.getenv('MIN_SPREAD', 0.05))
    max_spread: float = float(os.getenv('MAX_SPREAD', 0.50))
    inventory_penalty: float = float(os.getenv('INVENTORY_PENALTY', 0.01))
    volatility_adjustment: float = float(os.getenv('VOLATILITY_ADJUSTMENT', 0.02))
    
    # Trading Universe
    target_symbols: List[str] = os.getenv('TARGET_SYMBOLS', 'AAPL,SPY,QQQ,TSLA').split(',')
    min_volume: int = int(os.getenv('MIN_VOLUME', 100))
    min_open_interest: int = int(os.getenv('MIN_OPEN_INTEREST', 50))
    min_days_to_expiration: int = int(os.getenv('MIN_DTE', 7))
    max_days_to_expiration: int = int(os.getenv('MAX_DTE', 45))
    
    # Market Data
    risk_free_rate: float = float(os.getenv('RISK_FREE_RATE', 0.05))
    volatility_window: int = int(os.getenv('VOLATILITY_WINDOW', 30))

@dataclass
class MonitoringConfig:
    """Monitoring and alerting configuration"""
    log_level: str = os.getenv('LOG_LEVEL', 'INFO')
    max_log_files: int = int(os.getenv('MAX_LOG_FILES', 30))
    log_file_size_mb: int = int(os.getenv('LOG_FILE_SIZE_MB', 10))
    
    # Dashboard settings
    dashboard_host: str = os.getenv('DASHBOARD_HOST', '127.0.0.1')
    dashboard_port: int = int(os.getenv('DASHBOARD_PORT', 8050))
    dashboard_debug: bool = os.getenv('DASHBOARD_DEBUG', 'false').lower() == 'true'
    
    # Alert thresholds
    alert_portfolio_delta: float = float(os.getenv('ALERT_PORTFOLIO_DELTA', 80))
    alert_daily_loss: float = float(os.getenv('ALERT_DAILY_LOSS', 0.015))
    alert_system_error_count: int = int(os.getenv('ALERT_SYSTEM_ERROR_COUNT', 5))

@dataclass
class BacktestConfig:
    """Backtesting configuration"""
    commission_per_contract: float = float(os.getenv('COMMISSION_PER_CONTRACT', 0.65))
    slippage_bps: float = float(os.getenv('SLIPPAGE_BPS', 2.0))  # basis points
    initial_capital: float = float(os.getenv('INITIAL_CAPITAL', 100000))
    
    # Performance metrics
    benchmark_symbol: str = os.getenv('BENCHMARK_SYMBOL', 'SPY')
    risk_free_rate_source: str = os.getenv('RISK_FREE_RATE_SOURCE', '^TNX')

class Config:
    """Main configuration class"""
    
    # Environment settings
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
    DEBUG = ENVIRONMENT == 'development'
    TESTING = ENVIRONMENT == 'testing'
    PRODUCTION = ENVIRONMENT == 'production'
    
    # Trading mode
    PAPER_TRADING = os.getenv('PAPER_TRADING', 'true').lower() == 'true'
    
    @property
    def is_paper_trading(self) -> bool:
        return self.PAPER_TRADING or not self.PRODUCTION
    
    # Component configurations
    ibkr = IBKRConfig()
    database = DatabaseConfig()
    trading = TradingConfig()
    monitoring = MonitoringConfig()
    backtest = BacktestConfig()
    
    # Project paths
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
    LOGS_DIR = os.path.join(PROJECT_ROOT, 'logs')
    CONFIG_DIR = os.path.join(PROJECT_ROOT, 'config')
    
    @classmethod
    def validate(cls) -> Dict[str, bool]:
        """Validate configuration settings"""
        validation = {
            'ibkr_connection': cls.ibkr.host and cls.ibkr.port > 0,
            'database_url': bool(cls.database.url),
            'trading_symbols': len(cls.trading.target_symbols) > 0,
            'risk_limits': (
                cls.trading.max_daily_loss_pct > 0 and 
                cls.trading.max_daily_loss_pct < 0.1
            ),
            'directories_exist': all([
                os.path.exists(cls.DATA_DIR),
                os.path.exists(cls.LOGS_DIR)
            ])
        }
        return validation
    
    @classmethod
    def print_summary(cls):
        """Print configuration summary"""
        print("=== CONFIGURATION SUMMARY ===")
        print(f"Environment: {cls.ENVIRONMENT}")
        print(f"Paper Trading: {cls.is_paper_trading}")
        print(f"IBKR Port: {cls.ibkr.port}")
        print(f"Target Symbols: {cls.trading.target_symbols}")
        print(f"Max Portfolio Delta: {cls.trading.max_portfolio_delta}")
        print(f"Database: {cls.database.url}")
        
        validation = cls.validate()
        print(f"\nValidation: {all(validation.values())}")
        for check, status in validation.items():
            print(f"  {check}: {'✅' if status else '❌'}")

# Convenience function for easy imports
def get_config() -> Config:
    """Get configuration instance"""
    return Config()
'''
