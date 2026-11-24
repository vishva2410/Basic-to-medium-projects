import moviedb as mvs
def menu():
    while True:
        print("\n========== CINEMA RANKING SYSTEM ==========")
        print("1. View All Theatre Rankings")
        print("2. Add a Theatre")
        print("3. Delete a Theatre")
        print("4. Best Theatre Overall")
        print("5. Best Theatre by Type")
        print("6. Best Theatre by Projection Quality")
        print("7. Largest Theatre Overall")
        print("8. Largest Theatre by Type")
        print("9. Theatre to Avoid")
        print("10. View All IMAX Screens")
        print("11. Exit")

        choice = input("Please select an option: ")

        if choice == '1':
            mvs.view_rankings()

        elif choice == '2':
            name = input("Enter theatre name: ")
            scope = input("Enter screen size/scope: ")
            seat_comfort = float(input("Enter seat comfort rating: "))
            ac_quality = float(input("Enter AC quality rating: "))
            availability = float(input("Enter availability rating: "))
            projection_quality = int(input("Enter projection quality (2, 4, 8): "))
            theatre_type = input("Enter theatre type: ")
            rating = float(input("Enter overall rating: "))

            mvs.add(name, scope, seat_comfort, ac_quality,
                availability, projection_quality, theatre_type, rating)

            print("Theatre added successfully!")

        elif choice == '3':
            name = input("Enter theatre name to delete: ")
            mvs.delete(name)
            print("Theatre deleted successfully!")

        elif choice == '4':
            result = mvs.best_theatre()
            print("Best Theatre:", result if result else "No theatres found.")

        elif choice == '5':
            theatre_type = input("Enter theatre type: ")
            result = mvs.best_theatre_by_type(theatre_type)
            print("Best Theatre:", result if result else "No matching theatres found.")

        elif choice == '6':
            projection_quality = int(input("Enter projection quality (2, 4, 8): "))
            result = mvs.best_theatre_by_projection_quality(projection_quality)
            print("Best Theatre:", result if result else "No matching theatres found.")

        elif choice == '7':
            result = mvs.largest_theatre()
            print("Largest Theatre:", result if result else "No theatres found.")

        elif choice == '8':
            theatre_type = input("Enter theatre type: ")
            result = mvs.largest_theatre_by_type(theatre_type)
            print("Largest Theatre:", result if result else "No matching theatres found.")

        elif choice == '9':
            result = mvs.avoid_theatre()
            print("Theatre to Avoid:", result if result else "No theatres below rating 2.")

        elif choice == '10':
            result = mvs.imax_screens()
            if result:
                print("IMAX Screens:")
                for screen in result:
                    print(screen[0])
            else:
                print("No IMAX screens found.")

        elif choice == '11':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

mvs.create_table()
menu()
