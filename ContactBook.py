contacts = {}

while True:
    print('\n----- Contact Book App ----- ')
    print('1. Create Contact')
    print('2. View Contact')
    print('3. Update Contact')
    print('4. Delete Contact')
    print('5. Search Contact')
    print('6. Count Contact')
    print('7. Exit')


    chhoice = input('Enter your choice : ')

    if chhoice == '1':
        name = input('Enter your name : ')
        if name in contacts:
            print(f'Contact name {name} already existed !')

        else:
            age = input('Enter the age : ')
            email = input('Enter the email : ')
            mobile = input('Enter the number : ')
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f'Contact name {name} has been created successfully ....... !')


    elif chhoice == '2':
        name = input('Enter the contact to view : ')
        if name in contacts:
            contact = contacts[name]
            print(f'Name : {name}, Age : {age}, Mobile Number : {mobile}')
        else:
            print('Contact not found !')


    elif chhoice == '3':
        name = input('Enter the name to update contact : ')
        if name in contacts:
            age = input('Enter updated age : ')
            email = input('Enter updated email : ')
            mobile = input('Enter updated mobile number : ')
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
        
        else:
            print('Contacts not found !')


    elif chhoice == '4':
        name = input('Enter contact name to delete : ')
        if name in contacts:
            del contacts[name]
            print(f'Contact name {name} has been deleted successfully !')
        else:
            print('Contact not found !')


    elif chhoice == '5':
        search_name = input('Enter contacts name to search : ')
        found = False

        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Found - Name {name}, Age: {age}, Mobile Number: {mobile}, Email: {email}')
                food = True

        if not found:
            print('No contact found with that name')

    
    elif chhoice == '6':
        print(f'Total Contacts in your book : {len(contacts)}')

    elif chhoice == '7':
        print('Good bye ..... Closing the program !')

    else:
        print('Invaild Input')