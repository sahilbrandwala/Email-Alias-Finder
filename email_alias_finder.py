import re
import csv
from collections import defaultdict

# List of common role/alias addresses (customize as needed)
ROLE_BASED = {
    'info', 'admin', 'support', 'sales', 'contact', 'enquiry', 'help', 'hello',
    'team', 'office', 'service', 'billing', 'jobs', 'hr', 'careers', 'noreply', 'no-reply', 'newsletter', 'feedback'
}

def parse_email(email):
    """
    Parses email into username, plus-part (if present), and domain.
    """
    match = re.match(r'^([a-zA-Z0-9._%+-]+)(\+([a-zA-Z0-9._%+-]+))?@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$', email)
    if not match:
        return None
    username, _, plus, domain = match.groups()
    return username, plus, domain

def main():
    with open('emails.txt', 'r') as f:
        emails = [line.strip() for line in f if line.strip()]

    plus_aliases = []
    role_aliases = []
    mailbox_groups = defaultdict(list)
    seen = set()

    for email in emails:
        parsed = parse_email(email)
        if not parsed:
            continue  # skip invalid emails
        username, plus, domain = parsed
        base_mailbox = f"{username}@{domain}"
        root_mailbox = f"{username.split('+')[0]}@{domain}"

        # Group all variants under root mailbox (ignoring plus)
        mailbox_groups[root_mailbox].append(email)

        # Plus alias?
        if plus:
            plus_aliases.append(email)

        # Role-based alias?
        if username.lower() in ROLE_BASED:
            role_aliases.append(email)

    # Write plus-addressing aliases
    with open('plus_aliases.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Plus Alias Email'])
        for email in sorted(set(plus_aliases)):
            writer.writerow([email])

    # Write role-based aliases
    with open('role_aliases.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Role Alias Email'])
        for email in sorted(set(role_aliases)):
            writer.writerow([email])

    # Write grouped mailboxes
    with open('grouped_mailboxes.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Base Mailbox', 'All Related Emails'])
        for root, emails in sorted(mailbox_groups.items()):
            writer.writerow([root, "; ".join(sorted(set(emails)))])

    print("Done! See plus_aliases.csv, role_aliases.csv, and grouped_mailboxes.csv.")

if __name__ == "__main__":
    main()
