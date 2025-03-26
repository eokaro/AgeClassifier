import logging
import argparse

# Configure logging to output to both console and a log file
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("age_classifier.log"),
        logging.StreamHandler()
    ]
)

def classify_age(age: int) -> str:
    """
    Classifies a given age into a category.

    Args:
        age (int): The age to classify.

    Returns:
        str: The classification category ("infant", "child", "teenager", "adult").

    Raises:
        ValueError: If the age is negative.
    """
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age <= 1:
        return "infant"
    elif 1 < age < 13:
        return "child"
    elif 13 <= age < 20:
        return "teenager"
    else:
        return "adult"

def get_user_age() -> int:
    """
    Prompts the user to input their age and validates the input.

    Returns:
        int: The validated age entered by the user.
    """
    while True:
        try:
            user_input = input("Enter your age: ").strip()
            age = int(user_input)
            if age < 0:
                raise ValueError("Age must be non-negative.")
            return age
        except ValueError as e:
            logging.error(f"Invalid input: {e}")
            print("Invalid input. Please enter a valid non-negative integer for age.")

def parse_arguments() -> argparse.Namespace:
    """
    Parses command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments containing age if provided.
    """
    parser = argparse.ArgumentParser(description="Age Classification Utility")
    parser.add_argument("-a", "--age", type=int, help="Age to classify")
    return parser.parse_args()

def main():
    """
    Main function to run the age classification utility.
    """
    args = parse_arguments()
    
    # Determine age: use command-line argument if provided; otherwise, prompt the user.
    age: int = args.age if args.age is not None else get_user_age()
    
    try:
        category = classify_age(age)
        # Determine proper article ("an" for infant/adult, "a" for child/teenager)
        article = "an" if category in ["infant", "adult"] else "a"
        message = f"At age {age}, you are classified as {article} {category}."
        print(message)
        logging.info(f"Classified age {age} as {category}.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
