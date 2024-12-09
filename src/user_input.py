def get_invite_count():
    while True:
        try:
            invite_count = int(input("Enter the number of invitations: "))
            return invite_count
        except ValueError:
            print("Error: Enter a valid number.")
        except KeyboardInterrupt:
            print("\nOperation aborted.")
            exit(0)
