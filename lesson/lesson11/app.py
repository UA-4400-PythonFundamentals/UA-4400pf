
from loger_config import logger
from utils.gen import generate_users


def main():
    logger.info("Starting user generation process.")
    num_users = 5  # Example number of users to generate
    users = generate_users(num_users)
    logger.info(f"Generated {len(users)} users successfully.")
    for user in users:
        logger.debug(f"User details: {user}")

if __name__ == "__main__":
    main()
    logger.info("User generation process completed.")
