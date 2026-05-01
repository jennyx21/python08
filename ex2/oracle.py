import os
import sys
from dotenv import load_dotenv


def load_config():
    try:
        load_dotenv()
        print("Configuration loaded:")
        mode = os.getenv("MATRIX_MODE")
        database = os.getenv("DATABASE_URL")
        api = os.getenv("API_KEY")
        log = os.getenv("LOG_LEVEL")
        zion = os.getenv("ZION_ENDPOINT")
        print(f"Mode: {mode}")
        print(f"Database: conectet to: {database}")
        if api:
            print("API Access: Authenticated")
        else: 
            print("API Access: denied")
        print(f"Log Level: {log}")
        if zion:
            print(f"Zion Network: online")
        else: 
            print("Zion Network: offline")
    except:
        print(f"Failed to load configuration")


def security():
    print("Enviroment security check:")
    with open(__file__, "r") as f:
        code = f.read()
    if "API_KEY=" in code or "SECRECT" in code: 
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] Possible hardcoded secrets")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] No .env file found")
    
    if os.getenv("MATRIX_MODE") == "production":
        print("[OK] Running in production mode")
    elif os.getenv("MATRIX_MODE") == "development":
        print("[OK] Production overides avalible")
    else:
        print("[WARNING] wrong mode")


def main() -> None:
    print("ORACLE STATUS: Reading the Marix...\n")
    load_config()
    print()
    security()
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
