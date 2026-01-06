r"""
目标： 用 dict 做一个简单的命令行小工具，模拟“通讯录”。
要求（可以简单一点，不用太复杂）：
使用一个字典保存通讯录数据，例如：
contacts = {
    "Alice": "123456",
    "Bob": "987654",
}
提供一个简单菜单循环：
1. 查找联系人
2. 添加/修改联系人
3. 删除联系人
4. 显示全部联系人
0. 退出
"""
def find_contact(contacts, name):
    for contact in contacts:
        if contact == name:
            return contacts[contact]
    return None

def add_contact(contacts):
    print("1. Add contact")
    print("2. Modify contact")
    print("0. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter contact phone: ")
        contacts[name] = phone
    elif choice == "2":
        name = input("Enter contact name: ")
        phone = input("Enter contact phone: ")
        contacts[name] = phone
    elif choice == "0":
        return
    return contacts
    

def remove_contact(contacts, name):
    if name in contacts:
        del contacts[name]
    return contacts

def list_contacts(contacts):
    for contact in contacts:
        print(f"contact： {contact}， phone: {contacts[contact]}")



def main():
    contacts = {
    "Alice": "123456",
    "Bob": "987654",
}

    while True:
        print("\nMenu:")
        print("1. Find contact")
        print("2. Add/Modify contact")
        print("3. Remove contact")
        print("4. List all contacts")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = find_contact(contacts, name)
            if phone:
                print(f"{name}: {phone}")
            else:
                print(f"Contact {name} not found.")
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            name = input("Enter contact name: ")
            remove_contact(contacts, name)
        elif choice == "4":
            list_contacts(contacts)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()