from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    product_name: str = "RESURRECTION"
    anthropic_api_key: str = ""
    x402_pay_to: str = "0x0000000000000000000000000000000000000000"
    x402_network: str = "eip155:84532"
    x402_sync_on_start: bool = False
    checkout_provider: str = "dev"
    public_host: str = "127.0.0.1"
    price_private_run: str = "$5.00"  # placeholder, per-run price not yet set
    daily_compute_cap_usd: float = 5.0


settings = Settings()
