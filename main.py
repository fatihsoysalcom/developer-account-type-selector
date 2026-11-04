# This script simulates the decision-making process for choosing between Individual and Organization developer accounts,
# reflecting the concepts discussed in the article.

def get_user_input(prompt):
    """Helper function to get validated yes/no input."""
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please answer 'yes' or 'no'.")

print("Welcome to the Developer Account Type Selector!")
print("This tool helps you consider factors for choosing between an Individual or Organization developer account.")
print("\nAnswer a few questions to get a recommendation.\n")

# --- Decision Factors (reflecting article's points) ---

# Factor 1: Legal Entity (Kurumsal vs. Bireysel - legal responsibility)
has_legal_entity = get_user_input("1. Do you have a registered legal entity (e.g., company, LLC, corporation)? (yes/no): ")

# Factor 2: Team Collaboration (Kurumsal - team management capabilities)
plans_team = get_user_input("2. Do you plan to have multiple team members collaborating on the app? (yes/no): ")

# Factor 3: Business Intent (Bireysel for hobby, Kurumsal for serious business/growth potential)
commercial_intent = get_user_input("3. Is this application primarily for a commercial business venture or a hobby/personal project? (business/hobby): ").lower()

is_business_venture = (commercial_intent == 'business')

print("\n--- Recommendation ---")

# --- Logic for Recommendation ---

# If a legal entity exists or there's a strong business/team need, lean towards Organization.
if has_legal_entity or (plans_team and is_business_venture):
    account_type = "Organization (Kurumsal)"
    print(f"Based on your answers, an {account_type} developer account is likely the most suitable.")
    print("\nKey considerations for Organization accounts:")
    print("  - Legal entity required (company name displayed).") # Reflects legal responsibility
    print("  - Supports team management and roles.")             # Reflects team management
    print("  - Better for scaling and formal business operations.") # Reflects growth potential
    print("  - May involve more complex verification processes.")
elif plans_team:
    account_type = "Organization (Kurumsal)"
    print(f"Considering your plans for team collaboration, an {account_type} developer account is recommended.")
    print("\nKey considerations for Organization accounts:")
    print("  - Essential for managing multiple developers and roles.") # Reflects team management
    print("  - You may need to register a legal entity if you don't have one.")
    print("  - Provides a more professional appearance in app stores.")
else:
    account_type = "Individual (Bireysel)"
    print(f"Based on your answers, an {account_type} developer account seems appropriate.")
    print("\nKey considerations for Individual accounts:")
    print("  - Simpler setup, your personal name is displayed.") # Reflects simpler setup, personal identity
    print("  - Best for personal projects, hobbies, or sole proprietorships.")
    print("  - Limited or no team management features.")
    print("  - Easier initial verification.")

print("\nRemember, this is a general recommendation. Always consult official documentation and legal advice for your specific situation.")
