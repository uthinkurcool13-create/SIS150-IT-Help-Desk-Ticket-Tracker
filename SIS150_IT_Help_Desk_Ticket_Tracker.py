class HelpDeskTicket:
    def __init__(self, ticket_id, issue, priority):
        self.ticket_id = ticket_id
        self.issue = issue
        self.priority = priority
        self.status = "Open"

    def resolve_ticket(self):
        self.status = "Resolved"

    def display_ticket(self):
        print(f"Ticket #{self.ticket_id}")
        print(f"Issue: {self.issue}")
        print(f"Priority: {self.priority}")
        print(f"Status: {self.status}")
        print()


def show_menu():
    print("IT Help Desk Ticket Tracker")
    print("1. Create a ticket")
    print("2. View all tickets")
    print("3. Resolve a ticket")
    print("4. Exit")


def main():
    tickets = []

    while True:
        print()
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            issue = input("Describe the issue: ")

            priority = input("Enter priority (Low, Medium, High): ").title()
            while priority not in ["Low", "Medium", "High"]:
                print("Please enter Low, Medium, or High.")
                priority = input("Enter priority (Low, Medium, High): ").title()

            ticket_id = len(tickets) + 1
            new_ticket = HelpDeskTicket(ticket_id, issue, priority)
            tickets.append(new_ticket)

            print(f"Ticket #{ticket_id} created successfully.")

        elif choice == "2":
            if len(tickets) == 0:
                print("No tickets have been created.")
            else:
                print()
                print("All Tickets")
                print("-----------")
                for ticket in tickets:
                    ticket.display_ticket()

        elif choice == "3":
            if len(tickets) == 0:
                print("There are no tickets to resolve.")
            else:
                ticket_number = int(input("Enter the ticket number to resolve: "))
                found = False

                for ticket in tickets:
                    if ticket.ticket_id == ticket_number:
                        ticket.resolve_ticket()
                        print(f"Ticket #{ticket_number} has been resolved.")
                        found = True
                        break

                if not found:
                    print("Ticket not found.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
